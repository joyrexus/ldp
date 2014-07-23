'''Test suite for our list utility functions.'''

from util.list import *

def test_stretch():
    '''Testing stretch()'''
    result = stretch(['a', 'b', 'c'], upto=6, alt='x')
    assert result == ['a', 'b', 'c', 'x', 'x', 'x']

    list = ['a', 'b', 'c']
    result = stretch(list, upto=3)

def test_chunk():
    '''Testing chunk()'''
    L = 'a b c d'.split(" ")
    assert chunk(L, 2) == [['a', 'b'], ['c', 'd']]
    assert chunk(L, 3) == [['a'], ['b', 'c'], ['d']]
    assert chunk(L, 4) == [['a'], ['b'], ['c'], ['d']]
    assert chunk(L, 5) == [['a'], ['b'], [], ['c'], ['d']]
    assert [11, 10, 11, 10, 11, 10, 11, 10, 11, 10] == \
           [len(x) for x in chunk(range(105), 10)]

def test_parts():
    '''Testing parts()'''
    L = 'a b c d'.split(" ")
    assert parts(L, 2) == [['a', 'b'], ['c', 'd']]
    assert parts(L, 3) == [['a', 'b'], ['c'], ['d']]
    assert parts(L, 4) == [['a'], ['b'], ['c'], ['d']]
    assert parts(L, 5) == [['a'], ['b'], ['c'], ['d'], []]
    assert [11, 11, 11, 11, 11, 10, 10, 10, 10, 10] == \
           [len(x) for x in parts(range(105), 10)]

def test_popm():
    '''Testing popm()'''
    L = ['alpha', 'beta', 'gamma', 'delta']
    expected = ['delta', 'beta', 'alpha']
    assert popm(L, 0, 1, 3) == expected, 'Popped elements returned'
    assert L == ['gamma'], 'List is modified'

def test_move():
    '''Testing move()'''
    A = ['alpha', 'beta', 'gamma', 'delta']
    B = []
    move(A, B, 1, 2)
    assert A == ['alpha', 'delta']
    assert B == ['gamma', 'beta']

def test_q_popm():
    '''Testing Queue.popm()'''
    units = Queue('units', ['alpha', 'beta', 'gamma', 'delta'])
    assert units.name == 'units'
    assert units.popm(1, 3) == ['delta', 'beta'], 'Popped elements returned'
    assert units == ['alpha', 'gamma'], 'Queue is modified'

def test_q_pop_to():
    '''Testing Queue.pop_to()'''
    units = Queue('units', ['alpha', 'beta', 'gamma', 'delta'])
    omits = []
    units.pop_to(omits, 1, 2)
    assert omits == ['gamma', 'beta'], 'Elements moved to target'
    assert units == ['alpha', 'delta'], 'Queue is modified'

def test_paging():
    '''Testing paging features'''
    units = Queue('units', range(30))
    units.page_size = 4
    omits = Queue('omits', [])
    assert list(units.page()) == [(0,0), (1,1), (2,2), (3,3)]
    assert len(units.page.indices) == units.page.size
    assert list(units.page.indices) == [0, 1, 2, 3]
    assert list(units.page.values) == [0, 1, 2, 3]
    assert list(units.page(2)) == [(4,4), (5,5), (6,6), (7,7)]
    units.pop_to(omits, 1, 2)
    assert list(omits.page()) == [(0,2), (1,1)]
    assert list(units.page(1)) == [(0,0), (1,3), (2,4), (3,5)]
    assert list(units.page(2)) == [(4,6), (5,7), (6,8), (7,9)]
