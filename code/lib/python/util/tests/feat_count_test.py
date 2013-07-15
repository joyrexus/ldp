import os
from nose.tools import with_setup
from collections import defaultdict
from util.count import FeatureCounter

def setup():
    "Set up test fixtures."
    global count
    count = FeatureCounter('Subject', 'Session', 'Alpha', 'Beta')

def teardown():
    "Tear down test fixtures"
    count.clear()

def test_init():
    'Test initialization'
    assert type(count.feature['Subject']) == defaultdict
    assert type(count.feature['Session']) == defaultdict
    assert type(count.feature['Alpha']) == defaultdict
    assert type(count.feature['Beta']) == defaultdict
    assert count.features == ['Subject', 'Session', 'Alpha', 'Beta']

@with_setup(setup, teardown)
def test_inc():
    'Test increment method'
    count.inc(100, 1, 'A', 'B')
    assert count.counts == {(100, 1, 'A', 'B'): 1}
    count.inc(100, 1, 'A', 'B', amount=5), "increment by 5"
    assert count.counts == {(100, 1, 'A', 'B'): 6}
    count.dec(100, 1, 'A', 'B', amount=5), "decrement by 5"
    assert count.counts == {(100, 1, 'A', 'B'): 1}

@with_setup(setup, teardown)
def test_clear():
    'Test clear method'
    count.inc(100, 1, 'A', 'B')
    assert count.counts == {(100, 1, 'A', 'B'): 1}
    count.clear()
    assert count.counts == {}

@with_setup(setup, teardown)
def test_total():
    'Test total method'
    count.inc(100, 1, 'A', 'B')
    assert count.total(100, 1, 'A', 'B') == 1
    assert count.total(100, 1) == 1
    assert count.total(Subject=100) == 1
    count.inc(100, 1, 'A', 'X')
    assert count.total(100, 1, 'A', 'B') == 1
    assert count.total(100, 1, 'A') == 2
    assert count.total(100, 1) == 2
    assert count.total(100) == 2
    assert count.total(Subject=100) == 2
    assert count.total(Alpha="A") == 2
    assert count.total(Beta="B") == 1
    assert count.TOTAL == 8

@with_setup(setup, teardown)
def test_getitem():
    'Test getitem method'
    count.inc(100, 1, 'A', 'X')
    count.inc(100, 1, 'A', 'Y')
    assert count[100, 1, 'A', 'X'] == 1
    assert count[100, 1, 'A', 'Y'] == 1
    assert count[100, 1, 'A'] == 2
    assert count[100, 1] == 2
    assert count[100] == 2
    assert count[None, 1] == 2
    assert count[None, 2] == 0
    assert count[None, None, 'A'] == 2
    assert count[None, None, None, 'X'] == 1

@with_setup(setup, teardown)
def test_valuetuple():
    'Test valuetuple method'
    count.inc(100, 1, 'A', 'X')
    count.inc(100, 1, 'A', 'Y')
    v = count._valuetuple(Subject=100, Alpha='A')
    assert v == (100, None, 'A', None)
    assert count[v] == 2
    v = count._valuetuple(Subject=100, Beta='X')
    assert v == (100, None, None, 'X')
    assert count[v] == 1

@with_setup(setup, teardown)
def test_call():
    'Test call method'
    assert count[100, 1, 'A', 'B'] == 0
    count(100, 1, 'A', 'B')
    assert count[100, 1, 'A', 'B'] == 1
    assert count[100, 1, 'A'] == 1
    count(100, 1, 'A', 'B')
    assert count[100, 1, 'A', 'B'] == 2
    count(100, 1, 'A', 'B', amount=10), "increment by 10"
    assert count[100, 1, 'A', 'B'] == 12

@with_setup(setup, teardown)
def test_value():
    'Test value method'
    count(111, 1, 'A', 'B')
    count(222, 1, 'A', 'B')
    assert count.value('Subject', 111) == 1
    assert count.value('Subject', 222) == 1
    assert count.value('Session', 1) == 2
    assert count.value('Alpha', 'A') == 2
    assert count.value('Beta', 'B') == 2

@with_setup(setup, teardown)
def test_values():
    'Test values method'
    count(111, 1, 'A', 'B')
    count(222, 1, 'A', 'B')
    assert count.values('Subject') == [111, 222]
    assert count.values('Session') == [1]
    assert count.values('Alpha') == ['A']

def test_match():
    'Test match method'
    assert count._match(['a', None], ['a', 'b']) == True
    assert count._match([None, 'a'], ['a', 'b']) == False
    assert count._match(['a', 'c'], ['a', 'b']) == False
    assert count._match(['a', 'b'], ['a', 'b', 'c']) == True
    assert count._match(['a', 'b', 'c'], ['a', 'b']) == True
    assert count._match(['a', 'b', None], ['a', 'b']) == True

def test_insert():
    'Test insert method'
    assert count._insert(['a', 'c'], 'b', 1) == ('a', 'b', 'c')
    assert count._insert(['b', 'c'], 'a', 0) == ('a', 'b', 'c')

def test_join():
    'Test join method'
    assert count._join(range(3), newline=True) == '0\t1\t2\n'


report = [['Subject', 'Session', 'Code', 'Total'],
          [100, 1, 'A', 1],
          [100, 1, 'B', 1],
          [100, 2, 'C', 1]]

report_by_sess = [['Subject', 'Code', 1, 2],
                  [100, 'A', 1, 0],
                  [100, 'B', 1, 0],
                  [100, 'C', 0, 1]]

def new_setup():
    "Set up new test fixtures."
    global count
    count = FeatureCounter('Subject', 'Session', 'Code')

@with_setup(new_setup, teardown)
def test_report():
    'Test report method'
    count(100, 1, 'A')
    count(100, 1, 'B')
    count(100, 2, 'C')
    assert count.report() == report
    assert count.report('Session') == report_by_sess

subj_x_sess = [('Subject', (1,), (2,)), (111, 2, 1), (222, 1, 1)]

sess_x_subj = [('Session', (111,), (222,)), (1, 2, 1), (2, 1, 1)]

subj_x_code = [('Subject', ('A',), ('B',), ('C',)), 
               (111, 1, 1, 1), 
               (222, 1, 1, 0)]

sess_x_code = [('Session', ('A',), ('B',), ('C',)), 
               (1, 2, 1, 0), 
               (2, 0, 1, 1)]

subj_sess_x_code = [('Subject', 'Session', ('A',), ('B',), ('C',)),
                    (111, 1, 1, 1, 0),
                    (111, 2, 0, 0, 1),
                    (222, 1, 1, 0, 0),
                    (222, 2, 0, 1, 0)]

@with_setup(new_setup, teardown)
def test_pivot():
    'Test pivot method'
    count(111, 1, 'A')
    count(111, 1, 'B')
    count(111, 2, 'C')
    count(222, 1, 'A')
    count(222, 2, 'B')
    assert count.pivot(['Subject'], ['Session']) == subj_x_sess
    assert count.pivot(['Session'], ['Subject']) == sess_x_subj
    assert count.pivot(['Subject'], ['Code']) == subj_x_code
    assert count.pivot(['Session'], ['Code']) == sess_x_code
    assert count.pivot(['Subject', 'Session'], ['Code']) == subj_sess_x_code

@with_setup(new_setup, teardown)
def test_dump():
    '''Test dump/load methods'''
    import util
    count(100, 1, 'A')
    count(100, 1, 'B')
    count(100, 2, 'C')
    assert 3 == count[100]
    assert 2 == count[100, 1]
    assert 1 == count[100, 1, 'A']
    count.dump('count.dat')
    c = util.count.load('count.dat')
    assert 3 == c[100]
    assert 2 == c[100, 1]
    assert 1 == c[100, 1, 'A']
    os.remove('count.dat')
