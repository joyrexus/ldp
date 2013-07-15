from collections import Counter

class Freq(Counter): 

    def __getattr__(self, var):
        if var in self: return self[var]

    def __setattr__(self, var, value):
        if var in self: 
            self[var] = value
        else:
            self.__dict__[var] = value

    @property
    def avg(self):
        '''Average of values in distribution.'''
        return self.sum / len(self)

    @property
    def sum(self):
        '''Sum of values in distribution.'''
        return sum(self.values()) * 1.0

    @property
    def max(self):
        '''Element with maximum value in distribution.'''
        return self.most_common(1)[0]

    @property
    def maxvar(self):
        return self.most_common(1)[0][0]

    @property
    def maxval(self):
        '''Maximum value in distribution.'''
        return self.most_common(1)[0][1]

    def least_common(self, n):
        '''Return n least elements distribution.'''
        return self.most_common()[:-(n+1):-1]

    @property
    def min(self):
        '''Element with minimum value in distribution.'''
        return self.least_common(1)[0]

    @property
    def minvar(self):
        '''Variable with minimum value in distribution.'''
        return self.least_common(1)[0][0]

    @property
    def minval(self):
        '''Minimum value in distribution.'''
        return self.least_common(1)[0][1]

    def measure(self):
        '''Get the probability measure of the current distribution.'''
        self.prob = Freq()
        total = 1.0 * self.sum
        for e, n in self.items():
            self.prob[e] = n / total
        return self.prob


if __name__ == '__main__':

    freq = Freq(a=1, b=3, c=6)
    assert 'a' in freq
    assert freq['a'] == 1
    assert freq.a == 1
    assert freq.b == 3
    assert freq.c == 6
    freq.c += 1
    assert freq.c == 7
    freq.c -= 1
    assert freq.c == 6
    assert freq.sum == 10
    assert freq.max == ('c', 6)
    assert freq.maxvar == 'c'
    assert freq.maxval == 6
    assert freq.most_common(2) == [('c', 6), ('b', 3)]
    assert freq.least_common(2) == [('a', 1), ('b', 3)]
    assert freq.min == ('a', 1)
    assert freq.minvar == 'a'
    assert freq.minval == 1
    prob = freq.measure()
    assert freq.prob.a == .1
    assert freq.prob.b == .3
    assert freq.prob.c == .6
    assert prob.a == .1
    assert prob.b == .3
    assert prob.c == .6
    assert 3.3 < freq.avg < 3.4
