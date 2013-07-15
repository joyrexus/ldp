def parts(L, n):
    '''
    Partition L into n parts using every item in L
    and such that the resulting chunks differ in size
    by at most one element.

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


if __name__ == '__main__':

    # sample usage
    L = 'a b c d'.split(" ")
    assert parts(L, 2) == [['a', 'b'], ['c', 'd']]
    assert parts(L, 3) == [['a', 'b'], ['c'], ['d']]
    assert parts(L, 4) == [['a'], ['b'], ['c'], ['d']]
    assert parts(L, 5) == [['a'], ['b'], ['c'], ['d'], []]

    L = 'a b c d'.split(" ")
    assert chunk(L, 2) == [['a', 'b'], ['c', 'd']]
    assert chunk(L, 3) == [['a'], ['b', 'c'], ['d']]
    assert chunk(L, 4) == [['a'], ['b'], ['c'], ['d']]
    assert chunk(L, 5) == [['a'], ['b'], [], ['c'], ['d']]

    def check(L, n, verbose=True):
        '''
        Check that list L gets partitioned into n chunks 
        and that the total items in the resulting chunks 
        is equal to the size of the original list L.

        '''
        chunks = chunk(L, n)
        size = len(L)
        assert len(chunks) == n
        assert size == sum(len(chunk) for chunk in chunks)
        if verbose:
            msg = "\nYou want a list with {} items split into {} chunks"
            print msg.format(size, n)
            print "{} chunks produced:".format(len(chunks))
            for i, x in enumerate(chunks):
                print "\tchunk {}, size {}".format(i+1, len(x))

    L = range(1, 101)

    # for each p, check that L gets partitioned into p chunks
    for p in range(1, 10): check(L, p, verbose=False)

    L = 'a b c d'.split(" ")
    assert parts(L, 2) == [['a', 'b'], ['c', 'd']]
    assert parts(L, 3) == [['a', 'b'], ['c'], ['d']]
    assert parts(L, 4) == [['a'], ['b'], ['c'], ['d']]
    assert parts(L, 5) == [['a'], ['b'], ['c'], ['d'], []]

    # parts and chunk comparison
    assert [11, 11, 11, 11, 11, 10, 10, 10, 10, 10] == \
           [len(x) for x in parts(range(105), 10)]
    assert [11, 10, 11, 10, 11, 10, 11, 10, 11, 10] == \
           [len(x) for x in chunk(range(105), 10)]

