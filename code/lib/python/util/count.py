'''
util.count - basic counting and reporting utils.

'''
import pprint
from itertools import product
from collections import defaultdict

def load(file):
    '''Open a saved counter instance.'''
    import cPickle as pickle
    with open(file, 'rb') as f:
        return pickle.load(f)


class Counter(object):
    '''Simple count tracker.'''

    def __init__(self, desc='', amount=0):
        self.desc = desc
        self.total = amount

    def clear(self):
        self.total = 0

    def inc(self, amount=1):
        '''Increment count.'''
        self.total += amount
        return self.total

    def dec(self, amount=1):
        '''Decrement count.'''
        return self.inc(amount * -1)

    def __call__(self, amount=1):
        '''Increment count.'''
        return self.inc(amount)

    def dump(self, file):
        '''Save counter instance to file.'''
        import cPickle as pickle
        with open(file, 'wb') as f:
            pickle.dump(self, f)


class FeatureCounter(Counter):
    '''
    Count the values of a set of features.

    Initialize the counter with an ordered list of features:

    >>> count = FeatureCounter('Subject', 'Session', 'Code')

    You can then call the counter with a tuple of feature values (in the 
    same order) to increment the count of those feature values 
    as well as that particular combination of values:

    >>> count(100, 1, 'A')
    >>> count(100, 1, 'B')
    >>> count(100, 2, 'C')

    Use dictionary syntax to retrieve the count of particular 
    combinations of feature values:
    
    >>> count[100, 1, 'A']
    1
    >>> count[100, 1]
    2
    >>> count[100]
    3

    Use the report method to get a table of counts:

    >>> count.report()
    Subject Session Code    Total
    100     1       A       1
    100     1       B       1
    100     2       C       1

    You can specify a feature to get a breakdown of the values 
    for that feature:

    >>> count.report('Code')
    Subject Session A   B   C
    100     1       1   1   0
    100     2       0   0   1

    '''

    def __init__(self, *features):
        self.TOTAL = 0                  # sum of all feature value counts
        self.totals = defaultdict(int)  # cache totals when expensive
        self.counts = defaultdict(int)  # count feature value combinations
        self.feature = {}               # count values of individual features
        self.features = []              # list of features
        for f in features:
            self.features.append(f)
            self.feature[f] = defaultdict(int)

    def clear(self):
        '''Clear all counts.'''
        self.TOTAL = 0
        self.counts = defaultdict(int)
        self.totals = defaultdict(int)
        for f in self.features:
            self.feature[f] = defaultdict(int)

    def inc(self, *values, **kwargs):
        '''Increment count of each value and the value tuple.

        If *amount* keyword arg is given, increment by that amount.
        
        '''
        amount = kwargs.get('amount', 1)
        if len(values) < len(self.features):
            fs = ', '.join(self.features)
            msg = 'Need values for all features: {0}'.format(fs)
            raise ValueError(msg)
        for i, value in enumerate(values):
            self.feature[self.features[i]][value] += amount
            self.TOTAL += amount
        self.counts[tuple(values)] += amount

    def dec(self, *values, **kwargs):
        '''Decrement count of each value and the value tuple.'''
        minus = kwargs.get('amount', 1) * -1
        return self.inc(*values, amount=minus)

    def __call__(self, *values, **kwargs):
        '''Call increment method.'''
        return self.inc(*values, **kwargs)

    def total(self, *values, **kwargs):
        '''Get total of value tuple.'''
        if kwargs and not values:
            values = self._valuetuple(**kwargs)
        if len([v for v in values if v is not None]) < len(self.features):
            if tuple(values) in self.totals:
                return self.totals[tuple(values)]
            return sum(self.counts[k] for k in self.counts.keys() 
                                            if self._match(values, k))
        else:
            return self.counts[tuple(values)]

    def _valuetuple(self, **d):
        '''Return value tuple given feature/value pairs.

        Values are ordered to correspond to the feature sequence specified 
        when the FeatureCounter was initialized.
        
        >>> count = FeatureCounter('Subject', 'Session', 'Code')
        >>> count(100, 1, 'A')
        >>> count._valuetuple(Subject=100, Code='A')
        (100, None, 'A')
        >>> count._valuetuple(Session=1, Subject=100)
        (100, 1, None)
        
        '''
        t = [None for i in self.features]
        for feature, value in d.items():
            if feature not in self.features:
                fs = ', '.join(self.features)
                msg = '{0} is not a valid feature: {1}'.format(feature, fs)
                raise ValueError(msg)
            i = self.features.index(feature)
            t[i] = value
        return tuple(t)

    def _match(self, x, y):
        '''Does sequence x subsume y?

        Return True if all existing values in x match 
        their respective values in y.

        '''
        return all(x == y or x is None for x, y in zip(x, y))

    def __getitem__(self, values):
        '''Call total method.'''
        if type(values) is not tuple:
            values = (values,)              # convert to tuple
        return self.total(*values)

    def value(self, feat, value):
        '''Return total for a particular value of a particular feature.'''
        return self.feature[feat][value]

    def values(self, feat):
        '''Return values seen for a particular feature.'''
        return sorted(self.feature[feat].keys())

    def _insert(self, X, y, index):
        '''Insert y into list X at index and return tuple.'''
        copy = X[:]
        copy.insert(index, y)
        return tuple(copy)

    def _join(self, seq, separator="\t", newline=False):
        '''Return string of items in sequence joined by separator.'''
        joined = separator.join(str(x) for x in seq)
        joined += "\n" if newline else ""
        return joined

    def __str__(self):
        '''Return string representation of counter object.'''
        return pprint.pformat(self.report())

    def report(self, feature=None):
        '''Return report of value counts.

        If feature is given, breakdown counts by the values 
        of feature (i.e., with columns for each value of feature).
        
        '''
        table = []
        if not feature:
            table.append(self.features + ['Total'])
            for tup in sorted(self.counts.keys()):
                table.append(list(tup) + [self.counts[tup]])
        else:
            index = self.features.index(feature)
            y_values = self.values(feature)
            other_feats = [f for f in self.features if f is not feature]
            other_values = [self.values(f) for f in other_feats]
            table.append(other_feats + y_values)

            # iterate over each combination X of non-target values 
            for X in (list(x) for x in product(*other_values)):
                results = [self.counts[t] for t in (self._insert(X, y, index) 
                                          for y in y_values)]
                table.append(X + results)
        return table

    def print_report(self, feature=None, separator="\t"):
        '''Print report.'''
        self.pprint(self.report(feature), separator)

    def pivot(self, Y, X):
        '''Return contingency table crossing Y feature values with X
        feature values.

        Both X and Y must be lists (of feature names).

        The resulting contingency table will have rows for each Y value
        tuple and columns for each X value tuple. Each field in the table
        reflects the total frequency of the combined feature values.

        >>> count = FeatureCounter('Subject', 'Session', 'Code')
        >>> count(111, 1, 'A')
        >>> count(111, 2, 'B')
        >>> count(222, 2, 'C')

        >>> count.pivot(['Subject'], ['Code'])
        [('Subject', 'A', 'B', 'C'),
         (111, 1, 1, 0),
         (222, 0, 0, 1)]

        >>> count.pivot(['Subject', 'Session'], ['Code'])
        [('Subject', 'Session', 'A', 'B', 'C'),
         (111, 1, 1, 0, 0),
         (111, 2, 0, 1, 0),
         (222, 1, 0, 0, 0),
         (222, 2, 0, 0, 1)]

        '''
        table = []      # list of tuples

        y_tups = [i for i in product(*[self.values(y) for y in Y])]
        x_tups = [i for i in product(*[self.values(x) for x in X])]

        header = tuple(Y + x_tups)
        table.append(header)

        for y in y_tups:
            row = [i for i in y]
            for x in x_tups:
                feat_value_dict = dict(zip(X+Y, x+y))
                row.append(self.total(**feat_value_dict))
            table.append(tuple(row)) 

        return table

    def print_pivot(self, Y, X, separator="\t"):
        '''Print pivot report.'''
        self.pprint(self.pivot(Y, X), separator)

    def pprint(self, table, separator="\t"):
        '''Pretty-print a list of tuples.'''
        for row in table:
            print self._join(row, separator)


if __name__ == '__main__':

    count = FeatureCounter('Subject', 'Session', 'Code')
    count(100, 1, 'A')
    count(100, 1, 'B')
    count(100, 2, 'C')
    print count[100]
    print count[100, 1]
    print count[100, 1, 'A']
    print count[100, 2, 'B']
    print
    count.print_report('Code')
    count.print_pivot(['Subject', 'Session'], ['Code'])
    count.print_pivot(['Subject'], ['Session', 'Code'])
    print count.values('Session')
