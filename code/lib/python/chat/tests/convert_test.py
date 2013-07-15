import chat.unify
import chat.convert
from nose.tools import with_setup

orig, line = None, None

def setup_lines():
    '''Setup up line objects.'''
    global orig, line
    utt = 'do you want to read a book ?'
    mor = 'aux|do pro|you aux|want inf|to v|read&ZERO det|a n|book ?'
    syn = '1|5|AUX 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|7|DET 7|5|OBJ 8|5|PUNCT' 
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.convert.Line(utt, mor, syn)


@with_setup(setup_lines)
def test_pos_convert():
    '''Testing POS tag conversion'''
    assert line.word(1) == "do"
    assert orig.pos(1) == "aux"
    assert line.pos(1) == "MD"

    assert line.word(2) == "you"
    assert orig.pos(2) == "pro"
    assert line.pos(2) == "PRP"

    assert line.word(3) == "want"
    assert orig.pos(3) == "aux"
    assert line.pos(3) == "MD"

    assert line.word(4) == "to"
    assert orig.pos(4) == "inf"
    assert line.pos(4) == "TO"

    assert line.word(5) == "read"
    assert orig.pos(5) == "v"
    assert line.pos(5) == "VBD"

    assert line.word(6) == "a"
    assert orig.pos(6) == "det"
    assert line.pos(6) == "DT"


def test_adv_exception():
    '''Testing exception to adv conversion rule'''
    utt = 'maybe later on .'
    mor = 'adv|maybe adv|late-CP ptl|on .'
    syn = '1|2|JCT 2|0|ROOT-NV 3|2|PTL 4|2|PUNCT'
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.convert.Line(utt, mor, syn)
    assert line.word(2) == "later"
    assert orig.pos(2) == "adv"
    assert line.pos(2) == "RB"


def test_more_exception():
    '''Testing more/less/most/least exceptions'''
    utt = 'does he have any more parts ?'
    mor = 'aux|do&3S pro|he v|have qn|any qn|more n|part-PL ?'
    syn = '1|3|AUX 2|3|SUBJ 3|0|ROOT 4|6|QUANT 5|6|QUANT 6|3|OBJ 7|3|PUNCT'
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.convert.Line(utt, mor, syn)
    assert line.word(5) == "more"
    assert orig.pos(5) == "qn"
    assert line.pos(5) == "JJR"

    utt = 'you need more ?'
    mor = 'pro|you v|need adv|more ?'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|JCT 4|2|PUNCT'
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.convert.Line(utt, mor, syn)
    assert line.word(3) == "more"
    assert orig.pos(3) == "adv"
    assert line.pos(3) == "RB"


def test_qn_exception():
    '''Testing qn exception'''
    utt = "first let's get all the end ones ."
    mor = "adv|first aux|let's v|get qn|all det|the n|end pro:indef|one-PL ."
    syn = "1|3|JCT 2|3|AUX 3|0|ROOT 4|7|QUANT 5|7|DET 6|7|MOD 7|3|OBJ 8|3|PUNCT"
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.convert.Line(utt, mor, syn)
    assert line.word(4) == "all"
    assert orig.pos(4) == "qn"
    assert line.pos(4) == "PDT"


def test_rel_convert():
    '''Testing REL tag conversion'''
    utt = 'give it to me please .'
    mor = 'v|give pro|it prep|to pro|me co|please .'
    syn = '1|0|ROOT 2|1|OBJ 3|1|IOBJ 4|3|POBJ 5|1|COM 6|1|PUNCT'
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.convert.Line(utt, mor, syn)
    assert line.word(3) == "to"
    assert orig.rel(3) == "IOBJ"
    assert line.rel(3) == "DTV"

    utt = "it is a bride's veil ."
    mor = "pro|it v|be&3S det|a n|bride-POSS n|veil ."
    syn = "1|2|SUBJ 2|0|ROOT 3|6|DET 4|6|MOD 5|6|MOD 6|2|PRED 7|2|PUNCT"
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.convert.Line(utt, mor, syn)
    assert line.word(5) == "'s"
    assert orig.rel(5) == "MOD"
    assert line.rel(5) == "SUFFIX"


def test_coord_rule():
    '''Testing coord_rule method'''
    utt = 'to be or not to be .'
    mor = 'inf|to v|be conj:coo|or neg|not inf|to v|be .'
    syn = '1|2|INF 2|3|COORD-ROOT 3|0|ROOT  4|6|NEG 5|6|INF 6|3|COORD-ROOT 7|3|PUNCT'
        #  1|2|INF 2|0|ROOT       3|2|COORD 4|6|NEG 5|6|INF 6|3|CONJ       7|3|PUNCT
        #            * ^^^^         * ^^^^^                     ^^^^
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.unify.Line(utt, mor, syn)
    chat.convert.RelTagConverter().coord_rule(2, line, orig)

    assert line.word(2) == "be"
    assert orig.dep(2) == 3
    assert line.dep(2) == 0
    assert orig.rel(2) == "COORD-ROOT"
    assert line.rel(2) == "ROOT"
    
    assert line.word(3) == "or"
    assert orig.pos(3) == "conj:coo"
    assert orig.rel(3) == "ROOT"
    assert line.rel(3) == "COORD"
    assert orig.dep(3) == 0
    assert line.dep(3) == 2

    assert line.word(6) == "be"
    assert orig.dep(6) == 3
    assert line.dep(6) == 3

    utt = 'but do you want to go ?'
    mor = 'conj:coo|but aux|do pro|you aux|want inf|to v|go ?'
    syn = '1|0|ROOT 2|6|AUX 3|6|SUBJ 4|6|AUX 5|6|INF 6|1|COORD-ROOT 7|1|PUNCT'
        #  1|6|DEP  2|6|AUX 3|6|SUBJ 4|6|AUX 5|6|INF 6|0|ROOT       7|1|PUNCT
        #    * ^^^                                     * ^^^^
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.unify.Line(utt, mor, syn)
    chat.convert.RelTagConverter().coord_rule(6, line, orig)

    assert line.word(6) == "go"
    assert orig.dep(6) == 1
    assert line.dep(6) == 0
    assert orig.rel(6) == "COORD-ROOT"
    assert line.rel(6) == "ROOT"

    assert line.word(1) == "but"
    assert orig.dep(1) == 0
    assert orig.pos(1) == "conj:coo"
    assert line.dep(1) == 6
    assert orig.rel(1) == "ROOT"
    assert line.rel(1) == "DEP"

    for i in [2,3,4,5]:
        assert line.dep(i) == orig.dep(i)
        assert line.rel(i) == orig.rel(i)


def test_cpzr_convert():
    '''Testing REL tag conversion: CPZR/CJCT/XJCT'''
    utt = 'we can play after you eat .'
    mor = 'pro|we aux|can v|play conj:subor|after pro|you v|eat .'
    syn = '1|3|SUBJ 2|3|AUX 3|0|ROOT 4|6|CPZR 5|6|SUBJ 6|3|CJCT 7|3|PUNCT'
        #  1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|TMP  5|6|SUBJ 6|4|SUB  7|3|PUNCT 
        #                              * ^^^             * ^^^ 
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.convert.Line(utt, mor, syn)

    assert line.word(4) == "after"
    assert orig.pos(4) == "conj:subor"
    assert orig.rel(4) == "CPZR"
    assert line.rel(4) == "TMP"
    assert orig.dep(4) == 6
    assert line.dep(4) == 3

    assert line.word(6) == "eat"
    assert orig.rel(6) == "CJCT"
    assert line.rel(6) == "SUB"
    assert orig.dep(6) == 3
    assert line.dep(6) == 4


def test_aux_srl_rule():
    '''Testing aux_srl_rule method'''

    utt = 'this is going to be great .'
    mor = 'pro:dem|this aux|be&3S aux|go-PROG inf|to v|be adj|great .'
    syn = '1|5|SUBJ 2|5|AUX  3|5|AUX 4|5|INF 5|0|ROOT 6|5|PRED 7|5|PUNCT'
        #  1|2|SUBJ 2|0|ROOT 3|2|VC  4|5|INF 5|3|VC   6|5|PRED 7|5|PUNCT
        #    *        * ^^^^   * ^^            * ^^
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.unify.Line(utt, mor, syn)
    chat.convert.RelTagConverter().aux_srl_rule(1, line, orig)

    assert line.word(1) == "this"
    assert orig.rel(1) == "SUBJ"
    assert line.rel(1) == "SUBJ"
    assert orig.dep(1) == 5
    assert line.dep(1) == 2

    assert line.word(2) == "is"
    assert orig.rel(2) == "AUX"
    assert line.rel(2) == "ROOT"
    assert orig.dep(2) == 5
    assert line.dep(2) == 0

    assert line.word(3) == "going"
    assert orig.rel(3) == "AUX"
    assert line.rel(3) == "VC"
    assert orig.dep(3) == 5
    assert line.dep(3) == 2

    assert line.word(5) == "be"
    assert orig.rel(5) == "ROOT"
    assert line.rel(5) == "VC"
    assert orig.dep(5) == 0
    assert line.dep(5) == 3

    utt = 'can you go call Dad ?'
    mor = 'aux|can pro|you v|go v|call n:prop|Dad ?'
    syn = '1|4|AUX  2|4|SUBJ 3|4|SRL 4|0|ROOT 5|4|OBJ 6|4|PUNCT'
	    #  1|0|ROOT 2|1|SUBJ 3|1|VC  4|3|VC   5|4|OBJ 6|4|PUNCT
	    #    * ^^^^   * ^^^^   * ^^^   * ^^
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.unify.Line(utt, mor, syn)
    chat.convert.RelTagConverter().aux_srl_rule(1, line, orig)

    assert line.word(1) == "can"
    assert orig.rel(1) == "AUX"
    assert line.rel(1) == "ROOT"
    assert orig.dep(1) == 4
    assert line.dep(1) == 0

    assert line.word(2) == "you"
    assert orig.dep(2) == 4
    assert line.dep(2) == 1

    assert line.word(3) == "go"
    assert orig.rel(3) == "SRL"
    assert line.rel(3) == "VC"
    assert orig.dep(3) == 4
    assert line.dep(3) == 1

    assert line.word(4) == "call"
    assert orig.rel(4) == "ROOT"
    assert line.rel(4) == "VC"
    assert orig.dep(4) == 0
    assert line.dep(4) == 3


def test_aux_srl_convert():
    '''Testing REL tag conversion: AUX & SRL'''
    utt = 'this is going to be great .'
    mor = 'pro:dem|this aux|be&3S aux|go-PROG inf|to v|be adj|great .'
    syn = '1|5|SUBJ 2|5|AUX  3|5|AUX 4|5|INF 5|0|ROOT 6|5|PRED 7|5|PUNCT'
	    #  1|2|SBJ  2|0|ROOT 3|2|VC  4|3|VC  5|4|IM   6|5|PRD  7|2|P
        #    *        * ^^^    * ^^    * ^^    * ^^              * ^
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.convert.Line(utt, mor, syn)

    assert line.word(1) == "this"
    assert orig.rel(1) == "SUBJ"
    assert line.rel(1) == "SBJ"
    assert orig.dep(1) == 5
    assert line.dep(1) == 2

    assert line.word(2) == "is"
    assert orig.rel(2) == "AUX"
    assert line.rel(2) == "ROOT"
    assert orig.dep(2) == 5
    assert line.dep(2) == 0

    assert line.word(3) == "going"
    assert orig.rel(3) == "AUX"
    assert line.rel(3) == "VC"
    assert orig.dep(3) == 5
    assert line.dep(3) == 2

    assert line.word(5) == "be"
    assert orig.rel(5) == "ROOT"
    assert line.rel(5) == "IM"
    assert orig.dep(5) == 0
    assert line.dep(5) == 4

    assert line.word(7) == "."
    assert orig.rel(7) == "PUNCT"
    assert line.rel(7) == "P"
    assert orig.dep(7) == 5
    assert line.dep(7) == 2

    utt = "I'll go look for it and I'll see if we can put it in here, okay ?"
    mor = "pro|I aux|will v|go v|look prep|for pro|it conj:coo|and pro|I " \
        + "aux|will v|see conj:subor|if pro|we aux|can v|put&ZERO pro|it " \
        + "prep|in adv:loc|here co|okay ?"
    syn = "1|4|SUBJ 2|4|AUX 3|4|SRL 4|7|COORD-ROOT 5|4|JCT 6|5|POBJ " \
        + "7|0|ROOT 8|10|SUBJ 9|10|AUX 10|7|COORD-ROOT 11|14|CPZR " \
        + "12|14|SUBJ 13|14|AUX 14|10|COMP 15|14|OBJ 16|14|LOC " \
        + "17|16|POBJ 18|14|COM 19|7|PUNCT"
    '''
    Corrected:
        1   I   I           PRP _   2   SBJ
        2   'll will        MD  _   0   ROOT
        3   go  go          VB  _   2   VC
        4   look    look    VB  _   3   VC
        5   for for         IN  _   4   JCT
        6   it  it          PRP _   5   PMOD
        7   and and         CC  _   2   COORD
        8   I   I           PRP _   9   SBJ
        9   'll will        MD  _   7   CONJ
        10  see see         VB  _   9   VC
        11  if  if          IN  _   10  OBJ
        12  we  we          PRP _   13  SBJ
        13  can can         MD  _   11  SUB
        14  put put         VBD _   13  VC
        15  it  it          PRP _   14  OBJ
        16  in  in          IN  _   14  PUT
        17  here    here    RB  _   16  PMOD
        18  okay    okay    UH  _   14  DEP
        19  ?   ?           P   _   2   P
    '''
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.convert.Line(utt, mor, syn)

    assert line.word(1) == "I"
    assert orig.rel(1) == "SUBJ"
    assert line.rel(1) == "SBJ"
    assert orig.dep(1) == 4
    assert line.dep(1) == 2
    

def test_inf_rule():
    '''Testing inf_rule method'''
    utt = 'this is going to be great .'
    mor = 'pro:dem|this aux|be&3S aux|go-PROG inf|to v|be adj|great .'
    syn = '1|5|SUBJ 2|5|AUX 3|5|AUX 4|5|INF  5|0|ROOT 6|5|PRED 7|5|PUNCT'
	    #  1|4|SUBJ 2|4|AUX 3|4|AUX 4|0|ROOT 5|4|IM   6|5|PRED 7|5|PUNCT
        #             *       *       * ^^^^   * ^^
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.unify.Line(utt, mor, syn)
    chat.convert.RelTagConverter().inf_rule(4, line, orig)

    assert line.word(2) == "is"
    assert line.rel(2) == "AUX"
    assert orig.dep(2) == 5
    assert line.dep(2) == 4

    assert line.word(3) == "going"
    assert line.rel(3) == "AUX"
    assert orig.dep(3) == 5
    assert line.dep(3) == 4

    assert line.word(4) == "to"
    assert orig.rel(4) == "INF"
    assert line.rel(4) == "ROOT"
    assert orig.dep(4) == 5
    assert line.dep(4) == 0

    assert line.word(5) == "be"
    assert orig.rel(5) == "ROOT"
    assert line.rel(5) == "IM"
    assert orig.dep(5) == 0
    assert line.dep(5) == 4


def test_inf_convert():
    '''Testing REL tag conversion: INF'''
    utt = 'this is going to be great .'
    mor = 'pro:dem|this aux|be&3S aux|go-PROG inf|to v|be adj|great .'
    syn = '1|2|SUBJ 2|0|ROOT 3|2|VC 4|5|INF 5|3|VC 6|5|PRED 7|5|PUNCT'
	    #  1|2|SUBJ 2|0|ROOT 3|2|VC 4|3|VC  5|4|IM 6|5|PRED 7|5|PUNCT
        #                             * ^^    * ^^
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.convert.Line(utt, mor, syn)

    assert line.word(4) == "to"
    assert orig.rel(4) == "INF"
    assert line.rel(4) == "VC"
    assert orig.dep(4) == 5
    assert line.dep(4) == 3

    assert line.word(5) == "be"
    assert orig.rel(5) == "VC"
    assert line.rel(5) == "IM"
    assert orig.dep(5) == 3
    assert line.dep(5) == 4


def test_punct_convert():
    '''Testing REL tag conversion: PUNCT'''
    utt = 'this is going to be great .'
    mor = 'pro:dem|this aux|be&3S aux|go-PROG inf|to v|be adj|great .'
    syn = '1|5|SUBJ 2|5|AUX 3|5|AUX 4|5|INF  5|0|ROOT 6|5|PRED 7|5|PUNCT'
	    #  1|2|SBJ  2|0|ROOT 3|2|VC 4|3|VC   5|4|IM   6|5|PRED 7|2|P
        #                             * ^^     * ^^              * ^
    orig = chat.unify.Line(utt, mor, syn)
    line = chat.convert.Line(utt, mor, syn)

    assert line.word(4) == "to"
    assert orig.rel(4) == "INF"
    assert line.rel(4) == "VC"
    assert orig.dep(4) == 5
    assert line.dep(4) == 3

    assert line.word(5) == "be"
    assert orig.rel(5) == "ROOT"
    assert line.rel(5) == "IM"
    assert orig.dep(5) == 0
    assert line.dep(5) == 4

    assert line.word(7) == "."
    assert orig.rel(7) == "PUNCT"
    assert line.rel(7) == "P"
    assert orig.dep(7) == 5
    assert line.dep(7) == 2


def test_problem_line():
    '''Testing conversion of problematic line.'''
    utt = 'Gordan the most &xxx of &xxx people .'
    mor = 'n:prop|Gordan det|the pro:indef|most prep|of n|person&PL .'
    syn = '1|3|SUBJ 2|3|DET  3|0|ROOT-NV 4|3|MOD  5|4|POBJ 6|3|PUNCT'
        # '1|3|SBJ  2|3|NMOD 3|0|ROOT    4|3|NMOD 5|4|PMOD 6|3|P'
    line = chat.convert.Line(utt, mor, syn)
