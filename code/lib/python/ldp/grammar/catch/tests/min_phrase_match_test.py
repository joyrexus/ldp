from ldp.grammar import TokenList
from ldp.grammar.catch import MinimalPhraseMatcher

match = MinimalPhraseMatcher()

def bare_noun_test():
    '''Match lines with nouns lacking dependents'''
    utt = 'I want .'
    mor = 'pro|I v|want .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert not match.bare_noun(tokens)

    utt = 'I want cookie .'
    mor = 'pro|I v|want n|cookie .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|OBJ 4|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert match.bare_noun(tokens)

    utt = 'I need mom .'
    mor = 'pro|I v|need n:prop|mom .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|OBJ 4|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert not match.bare_noun(tokens), "Exclude proper nouns."

    utt = 'I want that cookie .'
    mor = 'pro|I v|want det|that n|cookie .'
    syn = '1|2|SUBJ 2|0|ROOT 3|4|DET 4|2|OBJ 5|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert not match.bare_noun(tokens)

    utt = 'because lots of babies have been born lately .'
    mor = '''conj:subor|because pro:indef|lot-PL prep|of n|baby-PL 
             aux|have aux|be&PERF part|bear&PERF adv:adj|late-LY .'''
    syn = '''1|7|CPZR 2|7|SUBJ 3|2|MOD 4|3|POBJ 5|7|AUX 6|7|AUX 
             7|0|ROOT 8|7|JCT 9|7|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.bare_noun(tokens)

    utt = 'can I have some of broccoli .'
    mor = 'aux|can pro|I v|have pro:indef|some prep|of n|broccoli .'
    syn = '1|3|AUX 2|3|SUBJ 3|0|ROOT 4|3|OBJ 5|4|MOD 6|5|POBJ 7|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.bare_noun(tokens)

    utt = "here is pizza ."
    mor = 'adv:loc|here v|be&3S n|pizza .'
    syn = '1|2|PRED 2|0|ROOT 3|2|SUBJ 4|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.bare_noun(tokens)

    utt = 'a butterfly wing .'
    mor = 'det|a n|butterfly n|wing .'
    syn = '1|3|DET 2|3|MOD 3|0|ROOT 4|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.bare_noun(tokens), "Do not match nouns that are modifiers."

    utt = 'this is a pig .'
    mor = 'pro:dem|this v|be&3S det|a n|pig .'
    syn = '1|2|SUBJ 2|0|ROOT 3|4|DET 4|2|PRED 5|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.bare_noun(tokens)

    utt = 'give it a little shake .'
    mor = 'v|give pro|it det|a adj|little n|shake .'
    syn = '1|0|ROOT 2|1|OBJ 3|5|DET 4|5|MOD 5|1|OBJ2 6|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.bare_noun(tokens)

    utt = 'good job .'
    mor = 'adj|good n|job .'
    syn = '1|2|MOD 2|0|ROOT 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.bare_noun(tokens)

    utt = "that is my clothes and this is Justin's closet ."
    mor = '''pro:dem|that v|be&3S pro:poss:det|my n:pt|clothes 
             conj:coo|and pro:dem|this v|be&3S n:prop|Justin-POSS 
             n|closet .'''
    syn = '''1|2|SUBJ 2|5|COORD 3|4|DET 4|2|PRED 5|0|ROOT 6|7|SUBJ 
             7|5|COORD 8|10|MOD 9|10|MOD 10|7|PRED 11|5|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.bare_noun(tokens)

    utt = "see Justin's guys ?"
    mor = 'v|see n:prop|Justin-POSS n|guy-PL ?'
    syn = '1|0|ROOT 2|4|MOD 3|4|MOD 4|1|OBJ 5|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.bare_noun(tokens)

    utt = 'these are my food for my kitchen so I can cook .'
    mor = '''pro:dem|these v|be&PRES pro:poss:det|my n|food prep|for
             pro:poss:det|my n|kitchen conj:subor|so pro|I aux|can 
             v|cook .'''
    syn = '''1|2|SUBJ 2|0|ROOT 3|4|DET 4|2|PRED 5|4|MOD 6|7|DET 
             7|5|POBJ 8|11|CPZR 9|11|SUBJ 10|11|AUX 11|2|CJCT 
             12|2|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.bare_noun(tokens)

    utt = 'why you holding m@l ?'
    mor = 'adv:wh|why pro|you part|hold-PROG n:let|m ?'
    syn = '1|3|JCT 2|3|SUBJ 3|0|ROOT 4|3|OBJ 5|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.bare_noun(tokens), "Do not match letters."

    utt = 'it aqua Mom .'
    mor = 'pro|it adj|aqua n:prop|Mom .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|VOC 4|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.bare_noun(tokens), "Do not match proper nouns."

    utt = 'getting kitty toes .'
    mor = 'part|get&PERF n|kitty n|toe-PL .'
    syn = '1|0|ROOT 2|3|MOD 3|1|OBJ 4|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.bare_noun(tokens), "Match nouns if their modifiers are nouns."

    utt = "It not in Zoe's closet ."
    mor = '''pro|it neg|not prep|in n:prop|Zoe-POSS n|closet .'''
    syn = '''1|3|SUBJ 2|3|NEG 3|0|ROOT 4|6|MOD 5|6|MOD 6|3|POBJ 
             7|3|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.bare_noun(tokens), "It not in Zoe's closet."

    utt = 'make a bucket of water .'
    mor = 'v|make det|a n|bucket prep|of n|water .'
    syn = '1|0|ROOT 2|3|DET 3|1|OBJ 4|3|MOD 5|4|POBJ 6|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.bare_noun(tokens)

    utt = 'make a bubble in water .'
    mor = 'v|make det|a n|bubble prep|in n|water .'
    syn = '1|0|ROOT 2|3|DET 3|1|OBJ 4|1|JCT 5|4|POBJ 6|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.bare_noun(tokens)

    utt = 'you do not want to write letters ?'
    mor = 'pro|you aux|do neg|not aux|want inf|to v|write n|letter-PL ?'
    syn = '''1|6|SUBJ 2|6|AUX 3|2|NEG 4|6|AUX 5|6|INF 6|0|ROOT 
             7|6|OBJ 8|6|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.bare_noun(tokens)

def det_noun_test():
    '''Match lines with two-element determiner+noun phrases'''
    utt = 'I want .'
    mor = 'pro|I v|want .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert not match.det_noun(tokens)

    utt = 'this is a pig .'
    mor = 'pro:dem|this v|be&3S det|a n|pig .'
    syn = '1|2|SUBJ 2|0|ROOT 3|4|DET 4|2|PRED 5|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.det_noun(tokens)

    utt = "Sam, we have to find those pieces ."
    mor = 'n:prop|Sam pro|we aux|have inf|to v|find det|those n|piece-PL .'
    syn = '1|5|VOC 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|7|DET 7|5|OBJ 8|5|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.det_noun(tokens)

    utt = "my keys ."
    mor = 'pro:poss:det|my n|key-PL .'
    syn = '1|2|DET 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.det_noun(tokens)

    utt = "it is my unbirthday today ."
    mor = 'pro|it v|be&3S pro:poss:det|my un#n|birthday n|today .'
    syn = '1|2|SUBJ 2|0|ROOT 3|5|DET 4|5|MOD 5|2|PRED 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.det_noun(tokens)

    utt = "give it a little shake ."
    mor = 'v|give pro|it det|a adj|little n|shake .'
    syn = '1|0|ROOT 2|1|OBJ 3|5|DET 4|5|MOD 5|1|OBJ2 6|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.det_noun(tokens)

    utt = 'good job .'
    mor = 'adj|good n|job .'
    syn = '1|2|MOD 2|0|ROOT 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.det_noun(tokens)

def adj_noun_test():
    '''Match lines with two-element adjective+noun phrases.'''
    utt = 'I want .'
    mor = 'pro|I v|want .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)

    utt = 'good job .'
    mor = 'adj|good n|job .'
    syn = '1|2|MOD 2|0|ROOT 3|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert match.adj_noun(tokens)

    utt = "that is blue bronco ."
    mor = 'pro:dem|that v|be&3S adj|blue n|bronco .'
    syn = '1|2|SUBJ 2|0|ROOT 3|4|MOD 4|2|PRED 5|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.adj_noun(tokens)

    utt = "give it a little shake ."
    mor = 'v|give pro|it det|a adj|little n|shake .'
    syn = '1|0|ROOT 2|1|OBJ 3|5|DET 4|5|MOD 5|1|OBJ2 6|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)

    utt = "see Justin's guys ?"
    mor = 'v|see n:prop|Justin-POSS n|guy-PL ?'
    syn = '1|0|ROOT 2|4|MOD 3|4|MOD 4|1|OBJ 5|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)

    utt = "cookie cutter ."
    mor = 'n|cookie n:v|cut-AGT .'
    syn = '1|2|MOD 2|0|ROOT 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)

    utt = "lucky glove up there ."
    mor = 'n:prop|Lucky n|glove prep|up adv:loc|there .'
    syn = '1|2|MOD 2|3|SUBJ 3|0|ROOT 4|3|POBJ 5|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)

    utt = "number four ?"
    mor = 'n|number det:num|four ?'
    syn = '1|0|ROOT 2|1|MOD 3|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)

    utt = "is that the right pattern ?"
    mor = 'v|be&3S pro:dem|that det|the adj|right n|pattern ?'
    syn = '1|0|ROOT 2|1|SUBJ 3|5|DET 4|5|MOD 5|1|PRED 6|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)

    utt = "kevy where is Mom's favorite truck ?"
    mor = '''n:prop|Kevy adv:wh|where v|be&3S n:prop|Mom-POSS 
             adj|favorite n|truck ?'''
    syn = '''1|3|VOC 2|3|PRED 3|0|ROOT 4|7|MOD 5|7|MOD 6|7|MOD 
             7|3|SUBJ 8|3|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)

    utt = "do you want your little dinosaurs, too ?"
    mor = '''aux|do pro|you v|want pro:poss:det|your adj|little
             n|dinosaur-PL post|too ?'''
    syn = '''1|3|AUX 2|3|SUBJ 3|0|ROOT 4|6|DET 5|6|MOD 6|3|OBJ 
             7|3|JCT 8|3|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)

    utt = "trunk on elephant ."
    mor = 'n|trunk prep|on n|elephant .'
    syn = '1|0|ROOT-NV 2|1|MOD 3|2|POBJ 4|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)

    utt = "knot in there ."
    mor = 'n|knot prep|in adv:loc|there .'
    syn = '1|0|ROOT-NV 2|1|MOD 3|2|POBJ 4|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)

    utt = 'it has big sharp teeth .'
    mor = 'pro|it v|have&3S adj|big adj|sharp n|tooth&PL .'
    syn = '1|2|SUBJ 2|0|ROOT 3|5|MOD 4|5|MOD 5|2|OBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)

    utt = 'red black naked bears .'
    mor = 'adj|red adj|black adj|naked n|bear-PL .'
    syn = '1|4|MOD 2|4|MOD 3|4|MOD 4|0|ROOT-NV 5|4|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)

    utt = 'big purple ball Mama .'
    mor = 'adj|big adj|purple n|ball n:prop|Mama .'
    syn = '1|3|MOD 2|3|MOD 3|0|ROOT-NV 4|3|VOC 5|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)

    utt = 'very good baby !'
    mor = 'adv:int|very adj|good n|baby !'
    syn = '1|2|JCT 2|3|MOD 3|0|ROOT-NV 4|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)

    utt = 'eyes full of water .'
    mor = 'n|eye-PL adj|full prep|of n|water .'
    syn = '1|0|ROOT-NV 2|1|MOD 3|2|JCT 4|3|POBJ 5|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_noun(tokens)

def quant_noun_test():
    '''Match lines with two-element quantifier+noun phrases.'''
    utt = 'I want .'
    mor = 'pro|I v|want .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert not match.quant_noun(tokens)

    utt = "did you have some sky on yours ?"
    mor = '''aux|do&PAST pro|you v|have qn|some n|sky prep|on 
             pro:poss|yours ?'''
    syn = '''1|3|AUX 2|3|SUBJ 3|0|ROOT 4|5|QUANT 5|3|OBJ 6|3|JCT 
             7|6|POBJ 8|3|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.quant_noun(tokens)

    utt = "no edges over here huh ?"
    mor = 'qn|no n|edge-PL prep|over adv:loc|here co|huh ?'
    syn = '1|2|QUANT 2|0|ROOT 3|2|JCT 4|3|POBJ 5|2|COM 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.quant_noun(tokens)

    utt = "look at all these boats ."
    mor = 'v|look ptl|at qn|all det|these n|boat-PL .'
    syn = '1|0|ROOT 2|1|PTL 3|5|QUANT 4|5|DET 5|1|OBJ 6|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.quant_noun(tokens)

    utt = "kevin we need to buy more straight pieces ."
    mor = '''n:prop|Kevin pro|we aux|need inf|to v|buy qn|more
             adj|straight n|piece-PL .'''
    syn = '''1|5|VOC 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|8|QUANT 
             7|8|MOD 8|5|OBJ 9|5|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.quant_noun(tokens)

    utt = "two block ."
    mor = 'det:num|two n|block .'
    syn = '1|2|QUANT 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.quant_noun(tokens)

    utt = 'I going draw some more names .'
    mor = 'pro|I aux|go-PROG v|draw qn|some qn|more n|name-PL .'
    syn = '1|3|SUBJ 2|3|AUX 3|0|ROOT 4|5|JCT 5|6|QUANT 6|3|OBJ 7|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.quant_noun(tokens)

    utt = 'one more color and then &xxx .'
    mor = 'det:num|one qn|more n|color conj:coo|and adv:tem|then .'
    syn = '''1|3|QUANT 2|3|QUANT 3|4|COORD-ROOT-NV 4|0|ROOT-NV 
             5|4|COORD-ROOT-NV 6|4|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.quant_noun(tokens)

    utt = "but if you try one more times then you'll get to do it ."
    mor = '''conj:coo|but conj:subor|if pro|you v|try det:num|one qn|more 
             n|time-PL adv:tem|then pro|you~aux|will aux|get inf|to v|do 
             pro|it .'''
    syn = '''1|0|ROOT 2|4|CPZR 3|4|SUBJ 4|13|CJCT 5|7|QUANT 6|7|QUANT 7|4|OBJ 
             8|13|JCT 9|13|SUBJ 10|13|AUX 11|13|AUX 12|13|INF 13|1|COORD-ROOT 
             14|13|OBJ 15|1|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.quant_noun(tokens)

    utt = 'only one children can sit there .'
    mor = 'adv|only det:num|one n|child&PL aux|can v|sit adv:loc|there .'
    syn = '1|2|JCT 2|3|QUANT 3|5|SUBJ 4|5|AUX 5|0|ROOT 6|5|JCT 7|5|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.quant_noun(tokens)

    utt = 'I want some more Barbie &xxx because I keep tearing &xxx up .'
    mor = '''pro|I v|want qn|some qn|more n:prop|Barbie conj:subor|because 
             pro|I aux|keep part|tear-PROG ptl|up .'''
    syn = '''1|2|SUBJ 2|0|ROOT 3|4|JCT 4|5|QUANT 5|2|OBJ 6|9|CPZR 7|9|SUBJ 
             8|9|AUX 9|2|CJCT 10|9|PTL 11|2|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.quant_noun(tokens)

def poss_noun_test():
    '''Match lines with two-element possessive+noun phrases.'''
    utt = 'I want .'
    mor = 'pro|I v|want .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert not match.poss_noun(tokens)

    utt = "this is our remote ."
    mor = 'pro:dem|this v|be&3S pro:poss:det|our n|remote .'
    syn = '1|2|SUBJ 2|0|ROOT 3|4|DET 4|2|PRED 5|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.poss_noun(tokens)

    utt = "because I fall and busted my head open ."
    mor = '''conj:subor|because pro|I v|fall conj:coo|and v|bust-PAST 
             pro:poss:det|my n|head adv|open .'''
    syn = '''1|3|CPZR 2|3|SUBJ 3|4|COORD 4|0|ROOT 5|4|COORD 6|7|DET 
             7|5|OBJ 8|5|JCT 9|4|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert match.poss_noun(tokens)

    utt = "I got to get all my money ."
    mor = '''pro|I aux|get&PAST inf|to v|get qn|all pro:poss:det|my n|money .'''
    syn = '''1|4|SUBJ 2|4|AUX 3|4|INF 4|0|ROOT 5|7|QUANT 6|7|DET 7|4|OBJ 
             8|4|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.poss_noun(tokens)

    utt = "what is our secret mission ?"
    mor = 'pro:wh|what v|be&3S pro:poss:det|our adj|secret n|mission ?'
    syn = '1|2|PRED 2|0|ROOT 3|5|DET 4|5|MOD 5|2|SUBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.poss_noun(tokens)

    utt = "my key ."
    mor = 'pro:poss:det|my n|key-PL .'
    syn = '1|2|DET 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.poss_noun(tokens)

    utt = 'these are Japan worms .'
    mor = 'pro:dem|these v|be&PRES n:prop|Japan n|worm-PL .'
    syn = '1|2|SUBJ 2|0|ROOT 3|4|MOD 4|2|PRED 5|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.poss_noun(tokens)

    utt = 'and I put my Batman band_aids on it .'
    mor = '''conj:coo|and pro|I v|put&ZERO pro:poss:det|my n:prop|Batman 
             n|band_aid-PL prep|on pro|it .'''
    syn = '''1|0|ROOT 2|3|SUBJ 3|1|COORD-ROOT 4|6|DET 5|6|MOD 6|3|OBJ 
             7|3|LOC 8|7|POBJ 9|1|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.poss_noun(tokens)

    utt = 'these are not Toygear tracks .'
    mor = 'pro:dem|these v|be&PRES neg|not n:prop|Toygear n|track-PL .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|NEG 4|5|MOD 5|2|PRED 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.poss_noun(tokens)

    utt = "it not in Zoe's closet ."
    mor = 'pro|it neg|not prep|in n:prop|Zoe-POSS n|closet .'
    syn = '1|3|SUBJ 2|3|NEG 3|0|ROOT 4|6|MOD 5|6|MOD 6|3|POBJ 7|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.poss_noun(tokens)

def det_pro_indef_test():
    '''Match lines with two-element determiner+indefinite-pronoun phrases.'''
    utt = 'I want .'
    mor = 'pro|I v|want .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert not match.det_pro_indef(tokens)

    utt = 'I want to play this one .'
    mor = 'pro|I aux|want inf|to v|play det|this pro:indef|one .'
    syn = '1|4|SUBJ 2|4|AUX 3|4|INF 4|0|ROOT 5|6|DET 6|4|OBJ 7|4|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.det_pro_indef(tokens)

    utt = 'what is that one ?'
    mor = 'pro:wh|what v|be&3S det|that pro:indef|one ?'
    syn = '1|2|PRED 2|0|ROOT 3|4|DET 4|2|SUBJ 5|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.det_pro_indef(tokens)

    utt = "I'll go get this big one ."
    mor = 'pro|I aux|will v|go v|get det|this adj|big pro:indef|one .'
    syn = '''1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|XCOMP 5|7|DET 6|7|MOD 
             7|4|OBJ 8|3|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.det_pro_indef(tokens)

    utt = "I'm going to put these in my one +..."
    mor = '''pro|I aux|be&1S aux|go-PROG inf|to v|put&ZERO pro:dem|these 
             prep|in pro:poss:det|my pro:indef|one +...'''
    syn = '''1|5|SUBJ 2|5|AUX 3|5|AUX 4|5|INF 5|0|ROOT 6|5|OBJ 
             7|5|LOC 8|9|DET 9|7|POBJ 10|5|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.det_pro_indef(tokens)

def adj_pro_indef_test():
    '''Match lines with two-element adjective+indefinite-pronoun phrases.'''
    utt = 'I want .'
    mor = 'pro|I v|want .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|PUNC'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_pro_indef(tokens)

    utt = "top one ?"
    mor = 'adj|top pro:indef|one ?'
    syn = '1|2|MOD 2|0|ROOT 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.adj_pro_indef(tokens)

    utt = "mom, I want blue one ."
    mor = 'n:prop|Mom pro|I v|want adj|blue pro:indef|one .'
    syn = '1|3|VOC 2|3|SUBJ 3|0|ROOT 4|5|MOD 5|3|OBJ 6|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert match.adj_pro_indef(tokens)

    utt = "I'll go get this big one ."
    mor = '''pro|I aux|will v|go v|get det|this adj|big pro:indef|one .'''
    syn = '''1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|XCOMP 5|7|DET 6|7|MOD 
             7|4|OBJ 8|3|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_pro_indef(tokens)

    utt = 'this is going to be my ancient one .'
    mor = '''pro:dem|this aux|be&3S aux|go-PROG inf|to v|be 
             pro:poss:det|my adj|ancient pro:indef|one .'''
    syn = '''1|5|SUBJ 2|5|AUX 3|5|AUX 4|5|INF 5|0|ROOT 6|8|DET 
             7|8|MOD 8|5|PRED 9|5|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_pro_indef(tokens)

    utt = "where is Mom's gold one ?"
    mor = '''adv:wh|where v|be&3S n:prop|Mom-POSS adj|gold 
             pro:indef|one ?'''
    syn = '''1|2|PRED 2|0|ROOT 3|6|MOD 4|6|MOD 5|6|MOD 6|2|SUBJ 
             7|2|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_pro_indef(tokens)

    utt = "some right here !"
    mor = 'pro:indef|some adv|right adv:loc|here !'
    syn = '1|0|ROOT-NV 2|3|JCT 3|1|MOD 4|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_pro_indef(tokens)

    utt = "One for me."
    mor = 'pro:indef|one prep|for pro|me .'
    syn = '1|0|ROOT-NV 2|1|MOD 3|2|POBJ 4|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not match.adj_pro_indef(tokens)
