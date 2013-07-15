from chat.syn import Token, Syn

def token_test():
    '''Testing Token init method'''
    tok = Token("1|2|SUBJ")
    expected = dict(num=1, dep=2, rel="SUBJ")
    assert tok == expected
    assert tok.num == 1
    assert tok.dep == 2
    assert tok.rel == "SUBJ"
    assert tok.head == 2, "alternate name for dep attr"
    assert tok.deprel == "SUBJ", "alternate name for rel attr"

def syn_test():
    '''Testing Syn init method'''
    input = '1|2|SUBJ 2|0|ROOT 3|6|DET 4|6|MOD 5|6|MOD 6|2|PRED 7|2|PUNCT'
    expected = [
        dict(num=1, dep=2, rel="SUBJ"),
        dict(num=2, dep=0, rel="ROOT"),
        dict(num=3, dep=6, rel="DET"),
        dict(num=4, dep=6, rel="MOD"),
        dict(num=5, dep=6, rel="MOD"),
        dict(num=6, dep=2, rel="PRED"),
        dict(num=7, dep=2, rel="PUNCT"),
    ]
    assert Syn(input) == expected
