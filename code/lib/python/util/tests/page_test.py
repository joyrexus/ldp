from util.page import Pager
from nose.tools import with_setup

page = None

def setup():
    '''Set up test fixtures.'''
    global page
    page = Pager(size=3, seq=range(8))

@with_setup(setup)
def test_init():
    '''Testing init'''
    assert page.size == 3

@with_setup(setup)
def test_pages():
    '''Testing pages'''
    assert page.pages == 3
    assert Pager(3, range(10)).pages == 4
    assert Pager(3, range(2)).pages == 1
    assert Pager(3, []).pages == 0

@with_setup(setup)
def test_num():
    '''Testing next, prev, and num'''
    assert page.num == 1
    assert page.next() == 2
    assert page.num == 2
    assert page.next() == 3
    assert page.num == 3
    assert page.next() == 3
    assert page.num == 3
    assert page.prev() == 2
    assert page.num == 2
    assert page.prev() == 1
    assert page.num == 1
    assert page.prev() == 1
    assert page.num == 1

@with_setup(setup)
def test_indices():
    '''Testing indices'''
    assert page.num == 1
    assert page.size == 3
    assert page.indices == [0, 1, 2]
    assert page.next() == 2
    assert page.indices == [3, 4, 5]
    assert page.next() == 3
    assert page.indices == [6, 7]

@with_setup(setup)
def test_values():
    '''Testing values'''
    assert page.num == 1
    assert list(page.values) == [0, 1, 2]
    assert page.next() == 2
    assert list(page.values) == [3, 4, 5]
    assert page.next() == 3
    assert list(page.values) == [6, 7]

def new_setup():
    '''Set up new test fixtures.'''
    global page
    page = Pager(2, ['a', 'b', 'c'])

@with_setup(new_setup)
def test_call():
    '''Testing __call__'''
    assert list(page.values) == ['a', 'b']
    assert list(page()) == [(0,'a'), (1,'b')]
    assert page.next() == 2
    assert list(page.values) == ['c']
    assert list(page()) == [(2,'c')]
    assert list(page(1)) == [(0,'a'), (1,'b')]
    assert list(page(4)) == []


