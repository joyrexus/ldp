import re
from base import Matcher


class TokenMatcher(Matcher):
    '''
    Each match method specifies rules for matching a particular
    grammatical item of interest.

    Each method takes a morphosyntactic Token as argument
    and will return True if the tokens contain a match for 
    that grammatical item.

    A Token is just a representation of a word tokens in
    an utterance along with that token's morphosyntactic annotation 
    given in the respective `mor` and `syn` columns.  See the Token
    class in the ldp.grammar module for more info and examples.

    '''
    # REGEX PATTERNS 
    # for identifying noun forms
    noun_pos = re.compile(r'^n\b')
    pronoun_pos = re.compile(r'^pro\b')
    # for identifying verbs tagged as participles
    prefix = r'(?:COORD-)?'
    forms = r'(?:ROOT|X?COMP|(?:[CX](?:MOD|JCT|PRED|SUBJ)))'
    verb_rel = re.compile(r'{0}{1}'.format(prefix, forms))
    # for identifying noun modifiers
    noun_mod_rel = re.compile(r"DET|QUANT|[CX]?MOD")
    # for identifying verb modifiers 
    verb_mod_rel = re.compile(r"INF|PTL|LOC|[CX]?JCT")

    def verb_copula(self, t):
        '''Test if token is the copula.'''
        return t.pos == "v" and t.lemma == "be"

    def verb_basic(self, t): 
        '''Test if token is a basic verb.'''
        return (t.pos.startswith("v") and t.lemma !="be") or \
              (t.pos == "part" and self.verb_rel.match(t.rel))

    def verb(self, t):
        '''Test if token is a verb (basic or aux).'''
        return self.verb_basic(t) or self.verb_copula(t) or t.pos == "aux"

    def pronoun_personal(self, t):
        '''Test if token is a personal pronoun.'''
        return t.pos == "pro" and t.lemma != "it"

    def pronoun(self, t):
        '''Test if token is a pronoun.'''
        return self.pronoun_pos.match(t.pos) and t.pos != "pro:poss:det"

    def noun_basic(self, t):
        '''Test if token is a basic noun.'''
        return self.noun_pos.match(t.pos) and t.pos != 'n:prop'

    def noun(self, t):
        '''Test if token is a noun.'''
        return self.noun_pos.match(t.pos) or self.pronoun(t)

    def det(self, t): 
        '''Test whether token t is a determiner.'''
        return t.pos == "det" and t.rel == "DET" and t.lemma != "another"
    
    def adj(self, t): 
        '''Test if token is an adjective.'''
        return t.pos.startswith("adj") and t.rel == "MOD"

    def poss(self, t): 
        '''Test if token is possessive.'''
        return (t.pos == "pro:poss:det" and t.rel == "DET") or t.pos == "POSS"

    def quant(self, t): 
        '''Test if token is a quantifier.'''
        return t.rel == "QUANT" or (t.lemma == "another" and t.rel == "DET")

    def noun_mod(self, t): 
        '''Test whether token t is a noun modifier.'''
        return self.noun_mod_rel.match(t.rel) 

    def verb_mod(self, t): 
        '''Test whether token t is a verb modifier.'''
        return self.verb_mod_rel.match(t.rel) 
