'''
Matcher classes for matching various kinds of 
morphosyntax Tokens and TokenLists.

'''
import re
from operator import itemgetter


class Matcher(object):
    '''
    Abstract Matcher class.

    '''
    @property
    def __methods__(self):
        '''Return list of methods.'''
        return [v for (k,v) in sorted(self.__class__.__dict__.items())
                            if not k.startswith('_') 
                            and callable(v)]

    @property
    def __synopsis__(self):
        '''Return string synopsis of available methods.'''
        msg = self.__class__.__name__ + '\n' + self.__doc__
        for m in self.__methods__:
            docstring = m.__doc__
            if docstring.startswith('\n'):
                msg += '\n  {}\n{}'.format(m.func_name, m.__doc__)
            else:
                msg += '\n  {}\n\n\t{}\n'.format(m.func_name, m.__doc__)
        return msg


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
    # for identifying modifiers
    mod_rel = re.compile(r"DET|QUANT|[CX]?MOD")

    def verb(self, t): 
        '''Test if token is a verb based on its pos and syntax.'''
        return t.pos.startswith("v") or \
               (t.pos == "part" and self.verb_rel.match(t.rel))

    def noun(self, t):
        '''
        Test if token is a noun based on its pos.

        '''
        return self.noun_pos.match(t.pos) or self.pronoun_pos.match(t.pos)

    def noun_simple(self, t):
        '''
        Test if token is a simple noun based on its pos.

        The class of simple nouns differ from nouns in general 
        in omitting pronoun forms.

        '''
        return self.noun_pos.match(t.pos)

    def det(self, t): 
        '''Test whether token t is a determiner.'''
        return t.pos == "det" and t.rel == "DET" and t.lemma != "another"
    
    def adj(self, t): 
        '''Test whether token t is an adjective.'''
        return t.pos.startswith("adj") and t.rel == "MOD"

    def quant(self, t): 
        '''Test whether token t is a quantifier.'''
        return t.rel == "QUANT" or (t.lemma == "another" and t.rel == "DET")

    def mod(self, t): 
        '''Test whether token t is a modifier.'''
        return self.mod_rel.match(t.rel) and not self.noun_simple(t)

    def poss(self, t): 
        '''Test whether token t is possessive.'''
        return (t.pos == "pro:poss:det" and t.rel == "DET") or t.pos == "POSS"

    def pro_indef(self, t):
        '''Test whether token t is an indefinite pronoun.'''
        return t.pos == "pro:indef"
            

class TokenListMatcher(TokenMatcher):
    '''
    The TokenListMatcher class contains Erica Cartmill's match 
    methods for matching lines with various phrase 
    types.

    Each match method specifies rules for matching a particular
    grammatical item of interest.  Each method takes a morphosyntactic 
    TokenList as argument and returns True if the tokens contain a 
    match for that grammatical item.

    A TokenList is just a representation of the word tokens in
    an utterance along with the morphosyntactic annotation given 
    in the respective `mor` and `syn` columns.  See the TokenList 
    class in the ldp.grammar module for more info and examples.

    '''
    def has_noun_simple(self, tokens):
        '''
        Match lines with a simple noun.

        '''
        return any(True for t in tokens if self.noun_simple(t))

    def has_noun_proper(self, tokens):
        '''
        Match lines with a proper noun.

        '''
        return any(True for t in tokens if t.pos == 'n:prop')

    def has_noun_plural(self, tokens):
        '''
        Match lines with a plural noun.

        '''
        return any(True for t in tokens if self.noun(t) 
                                        and t.suffix == "PL")

    def has_pronoun_personal(self, tokens):
        '''
        Match lines with a personal pronoun.

        This will not match reflexive prounouns ("myself").

        '''
        return any(True for t in tokens if t.pos == 'pro' 
                                        and t.lemma != 'it')

    def has_past_tense(self, tokens):
        '''
        Match lines with a past tense verb form.

        '''
        return any(True for t in tokens if t.suffix == 'PAST')

    def has_infinitive(self, tokens):
        '''
        Match lines with an infinitive. 

        '''
        return any(True for t in tokens if t.pos == 'inf'
                                       and t.rel == 'INF')

    def has_progressive(self, tokens):
        '''
        Match lines with a progressive form.

        '''
        return any(True for t in tokens if t.suffix == 'PROG'
                                        and not t.rel.startswith('MOD'))

    def has_verb_third_singular(self, tokens):
        '''
        Match lines with a third person singular verb form.

        '''
        return any(True for t in tokens if t.suffix == '3S'
                                        and t.lemma != 'be')

    def has_conj_noncoord(self, tokens):
        '''
        Match lines with a non-coordinating conjunction.

        '''
        return any(True for t in tokens if t.pos == 'conj:subor')

    def has_clausal_complement(self, tokens):
        '''
        Match lines with a clausal complement.

        '''
        return any(True for t in tokens if t.rel in ['COMP', 'XCOMP'])

    def has_clausal_adjunct(self, tokens):
        '''
        Match lines with a clausal adjunct.

        '''
        return any(True for t in tokens if t.rel in ['CJCT', 'XJCT'])

    def has_clausal_predicate(self, tokens):
        '''
        Match lines with a clausal predicate.

        '''
        return any(True for t in tokens if t.rel in ['CPED', 'XPRED'])

    def has_clausal_modifier(self, tokens):
        '''
        Match lines with a clausal modifier.

        '''
        return any(True for t in tokens if t.rel in ['CMOD', 'XMOD'])

    def has_clausal_subject(self, tokens):
        '''
        Match lines with a clausal subject.

        '''
        return any(True for t in tokens if t.rel in ['CSUBJ', 'XSUBJ'])


class PhraseMatcher(TokenMatcher):
    '''
    The PhraseMatcher class contains methods for matching 
    a list of word tokens containing various phrase types.
    
    (The list of word tokens is just a representation of an LDP 
    transcript utterance that's been morphosyntactically annotated 
    and tokenized as a TokenList)

    Each match method specifies rules for matching a particular
    grammatical item of interest.  Each method takes a morphosyntactic 
    TokenList as argument and returns True if the tokens contain a 
    match for that grammatical item.

    A TokenList is a representation of the word tokens in an utterance 
    along with the morphosyntactic annotation given in the respective 
    `mor` and `syn` columns of an annotated transcript.  See the TokenList 
    class in the ldp.grammar module for more info and examples.

    '''
    def _check(self, tokens, p_cond, c_cond):
        '''
        Match lines with a phrase meeting both parent and child 
        conditions.

        Look for parents meeting parent condition and then check
        their children to see if any meet the child condition.
        
        Both the `p_cond` and `c_cond` arguments should be 
        functions that take a token as argument and test for 
        relevant conditions.

        '''
        parents = [t for t in tokens if p_cond(t)]
        for p in parents:   
            children = tokens.dependent_on(p)
            for c in children:
                if c_cond(c): return True
            
    def _test(self, tokens, p_cond, c_cond):
        '''
        Match lines with a phrase meeting both parent and
        and children condition.

        This is just like the `_check` method, except the
        `c_cond` argument tests a parent's dependents all at 
        once, rather than testing one dependent at a time.  
        That is, we pass in a condition for testing the set of 
        children rather than a condition for a single child.

        First, look for parents meeting the parent condition;
        then check each parent's set of dependents (children)
        to see if they meet the children condition.

        The `p_cond` argument should be a function that takes 
        a token as argument and tests for the relevant condition.

        The `c_cond` argument should be a function that takes 
        a set of tokens (a particular parent's dependencies
        or "children") as argument and tests for relevant 
        condition in the child tokens.

        '''
        parents = [t for t in tokens if p_cond(t)]
        for p in parents: 
            children = tokens.dependent_on(p)
            if c_cond(children): return True

    def noun_noun(self, tokens):
        '''
        Match lines with a noun+noun phrase.

        Look for simple nouns with a dependent that's a modifying noun.

        '''
        c_cond = lambda c: self.noun(c) and c.rel == 'MOD'
        return self._check(tokens, self.noun_simple, c_cond)

    def det_noun(self, tokens):
        '''
        Match lines with any determiner+noun phrase.

        Look for simple nouns with a dependent that's a determiner.

        '''
        return self._check(tokens, self.noun_simple, self.det)

    def adj_noun(self, tokens):
        '''
        Match lines with any adjective+noun phrase.

        Look for simple nouns with a dependent that's an adjective.

        '''
        return self._check(tokens, self.noun_simple, self.adj)

    def quant_noun(self, tokens):
        '''
        Match lines with any quantifier+noun phrase.

        Look for nouns with a dependent that's a quantifier.
        
        '''
        return self._check(tokens, self.noun_simple, self.quant)

    def poss_noun(self, tokens):
        '''
        Match lines with any possessive+noun phrase.

        Look for simple nouns with a dependent that's a possessive.
        
        '''
        return self._check(tokens, self.noun_simple, self.poss) or \
               self.poss_s_noun(tokens)

    def poss_s_noun(self, tokens):
        c_cond = lambda t: (self.noun(t) or (t.pos == 'POSS' and t.rel == 'MOD'))
        return self._check(tokens, self.noun_simple, c_cond)

    def not_subjects(self, tokens):
        '''
        Test that all tokens do not have a subject relation.

        '''
        return not any(t.rel.endswith('SUBJ') for t in tokens)

    def prep_root(self, tokens):
        '''
        Match utterances with a preposition serving as root.

        We're excluding instances where the preposition's
        dependents stand in a subject relation to the preposition.

        '''
        is_prep_root = lambda t: t.rel.startswith('ROOT') and t.pos == 'prep'
        return self._test(tokens, is_prep_root, self.not_subjects)

    def prep_mod_verbal(self, tokens):
        '''
        Match utterances with a preposition modifying a verb or auxiliary.

        For each utterance, look for a word token P that can be 
        classified as a verb or an auxiliary.

        We have a match if P exists and has a dependent C that's a preposition.

        '''
        parent = lambda t: self.verb(t) or t.pos == 'aux'
        child = lambda t: t.pos == 'prep'
        return self._check(tokens, parent, child)

    def prep_mod_noun(self, tokens):
        '''
        Match utterances with a preposition modifying a noun.

        Preposition Modifying Subject Noun
        x.pos = "prep"
            and x.dep = y.num
            and y.is_noun and y.rel is "SUBJ"

        Preposition Modifying Non-Subject Noun
        x.pos = "prep"
            and x.dep = y.num
            and y.is_noun and y.rel is not "SUBJ"
        '''
        pass

    def has_det_poss(self, tokens):
        '''
        Test whether tokens contains both a possessive and quantifier.

        '''
        return any(self.det(t) for t in tokens) and \
               any(self.poss(t) for t in tokens)

    def det_poss_noun(self, tokens):
        '''
        Match lines with a noun with a determiner and possessive as 
        dependents.

        '''
        return self._check(tokens, self.noun_simple, self.has_det_poss)

    def has_det_adj(self, tokens):
        '''
        Test whether tokens contains both a determiner and adjective.

        '''
        return any(self.det(t) for t in tokens) and \
               any(self.adj(t) for t in tokens)

    def det_adj_noun(self, tokens):
        '''
        Match lines with a noun with a determiner 
        and adjective as dependents.

        '''
        return self._test(tokens, self.noun_simple, self.has_det_adj)

    def det_adj_pro_indef(self, tokens):
        '''
        Match lines with an indefinite pronoun with a determiner 
        and adjective as dependents.

        '''
        return self._test(tokens, self.pro_indef, self.has_det_adj)

    def has_det_quant(self, tokens):
        '''
        Test whether tokens contains both a determiner and quantifier.

        '''
        return any(self.det(t) for t in tokens) and \
               any(self.quant(t) for t in tokens)

    def det_quant_noun(self, tokens):
        '''
        Match lines with a noun with a determiner 
        and quantifier as dependents.

        '''
        return self._test(tokens, self.noun_simple, self.has_det_quant)

    def has_poss_adj(self, tokens):
        '''
        Test whether tokens contains both a possessive and adjective.

        '''
        return any(self.poss(t) for t in tokens) and \
               any(self.adj(t) for t in tokens)

    def poss_adj_noun(self, tokens):
        '''
        Match lines with a noun with a determiner 
        and adjective as dependents.

        '''
        return self._test(tokens, self.noun_simple, self.has_poss_adj)

    def has_poss_quant(self, tokens):
        '''
        Test whether tokens contains both a possessive and quantifier.

        '''
        return any(self.poss(t) for t in tokens) and \
               any(self.quant(t) for t in tokens)

    def poss_quant_noun(self, tokens):
        '''
        Match lines with a noun with a possessive
        and quantifier as dependents.

        '''
        return self._test(tokens, self.noun_simple, self.has_poss_quant)


class MinimalPhraseMatcher(TokenMatcher):
    '''
    The MinimalPhraseMatcher class contains Dea Hunsicker's match 
    methods for matching lines with various simple phrase types.

    Each match method specifies rules for matching a particular
    grammatical item of interest.  Each method takes a morphosyntactic 
    TokenList as argument and returns True if the tokens contain a 
    match for that grammatical item.

    A TokenList is just a representation of the word tokens in
    an utterance along with the morphosyntactic annotation given 
    in the respective `mor` and `syn` columns.  See the TokenList 
    class in the ldp.grammar module for more info and examples.

    '''
    def _check(self, tokens, parent, child):
        '''
        Match lines with a two-element phrase meeting
        both parent and child conditions.

        Look for parents meeting parent conditions and then check
        their children to see that they meet child conition.
        
        Both the `child_cond` and `parent_cond` arguments should be 
        functions that take tokens as arguments and test for relevant
        conditions.

        '''
        # test for valid child tokens (meets child condition and has no deps)
        valid = lambda t: child(t) and not tokens.dependent_on(t)
        parents = [t for t in tokens if parent(t)]
        for p in parents: # test children of each parent
            dependents = tokens.dependent_on(p)
            if not dependents: continue
            if len(dependents) == 1 and valid(dependents[0]): return True
            targets = [d for d in dependents if valid(d)]
            if len(targets) == 1:
                others = [d for d in dependents if d not in targets]
                if not self._phrase_dependent(others): return True

    def _phrase_dependent(self, tokens): 
        '''
        Test whether any token is potentially phrase dependent.
        
        '''
        return any(t.rel in ["MOD","ENUM","QUANT","DET"] for t in tokens)

    bare_noun_pos = re.compile(r'n:(?!let|prop)|n$')

    def bare_noun(self, tokens):
        '''
        Match lines with standalone/unmodified nouns.

        (Excluding nouns dependent on a modifier.)

        '''
        # test for valid child tokens (meets child condition and has no deps)
        valid = lambda t: not self.mod(t) and not tokens.dependent_on(t)
        nouns = [t for t in tokens if self.bare_noun_pos.match(t.pos)
                                  and t.rel != 'MOD']
        for n in nouns: # test children of each noun
            if tokens.num(n.dep).rel == 'MOD': continue 
            dependents = tokens.dependent_on(n)
            if not dependents: return True
            if len(dependents) == 1 and valid(dependents[0]): return True
            targets = [d for d in dependents if valid(d)]
            if len(targets) == 1:
                others = [d for d in dependents if d not in targets]
                if not self._phrase_dependent(others): return True

    def det_noun(self, tokens):
        '''
        Match lines with a two-element determiner+noun phrase.

        Look for simple nouns with only a single dependent, where
        that dependent is a determiner.

        '''
        return self._check(tokens, self.noun_simple, self.det)

    def adj_noun(self, tokens):
        '''
        Match lines with a two-element adjective+noun phrase.

        Look for simple nouns with only a single dependent, where
        that dependent is an adjective.

        '''
        return self._check(tokens, self.noun_simple, self.adj)

    def quant_noun(self, tokens):
        '''
        Match lines with a two-element quantifier+noun phrase.

        Look for simple nouns with only a single dependent, where
        that dependent is a quantifier.
        
        '''
        return self._check(tokens, self.noun_simple, self.quant)

    def poss_noun(self, tokens):
        '''
        Match lines with a two-element possessive+noun phrase.

        Look for simple nouns with only a single dependent, where
        that dependent is possessive.
        
        '''
        return self._check(tokens, self.noun_simple, self.poss) or \
               self.poss_s_noun(tokens)

    def poss_s_noun(self, tokens):
        '''
        Match lines with a two-element possessive+noun phrase,
        where the possessive is marked by a possessive 's.

        utt = "it not in Zoe's closet ."
        mor = 'pro|it neg|not prep|in n:prop|Zoe-POSS n|closet .'
                                      n:prop|Zoe POSS|'s
        syn = '1|3|SUBJ 2|3|NEG 3|0|ROOT 4|6|MOD 5|6|MOD 6|3|POBJ 7|3|PUNCT'

        '''
        # a token is valid if it's a noun or possessive form with no deps
        valid = lambda t: (self.noun(t) or (t.pos == 'POSS' and t.rel == 'MOD')) \
                          and not tokens.dependent_on(t)
        nouns = [t for t in tokens if self.noun_simple(t)]
        for n in nouns:
            dependents = tokens.dependent_on(n)
            if not dependents: continue
            if any(d.pos == 'POSS' for d in dependents):
                targets = [d for d in dependents if valid(d)]
                # check for possessive noun targets
                if len(targets) == 2 and all(t.dep == n.num for t in targets):
                    others = [d for d in dependents if d not in targets]
                    return not self._phrase_dependent(others)

    def det_pro_indef(self, tokens):
        '''
        Match lines with a two-element phrase consisting
        of an indefinite pronoun with a determiner as its only
        dependent.

        '''
        return self._check(tokens, self.pro_indef, self.det)

    def adj_pro_indef(self, tokens):
        '''
        Match lines with a two-element phrase consisting
        of an indefinite pronoun with a determiner as its only
        dependent.

        '''
        return self._check(tokens, self.pro_indef, self.adj)


if __name__ == '__main__':

    match = PhraseMatcher()
    print match.__methods__
    print match.__synopsis__

    raise SystemExit

    utt = 'this is a pig .'
    mor = 'pro:dem|this v|be&3S det|a n|pig .'
    syn = '1|2|SUBJ 2|0|ROOT 3|4|DET 4|2|PRED 5|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.det_noun(tokens)
    assert not match.adj_noun(tokens)
    # assert match.any_det_noun(tokens)
    # assert not match.any_adj_noun(tokens)

