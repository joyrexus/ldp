from ldp.grammar import TokenList
from ldp.grammar.match import PhraseMatcher


match = PhraseMatcher()


def noun_noun_test():
    '''Match lines with any noun+noun phrase'''
    utt = 'I color the dog nose .'
    mor = 'pro|I v|color det|the n|dog n|nose .'
    syn = '1|2|SUBJ 2|0|ROOT 3|5|DET 4|5|MOD 5|2|OBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.noun_noun(tokens)

    utt = 'dog eat people food .'
    mor = 'n|dog v|eat n|person&PL n|food .'
    syn = '1|2|SUBJ 2|0|ROOT 3|4|MOD 4|2|OBJ 5|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.noun_noun(tokens)

    utt = "doll's shoes ."
    mor = "n|doll-POSS n|shoe-PL ."
    syn = "1|3|MOD 2|3|MOD 3|0|ROOT-NV 4|3|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert not match.noun_noun(tokens)

    utt = 'little circle .'
    mor = 'adj|little n|circle .'
    syn = '1|2|MOD 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.noun_noun(tokens)


def det_noun_test():
    '''Match lines with a determiner+noun phrase'''
    utt = 'I color the dog nose .'
    mor = 'pro|I v|color det|the n|dog n|nose .'
    syn = '1|2|SUBJ 2|0|ROOT 3|5|DET 4|5|MOD 5|2|OBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.det_noun(tokens)

    utt = 'house shoes .'
    mor = 'n|house n|shoe-PL .'
    syn = '1|2|MOD 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.det_noun(tokens)

    utt = 'that the &xxx +...'
    mor = 'pro:dem|that det|the +...'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.det_noun(tokens)


def adj_noun_test():
    '''Match lines with an adjective+noun phrase'''
    utt = 'little circle .'
    mor = 'adj|little n|circle .'
    syn = '1|2|MOD 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.adj_noun(tokens)

    utt = 'I color the dog nose .'
    mor = 'pro|I v|color det|the n|dog n|nose .'
    syn = '1|2|SUBJ 2|0|ROOT 3|5|DET 4|5|MOD 5|2|OBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)


def quant_noun_test():
    '''Match lines with a quantifier+noun phrase'''
    utt = '''so do we have all the green ones now ?'''
    mor = '''co|so aux|do pro|we v|have qn|all det|the adj|green
             pro:indef|one-PL adv|now ?'''
    syn = '''1|4|COM 2|4|AUX 3|4|SUBJ 4|0|ROOT 5|8|QUANT 6|8|DET
             7|8|MOD 8|4|OBJ 9|4|JCT 10|4|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.quant_noun(tokens), 'Is this correct?'

    utt = 'little circle .'
    mor = 'adj|little n|circle .'
    syn = '1|2|MOD 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.quant_noun(tokens)

    utt = 'yeah, but I want another.'
    mor = 'co|yeah conj:coo|but pro|I v|want pro:indef|another .'
    syn = '1|2|COM 2|0|ROOT 3|4|SUBJ 4|2|COORD-ROOT 5|4|OBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.quant_noun(tokens)

    utt = "let's pretend that this is a swamp with all the +..."
    mor = "aux|let's v|pretend rel|that pro:dem|this v|be&3S det|a n|swamp prep|with qn|all det|the +..."
    syn = "1|2|AUX 2|0|ROOT 3|5|CPZR 4|5|SUBJ 5|2|COMP 6|7|DET 7|5|PRED 8|2|JCT 9|10|QUANT 10|8|DET-POBJ 11|2|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert not match.quant_noun(tokens)


def poss_noun_test():
    '''Match lines with a possessive+noun phrase'''
    utt = "just like Connor@n's snake ."
    mor = "adv:int|just prep|like n:prop|Connor@n-POSS n|snake ."
    syn = "1|2|JCT 2|0|ROOT 3|5|MOD 4|5|MOD 5|2|POBJ 6|2|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert match.poss_noun(tokens)

    utt = 'your turn .'
    mor = 'pro:poss:det|your n|turn .'
    syn = '1|2|DET 2|0|ROOT 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.poss_noun(tokens)

    utt = 'my turn .'
    mor = 'pro:poss:det|my n|turn .'
    syn = '1|2|DET 2|0|ROOT 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.poss_noun(tokens)

    utt = 'house shoes .'
    mor = 'n|house n|shoe-PL .'
    syn = '1|2|MOD 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.poss_noun(tokens)

    utt = 'is its +...'
    mor = 'v|be&3S pro:poss:det|its +...'
    syn = '1|0|ROOT 2|1|DET-SUBJ 3|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.poss_noun(tokens)


def poss_s_noun_test():
    "Match lines with a possessive-s+noun phrase"
    utt = "just like Connor@n's snake ."
    mor = "adv:int|just prep|like n:prop|Connor@n-POSS n|snake ."
    syn = "1|2|JCT 2|0|ROOT 3|5|MOD 4|5|MOD 5|2|POBJ 6|2|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert match.poss_s_noun(tokens)

    utt = 'house shoes .'
    mor = 'n|house n|shoe-PL .'
    syn = '1|2|MOD 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.poss_s_noun(tokens)

    utt = "this is Daddy's ."
    mor = "pro:dem|this v|be&3S n:prop|Daddy-POSS ."
    syn = "1|2|SUBJ 2|0|ROOT 3|4|MOD 4|2|PRED 5|2|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert not match.poss_s_noun(tokens)


def my_noun_test():
    '''Match lines with a possessive-my+noun phrase'''
    utt = 'it would probably hurt my belly .'
    mor = 'pro|it aux|will&COND adv:adj|probable-LY v|hurt&ZERO pro:poss:det|my n|belly .'
    syn = '1|4|SUBJ 2|4|AUX 3|4|JCT 4|0|ROOT 5|6|DET 6|4|OBJ 7|4|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.my_noun(tokens)

    utt = 'going to hurt your +...'
    mor = 'aux|go-PROG inf|to v|hurt&ZERO pro:poss:det|your +...'
    syn = '1|3|AUX 2|3|INF 3|0|ROOT 4|3|DET-OBJ 5|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.my_noun(tokens)

    utt = 'house shoes .'
    mor = 'n|house n|shoe-PL .'
    syn = '1|2|MOD 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.my_noun(tokens)


def poss_noun_sans_my_test():
    '''Match lines with a possessive+noun phrase without `my`'''
    utt = 'your turn .'
    mor = 'pro:poss:det|your n|turn .'
    syn = '1|2|DET 2|0|ROOT 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.poss_noun_sans_my(tokens)

    utt = "it's a bunny+rabbit's ears !"
    mor = "pro|it~v|be&3S det|a n|+n|bunny+n|rabbit-POSS n|ear-PL !"
    syn = "1|2|SUBJ 2|0|ROOT 3|6|DET 4|6|MOD 5|6|MOD 6|2|PRED 7|2|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert match.poss_noun_sans_my(tokens)

    utt = 'house shoes .'
    mor = 'n|house n|shoe-PL .'
    syn = '1|2|MOD 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.poss_noun_sans_my(tokens)

    utt = 'it would probably hurt my belly .'
    mor = 'pro|it aux|will&COND adv:adj|probable-LY v|hurt&ZERO pro:poss:det|my n|belly .'
    syn = '1|4|SUBJ 2|4|AUX 3|4|JCT 4|0|ROOT 5|6|DET 6|4|OBJ 7|4|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.poss_noun_sans_my(tokens)


def prep_root_test():
    '''Match lines with a root preposition w/out subject dependents'''
    utt = 'I want .'
    mor = 'pro|I v|want .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert not match.prep_root(tokens)

    utt = 'how+about in your Dash cup ?'
    mor = 'adv:wh|how+about prep|in pro:poss:det|your n:prop|Dash n|cup ?'
    syn = '1|2|JCT 2|0|ROOT 3|5|DET 4|5|MOD 5|2|POBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.prep_root(tokens)

    utt = 'over there ?'
    mor = 'prep|over adv:loc|there ?'
    syn = '1|0|ROOT-NV 2|1|POBJ 3|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.prep_root(tokens)

    utt = 'what over there ?'
    mor = 'pro:wh|what prep|over adv:loc|there ?'  
    syn = '1|2|JCT 2|0|ROOT 3|2|POBJ 4|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.prep_root(tokens)


def prep_mod_noun_test():
    '''Match lines with prepositions modifying nouns'''
    utt = 'this is for my puzzle .'
    mor = 'pro:dem|this v|be&3S prep|for pro:poss:det|my n|puzzle .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PRED 4|5|DET 5|3|POBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.prep_mod_noun(tokens)

    utt = 'this belongs with my puzzle .'
    mor = 'pro:dem|this v|belong-3S prep|with pro:poss:det|my n|puzzle .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|JCT 4|5|DET 5|3|POBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.prep_mod_noun(tokens)

    utt = 'this is the puzzle with twenty pieces .'
    mor = 'pro:dem|this v|be&3S det|the n|puzzle prep|with det:num|twenty n|pieces .'
    syn = '1|2|SUBJ 2|0|ROOT 3|4|DET 4|2|PRED 5|4|MOD 6|7|QUANT 7|5|POBJ 8|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.prep_mod_noun(tokens)


def prep_mod_verb_test():
    '''Match lines with prepositions modifying verbs'''
    utt = 'this is for my puzzle .'
    mor = 'pro:dem|this v|be&3S prep|for pro:poss:det|my n|puzzle .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PRED 4|5|DET 5|3|POBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.prep_mod_verb(tokens)

    utt = 'put it in there .'
    mor = 'v|put&ZERO pro|it prep|in adv:loc|there .'
    syn = '1|0|ROOT 2|1|OBJ 3|1|LOC 4|3|POBJ 5|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.prep_mod_verb(tokens)
    
    utt = 'what over there ?'
    mor = 'pro:wh|what prep|over adv:loc|there ?'
    syn = '1|2|JCT 2|0|ROOT 3|2|POBJ 4|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.prep_mod_verb(tokens)

    utt = "what's green on it ?"
    mor = "pro:wh|what~v|be&3S adj|green prep|on pro|it ?"
    syn = "1|2|SUBJ 2|0|ROOT 3|2|PRED 4|2|JCT 5|4|POBJ 6|2|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert match.prep_mod_verb(tokens)

    utt = 'this is the puzzle with twenty pieces .'
    mor = 'pro:dem|this v|be&3S det|the n|puzzle prep|with det:num|twenty n|pieces .'
    syn = '1|2|SUBJ 2|0|ROOT 3|4|DET 4|2|PRED 5|4|MOD 6|7|QUANT 7|5|POBJ 8|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.prep_mod_verb(tokens)


def adverb_verb_test():
    '''Match lines with adverbs modifying verbs.'''
    utt = "and then the eyes go into the pink ."
    mor = "conj:coo|and adv:tem|then det|the n|eye-PL v|go prep|into det|the n|pink ."
    syn = "1|0|ROOT 2|5|JCT 3|4|DET 4|5|SUBJ 5|1|COORD 6|5|JCT 7|8|DET 8|6|POBJ 9|1|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert match.adverb_verb(tokens) 


def infinitive_verb_test():
    '''Match lines with infinitive verbs.'''
    utt = "I don't want to get wet ."
    mor = "pro|I aux|do~neg|not aux|want inf|to v|get adj|wet ."
    syn = "1|6|SUBJ 2|6|AUX 3|2|NEG 4|6|AUX 5|6|INF 6|0|ROOT 7|6|PRED 8|6|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert match.infinitive_verb(tokens) 


def particle_verb_test():
    '''Match lines with verbs and particles.'''
    utt = 'help me clean it up .'
    mor = 'v|help pro|me v|clean pro|it ptl|up .'
    syn = '1|0|ROOT 2|1|OBJ 3|1|XCOMP 4|3|OBJ 5|3|PTL 6|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.particle_verb(tokens)


def phrase_mod_verb_test():
    '''Match lines where a verb is modified by a separate word.'''
    utt = "and then the eyes go into the pink ."
    mor = "conj:coo|and adv:tem|then det|the n|eye-PL v|go prep|into det|the n|pink ."
    syn = "1|0|ROOT 2|5|JCT 3|4|DET 4|5|SUBJ 5|1|COORD 6|5|JCT 7|8|DET 8|6|POBJ 9|1|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert match.phrase_mod_verb(tokens) 

    utt = "I walk fast ."
    mor = "pro|I v|walk adv|fast ."
    syn = "1|2|SUBJ 2|0|ROOT 3|2|JCT 4|2|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert match.phrase_mod_verb(tokens) 


def unmodified_verb_test():
    '''Match lines with unmodified verbs.'''
    utt = 'help me clean it up .'
    mor = 'v|help pro|me v|clean pro|it ptl|up .'
    syn = '1|0|ROOT 2|1|OBJ 3|1|XCOMP 4|3|OBJ 5|3|PTL 6|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.unmodified_verb(tokens)

    utt = 'clean it up .'
    mor = 'v|clean pro|it ptl|up .'
    syn = '1|0|ROOT 2|1|OBJ 3|1|PTL 4|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.unmodified_verb(tokens)


def phrase_mod_noun_test():
    '''Match lines where a noun is modified by a separate word.'''
    utt = 'little circle .'
    mor = 'adj|little n|circle .'
    syn = '1|2|MOD 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.phrase_mod_noun(tokens)
    
    utt = "just like Connor@n's snake ."
    mor = "adv:int|just prep|like n:prop|Connor@n-POSS n|snake ."
    syn = "1|2|JCT 2|0|ROOT 3|5|MOD 4|5|MOD 5|2|POBJ 6|2|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert match.phrase_mod_noun(tokens)

    utt = "no more monsters jumping on the bed !"
    mor = "qn|no qn|more n|monster-PL part|jump-PROG prep|on det|the n|bed !"  
    syn = "1|2|JCT 2|3|QUANT 3|0|ROOT-NV 4|3|XMOD 5|4|JCT 6|7|DET 7|5|POBJ 8|3|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert match.phrase_mod_noun(tokens)

    utt = "the girl in the house !"
    mor = "det|the n|girl prep|in det|the n|house !" 
    syn = "1|2|DET 2|0|ROOT-NV 3|2|MOD 4|5|DET 5|3|POBJ 6|2|PUNCT "
    tokens = TokenList(utt, mor, syn)
    assert match.phrase_mod_noun(tokens)

    utt = "girl in it !"
    mor = "n|girl prep|in pro|it !" 
    syn = "1|2|SUBJ 2|0|ROOT-NV 3|2|POBJ 4|2|PUNCT "
    tokens = TokenList(utt, mor, syn)
    assert not match.phrase_mod_noun(tokens)


def unmodified_noun_test():
    '''Match lines with unmodified nouns.'''
    utt = '&xxx doggie ?'
    mor = 'n|dog-DIM ?'
    syn = '1|0|ROOT 2|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.unmodified_noun(tokens)
    
    utt = 'little circle .'
    mor = 'adj|little n|circle .'
    syn = '1|2|MOD 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.unmodified_noun(tokens)
    
    utt = '&xxx dog ?'
    mor = 'n|dog ?'
    syn = '1|0|ROOT 2|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.unmodified_noun(tokens)


def modified_noun_test():
    '''Match lines with unmodified nouns.'''
    utt = '&xxx doggie ?'
    mor = 'n|dog-DIM ?'
    syn = '1|0|ROOT 2|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.modified_noun(tokens)
    
    utt = 'little circle .'
    mor = 'adj|little n|circle .'
    syn = '1|2|MOD 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.modified_noun(tokens)
    
    utt = '&xxx dog ?'
    mor = 'n|dog ?'
    syn = '1|0|ROOT 2|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.modified_noun(tokens)


def dangling_coordinator_test():
    '''Match lines where a coordinating conjunction does not coordinate two elements.'''
    utt = 'and I like it .'
    mor = 'conj:coo|and pro|I v|like pro|it .'
    syn = '1|0|ROOT 2|3|SUBJ 3|1|COORD 4|3|OBJ 5|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.dangling_coordinator(tokens)
    
    utt = 'and let her run out .'
    mor = 'conj:coo|and v|let pro|her v|run adv:loc|out .'
    syn = '1|0|ROOT 2|1|COORD 3|2|OBJ 4|2|XCOMP 5|4|JCT 6|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.dangling_coordinator(tokens)

    utt = 'I like John and Mary .'
    mor = 'pro|I v|like n:prop|John conj:coo|and n:prop|Mary .'
    syn = '1|2|SUBJ 2|0|ROOT 3|4|COORD 4|2|OBJ 5|4|COORD 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.dangling_coordinator(tokens)


def coordinated_nouns_test():
    '''Match lines where a coordinating conjunction coordinates two noun elements.'''
    utt = 'I like John and Mary .'
    mor = 'pro|I v|like n:prop|John conj:coo|and n:prop|Mary .'
    syn = '1|2|SUBJ 2|0|ROOT 3|4|COORD 4|2|OBJ 5|4|COORD 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.coordinated_nouns(tokens)
    
    utt = 'you and Patrick@n +...'
    mor = 'pro|you conj:coo|and n:prop|Patrick +...'
    syn = '1|2|COORD 2|0|ROOT-NV 3|2|COORD 4|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.coordinated_nouns(tokens)

    utt = 'can you make it into a worm or a snake ?'
    mor = 'aux|can pro|you v|make pro|it prep|into det|a n|worm conj:coo|or det|a n|snake ?'
    syn = '1|3|AUX 2|3|SUBJ 3|0|ROOT 4|3|OBJ 5|3|JCT 6|7|DET 7|8|COORD 8|5|POBJ 9|10|DET 10|8|COORD 11|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.coordinated_nouns(tokens)

    utt = 'and dogs +...' 
    mor = 'conj:coo|and n|dog-PL +...'
    syn = '1|0|ROOT 2|1|COORD 3|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.coordinated_nouns(tokens)
    
    utt = 'chicken and some potatoes, yes .'
    mor = 'n|chicken conj:coo|and qn|some n|potato-PL co|yes .'
    syn = '1|2|COORD 2|0|ROOT 3|4|QUANT 4|2|COORD 5|2|COM 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.coordinated_nouns(tokens)


def coordinated_verbs_test():
    '''Match lines where a coordinating conjunction coordinates two verb elements.'''  
    utt = 'I like and respect Mary .'
    mor = 'pro|I v|like conj:coo|and v|respect n:prop|Mary .'
    syn = '1|2|SUBJ 2|3|COORD 3|0|ROOT 4|3|COORD 5|4|OBJ 6|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.coordinated_verbs(tokens)
    
    utt = 'and I like it .'
    mor = 'conj:coo|and pro|I v|like pro|it .'
    syn = '1|0|ROOT 2|3|SUBJ 3|1|COORD 4|3|OBJ 5|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.coordinated_verbs(tokens)


def simple_verbs_test():
    '''match lines with a verb in the simple aspect.''' 
    utt = "I'll be good for now ."
    mor = "pro|I~aux|will v|be adj|good prep|for adv|now ."
    syn = "1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|PRED 5|3|JCT 6|5|POBJ 7|3|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert match.simple_verbs(tokens)
 
    utt = "it was very dark in there ."
    mor = "pro|it v|be&PAST&13S adv:int|very adj|dark prep|in adv:loc|there ."
    syn = "1|2|SUBJ 2|0|ROOT 3|4|JCT 4|2|PRED 5|4|JCT 6|5|POBJ 7|2|PUNCT"
    tokens = TokenList(utt, mor, syn)
    print tokens
    assert match.simple_verbs(tokens)
    
    utt = "I walk ."
    mor = "pro|I v|walk ."
    syn = "1|2|SUBJ 2|0|ROOT 3|2|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert match.simple_verbs(tokens)
    
    utt = "he's been causing trouble at the zoo ."
    mor = "pro|he~aux|have&3S aux|be&PERF part|cause-PROG n|trouble prep|at det|the n|zoo ."
    syn = "1|4|SUBJ 2|4|AUX 3|4|AUX 4|0|ROOT 5|4|OBJ 6|4|JCT 7|8|DET 8|6|POBJ 9|4|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert not match.simple_verbs(tokens)


def perfect_verbs_test():
    '''match lines with a verb in the perfective aspect'''
    utt = 'have you ever seen a cheetah ?'
    mor = 'aux|have pro|you adv|ever part|see&PERF det|a n|cheetah ?'
    syn = '1|4|AUX 2|4|OBJ 3|4|JCT 4|0|ROOT 5|6|DET 6|4|OBJ 7|4|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.perfect_verbs(tokens)
    assert not match.simple_verbs(tokens)

    utt = 'trains had lost the plane .'
    mor = 'n|train-PL aux|have&PAST part|lose&PAST det|the n|plane .'
    syn = '1|3|SUBJ 2|3|AUX 3|0|ROOT 4|5|DET 5|3|OBJ 6|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.perfect_verbs(tokens)
    
    utt = "he's been causing trouble at the zoo ."
    mor = "pro|he~aux|have&3S aux|be&PERF part|cause-PROG n|trouble prep|at det|the n|zoo ."
    syn = "1|4|SUBJ 2|4|AUX 3|4|AUX 4|0|ROOT 5|4|OBJ 6|4|JCT 7|8|DET 8|6|POBJ 9|4|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert not match.perfect_verbs(tokens)



def progressive_verbs_test():
    '''match lines with a verb in the progressive aspect''' 
    utt = "it's coming from up there ."
    mor = "pro|it~aux|be&3S part|come-PROG prep|from prep|up adv:loc|there ."
    syn = "1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|JCT 5|4|JCT 6|5|POBJ 7|3|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert match.progressive_verbs(tokens)
    assert not match.simple_verbs(tokens)
    
    utt = "I'm going to go check it out ."
    mor = "pro|I~aux|be&1S aux|go-PROG inf|to v|go v|check pro|it ptl|out ."
    syn = "1|6|SUBJ 2|6|AUX 3|6|AUX 4|5|INF 5|6|SRL 6|0|ROOT 7|6|OBJ 8|6|PTL 9|6|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert not match.progressive_verbs(tokens)


def perfect_progressive_verbs_test():
    '''match lines with a verb in the perfect progressive aspect'''
    utt = "he's been causing trouble at the zoo ."
    mor = "pro|he~aux|have&3S aux|be&PERF part|cause-PROG n|trouble prep|at det|the n|zoo ."
    syn = "1|4|SUBJ 2|4|AUX 3|4|AUX 4|0|ROOT 5|4|OBJ 6|4|JCT 7|8|DET 8|6|POBJ 9|4|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert match.perfect_progressive_verbs(tokens)
    assert not match.simple_verbs(tokens)


def future_verbs_test():
    '''match lines with a verb in the future tense''' 
    utt = "I'll be good for now ."
    mor = "pro|I~aux|will v|be adj|good prep|for adv|now ."
    syn = "1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|PRED 5|3|JCT 6|5|POBJ 7|3|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert match.future_verbs(tokens)
    assert match.simple_verbs(tokens)
    
    # utt = "what is this stamp going to do ?"
    # mor = "pro:wh|what aux|be&3S det|this n|stamp aux|go-PROG inf|to v|do ?"
    # syn = "1|7|OBJ 2|7|AUX 3|4|DET 4|7|SUBJ 5|7|AUX 6|7|INF 7|0|ROOT 8|7|PUNCT"
    # tokens = TokenList(utt, mor, syn)
    # assert match.future_verbs(tokens)
    # assert match.simple_verbs(tokens)


def past_verbs_test():
    '''match lines with a verb in the past tense''' 
    utt = 'trains had lost the plane .'
    mor = 'n|train-PL aux|have&PAST part|lose&PERF det|the n|plane .'
    syn = '1|3|SUBJ 2|3|AUX 3|0|ROOT 4|5|DET 5|3|OBJ 6|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.past_verbs(tokens)
    
    utt = 'so the block ran away into the tunnel .'
    mor = 'conj:subor|so det|the n|block v|run&PAST adv|away prep|into det|the n|tunnel .'
    syn = '1|4|CPZR 2|3|DET 3|4|SUBJ 4|0|ROOT 5|4|JCT 6|4|JCT 7|8|DET 8|6|POBJ 9|4|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.past_verbs(tokens)
    
    utt = 'we got to get some Christmas shopping done today, huh ?'
    mor = 'pro|we aux|get&PAST inf|to v|get qn|some n:prop|Christmas n:gerund|shop-GERUND part|do&PERF n|today co|huh ?'
    syn = '1|4|SUBJ 2|4|AUX 3|4|INF 4|0|ROOT 5|7|QUANT 6|7|MOD 7|4|OBJ 8|4|PRED 9|4|JCT 10|4|COM 11|4|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.past_verbs(tokens)



def present_verbs_test():
    '''match lines with a verb in the present tense'''
    utt = "it's coming from up there ."
    mor = "pro|it~aux|be&3S part|come-PROG prep|from prep|up adv:loc|there ."
    syn = "1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|JCT 5|4|JCT 6|5|POBJ 7|3|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert match.present_verbs(tokens)

    utt = "I had to put my &xxx in the air ."
    mor = "pro|I aux|have&PAST inf|to v|put pro:poss:det|my prep|in det|the n|air ."
    syn = "1|4|SUBJ 2|4|AUX 3|4|INF 4|0|ROOT 5|4|DET-OBJ 6|4|LOC 7|8|DET 8|6|POBJ 9|4|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert not match.present_verbs(tokens)

    utt = "we'll do these later ."
    mor = "pro|we~aux|will v|do pro:dem|these adv|late-CP ."
    syn = "1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|OBJ 5|3|JCT 6|3|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert not match.present_verbs(tokens)

    utt = "I will fix it for you ."
    mor = "pro|I aux|will v|fix pro|it prep|for pro|you ."
    syn = "1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|OBJ 5|3|JCT 6|5|POBJ 7|3|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert not match.present_verbs(tokens)
