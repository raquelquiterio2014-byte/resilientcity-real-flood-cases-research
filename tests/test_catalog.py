import copy
import json
import tempfile
import unittest
from pathlib import Path
from research.catalog import load_catalog, save_registration
from research.engine import Engine, validate_case
ROOT=Path(__file__).resolve().parents[1]
class RegistryTests(unittest.TestCase):
    def test_ten_cases_and_sources(self):
        data=load_catalog(ROOT/'data/catalog.json')
        self.assertEqual(len(data),10)
        self.assertEqual(sum(len(c['sources']) for c in data),24)
        self.assertEqual(sum(c['evidence_cutoff'] is None for c in data),9)
        self.assertTrue(all(not c['evidence'] for c in data))
    def test_persistence_upsert(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'catalog.json';path.write_bytes((ROOT/'data/catalog.json').read_bytes())
            case=load_catalog(path)[1];case['notes']='changed'
            self.assertEqual(len(save_registration(path,case)),10)
            self.assertEqual(load_catalog(path)[1]['notes'],'changed')
            case=copy.deepcopy(case);case['incident_id']='NEW';case['title']='New registration'
            self.assertEqual(len(save_registration(path,case)),11)
            self.assertEqual(len(load_catalog(path)),11)
    def test_pending_cutoff_never_calls_gateway(self):
        case=load_catalog(ROOT/'data/catalog.json')[1]
        case['evidence']=[{'id':'E1','url':'https://example.org/test','publisher':'Test',
            'published_at':'2024-10-01T08:00:00Z','available_at':'2024-10-01T08:00:00Z',
            'excerpt':'Unit fixture','verified':True}]
        class FailIfCalled:
            model='mock'
            def generate(self,*args): raise AssertionError('Must not call LLM')
        with tempfile.TemporaryDirectory() as d:
            report,_=Engine(d,'gemini',FailIfCalled()).run(case)
        self.assertIn('Evidence cutoff pending researcher selection',report['safety']['issues'])
        self.assertEqual(report['safety']['research_state'],'BLOCKED')
        self.assertEqual(report['admitted_evidence_ids'],[])
        self.assertEqual(report['excluded'][0]['id'],'E1')
    def test_research_sources_not_in_prompt(self):
        case=load_catalog(ROOT/'data/catalog.json')[0]
        case['sources']=[{'summary_paraphrase':'SOURCE_SECRET_MARKER'}]
        case['evidence']=[{'id':'E1','url':'https://example.org/test','publisher':'Test',
            'published_at':'2023-11-01T08:00:00Z','available_at':'2023-11-01T08:00:00Z',
            'excerpt':'Unit fixture','verified':True}]
        calls=[]
        class Fake:
            model='mock'
            def generate(self,role,state):
                calls.append(json.dumps(state))
                return {'summary':'Test','evidence_ids':['E1'],'uncertainties':[],
                        'abstain':False,'revision_required':False}
        with tempfile.TemporaryDirectory() as d: Engine(d,'gemini',Fake()).run(case)
        self.assertEqual(len(calls),5)
        self.assertNotIn('SOURCE_SECRET_MARKER',''.join(calls))
    def test_duplicate_registry_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'catalog.json';case=load_catalog(ROOT/'data/catalog.json')[0]
            path.write_text(json.dumps([case,case]))
            with self.assertRaises(ValueError):load_catalog(path)
    def test_bad_cutoff_still_rejected(self):
        case=load_catalog(ROOT/'data/catalog.json')[1];case['evidence_cutoff']='unknown'
        with self.assertRaises(ValueError):validate_case(case)
