from ldp.grammar import TokenList


def depth_from_test():
    '''Testing depth_from method'''
    utt = '''we make cloth more beautiful than any you could imagine, 
             said the first .'''
    mor = '''pro|we v|make n|cloth adv|more adj|beautiful prep|than 
             pro:indef|any pro|you aux|could v|imagine v|say&PAST 
             det|the adj|first .'''
    syn = '''1|2|SUBJ 2|11|COMP 3|2|OBJ 4|5|JCT 5|3|MOD 6|5|JCT 7|6|POBJ
             8|10|SUBJ 9|10|AUX 10|7|CMOD 11|0|ROOT 12|13|DET 13|11|SUBJ 
             14|11|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    parent = tokens.num(3)
    assert parent.word == "cloth"
    assert tokens.paths_from(parent) == \
           ['cloth', ['beautiful', ['more'], 
                                   ['than', ['any', ['imagine', ['you'], 
                                                                ['could']]]]]]
    # LEVELS:        1             2        3       4           5      
    assert tokens.max_path_from(parent) == \
           ['cloth', ['beautiful', ['than', ['any', ['imagine', ['you']]]]]]
    assert tokens.depth_from(parent) == 5

    utt = '''we make beautiful expensive exotic fine sparkly brocade silk 
             cloth said the first .'''
    mor = '''pro|we v|make adj|beautiful adj|expensive adj|exotic adj|fine
             adj|sparkly n|brocade n|silk n|cloth v|say&PAST det|the 
             adj|first .'''
    syn = '''1|2|SUBJ 2|11|COMP 3|10|MOD 4|10|MOD 5|10|MOD 6|10|MOD 
             7|10|MOD 8|10|MOD 9|10|MOD 10|2|OBJ 11|0|ROOT 12|13|DET 
             13|11|SUBJ 14|11|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    parent = tokens.num(10)
    assert parent.word == "cloth"
    assert tokens.paths_from(parent) == \
           ['cloth', ['beautiful'], 
                     ['expensive'], 
                     ['exotic'], 
                     ['fine'], 
                     ['sparkly'],
                     ['brocade'], 
                     ['silk']]
    assert tokens.max_path_from(parent) == ['cloth', ['beautiful']]
    assert tokens.depth_from(parent) == 1

    utt = '''an alligator is about to catch a deer that was drinking at the 
             river's edge .'''
    mor = '''det|a n|alligator aux|be&3S aux|about inf|to v|catch det|a n|deer 
             rel|that aux|be&PAST&13S part|drink-PROG prep|at det|the 
             n|river-POSS n|edge .''' 
    syn = '''1|2|DET 2|6|SUBJ 3|6|AUX 4|6|AUX 5|6|INF 6|0|ROOT 7|8|DET 8|6|OBJ 
             9|11|CPZR 10|11|AUX 11|8|CMOD 12|11|JCT 13|14|DET 14|16|MOD 
             15|16|MOD 16|12|POBJ 17|6|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    parent = tokens.num(8)
    assert parent.word == "deer"
    assert tokens.paths_from(parent) == \
           ['deer', ['a'], 
                    ['drinking', ['that'], 
                                 ['was'], 
                                 ['at', ['edge', ['river', ['the']],
                                                 ["'s"]]]]]
    # LEVELS:       1            2      3        4         5      
    assert tokens.max_path_from(parent) == \
           ['deer', ['drinking', ['at', ['edge', ['river', ['the']]]]]]
    assert tokens.depth_from(parent) == 5

    utt = '''some mammals can hold their breath for almost two hours before
             they have to come up to the surface for air .'''
    mor = '''qn|some n|mammal-PL aux|can v|hold pro:poss:det|their n|breath 
             prep|for adv|almost det:num|two n|hour-PL conj:subor|before 
             pro|they aux|have inf|to v|come adv:loc|up prep|to det|the 
             n|surface prep|for n|air .'''
    syn = '''1|2|QUANT 2|4|SUBJ 3|4|AUX 4|0|ROOT 5|6|DET 6|4|OBJ 7|4|JCT 
             8|9|JCT 9|10|QUANT 10|7|POBJ 11|15|CPZR 12|15|SUBJ 13|15|AUX 
             14|15|INF 15|4|CJCT 16|15|JCT 17|16|JCT 18|19|DET 19|17|POBJ 
             20|15|JCT 21|20|POBJ 22|4|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    parent = tokens.num(4)
    assert parent.word == "hold"
    assert tokens.paths_from(parent) == \
           ['hold', ['mammals', ['some']], 
                    ['can'], ['breath', ['their']], 
                             ['for', ['hours', ['two', ['almost']]]],
                    ['come', ['before'], 
                             ['they'], 
                             ['have'], 
                             ['to'], 
                             ['up', ['to', ['surface', ['the']]]], 
                             ['for', ['air']]], 
                    ['.']]
    # LEVELS:       1        2      3      4           5      
    assert tokens.max_path_from(parent) == \
           ['hold', ['come', ['up', ['to', ['surface', ['the']]]]]]
    assert tokens.depth_from(parent) == 5

    utt = '''let me see how it turned out . '''
    mor = '''v|let&ZERO pro|me v|see adv:wh|how pro|it v|turn-PAST ptl|out .'''
    syn = '''1|0|ROOT 2|1|OBJ 3|1|XCOMP 4|6|JCT 5|6|SUBJ 6|3|COMP 7|6|PTL 
             8|1|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    parent = tokens.num(1)
    assert parent.word == "let"
    assert tokens.paths_from(parent) == \
           ['let', ['me'], 
                   ['see', ['turned', ['how'], 
                                      ['it'], 
                                      ['out']]], 
                   ['.']]
    # LEVELS:      1       2          3
    assert tokens.max_path_from(parent) == \
           ['let', ['see', ['turned', ['how']]]]
    assert tokens.depth_from(parent) == 3
    
    
def exclude_coord_test():
    '''Testing exclusion of coordinating nodes'''
    utt = '''so if you don't tell Trevor or his friend, you could use their 
             colored pencils here .'''
    mor = '''co|so conj:subor|if pro|you aux|do~neg|not v|tell n:prop|Trevor 
             conj:coo|or pro:poss:det|his n|friend pro|you aux|could v|use 
             pro:poss:det|their adj|colored n|pencil-PL adv:loc|here .'''
    syn = '''1|6|COM 2|6|CPZR 3|6|SUBJ 4|6|AUX 5|4|NEG 6|12|CJCT 7|8|COORD 
             8|6|OBJ 9|10|DET 10|8|COORD 11|13|SUBJ 12|13|AUX 13|0|ROOT 
             14|16|DET 15|16|MOD 15|13|OBJ 16|13|JCT 17|13|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    parent = tokens.num(13)
    assert parent.word == "use"
    assert tokens.depth_from(parent) == 5
    assert tokens.paths_from(parent) == \
           ['use', ['you'], 
                   ['could', ['tell', ['so'], 
                                      ['if'], 
                                      ['you'], 
                                      ['do', ["n't"]],
                                      ['or', ['Trevor'], 
                                             ['friend', ['his']]]]],
                   ['pencils'], 
                   ['here', ['their'], 
                            ['colored']], 
                   ['.']]
    # LEVELS:      1        2        3       4          5
    '''
    HL wrote ...

        Ideally, I'd like to be able to exclude coordination from counting 
        towards depth, but if that's too complicated no big deal.  

        I.e. to treat things with POS *NEG* and *COORD* as empty nodes - 
        anything lower down in the tree from a *COORD* would count, but it 
        itself wouldn't add to the total length.  Possible?

    HL had ...
    
        assert tokens.depth_from(parent) == 4

        max_branch == (13, 6, 10, 9)
                      ['use', 'tell', 'friend', 'his']
    '''
