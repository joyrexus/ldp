import os
from nose.tools import with_setup
from util.count import Counter, FeatureCounter

def setup():
    '''Set up test fixtures.'''
    global count
    count = Counter('Test Counter')

def teardown():
    '''Tear down test fixtures'''
    count.clear()

@with_setup(setup, teardown)
def test_init():
    '''Test Counter'''
    assert count.desc == "Test Counter"

@with_setup(setup, teardown)
def test_inc():
    '''Test increment method'''
    count.inc(3)
    assert count.total == 3
    count.inc()
    assert count.total == 4

@with_setup(setup, teardown)
def test_clear():
    '''Test clear method'''
    count.inc(3)
    assert count.total == 3
    count.clear()
    assert count.total == 0

@with_setup(setup, teardown)
def test_call():
    '''Test call method'''
    count(3)
    assert count.total == 3
    count()
    assert count.total == 4
