"""
ldp.grammar - provides convenient representation of CHAT-based 
              morphosyntactic annotation.

Use the TokenList class to create unified representations of annotated 
utterances produced by CLAN's part-of-speech tagger (``mor``) and 
grammatical dependency parser (``grasp``).

The TokenList constructor takes an utterance (``utt``), it's part-of-speech
annotation (``pos``), and it's syntactic annotation (``syn``) and return a list
of Token objects that make it easy to access the morphosyntactic features of
each word token in the utterance.

    >>> from ldp.grammar import TokenList
    >>> utt = 'do you want to read a book ?'
    >>> mor = 'aux|do pro|you aux|want inf|to v|read&ZERO det|a n|book ?'
    >>> syn = '1|5|AUX 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|7|DET 7|5|OBJ 8|5|PUNCT' 
    >>> tokens = TokenList(utt, mor, syn)
    >>> print tokens
    0   do  do  aux _   5   AUX
    1   you you pro _   5   SUBJ
    2   want    want    aux _   5   AUX
    3   to  to  inf _   5   INF
    4   read    read    v   _   0   ROOT
    5   a   a   det _   7   DET
    6   book    book    n   _   5   OBJ
    7   ?   ?   ?   _   5   PUNCT
    >>> tokens[0]
    Token(lemma='do', prefix=None, num=1, word='do', 
          suffix=None, rel='AUX', irreg=False, dep=5, pos='aux')
    >>> tokens.words
    ['do', 'you', 'want', 'to', 'read', 'a', 'book', '?']
    >>> tokens.lemmas
    ['do', 'you', 'want', 'to', 'read', 'a', 'book', '?']
    >>> for t in tokens:
    ...     if t.is_verb: print t.lemma, t.pos
    ... 
    read v

"""
import re
from chat import Utt, Mor, Syn
import ldp.data


# regex pattern for identifying verbs tagged as participles
prefix = r'(?:COORD-)?'
forms = r'(?:ROOT|CMOD|XMOD|CJCT|XJCT|COMP|XCOMP|CPRED|XPRED|CSUBJ|XSUBJ)'
verb_rel = re.compile(r'{0}{1}'.format(prefix, forms))


class Token(object):
    '''
    Representation of a word token and its grammatical features.
    
    '''
    def __init__(self, *dicts): 
        '''
        Unify the dicts passed as args to create a struct-like object 
        storing all of the features associated with the token
        being constructed.

        The dicts should contain the token's features as keywords and 
        feature-values as values, e.g.: dict(word="jump", pos="v")
        
        '''
        for d in dicts: self.__dict__.update(d)

    def __repr__(self):
        args = ['{0}={1}'.format(k, repr(v)) for k, v in self.__dict__.items()]
        return 'Token({0})'.format(', '.join(args))

    def __call__(self, match): 
        'Takes a boolean match/test function that takes self as argument.'
        return match(self)

    @property
    def is_verb(self): 
        '''Test if token is a verb based on its pos and syntax.'''
        return self.pos.startswith("v") or (self.pos == "part" and 
                                            verb_rel.match(self.rel))

    @property
    def head(self):
        '''Return index number of the word's grammatical head.'''
        return getattr(self, 'dep', None)

    @property
    def deprel(self):
        '''Return dependency relation of word to its head.'''
        return getattr(self, 'rel', None)


class TokenList(list):
    '''
    Tokenized representation of annotated utterances produced by 
    CLAN's part-of-speech tagger (``mor``) and grammatical 
    dependency parser (``grasp``).

    '''
    def __init__(self, utt, mor, syn=""):
        '''
        Initialize a MorphoSyntax Line object.

        Creates a list representation of the utterance, comprised of token
        objects (representing the morphosyntactic features of each word token).

        Such a Line object provides a unified representation of the utt, mor, 
        and syn column values in an utterance line of a transcript.

        '''
        UTT, MOR, SYN = Utt(utt), Mor(mor), Syn(syn)
        if syn:
            self.syntax = True
            try:
                assert len(UTT) == len(MOR) == len(SYN)
            except AssertionError:
                print "Warning: differing number of tokens in feature dicts!"
                print 'UTT:', len(UTT), UTT
                print 'MOR:', len(MOR), MOR
                print 'SYN:', len(SYN), SYN
                raise SystemExit
            return list.__init__(self, (Token(*t) for t in zip(UTT, MOR, SYN)))
        else:
            self.syntax = False
            return list.__init__(self, (Token(*t) for t in zip(UTT, MOR)))

    def __str__(self):
        '''
        Return a formatted representation of word tokens in 
        line and their annotation features.

        The output rendered is in "dependency format", and consists of 7
        fields:

        ID: token counter, starting at 1 for each new sentence
        FORM: word form or punctuation symbol
        LEMMA: lemma or stem of word form
        POSTAG: fine-grained part-of-speech tag
        FEATS: extra features ('_' indicates no extra feature)
        HEAD: head ID of the current token
        DEPREL: dependency relation to the HEAD

        Each field is delimited by a tab character ('\t'). Each sentence is
        delimited by a blank line. The last two fields (HEAD, DEPREL) are
        optional for decoding.
        
        '''
        line = []
        for i, t in enumerate(self):
            if self.syntax:
                features = [str(i+1), t.word, t.lemma, t.pos, '_', str(t.dep), t.rel]
            else:
                features = [str(i+1), t.word, t.lemma, t.pos]
            line.append("\t".join(features))
        line.append('')
        return "\n".join(line)

    def __call__(self, match): 
        'Takes a boolean match/test function that takes self as argument.'
        return match(self)

    @property
    def words(self):
        '''Return each word token in line.'''
        return [t.word for t in self]

    @property
    def lemmas(self):
        '''Return each word token's lemma in line.'''
        return [t.lemma for t in self]

    def num(self, n):
        '''
        Return word token number n.
        
        Token numbers are based on word order.  The first
        word in a TokenList is token number 1. Thus, each 
        token's word number is 1 greater than it's index.

        For example, suppose we have a TokenList based
        for the utterance "do you want to read a book":

            do  you  want  to  read  a  book  ?
            1   2    3     4   5     6  7     8

        '''
        if n < 1: 
            t = Token(dict(pos=None, dep=None, rel=None))
            return t
        return self[n - 1]

    def dependent_on(self, t):
        '''Return list of tokens immediately dependent on token t.'''
        return [d for d in self if d.dep == t.num]

    def paths_from(self, t, verbose=False):
        '''Return list of dependency paths from token t.'''
        paths = [t.word]
        for d in self.dependent_on(t):
            if verbose:
                print "{0} {1} => {2} {3}".format(t.num, t.word, d.num, d.word)
            paths.append(self.paths_from(d, verbose))
        return paths

    def depth_from(self, t):
        '''Return depth (length of maximum dependency path) from token t.'''
        depth = 0
        D = self.dependent_on(t)
        if D:
            depth += 1
            depth += max(self.depth_from(d) for d in D)
        return depth

    def max_path_from(self, t, index=False):
        '''Return dependency path of max depth from token t.'''
        path = [(t.num, t.word)] if index else [t.word]
        deps = self.dependent_on(t)
        if deps:
            m = max(deps, key=self.depth_from)
            path.append(self.max_path_from(m, index))
        return path


class Transcript(object):
    '''
    Provide unified representation of chat, mor, and syn column values in 
    a transcript.
    
    '''
    def __init__(self, subject, session):
        self.subject = subject
        self.session = session
        self.transcript = ldp.data.Transcript(subject, session)

    def __call__(self, speaker="parent"):
        '''Yields MorphoSyntax Line objects for speaker.'''
        return self.__iter__(speaker)

    def __iter__(self, speaker="parent"):
        '''Yields MorphoSyntax Line objects for speaker.'''
        if speaker not in ("parent", "child"):
            raise ValueError('speaker argument must be "parent" or "child"')
        UTT, MOR, SYN = ("c_chat", "c_mor", "c_syn") if speaker is "child" else \
                        ("p_chat", "p_mor", "p_syn")
        columns = "id, {0}, {1}, {2}".format(UTT, MOR, SYN)
        condition = '{0} != ""'.format(SYN)
        for id, utt, mor, syn in self.transcript(columns, condition):
            yield id, TokenList(utt, mor, syn)



if __name__ == '__main__':

    utt = 'do you want to read a book ?'
    mor = 'aux|do pro|you aux|want inf|to v|read&ZERO det|a n|book ?'
    syn = '1|5|AUX 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|7|DET 7|5|OBJ 8|5|PUNCT' 

    # tokens = TokenList(utt, mor, syn)
    tokens = TokenList(utt, mor)
    print tokens
    print tokens.words
    print tokens.lemmas
    assert tokens.num(1).word == 'do'

    for t in tokens: 
        if t.is_verb: 
            print t.lemma, t.pos
