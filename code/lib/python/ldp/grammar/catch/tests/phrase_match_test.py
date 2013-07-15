from ldp.grammar import TokenList
from ldp.grammar.catch import PhraseMatcher

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

    utt = 'house shoes .'
    mor = 'n|house n|shoe-PL .'
    syn = '1|2|MOD 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.noun_noun(tokens)

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
    assert not match.quant_noun(tokens), 'Is this correct?'

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

def not_subjects_test():
    '''Test that all tokens do not contain a subject'''
    utt = 'I want .'
    mor = 'pro|I v|want .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert not match.not_subjects(tokens)
    assert match.not_subjects(tokens[1:])

def prep_root_test():
    '''Match lines with root prepositions without any subject dependents'''
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

def prep_mod_verbal_test():
    '''Match lines with prepositions modifying verbs or auxiliaries'''
    utt = 'this is for my puzzle .'
    mor = 'pro:dem|this v|be&3S prep|for pro:poss:det|my n|puzzle .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PRED 4|5|DET 5|3|POBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.prep_mod_verbal(tokens)

    utt = 'put it in there .'
    mor = 'v|put&ZERO pro|it prep|in adv:loc|there .'
    syn = '1|0|ROOT 2|1|OBJ 3|1|LOC 4|3|POBJ 5|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.prep_mod_verbal(tokens)

    utt = 'what over there ?'
    mor = 'pro:wh|what prep|over adv:loc|there ?'  
    syn = '1|2|JCT 2|0|ROOT 3|2|POBJ 4|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.prep_mod_verbal(tokens)

def prep_mod_noun():
    '''Match lines with prepositions modifying nouns'''
    utt = 'this is for my puzzle .'
    mor = 'pro:dem|this v|be&3S prep|for pro:poss:det|my n|puzzle .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PRED 4|5|DET 5|3|POBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.prep_mod_noun(tokens)


'''
[*] prepositions as sentence roots
[*] prepositional phrases modifying verbs or auxiliaries
[ ] prepositional phrases modifying nouns

Preposition Modifying Subject Noun
x.pos = "prep"
    and x.dep = y.num
    and y.is_noun and y.rel is "SUBJ"

Preposition Modifying Non-Subject Noun
x.pos = "prep"
    and x.dep = y.num
    and y.is_noun and y.rel is not "SUBJ"
'''

def det_adj_noun_test():
    '''Match lines with determiner+adjective+noun phrases.'''
    utt = 'I want .'
    mor = 'pro|I v|want .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert not match.det_adj_noun(tokens)

    utt = "is that the right pattern ?"
    mor = 'v|be&3S pro:dem|that det|the adj|right n|pattern ?'
    syn = '1|0|ROOT 2|1|SUBJ 3|5|DET 4|5|MOD 5|1|PRED 6|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.det_adj_noun(tokens)

    utt = "that probably goes by this pretty blue stuff, huh ?"
    mor = '''pro:dem|that adv:adj|probable-LY v|go-3S prep|by 
             det|this adj|pretty adj|blue n|stuff co|huh ?'''
    syn = '''1|3|SUBJ 2|3|JCT 3|0|ROOT 4|3|JCT 5|8|DET 6|8|MOD 
             7|8|MOD 8|4|POBJ 9|3|COM 10|3|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.det_adj_noun(tokens)

    utt = "Kevin we need to buy more straight pieces ."
    mor = '''n:prop|Kevin pro|we aux|need inf|to v|buy qn|more 
             adj|straight n|piece-PL .'''
    syn = '''1|5|VOC 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|8|QUANT 
             7|8|MOD 8|5|OBJ 9|5|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.det_adj_noun(tokens)

    utt = "what is our secret mission ?"
    mor = 'pro:wh|what v|be&3S pro:poss:det|our adj|secret n|mission ?'
    syn = '1|2|PRED 2|0|ROOT 3|5|DET 4|5|MOD 5|2|SUBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.det_adj_noun(tokens)

def det_adj_pro_indef_test():
    '''Match lines with determiner+adjective+indefinite-pronoun phrases.'''
    utt = 'I want to play this one .'
    mor = 'pro|I aux|want inf|to v|play det|this pro:indef|one .'
    syn = '1|4|SUBJ 2|4|AUX 3|4|INF 4|0|ROOT 5|6|DET 6|4|OBJ 7|4|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.det_adj_pro_indef(tokens)

    utt = 'what is that one ?'
    mor = 'pro:wh|what v|be&3S det|that pro:indef|one ?'
    syn = '1|2|PRED 2|0|ROOT 3|4|DET 4|2|SUBJ 5|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.det_adj_pro_indef(tokens)

    utt = "I'll go get this big one ."
    mor = 'pro|I aux|will v|go v|get det|this adj|big pro:indef|one .'
    syn = '''1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|XCOMP 5|7|DET 6|7|MOD 
                      7|4|OBJ 8|3|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.det_adj_pro_indef(tokens)

    utt = 'is that the right one ?'
    mor = 'v|be&3S pro:dem|that det|the adj|right pro:indef|one ?'
    syn = '1|0|ROOT 2|1|SUBJ 3|5|DET 4|5|MOD 5|1|PRED 6|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.det_adj_pro_indef(tokens)

    utt = 'that the wrong one Mom .'
    mor = 'pro:dem|that det|the adj|wrong pro:indef|one n:prop|Mom .'
    syn = '1|4|SUBJ 2|4|DET 3|4|MOD 4|0|ROOT 5|4|VOC 6|4|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.det_adj_pro_indef(tokens)

    utt = '''so do we have all the green ones now ?'''
    mor = '''co|so aux|do pro|we v|have qn|all det|the adj|green
             pro:indef|one-PL adv|now ?'''
    syn = '''1|4|COM 2|4|AUX 3|4|SUBJ 4|0|ROOT 5|8|QUANT 6|8|DET
             7|8|MOD 8|4|OBJ 9|4|JCT 10|4|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.det_adj_pro_indef(tokens)

    utt = '''Where's my green one at?'''
    mor = '''adv:wh|where v|be&3S pro:poss:det|my adj|green
             pro:indef|one ptl|at ?'''
    syn = '''1|2|PRED 2|0|ROOT 3|5|DET 4|5|MOD 5|2|SUBJ 6|2|PTL
             7|2|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.det_adj_pro_indef(tokens)

def det_quant_noun_test():
    '''Match lines with determiner+quantifier+noun phrases.'''
    pass

def poss_quant_noun_test():
    '''Match lines with possessive+quantifier+noun phrases.'''
    pass

def poss_adj_noun_test():
    '''Match lines with possessive+adjective+noun phrases.'''
    pass
