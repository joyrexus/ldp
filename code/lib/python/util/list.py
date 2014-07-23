'''Basic list and queueing utilities.'''

def stretch(list, upto, alt=''):
    if len(list) < upto:
        return [list[i] if len(list) > i else alt for i in range(upto)]
    else:
        return list

def parts(L, n):
    '''
    Partition L into n parts using every item in L and 
    such that the resulting chunks differ in size by 
    at most one element.

    >>> L = ['a', 'b', 'c', 'd']
    ['a', 'b', 'c', 'd']
    >>> parts(L, 2)
    [['a', 'b'], ['c', 'd']]
    >>> parts(L, 3)
    [['a', 'b'], ['c'], ['d']]
    >>> parts(L, 4)
    [['a'], ['b'], ['c'], ['d']]
    >>> parts(L, 5)
    [['a'], ['b'], ['c'], ['d'], []]

    '''
    q, r = divmod(len(L), n)
    I = [q*i + min(i, r) for i in xrange(n+1)]
    return [L[I[i]:I[i+1]] for i in xrange(n)]

def chunk(L, n): 
    '''
    Partition L into n chunks using every item in L
    and such that the resulting chunks differ in size
    by at most one element.

    '''
    size = len(L) / float(n) 
    I = lambda i: int(round(i))
    return [ L[I(size*i):I(size*(i+1))] for i in xrange(n) ]

def popm(arr, *args):
    '''
    Pop multiple items from an array by index. 
    
    Returns an array of popped elements in index descending order:

        >>> L = ['alpha', 'beta', 'gamma', 'delta']
        >>> popm(L, 0, 1, 3)
        ['delta', 'beta', 'alpha']
        >>> L
        ['gamma']
    
    '''
    popped = []
    for i in sorted(args, reverse=True):
        popped.append(arr.pop(i))
    return popped

def move(source, target, *indices):
    '''
    Remove elements at indices from source and append to target.

    Both source and target are assumed to be mutable lists.

        >>> A = ['alpha', 'beta', 'gamma', 'delta']
        >>> B = []
        >>> move(source=A, target=B, 1, 2)
        >>> A
        ['alpha', 'delta']
        >>> B
        ['gamma', 'beta']

    '''
    target.extend(popm(source, *indices))


from util.page import Pager

class Queue(list):
    '''
    Our Queue class adds a few methods to standard lists.
    
        >>> q = Queue('units', ['alpha', 'beta', 'gamma', 'delta'])
        >>> q.name
        'units'
        >>> p = q.popm(1, 3)
        >>> p
        ['delta', 'beta']
        >>> q
        ['alpha', 'gamma']
        >>> q.pop_to(p, 0, 1)
        >>> p
        ['delta', 'beta', 'gamma', 'alpha']
        >>> q
        []

    '''
    def __init__(self, name, seq=[]):
        list.__init__(self, seq)
        self.name = name
        self.page = Pager(size=10, seq=self)

    @property
    def page_size(self):
        return self.page.size

    @page_size.setter
    def page_size(self, size):
        self.page.size = size

    def popm(self, *indices):
        '''Pop elements at indices.
        
        >>> q = Queue('units', ['alpha', 'beta', 'gamma', 'delta'])
        >>> q.popm(1, 3)
        ['delta', 'beta']
        >>> q
        ['alpha', 'gamma']

        '''
        popped = []
        for i in sorted(indices, reverse=True):
            popped.append(self.pop(i))
        return popped

    def pop_to(self, target, *indices):
        '''Pop elements at indices and append to target.

        >>> q = Queue('units', ['alpha', 'beta', 'gamma', 'delta'])
        >>> p = []
        >>> q.pop_to(p, 1, 2)
        >>> p
        ['gamma', 'beta']
        >>> q
        ['alpha', 'delta']

        '''
        if not indices:
            indices = range(len(self))
        target.extend(self.popm(*indices))
        return target


if __name__ == '__main__':

    ## parts and chunk demo/comparison

    L = 'a b c d'.split(" ")

    assert parts(L, 2) == [['a', 'b'], ['c', 'd']]
    assert parts(L, 3) == [['a', 'b'], ['c'], ['d']]
    assert parts(L, 4) == [['a'], ['b'], ['c'], ['d']]
    assert parts(L, 5) == [['a'], ['b'], ['c'], ['d'], []]

    assert chunk(L, 2) == [['a', 'b'], ['c', 'd']]
    assert chunk(L, 3) == [['a'], ['b', 'c'], ['d']]
    assert chunk(L, 4) == [['a'], ['b'], ['c'], ['d']]
    assert chunk(L, 5) == [['a'], ['b'], [], ['c'], ['d']]

    assert [11, 11, 11, 11, 11, 10, 10, 10, 10, 10] == \
           [len(x) for x in parts(range(105), 10)]

    assert [11, 10, 11, 10, 11, 10, 11, 10, 11, 10] == \
           [len(x) for x in chunk(range(105), 10)]

    # demo of Queue

    units = Queue('units', ['alpha', 'beta', 'gamma', 'delta'])
    omits = Queue('omits', [])

    assert units == ['alpha', 'beta', 'gamma', 'delta']
    assert omits == []
    units.pop_to(omits) # popping to omits
    assert omits == ['delta', 'gamma', 'beta', 'alpha']
    assert units == []

    units = Queue('units', ['alpha', 'beta', 'gamma', 'delta'])
    omits = Queue('omits')

    assert units.name is "units"
    units.pop_to(omits, 1, 2)           # pop items with index 1 and 2
    assert units == ['alpha', 'delta']  # remaining in units
    assert omits == ['gamma', 'beta']   # now in omits"

    units = Queue('units', ['alpha', 'beta', 'gamma', 'delta'])
    popped = units.popm(1, 3)           # pop items with index 1 and 3
    assert popped == ['delta', 'beta']  # popped from units
    assert units == ['alpha', 'gamma']  # remaining in units
    assert units.popm(0, 1) == ['gamma', 'alpha']
    assert not units                    # and now units is empty!

    '''
    units = Queue('units', range(30))
    units.page_size = 5
    omits = Queue('omits', [])
    omits.page_size = 5
    print 'page 1 of units:'
    for i, num in units.page(1): print i, num
    print 'page 2 of units:'
    for i, num in units.page(2): print i, num
    print 'popping off items with index 1 and 2'
    units.pop_to(omits, 1, 2)
    print 'page 1 of units:'
    for i, num in units.page(1): print i, num
    print 'page 2 of units:'
    for i, num in units.page(2): print i, num
    print 'omits:'
    for i, num in omits.page(): print i, num
    '''

