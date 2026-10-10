"""Tkinter UI: worker threads communicate through a queue; no UI calls in workers."""
import json
import queue
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from pathlib import Path
from research.engine import Engine, validate_case
from research.catalog import load_catalog, save_registration
ROOT = Path(__file__).resolve().parent

def launch():
    root = tk.Tk()
    root.title('ResilientCity AI | Real Flood Cases Research')
    root.geometry('1080x740'); root.minsize(720, 520)
    style = ttk.Style(root); style.theme_use('clam')
    style.configure('TFrame', background='#102b3a')
    style.configure('TLabel', background='#102b3a', foreground='#eff7fa')
    style.configure('Title.TLabel', font=('Segoe UI', 19, 'bold'))
    shell = ttk.Frame(root, padding=18); shell.pack(fill='both', expand=True)
    ttk.Label(shell, text='RESILIENTCITY AI', style='Title.TLabel').pack(anchor='w')
    ttk.Label(shell, text='Real Flood Cases Research • v0.2 • retrospective validation pending').pack(anchor='w', pady=(2,14))
    tools = ttk.Frame(shell); tools.pack(fill='x')
    catalog = load_catalog(ROOT/'data/catalog.json')
    selection = ttk.Combobox(tools, values=[c['title'] for c in catalog], state='readonly', width=42)
    selection.pack(side='left', padx=(0,8)); selection.current(0)
    mode = ttk.Combobox(tools, values=['offline', 'gemini'], state='readonly', width=10)
    mode.pack(side='left', padx=8); mode.current(0)
    actions = ttk.Frame(shell); actions.pack(fill='x', pady=(8,0))
    tabs = ttk.Notebook(shell); tabs.pack(fill='both', expand=True, pady=14)
    editor = ScrolledText(tabs, wrap='word', font=('Consolas',11), undo=True)
    results = ScrolledText(tabs, wrap='word', font=('Consolas',11))
    sources_view = ScrolledText(tabs, wrap='word', font=('Segoe UI',11))
    tabs.add(editor, text='Case & evidence JSON'); tabs.add(sources_view, text='Sources & registration'); tabs.add(results, text='Report & agent trace')
    status = tk.StringVar(value='Offline mode tests the workflow. Add verified evidence before Gemini analysis.')
    ttk.Label(shell, textvariable=status, wraplength=950).pack(anchor='w')
    messages = queue.Queue()
    last_folder = [None]
    busy = [False]
    def show_registration(case):
        sources_view.configure(state='normal'); sources_view.delete('1.0','end')
        lines = [case['title'], 'ID: '+case['incident_id'],
                 'Validation: '+case.get('validation_status','pending'),
                 'Cutoff: '+str(case.get('evidence_cutoff') or 'PENDING — select a justified decision time'),
                 'Evidence entries: '+str(len(case.get('evidence',[]))),
                 'Source candidates: '+str(len(case.get('sources',[]))),
                 '', 'Missing: '+ '; '.join(case.get('missing',[])),
                 '', 'SOURCE CANDIDATES (not admitted evidence)']
        for src in case.get('sources',[]):
            lines += ['', src.get('title','Untitled'), src.get('url',''),
                      src.get('publisher','')+' | '+src.get('publication_label','Unknown date'),
                      'Role: '+src.get('source_role','pending'),
                      'Access: '+src.get('access_status','pending'),
                      src.get('summary_paraphrase',''),src.get('notes','')]
        sources_view.insert('1.0','\n'.join(lines)); sources_view.configure(state='disabled')
    def load_case(event=None):
        if busy[0]: return
        editor.delete('1.0','end')
        case = catalog[selection.current()]
        editor.insert('1.0', json.dumps(case, indent=2, ensure_ascii=False))
        show_registration(case)
        status.set(str(len(catalog))+' registered cases • '+case['title']+' • retrospective validation pending')
    selection.bind('<<ComboboxSelected>>', load_case)
    def import_case():
        name = filedialog.askopenfilename(filetypes=[('Case JSON','*.json')])
        if not name: return
        try:
            case = validate_case(json.loads(Path(name).read_text(encoding='utf-8')))
            editor.delete('1.0','end'); editor.insert('1.0',json.dumps(case,indent=2,ensure_ascii=False)); show_registration(case)
        except Exception as exc: messagebox.showerror('Invalid case',str(exc))
    def save_case():
        try: case = validate_case(json.loads(editor.get('1.0','end')))
        except Exception as exc: messagebox.showerror('Invalid case',str(exc)); return
        name = filedialog.asksaveasfilename(defaultextension='.json',filetypes=[('Case JSON','*.json')])
        if name: Path(name).write_text(json.dumps(case,indent=2,ensure_ascii=False),encoding='utf-8')
    def register():
        nonlocal catalog
        if busy[0]: return
        try:
            case = validate_case(json.loads(editor.get('1.0','end')))
            catalog = save_registration(ROOT/'data/catalog.json',case)
            selection.configure(values=[c['title'] for c in catalog])
            selection.current(next(i for i,c in enumerate(catalog) if c['incident_id']==case['incident_id']))
            show_registration(case)
            status.set('Registration saved locally • '+str(len(catalog))+' cases • no validation approval')
        except Exception as exc: messagebox.showerror('Registration',str(exc))
    def run():
        try: case = validate_case(json.loads(editor.get('1.0','end')))
        except Exception as exc: messagebox.showerror('Invalid case',str(exc)); return
        chosen = mode.get()
        from research.engine import partition
        if chosen == 'gemini' and partition(case)[0] and not messagebox.askokcancel('Gemini analysis',
                'Send admitted evidence excerpts and intermediate agent outputs to Google Gemini? This run may make up to 5 agent calls plus retries.'): return
        busy[0] = True; run_button.configure(state='disabled'); selection.configure(state='disabled')
        status.set('Running research workflow…'); tabs.select(results)
        def worker():
            try: messages.put(('done',Engine(ROOT/'outputs',chosen).run(case)))
            except Exception as exc: messages.put(('error',type(exc).__name__ + ': ' + str(exc)))
        threading.Thread(target=worker,daemon=True).start()
    def poll():
        try:
            kind, value = messages.get_nowait()
            busy[0] = False; run_button.configure(state='normal'); selection.configure(state='readonly')
            if kind == 'error': status.set('Run failed'); messagebox.showerror('Research run',value)
            else:
                report, folder = value; last_folder[0] = folder
                results.delete('1.0','end'); results.insert('1.0',(folder/'report.md').read_text(encoding='utf-8'))
                results.insert('end','\n\nACTUAL EXECUTION TRACE\n'+(folder/'trace.jsonl').read_text(encoding='utf-8'))
                status.set(report['safety']['research_state'] + ' • Reports saved: ' + str(folder))
        except queue.Empty: pass
        root.after(150,poll)
    def export():
        if not last_folder[0]: messagebox.showinfo('Export','Run one analysis first.'); return
        name = filedialog.asksaveasfilename(defaultextension='.md',filetypes=[('Markdown report','*.md')])
        if name: Path(name).write_bytes((last_folder[0]/'report.md').read_bytes())
    ttk.Button(actions,text='Import',command=import_case).pack(side='left',padx=4)
    ttk.Button(actions,text='Export case',command=save_case).pack(side='left',padx=4)
    ttk.Button(actions,text='Register / update',command=register).pack(side='left',padx=4)
    run_button = ttk.Button(actions,text='Run research',command=run); run_button.pack(side='left',padx=4)
    ttk.Button(actions,text='Export',command=export).pack(side='left',padx=4)
    load_case(); poll(); root.mainloop()
if __name__ == '__main__': launch()
