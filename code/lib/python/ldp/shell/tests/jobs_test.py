import os
from ldp.shell.jobs import indexargs, Runner, Editor

PWD = os.path.dirname(__file__) or '.'
PATH = PWD + '/../../jobs/tests/jobfiles'
runner = Runner(PATH)

def test_indexargs():
    '''Testing indexargs decorator'''
    class Bar(): viz_qsize = 20
    @indexargs
    def foo(self, *indices): return indices
    assert foo(Bar(), "1 2 3 x 5") == (1, 2, 3, 5)
    assert foo(Bar(), "1-5") == (1, 2, 3, 4, 5)
    assert foo(Bar(), "1-5 9 22") == (1, 2, 3, 4, 5, 9, 22)
    assert foo(Bar(), "1-3 5 9-10") == (1, 2, 3, 5, 9, 10)

def test_init():
    '''Testing init method'''
    assert len(runner.jobfiles.keys()) == 4

def test_issue():
    '''Testing issue method''' 
    assert runner.issue('spelling') == 'spelling corrections'

def test_kind():
    '''Testing kind method''' 
    assert runner.kind('spelling') == 'BatchSuspectSubstring'

def test_options():
    '''Testing options property'''
    expected = [('scratch', u'spelling corrections'), 
                ('spelling', u'spelling corrections'), 
                ('times', u'time conversion'),
                ('schema', u'ISSUE DESCRIPTION')]
    assert runner.options == expected

def test_edit_cache():
    '''Testing edit cache'''
    pass
