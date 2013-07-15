from ldp.grammar import Token, TokenList
from ldp.grammar.catch import TokenMatcher, TokenListMatcher

match = TokenListMatcher()

def verb_rel_test():
    '''Test verb_rel regex pattern'''
    VERB_REL = ["ROOT", "CSUBJ", "XSUBJ", 
                        "CPRED", "XPRED", 
                        "COMP", "XCOMP", 
                        "CMOD", "XMOD", 
                        "CJCT", "XJCT"]
    assert all(TokenListMatcher().verb_rel.match(r) for r in VERB_REL)

def token_match_test():
    '''Test TokenMatcher match methods'''
    match = TokenMatcher()

    t = Token(dict(word="jumping", lemma="jump", pos="v"))
    assert match.verb(t)
    assert not match.noun(t)

    t = Token(dict(word="foo", pos="n:v"))
    assert match.noun(t)
    assert match.noun_simple(t)

    t = Token(dict(word="foo", pos="neg"))
    assert not match.noun(t)
    assert not match.noun_simple(t)

    t = Token(dict(word="foo", pos="neg"))
    assert not match.noun(t)
    assert not match.noun_simple(t)

    t = Token(dict(word="foo", pos="pro:dem"))
    assert match.noun(t)
    assert not match.noun_simple(t)

    t = Token(dict(lemma="the", pos="det", rel="DET"))
    assert match.det(t), "is determiner"

    t = Token(dict(lemma="another", pos="det", rel="DET"))
    assert not match.det(t), "is not determiner"
    assert match.quant(t), "is a quantifier"

    t = Token(dict(word="sunny", pos="adj", rel="MOD"))
    assert match.adj(t), "is an adjective"

    t = Token(dict(lemma="some", rel="QUANT"))
    assert match.quant(t), "is a quantifier"

    t = Token(dict(word="your", pos="pro:poss:det", rel="DET"))
    assert match.poss(t), "is possessive"

    t = Token(dict(word="'s", pos="POSS", rel="POBJ"))
    assert match.poss(t), "is possessive"

    t = Token(dict(word="some", pos="pro:indef", rel="OBJ"))
    assert match.pro_indef(t), "is an indefinite pronoun"

def noun_simple_test():
    '''Match lines with a simple noun'''
    utt = "that is blue bronco ."
    mor = 'pro:dem|that v|be&3S adj|blue n|bronco .'
    syn = '1|2|SUBJ 2|0|ROOT 3|4|MOD 4|2|PRED 5|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.has_noun_simple(tokens)

    utt = 'I want .'
    mor = 'pro|I v|want .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert not match.has_noun_simple(tokens)

def noun_proper_test():
    '''Match lines with a proper noun'''
    utt = 'I want .'
    mor = 'pro|I v|want .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert not match.has_noun_proper(tokens)

    utt = 'Anielle .'
    mor = 'n:prop|Anielle .'
    syn = '1|0|ROOT-NV 2|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.has_noun_proper(tokens)

    utt = "no that's Chanukkah ."
    mor = 'co|no pro:dem|that~v|be&3S n:prop|Chanukkah .'
    syn = '1|3|COM 2|3|SUBJ 3|0|ROOT 4|3|PRED 5|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.has_noun_proper(tokens)
    assert tokens(match.has_noun_proper)

def noun_plural_test():
    '''Match lines with a plural noun'''
    utt = 'I want .'
    mor = 'pro|I v|want .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert not match.has_noun_plural(tokens)
    assert not tokens(match.has_noun_plural)

def pronoun_personal_test():
    '''Match lines with a personal pronoun'''
    utt = 'I want .'
    mor = 'pro|I v|want .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert match.has_pronoun_personal(tokens)
    assert tokens(match.has_pronoun_personal)

    utt = "my keys ."
    mor = 'pro:poss:det|my n|key-PL .'
    syn = '1|2|DET 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.has_pronoun_personal(tokens)
    assert not tokens(match.has_pronoun_personal)

def past_tense_test():
    '''Match lines with a past tense verb form'''
    utt = 'I want .'
    mor = 'pro|I v|want .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert not match.has_past_tense(tokens)
    assert not tokens(match.has_past_tense)

    utt = "did you have some sky on yours ?"
    mor = '''aux|do&PAST pro|you v|have qn|some n|sky prep|on 
             pro:poss|yours ?'''
    syn = '''1|3|AUX 2|3|SUBJ 3|0|ROOT 4|5|QUANT 5|3|OBJ 6|3|JCT 
             7|6|POBJ 8|3|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.has_past_tense(tokens)
    assert tokens(match.has_past_tense)

    utt = 'I got to win .'
    mor = 'pro|I aux|get&PAST inf|to v|win .'
    syn = '1|4|SUBJ 2|4|AUX 3|4|INF 4|0|ROOT 5|4|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.has_past_tense(tokens)
    assert tokens(match.has_past_tense)

    utt = 'alright, I got to go wake Dad .'
    mor = 'co|alright pro|I aux|get&PAST inf|to v|go v|wake n:prop|Dad .'
    syn = '1|6|COM 2|6|SUBJ 3|6|AUX 4|5|INF 5|6|SRL 6|0|ROOT 7|6|OBJ 8|6|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.has_past_tense(tokens)
    assert tokens(match.has_past_tense)

def infinitive_test():
    '''Match lines with an infinitive form'''
    utt = 'I got to win .'
    mor = 'pro|I aux|get&PAST inf|to v|win .'
    syn = '1|4|SUBJ 2|4|AUX 3|4|INF 4|0|ROOT 5|4|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.has_infinitive(tokens)

    utt = 'you have to .'
    mor = 'pro|you aux|have inf|to .'
    syn = '1|3|SUBJ 2|3|AUX 3|0|INF-ROOT 4|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.has_infinitive(tokens)

    utt = "I don't know how to ."
    mor = 'pro|I aux|do~neg|not v|know adv:wh|how inf|to .'
    syn = '1|4|SUBJ 2|4|AUX 3|2|NEG 4|0|ROOT 5|6|JCT 6|4|INF-XCOMP 7|4|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.has_infinitive(tokens)

    utt = '''or you can put it anywhere you want to .'''
    mor = '''conj:coo|or pro|you aux|can v|put&ZERO pro|it adv:loc|anywhere
             pro|you aux|want inf|to .'''
    syn = '''1|0|ROOT 2|4|SUBJ 3|4|AUX 4|1|COORD 5|4|OBJ 6|4|LOC 7|9|SUBJ
             8|9|AUX 9|6|INF-CJCT 10|1|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.has_infinitive(tokens)

def progessive_test():
    '''Match lines with a progressive form'''
    utt = "I'm going to put these in my one +..."
    mor = '''pro|I aux|be&1S aux|go-PROG inf|to v|put&ZERO pro:dem|these 
             prep|in pro:poss:det|my pro:indef|one +...'''
    syn = '''1|5|SUBJ 2|5|AUX 3|5|AUX 4|5|INF 5|0|ROOT 6|5|OBJ 
             7|5|LOC 8|9|DET 9|7|POBJ 10|5|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.has_progressive(tokens)

    utt = 'here is the missing hamburger .'
    mor = 'adv:loc|here v|be&3S det|the part|miss-PROG n|hamburger .'
    syn = '1|2|PRED 2|0|ROOT 3|5|DET 4|5|MOD 5|2|SUBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.has_progressive(tokens)

def verb_third_singular_test():
    '''Match lines with a third person singular form'''
    utt = "that probably goes by this pretty blue stuff, huh ?"
    mor = '''pro:dem|that adv:adj|probable-LY v|go-3S prep|by 
             det|this adj|pretty adj|blue n|stuff co|huh ?'''
    syn = '''1|3|SUBJ 2|3|JCT 3|0|ROOT 4|3|JCT 5|8|DET 6|8|MOD 
             7|8|MOD 8|4|POBJ 9|3|COM 10|3|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.has_verb_third_singular(tokens)

    utt = "Mama, it's your turn ."
    mor = 'n:prop|Mama pro|it~v|be&3S pro:poss:det|your n|turn .'
    syn = '1|3|VOC 2|3|SUBJ 3|0|ROOT 4|5|DET 5|3|PRED 6|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.has_verb_third_singular(tokens)

    utt = 'no, what was it ?'
    mor = 'co|no pro:wh|what v|be&PAST&13S pro|it ?'
    syn = '1|3|COM 2|3|PRED 3|0|ROOT 4|3|SUBJ 5|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.has_verb_third_singular(tokens)

def conj_noncoord_test():
    '''Match lines with a non-coordinating conjunction'''
    utt = "you'll see if you like them ."
    mor = "pro|you~aux|will v|see conj:subor|if pro|you v|like pro|them ."
    syn = '''1|3|SUBJ 2|3|AUX 3|0|ROOT 4|6|CPZR 5|6|SUBJ 6|3|COMP
             7|6|OBJ 8|3|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.has_conj_noncoord(tokens)

def clausal_complement_test():
    '''Match lines with a clausal complement'''
    utt = "I'll go get this big one ."
    mor = 'pro|I aux|will v|go v|get det|this adj|big pro:indef|one .'
    syn = '''1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|XCOMP 5|7|DET 6|7|MOD 
             7|4|OBJ 8|3|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.has_clausal_complement(tokens)

def clausal_adjunct_test():
    '''Match lines with a clausal adjunct'''
    utt = "some right here !"
    mor = 'pro:indef|some adv|right adv:loc|here !'
    syn = '1|0|ROOT-NV 2|3|JCT 3|1|MOD 4|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.has_clausal_adjunct(tokens)

    utt = "but if you try one more times then you'll get to do it ."
    mor = '''conj:coo|but conj:subor|if pro|you v|try det:num|one qn|more 
             n|time-PL adv:tem|then pro|you~aux|will aux|get inf|to v|do 
             pro|it .'''
    syn = '''1|0|ROOT 2|4|CPZR 3|4|SUBJ 4|13|CJCT 5|7|QUANT 6|7|QUANT 7|4|OBJ 
             8|13|JCT 9|13|SUBJ 10|13|AUX 11|13|AUX 12|13|INF 13|1|COORD-ROOT 
             14|13|OBJ 15|1|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.has_clausal_adjunct(tokens)

def clausal_predicate_test():
    '''Match lines with a clausal predicate'''
    utt = "because you don't seem to know how to act with friends ."
    mor = '''conj:subor|because pro|you aux|do neg|not v|seem inf|to 
             v|know adv:wh|how inf|to v|act prep|with n|friend-PL .'''
    syn = '''1|5|CPZR 2|5|SUBJ 3|5|AUX 4|3|NEG 5|0|ROOT 6|7|INF 7|5|XPRED 
             8|10|JCT 9|10|INF 10|7|XCOMP 11|10|JCT 12|11|POBJ 13|5|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.has_clausal_predicate(tokens)

def clausal_modifier_test():
    '''Match lines with a clausal modifier'''
    utt = '''you can move anybody you want to move .'''
    mor = '''pro|you aux|can v|move pro:indef|anybody pro|you 
             aux|want inf|to v|move .'''
    syn = '''1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|OBJ 5|8|SUBJ 6|8|AUX 
             7|8|INF 8|4|XMOD 9|3|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.has_clausal_modifier(tokens)

def clausal_subject_test():
    '''Match lines with a clausal subject'''
    utt = 'so fighting makes him a bad guy ?'
    mor = 'co|so part|fight-PROG v|make-3S pro|him det|a adj|bad n|guy ?'
    syn = '''1|3|COM 2|3|XSUBJ 3|0|ROOT 4|3|OBJ 5|7|DET 6|7|MOD 7|3|PRED 
             8|3|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.has_clausal_subject(tokens)

    utt = "you think getting up there is something you're allowed to do ?"
    mor = '''pro|you v|think part|get-PROG prep|up adv:loc|there v|be&3S 
             pro:indef|something pro|you~aux|be&PRES part|allow-PERF inf|to 
             v|do ?'''
    syn = '''1|2|SUBJ 2|0|ROOT 3|6|XSUBJ 4|3|PRED 5|4|POBJ 6|2|COMP 7|6|PRED 
             8|10|SUBJ 9|10|AUX 10|7|CMOD 11|12|INF 12|10|XCOMP 13|2|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.has_clausal_subject(tokens)

    utt = '''no, licking the knife is not a good thing .'''
    mor = '''co|no part|lick-PROG det|the n|knife v|be&3S neg|not det|a 
             adj|good n|thing .'''
    syn = '''1|5|COM 2|5|XSUBJ 3|4|DET 4|2|OBJ 5|0|ROOT 6|5|NEG 7|9|DET 8|9|MOD 
             9|5|PRED 10|5|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.has_clausal_subject(tokens)
