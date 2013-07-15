from chat.unify import Line
from nose.tools import with_setup

line = None

def setup_line():
    '''Setup up line objects.'''
    global line
    utt = 'do you want to read a book ?'
    mor = 'aux|do pro|you aux|want inf|to v|read&ZERO det|a n|book ?'
    syn = '1|5|AUX 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|7|DET 7|5|OBJ 8|5|PUNCT' 
    line = Line(utt, mor, syn)

@with_setup(setup_line)
def test_getattr():
    '''Testing getattr method of Line class'''
    assert line.word(1) == "do"
    assert line.pos(1) == "aux"
    assert line.dep(1) == 5
    assert line.rel(1) == "AUX"

    assert line.head(1) == 5, "same as dep attr"
    assert line.deprel(1) == "AUX", "same as rel attr"

    assert line.word(2) == "you"
    assert line.pos(2) == "pro"
    assert line.dep(2) == 5
    assert line.rel(2) == "SUBJ"

    assert line.word(3) == "want"
    assert line.pos(3) == "aux"
    assert line.dep(3) == 5
    assert line.rel(3) == "AUX"

    assert line.word(5) == "read"
    assert line.suffix(5) == "ZERO"
    assert line.pos(5) == "v"
    assert line.dep(5) == 0
    assert line.rel(5) == "ROOT"

    assert line.word(8) == "?"
    assert line.pos(8) == "?"
    assert line.dep(8) == 5
    assert line.rel(8) == "PUNCT"

@with_setup(setup_line)
def test_set_pos():
    '''Testing set_pos method of Line class'''
    assert line.pos(1) == "aux"
    line.set_pos(index=1, tag="XXX")
    assert line.pos(1) == "XXX"

@with_setup(setup_line)
def test_set_rel():
    '''Testing set_rel method of Line class'''
    assert line.rel(1) == "AUX"
    line.set_rel(index=1, tag="XXX")
    assert line.rel(1) == "XXX"

def test_valid():
    '''Testing valid property of Line class'''
    utt = 'do you want to read a book ?'
    mor = 'aux|do pro|you aux|want inf|to v|read&ZERO det|a n|book ?'
    syn = '1|5|AUX 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|7|DET 7|5|OBJ 8|5|PUNCT' 
    line = Line(utt, mor, syn)
    assert line.valid

    utt = 'do you want to read a book ?'
    mor = 'aux|do pro|you aux|want ?'                                   # !!!
    syn = '1|5|AUX 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|7|DET 7|5|OBJ 8|5|PUNCT' 
    line = Line(utt, mor, syn)
    assert not line.valid

    utt = 'do you want to read a book ?'
    mor = 'aux|do pro|you aux|want inf|to v|read&ZERO det|a n|book ?'
    syn = '1|5|AUX 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|5|OBJ 7|5|PUNCT' # !!!
    line = Line(utt, mor, syn)
    assert not line.valid

@with_setup(setup_line)
def test_pos():
    '''Testing POS property of Line class'''
    assert line.POS == ['aux', 'pro', 'aux', 'inf', 'v', 'det', 'n', '?']

@with_setup(setup_line)
def test_rel():
    '''Testing REL property of Line class'''
    assert line.REL == ['AUX', 'SUBJ', 'AUX', 'INF', 'ROOT', 'DET', 'OBJ', 'PUNCT']

@with_setup(setup_line)
def test_dep():
    '''Testing DEP property of Line class'''
    assert line.DEP == [5, 5, 5, 5, 0, 7, 5, 5]

@with_setup(setup_line)
def test_words():
    '''Testing words property of Line class'''
    assert line.words == ['do', 'you', 'want', 'to', 'read', 'a', 'book', '?']

