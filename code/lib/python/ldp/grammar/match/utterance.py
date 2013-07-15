from token import TokenMatcher


class WordMatcher(TokenMatcher):
    '''
    This class contains methods for matching utterances containing 
    various word types.
    
    Each match method specifies rules for matching a particular word
    type item of interest.  Each takes a tokenized utterance (TokenList)
    as argument and returns a list of the tokens matching the particular 
    word type being tested.

    A TokenList is a representation of the word tokens in an utterance 
    along with the morphosyntactic annotation given in the respective 
    `mor` and `syn` columns of an annotated transcript.  See the TokenList 

    '''
    def _list(self, tokens, cond):
        return [t for t in tokens if cond(t)]

    def conj_subor(self, tokens):
        '''Match all subordinating conjunctions in tokens.'''
        return self._list(tokens, lambda t: t.pos == "conj:subor")

    def nouns(self, tokens):
        '''Match all nouns in tokens.'''
        return self._list(tokens, self.noun)

    def nouns_plural(self, tokens):
        '''Match plural nouns in tokens.'''
        cond = lambda t: self.noun(t) and t.suffix == 'PL'
        return self._list(tokens, cond)

    def nouns_basic(self, tokens):
        '''Match basic nouns in tokens.'''
        return self._list(tokens, self.noun_basic)

    def nouns_proper(self, tokens):
        '''Match proper nouns in tokens.'''
        return self._list(tokens, lambda t: t.pos == "n:prop")

    def pronouns(self, tokens):
        '''Match all pronouns in tokens.'''
        return self._list(tokens, self.pronoun)

    def pronouns_personal(self, tokens):
        '''Match personal pronouns in tokens.'''
        return self._list(tokens, self.pronoun_personal)

    def pronouns_demonstrative(self, tokens):
        '''Match demonstrative pronouns in tokens.'''
        return self._list(tokens, lambda t: t.pos == "pro:dem")

    def pronouns_possessive(self, tokens):
        '''Match possessive pronouns in tokens.'''
        return self._list(tokens, lambda t: t.pos == "pro:poss")

    def pronouns_misc(self, tokens):
        '''
        Match the following types of pronouns in tokens:

        * indefinite
        * existential
        * reflexive
        * WH (e.g., "who", "which")

        '''
        cond = lambda t: t.pos in ["pro:indef", "pro:exist", 
                                   "pro:refl", "pro:wh"]
        return self._list(tokens, cond)
 
    def pronouns_it(self, tokens):
        '''Match 'it' in tokens.'''
        return self._list(tokens, lambda t: t.word == "it")

    def verbs(self, tokens):
        '''Match verbs in tokens.'''
        return self._list(tokens, self.verb) 
 
    def verbs_aux(self, tokens):
        '''Match auxilliary verbs in tokens.'''
        return self._list(tokens, lambda t: t.pos == "aux") 
    
    def verbs_basic(self, tokens):
        '''Match basic verbs in tokens.'''
        return self._list(tokens, lambda t: self.verb_basic(t)) 

    def verbs_copula(self, tokens):
        '''Match copula in tokens.'''
        return self._list(tokens, lambda t: self.verb_copula(t)) 

    def verbs_past(self, tokens):
        '''Match past verbs in tokens.'''
        return self._list(tokens, lambda t: self.verb(t) and t.suffix == "PAST") 

    def verbs_progressive(self, tokens):
        '''Match progressive verbs in tokens.'''
        return self._list(tokens, lambda t: self.verb(t) and t.suffix == "PROG") 
    
    def verbs_third_singular(self, tokens):
        '''Match third singular verbs in tokens, excluding the copula.'''
        cond = lambda t: self.verb(t) and t.suffix == "3S" and not self.verb_copula(t)
        return self._list(tokens, cond) 
    
    def verbs_morph_misc(self, tokens):
        '''Match all other morphologically modified verbs in tokens.''' 
        cond = lambda t: self.verb(t) and t.suffix in ["13S", "1S", \
                                                        "COND", "PERF", "PRES"]
        return self._list(tokens, cond) 
    
    def verbs_morph(self, tokens):
        '''Match lines with a verb that has a suffix.'''
        cond = lambda t: self.verb(t) and t.suffix != None
        return self._list(tokens, cond) 

    def clausal_complements(self, tokens):
        '''Match clausal complements in tokens.'''
        cond = lambda t: t.rel in ["COMP","XCOMP"]
        return self._list(tokens, cond) 

    def clausal_adjuncts(self, tokens):
        '''Match clausal adjuncts in tokens.'''
        cond = lambda t: t.rel in ["CJCT","XJCT"]
        return self._list(tokens, cond) 

    def clausal_modifiers(self, tokens):
        '''Match clausal modifiers in tokens.'''
        cond = lambda t: t.rel in ["CMOD","XMOD"]
        return self._list(tokens, cond) 

    def clausal_predicates(self, tokens):
        '''Match clausal predicates in tokens.'''
        cond = lambda t: t.rel in ["CPRED","XPRED"]
        return self._list(tokens, cond) 

    def clausal_subjects(self, tokens):
        '''Match clausal subjects in tokens.'''
        cond = lambda t: t.rel in ["CSUBJ","XSUBJ"]
        return self._list(tokens, cond) 


class PhraseMatcher(TokenMatcher):
    '''
    This class contains methods for matching utterances containing 
    various phrase types.
    
    Each match method specifies rules for matching a particular phrase 
    type item of interest.  Each takes a tokenized utterance (TokenList)
    as argument and returns True if the tokens contain a match for the
    particular phrase type being matched.

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

        Look for nouns with a dependent that's a modifying noun.

        '''
        c_cond = lambda c: self.noun(c) and c.rel == 'MOD' and c.suffix != 'POSS'
        return self._check(tokens, self.noun, c_cond)

    def det_noun(self, tokens):
        '''
        Match lines with any determiner+noun phrase.

        Look for nouns with a dependent that's a determiner.

        '''
        return self._check(tokens, self.noun, self.det)

    def adj_noun(self, tokens):
        '''
        Match lines with any adjective+noun phrase.

        Look for nouns with a dependent that's an adjective.

        '''
        return self._check(tokens, self.noun, self.adj)

    def quant_noun(self, tokens):
        '''
        Match lines with any quantifier+noun phrase.

        Look for nouns with a dependent that's a quantifier.
        
        '''
        return self._check(tokens, self.noun, self.quant)

    def my_noun(self, tokens):
        '''
        Match lines with a my+noun phrase.

        Look for nouns with a dependent that's "my"
        
        '''
        c_cond = lambda c: c.rel == "DET" and c.lemma == "my"
        return self._check(tokens, self.noun, c_cond)

    def poss_noun_sans_my(self, tokens):
        '''
        Match lines with a possessive+noun phrase where 
        the noun's dependent is a possessive other than "my".
        
        '''
        c_cond = lambda c: self.poss(c) and c.lemma != 'my'
        return self._check (tokens, self.noun, c_cond)

    def poss_noun(self, tokens):
        '''
        Match lines with any possessive+noun phrase.

        Look for nouns with a dependent that's a possessive.
        
        '''
        return self._check(tokens, self.noun, self.poss) or \
               self.poss_s_noun(tokens)

    def poss_s_noun(self, tokens):
        '''
        Match lines with any possessive-s+noun phrase.

        '''
        c_cond = lambda t: (t.pos == 'POSS' and t.rel == 'MOD')
        return self._check(tokens, self.noun, c_cond)

    def prep_root(self, tokens):
        '''
        Match lines with a preposition serving as root.

        We're excluding instances where the preposition's 
        dependents stand in a subject relation to the preposition.

        '''
        p_is_prep_root = lambda t: t.rel.startswith('ROOT') and t.pos == 'prep'
        c_not_subjects = lambda T: not any(t.rel.endswith('SUBJ') for t in T)
        return self._test(tokens, p_is_prep_root, c_not_subjects)

    def prep_mod_noun(self, tokens):
        '''
        Match lines with a preposition modifying a noun.
        
        '''
        cond = lambda t: t.pos == 'prep' and t.rel == 'MOD'
        return self._check(tokens, self.noun, cond) 

    def prep_mod_verb(self, tokens):
        '''
        Match lines with a preposition modifying a verb.
        
        ''' 
        cond = lambda t: t.pos == 'prep' and t.rel in ["JCT", "LOC"]
        return self._check(tokens, self.verb, cond) 

    def infinitive_verb(self, tokens):
        '''
        Match lines with any verb conjugated in the infinitive.
    
        Look for verbs with a dependent that's an infinitive particle. 

        '''
        return self._check(tokens, self.verb, lambda t: t.pos =="inf")

    def particle_verb(self, tokens):
        '''
        Match lines with any phrasal verb. 
    
        Look for verbs with a dependent that's a particle.

        '''
        return self._check(tokens, self.verb, lambda t: t.pos =="ptl")

    def adverb_verb(self, tokens):
        '''
        Match lines with an adverb+verb phrase. 
    
        Look for verbs with a dependent that's an adverb. 

        '''
        return self._check(tokens, self.verb, lambda t: (t.pos.startswith("adv") and t.rel =="JCT"))

    def phrase_mod_verb(self, tokens):
        '''
        Match lines with a verb modified by a separate word in a verb phrase. 
    
        '''
        return self._check(tokens, self.verb, lambda t: self.verb_mod(t)) 
    
    def unmodified_verb(self, tokens):
        '''
        Match lines with a verb that does not have a suffix and is not 
        modified by a separate word in a verb phrase. 
    
        '''
        c_cond = lambda T: not any(t for t in T if self.verb_mod(t)) 
        p_cond = lambda t: self.verb(t) and t.suffix == None
        return self._test(tokens, p_cond, c_cond)
    
    def modified_verb(self, tokens):
        '''
        Match lines with a verb that either has a suffix or is 
        modified by a separate word in a verb phrase. 
    
        '''
        p_cond_1 = lambda t: self.verb(t) and t.suffix != None
        p_cond_2 = lambda t: self.verb(t) and t.suffix == None
        return self._check(tokens, p_cond_1, lambda t: True) \
                or self._check(tokens, p_cond_2, self.verb_mod)
    
    def phrase_mod_noun(self, tokens):
        ''' 
        Match lines with a noun modified by a separate word in a noun phrase. 

        '''
        return self._check(tokens, self.noun, self.noun_mod) 

    def unmodified_noun(self, tokens):
        '''
        Match lines with a noun that does not have a suffix and is not 
        modified by a separate word in a noun phrase. 
    
        '''
        c_cond = lambda T: not any(t for t in T if self.noun_mod(t)) 
        p_cond = lambda t: self.noun(t) and t.suffix == None
        return self._test(tokens, p_cond, c_cond)
    
    def modified_noun(self, tokens):
        '''
        Match lines with a noun that either has a suffix or is
        modified by a separate word in a noun phrase. 
    
        '''
        p_cond_1 = lambda t: self.noun(t) and t.suffix != None
        p_cond_2 = lambda t: self.noun(t) and t.suffix == None
        return self._check(tokens, p_cond_1, lambda t: True) \
            or self._check(tokens, p_cond_2, self.noun_mod)
    
    def dangling_coordinator(self, tokens):
        '''
        Match lines with a coordinating conjunction with only one coordinated dependent. 
        
        '''
        c_cond = lambda T: len([t for t in T if t.rel.startswith('COORD')]) == 1
        return self._test(tokens, lambda t: t.pos == "conj:coo", c_cond)

    def coordinated_nouns(self, tokens):
        '''
        Match lines with at least two coordinated nouns.
        
        '''
        c_cond = lambda T: len([t for t in T if t.rel.startswith('COORD') and self.noun(t)]) > 1
        return self._test(tokens, lambda t: t.pos == "conj:coo", c_cond)

    def coordinated_verbs(self, tokens):
        '''
        Match lines with at least two coordinated verbs. 
        
        '''
        c_cond = lambda T: len([t for t in T if t.rel.startswith('COORD') and self.verb(t)]) > 1
        return self._test(tokens, lambda t: t.pos == "conj:coo", c_cond)

    def simple_verbs(self, tokens):
        '''
        Match all verbs in the simple aspect.
        
        '''
        p_cond = lambda t: t.pos.startswith("v")
        return self._check(tokens, p_cond, lambda t: True) 

    def perfect_verbs(self, tokens):
        '''
        Match all verbs in the perfective aspect.
        
        ''' 
        p_cond = lambda t: t.pos == "part" and t.suffix in ["PERF", "PAST"]
        c_cond = lambda t: t.rel == "AUX" and t.lemma == "have"
        return self._check(tokens, p_cond, c_cond)

    def progressive_verbs(self, tokens):
        '''
        Match all verbs in the progressive aspect.
        
        ''' 
        p_cond = lambda t: t.pos == "part" and t.suffix == "PROG"
        c_cond = lambda t: t.rel == "AUX" and t.lemma == "be"
        return self._check(tokens, p_cond, c_cond) 
   
    def perfect_progressive_verbs(self, tokens):
        '''
        Match all verbs in the perfect progressive aspect.
        
        ''' 
        p_cond = lambda t: t.pos == "part" and t.suffix == "PROG"
        c_cond = lambda t: t.rel == "AUX" and t.word == "been"
        return self._check(tokens, p_cond, c_cond)

    def future_verbs(self, tokens):
        '''
        Match all verbs in the future tense.
        
        ''' 
        cond = lambda t: t.rel == "AUX" and t.lemma == "will" and t.suffix != "COND"
        return self._check(tokens, self.verb, cond) 

    def past_verbs(self, tokens):
        '''
        Match all verbs in the past tense.
        
        '''
        return any(t.suffix == 'PAST' for t in tokens)
    
    def present_verbs(self, tokens):
        '''
        Match all verbs in the present tense.
        
        '''
        p_cond = lambda t: self.verb(t) and t.suffix != "PAST" and t.pos != "aux"
        c_cond = lambda T: not any(t for t in T if (t.lemma == "will" or t.suffix == "PAST")) 
        return self._test(tokens, p_cond, c_cond) 



if __name__ == '__main__':

    from ldp.grammar import TokenList

    match = PhraseMatcher()
    print match.__synopsis__  # print a synopsis of the match methods

    utt = 'this is a pig .'
    mor = 'pro:dem|this v|be&3S det|a n|pig .'
    syn = '1|2|SUBJ 2|0|ROOT 3|4|DET 4|2|PRED 5|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.det_noun(tokens)
    assert not match.adj_noun(tokens)
