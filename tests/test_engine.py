import copy
import json
import tempfile
import unittest
from pathlib import Path
from research.engine import Engine, partition, validate_case, validate_output

class Tests(unittest.TestCase):
    def setUp(self):
        self.case = {'incident_id':'TEST','title':'Unit fixture (not a real event)',
                     'location':'Test location','evidence_cutoff':'2023-11-06T08:00:00Z','evidence':[]}
        self.e = {'id':'E1','url':'https://example.org/test','publisher':'Test',
                  'published_at':'2023-11-06T07:00:00Z','available_at':'2023-11-06T07:00:00Z',
                  'excerpt':'Synthetic unit test only','verified':True}
    def test_empty_abstains(self):
        with tempfile.TemporaryDirectory() as d:
            report, folder = Engine(d).run(self.case)
            self.assertEqual(report['safety']['research_state'],'BLOCKED')
            trace = [json.loads(x) for x in (folder/'trace.jsonl').read_text().splitlines()]
            self.assertEqual(len(trace),8)
            self.assertTrue((folder/'report.md').is_file())
            self.assertFalse(report['safety']['operational_authorization'])
    def test_cutoff(self):
        self.case['evidence'] = [self.e,dict(self.e,id='E2',available_at='2023-11-07T07:00:00Z')]
        admitted, excluded = partition(self.case)
        self.assertEqual([e['id'] for e in admitted],['E1']); self.assertEqual(excluded[0]['id'],'E2')
    def test_unverified(self):
        self.case['evidence'] = [dict(self.e,verified=False)]
        self.assertFalse(partition(self.case)[0])
    def test_duplicate(self):
        self.case['evidence'] = [self.e,self.e]
        with self.assertRaises(ValueError): validate_case(self.case)
    def test_naive_date(self):
        self.case['evidence_cutoff']='2023-11-06T08:00:00'
        with self.assertRaises(ValueError): validate_case(self.case)
    def test_unknown_citation(self):
        with self.assertRaises(ValueError):
            validate_output({'summary':'x','evidence_ids':['FAKE'],'uncertainties':[],
                             'abstain':False,'revision_required':False},{'E1'})
    def test_dependency_and_leakage(self):
        calls=[]
        class Fake:
            model='mock'
            def generate(s,role,state):
                calls.append((role,copy.deepcopy(state)))
                return {'summary':'Test only','evidence_ids':['E1'],'uncertainties':[],
                        'abstain':False,'revision_required':False}
        self.case['evidence']=[self.e,dict(self.e,id='LATE',published_at='2023-11-07T09:00:00Z',available_at='2023-11-07T09:00:00Z')]
        with tempfile.TemporaryDirectory() as d:
            report,_=Engine(d,'gemini',Fake()).run(self.case)
        self.assertEqual(len(calls),5)
        self.assertIn('Decision',calls[-1][1]['agents'])
        self.assertNotIn('LATE',json.dumps(calls))
        self.assertEqual(report['safety']['research_state'],'REVIEW_REQUIRED')
        self.assertFalse(report['safety']['operational_authorization'])
    def test_failure_stops_calls(self):
        calls=[]
        class Broken:
            model='mock'
            def generate(s,role,state): calls.append(role); raise RuntimeError('mock failure')
        self.case['evidence']=[self.e]
        with tempfile.TemporaryDirectory() as d:
            report,_=Engine(d,'gemini',Broken()).run(self.case)
        self.assertEqual(len(calls),1)
        self.assertEqual(report['safety']['research_state'],'BLOCKED')
    def test_critic_blocks(self):
        class Fake:
            model='mock'
            def generate(s,role,state):
                return {'summary':'Test only','evidence_ids':['E1'],'uncertainties':[],
                        'abstain':False,'revision_required':role=='Critic'}
        self.case['evidence']=[self.e]
        with tempfile.TemporaryDirectory() as d:
            report,_=Engine(d,'gemini',Fake()).run(self.case)
        self.assertIn('Critical revision required',report['safety']['issues'])
if __name__=='__main__': unittest.main()
