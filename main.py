import argparse
import json
from pathlib import Path
from research.engine import Engine
ROOT = Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--case', help='Path to case JSON; omit to open GUI')
    parser.add_argument('--mode', choices=['offline', 'gemini'], default='offline')
    args = parser.parse_args()
    if args.case:
        report, folder = Engine(ROOT / 'outputs', args.mode).run(json.loads(Path(args.case).read_text(encoding='utf-8')))
        print(report['safety']['research_state'], folder)
    else:
        from gui import launch
        launch()
if __name__ == '__main__': main()
