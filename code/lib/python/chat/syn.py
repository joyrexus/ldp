
class Token(dict):
    '''
    Feature dict for element from a syn string.

    '''
    def __init__(self, tok):
        '''
        Initialize a syn token object.
        
        >>> Token("5|0|ROOT")
        {'dep': 0, 'num': 5, 'rel': 'ROOT'}

        '''
        num, dep, rel = tok.split("|")
        dict.__init__(self, dict(num=int(num), dep=int(dep), rel=rel))

    @property
    def head(self): 
        '''Alias name for *dep* ("dependency") attribute.'''
        return self['dep']

    @property
    def deprel(self): 
        '''Alias name for *rel* ("grammatical relation") attribute.'''
        return self['rel']

    def __getattr__(self, attr): return self[attr]

    def __setattr__(self, attr, value): self[attr] = value


class Syn(list):
    '''
    Use for tokenizing annotated utterances produced by 
    clan's grammatical dependency parser (``grasp``).

    '''
    def __init__(self, syn):
        '''
        Initialize a Syn object.

        Create a list representation of a syn string, where each item is a
        dict of feature annotations for the corresponding utterance token.

        '''
        list.__init__(self, [Token(i) for i in syn.split() if "|" in i])


if __name__ == '__main__':

    print Token('1|3|SUBJ')

    print Syn('1|0|ROOT 2|1|OBJ 3|1|IOBJ 4|3|POBJ 5|1|COM 6|1|PUNCT')

