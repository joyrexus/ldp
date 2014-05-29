from ldp.gesture import *

gf = GestureForm()
gg = GestureGloss()
lrb = LRB()


def test_parse():
    '''Testing parse method of various gesture classes'''
    for g in [gf, gg, lrb]:
        assert g.parse('x + y + z') == 'x y z'.split()
        assert g.parse('x . y . z') == 'x y z'.split()
        assert g.parse('x - y - z') == 'x y z'.split()
        assert g.parse('x / y / z') == 'x y z'.split()

def test_parse_gf():
    '''Testing parse method of GestureForm'''
    assert gf.parse('a + b - c . d / e ', subcodes=False) == 'a b c d e'.split()
    assert gf('a + b - c . d / e ', subcodes=False) == 'a b c d e'.split()


def test_has_keyword_gg():
    '''Testing has_keyword method of GestureGloss'''
    assert gg.has_keyword('foo in bar')
    assert gg.has_keyword('the big jar')
    assert gg.has_keyword('the red jar')
    assert not gg.has_keyword('the jar')

def test_normalize_gg():
    '''Testing normalize method of GestureGloss'''
    assert gg.normalize('the big jar') == 'the jar'
    assert gg.normalize('the big brown jar') == 'the jar'
    assert gg.normalize('give the ball') == 'give'
    assert gg.normalize("this is mom's big ball") == 'ball'
    assert gg.normalize("foo in bar") == 'foo'
    assert gg.normalize("foo with bar") == 'foo'
    assert gg.normalize("foo with bar (baz)") == 'foo'
    assert gg.normalize("mom's foo with bar") == 'foo'

def test_parse_and_norm_gg():
    '''Testing parse_and_norm method of GestureGloss'''
    assert gg.parse_and_norm("foo with bar. foo with bar") == ['foo', 'foo']
    assert gg.parse_and_norm("foo with bar. mom's foo") == ['foo', 'foo']
    assert gg.parse_and_norm("mom's foo in bar") == ['foo']
    assert gg.parse_and_norm("mom's (nice) foo in bar") == ['foo']


gt = GestureType()

def test_valid_gt():
    '''Testing for valid GestureType codes'''
    invalid = "X E;X R.x R.m;X R.m.q R.a.e.q"
    assert all(not gt.valid(v) for v in invalid.split())

    valid = "C DP DP.nl DS DSDP G E FA S R.a R.d R.m R.met " \
          + "R.a.pp R.d.pp R.m.pp R.met.pp " \
          + "R.a.e R.d.e R.m.e R.met.e"
    assert all(gt.valid(v) for v in valid.split())

def test_compound_gt():
    '''Testing compound method'''
    assert gt.compound('E;E')
    assert gt.compound('DP.nl;E')
    assert not gt.compound('E')
    assert not gt.compound('DP.nl')

def test_parse_gt():
    '''Testing parse method of GestureType'''
    assert gt.parse('E;G;FA') == ['E', 'G', 'FA']
    assert gt.parse('E;G (x3);R.a.e (x2)') == 'E G G G R.a.e R.a.e'.split()
    assert gt.parse('E;G (x3);R.a.e (x2)', subcodes=False) == 'E G G G R R'.split()

def test_call_gt():
    '''Testing callability of GestureType instance'''
    assert gt('DS;DP.nl;E (x3)') == 'DS DP.nl E E E'.split()
    assert gt('DS;DP.nl (x2);E (x3)') == 'DS DP.nl DP.nl E E E'.split()
    assert gt('DS;DP.nl (x2);E (x3)', subcodes=False) == 'DS DP DP E E E'.split()
    assert gt(u'') == []

def test_valid_values_gt():
    '''Testing valid_values method of GestureType'''
    assert gt.valid_values('DS;DP.nl;E(x3)') == 'DS DP.nl E E E'.split()
    assert gt.valid_values('DS;DP.nl;E(x3);Q(x2)') == 'DS DP.nl E E E'.split()
    assert gt.invalid_values('DS;DP.nl;E(x3)') == []
    assert gt.invalid_values('DS;DP.nl;E(x3);Q;Z') == 'Q Z'.split()


gsr = GestureSpeechRelation()

def test_valid_gsr():
    '''Testing for valid GestureSpeechRelation codes'''
    invalid = "Y Y;FA FA;Y ADD.x FA;ADD.x ELAB.q"
    assert all(not gsr.valid(v) for v in invalid.split())

    valid = "ADD ADD.err ADD.err.s ADD.f ADD.met ADD.nr ADD.ns " \
          + "ADD.a ADD.d ADD.q ADD.s DA E E.b ELAB.a ELAB.b FA MS " \
          + "RF RF.d RF.a RF.p UC X DA;DA X;X;X X(x3)"
    assert all(gsr.valid(v) for v in valid.split())

def test_valid_parse_gsr():
    '''Testing (in)valid_values method'''
    assert gsr.valid_values("X;X;Y;Y") == ['X', 'X']
    assert gsr.invalid_values("X;X;Y;Y") == ['Y', 'Y']
    assert gsr.valid_values("X(x3);Y;Y;Z(x3)") == ['X', 'X', 'X']
    assert gsr.invalid_values("X(x3);Y;Y;Z(x3)") == ['Y', 'Y', 'Z(x3)']

def test_compound_gsr():
    '''Testing compound method'''
    assert not gsr.compound("ADD")
    assert not gsr.compound("RF.p")
    assert not gsr.compound('X')
    assert gsr.compound("X;X")

def test_parse_gsr():
    '''Testing parse method'''
    assert gsr.parse("X;X") == ['X', 'X']
    assert gsr.parse("X;RF.p;RF.d") == ['X', 'RF.p', 'RF.d']
    assert gsr.parse("E;X (x3)") == ['E', 'X', 'X', 'X'] 
    assert gsr.parse("E;X (x3)", expand=False) == ['E', 'X(x3)'] 
    assert gsr.parse("E.b") == ['E.b']
    assert gsr.parse("E.b (x3)", subcodes=False) == ['E','E','E']
    assert gsr.parse("E.b", subcodes=False) == ['E']
    assert gsr.parse("X;RF.p;RF.d", subcodes=False) == ['X','RF','RF']
    assert gsr.parse('') == []

def test_expand_gsr():
    '''Testing expansion of repeated codes'''
    assert gsr.expandable("X (x3)")
    assert gsr.parse("X (x3)") == ['X', 'X', 'X']
    assert gsr.expandable("E;X (x3)")
    assert gsr.parse("E;X (x3)") == ['E', 'X', 'X', 'X'] 
    assert gsr.expandable("E;RF(x3);X(x3)")
    assert gsr.parse("E;RF(x3);X(x3)") == ['E','RF','RF','RF','X','X','X']

def test_call_gsr():
    '''Testing callability of GestureSpeechRelation instance'''
    assert gsr.parse('X;X;FA') == ['X', 'X', 'FA']
    assert gsr('X;X;FA') == ['X', 'X', 'FA']
    assert gsr('X;X;E.b (x3)') == ['X', 'X', 'E.b', 'E.b', 'E.b']
    assert gsr('X;X;E.b (x3)', subcodes=False) == ['X', 'X', 'E', 'E', 'E']
    assert gsr('') == []


def test_parse_lrb():
    '''Testing parse method'''
    assert lrb.parse("R,R,L") == ['R', 'R', 'L']
    assert lrb.parse("L (x3)") == ['L', 'L', 'L']
    assert lrb.parse("R + L (x3)") == ['R', 'L', 'L', 'L']
    assert lrb.parse("LF.RF.L (x3)") == ['LF', 'RF', 'L', 'L', 'L']
    assert lrb.parse("LF.RF.L(x3).W") == ['LF', 'RF', 'L', 'L', 'L', 'W']

