import time


class Counter(object):
    '''
    Track iterations and items iterated over.

    '''
    def __init__(self, desc=''):
        self.desc = desc
        self.starts, self.items = 0, 0

    def __call__(self, seq):
        '''Yield items in sequence while counting.'''
        self.starts += 1
        for i in seq:
            self.items += 1
            yield i

    def __repr__(self):
        results = "{0}\n  starts: {1}\n   items: {2}"
        return results.format(self.desc, self.starts, self.items)


class Timed: 
    '''
    Struct for holding/representing timed attributes.
    
    '''
    def __init__(self, **entries): self.__dict__.update(entries)

    def __repr__(self):
        args = ['{0}: {1}'.format(k, repr(v)) for (k,v) in vars(self).items()]
        return '\n'.join(sorted(args, reverse=True))


class Timer(object): 
    '''
    Utility for timing function calls.

    '''
    def __call__(self, f, *args):
        '''Call f with args and return Timed object.'''
        start = time.clock()
        result = f(*args)
        stop = time.clock()
        diff = stop - start
        return Timed(name=f.__name__, time=diff, result=result)

    def run(self, n, f, *args):
        ''''
        Call f with args n-times (if int) returning min, avg, max.

        If n is a float then call f for up to n-seconds.

        '''
        times = []
        results = []
        if type(n) is int:
            for _ in range(n):
                r = self(f, *args)      # timed object returned
                times.append(r.time)
                results.append(r.result)
        else:
            start, last = time.clock(), 0
            while last - start < n:
                times.append(self(f, *args).time)
                last = time.clock()
        return Timed(name=f.__name__, results=results, 
                                      times=times,
                                      min=min(times), 
                                      max=max(times),
                                      avg=self.avg(times), n=n)

    def avg(self, nums):
        'Return average (mean) of a sequence of numbers.'
        return sum(nums) / float(len(nums))


# simpler version of Timer
def timer(func, *args):
    '''Call func with args and return time in secs and result.'''
    start = time.clock()
    result = func(*args)
    stop = time.clock()
    return stop - start, result


if __name__ == '__main__':

    def fact(n):
        return 1 if n <= 1 else n * fact(n - 1)
    def ffact(n):
        return 1 if n <= 1 else fact(n) * ffact(n - 1)

    print timer(map, ffact, [1,2,3])

    timer = Timer()
    n = 25
    t = timer(ffact, n)
    print '{0}({1}) took {2} secs to run'.format(t.name, n, t.time)
    print
    t = timer.run(1.0, ffact, n)
    print '{0}({1}) took {2} secs to run on average'.format(t.name, n, t.avg)
    print
    count = Counter('Iterations over foo')
    for i in range(5):
        for j in count(range(10)): fact(10)
    print count
    t = timer.run(10, ffact, n)
    print t

