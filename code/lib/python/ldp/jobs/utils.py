import os
import re
from operator import itemgetter
from collections import defaultdict
from ldp.data import Utterances


class FindUnits(Utterances):
    '''
    Return units for each column value in utterances matching pattern.

    Specify a match group named "suspect" to specify the suspect item within 
    the match pattern. (See example below.)

        >>> find = FindUnits()
        >>> pattern = r'\b(?P<suspect>gl\w+ing)\b'
        >>> units = find(pattern, limit=10000, verbose=True)
        p_utts (10220500094):   "he thought he saw some dark eyes glinting."
        p_chat (10220500094):   he thought he saw some dark eyes glinting .
        >>> units
        [
            {
                'id': 10220500094L, 
                'column': 'p_utts', 
                'value': '"he thought he saw some dark eyes glinting."',
                'suspect': 'glinting'
            }, 
            {
                'id': 10220500094L,
                'column': 'p_chat', 
                'value': u'he thought he saw some dark eyes glinting .',
                'suspect': 'glinting'
            }
        ]


    '''
    def __init__(self, ds_env_var="LDP_DB"):
        ds_path = os.environ[ds_env_var]
        self.SUSPECTS = defaultdict(int)
        self.UNITS = defaultdict(list)      # store units found by suspect
        super(FindUnits, self).__init__(ds_path)

    def __call__(self, pattern, where='', 
                                limit='', 
                                condition=lambda x: True,
                                verbose=False,
                                columns=('p_utts', 'c_utts')):
        '''Returns a list of units for each column value matching pattern.'''
        regex = re.compile(pattern)
        units = []
        for row in self.select(where=where, limit=limit):
            id = row['id']
            for column in columns:
                value = row[column]
                match = regex.search(value) 
                if match and condition(value):
                    unit = dict(id=id, column=column, value=value)
                    suspect = match.group('suspect') or 'NO SUSPECT'
                    unit['suspect'] = suspect
                    self.SUSPECTS[suspect] += 1
                    self.UNITS[suspect].append(unit)    # aggregate by suspect
                    units.append(unit)
                    if verbose:
                        print "{0} ({1}):\t{2}\t{3}".format(column, id, 
                                                            suspect, value)
        return units

    def units(self, suspect):
        '''Return units found with suspect.'''
        return self.UNITS[suspect]

    @property
    def suspects(self):
        '''Return list of all unique suspects found.'''
        return sorted(self.SUSPECTS.keys())

    @suspects.deleter
    def suspects(self):
        self.SUSPECTS = defaultdict(int)

    @property
    def suspect_counts(self):
        '''Return list of tuples: (suspect, count).'''
        return sorted(self.SUSPECTS.items(), key=itemgetter(1))


class Context(Utterances):
    '''
    Provides access to utterance context by utterance row id.
    
        >>> context = Context()
        >>> [(p, c, x) for p, c, x in context(id=10290900403, window=2)]
        [(u'', u'uh, 8:30.', u''), (u'8:30?', u'', u''), (u'', u'8:30.', u'')]

    '''
    def __init__(self, ds_env_var="LDP_DB"):
        ds_path = os.environ[ds_env_var]
        super(Context, self).__init__(ds_path)

    def __call__(self, id, window=5, columns='p_utts, c_utts, context'):
        '''
        Returns an iterator containing tuples of column values for a 
        range of rows (window) preceding and following a particular 
        row (id). 

        '''
        return self.context(id, window, columns)


if __name__ == '__main__':

    pattern = r'\b(?P<suspect>gl\w+ing)\b'
    find = FindUnits('LDP_DB')
    units = find(pattern, limit=10000, verbose=True)
    print units
    '''
    context = Context(ds_env_var='LDP_DB')
    print [(p, c, x) for p, c, x in context(id=10290900403, window=2)]
    '''
