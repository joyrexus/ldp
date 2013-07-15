from math import ceil


class Pager(object):
    '''
    Handle pagination of iterables.

    Takes a view size and the total size of the iterable as arguments.

    >>> page = Pager(3, range(5))
    >>> page.pages
    3
    >>> page.num
    1
    >>> page.values
    [0, 1, 2]
    >>> page.next()
    2
    >>> page.values
    [3, 4]

    '''
    def __init__(self, size, seq):
        self.size = size
        self.seq = seq
        self.num = 1

    def next(self):
        '''Increment page number.'''
        if self.has_next:
            self.num += 1
        return self.num

    def prev(self):
        '''Decrement page number.'''
        if self.has_prev:
            self.num -= 1
        return self.num

    @property
    def total(self):
        '''Total number of items in sequence.'''
        return len(self.seq)

    @property
    def pages(self):
        '''Return total number of pages.'''
        if self.total == 0:
            return 0
        else:
            return int(ceil(self.total / float(self.size)))

    @property
    def has_prev(self):
        return self.num > 1

    @property
    def has_next(self):
        return self.num < self.pages

    @property
    def indices(self):
        '''Return indices for current page.'''
        start = (self.num - 1) * self.size
        stop  = (start + self.size) if ((start + self.size) < self.total) \
                                    else self.total
        return range(start, stop)

    @property
    def values(self):
        '''Return iterator of values for current page.'''
        return (self.seq[i] for i in self.indices)

    def __call__(self, num=None):
        '''Return iterator of values for current page.'''
        if num:
            if num > self.pages: return []
            self.num = num
        return ((i, self.seq[i]) for i in self.indices)
