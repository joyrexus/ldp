from ldp.grammar import Token, TokenList
from nose.tools import with_setup

tokens = None

def setup_tokens():
    '''Setup up TokenList object.'''
    global tokens
    utt = 'do you want to read a book ?'
    mor = 'aux|do pro|you aux|want inf|to v|read&ZERO det|a n|book ?'
    syn = '1|5|AUX 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|7|DET 7|5|OBJ 8|5|PUNCT' 
    tokens = TokenList(utt, mor, syn)

def test_token():
    '''Testing Token constructor'''
    t = Token(dict(word="jumping", lemma="jump", pos="v"))
    assert t.word is "jumping"
    assert t.pos is "v"
    assert t.lemma is "jump"
    assert t.is_verb
    assert t.head is None

@with_setup(setup_tokens)
def test_tokens():
    '''Testing TokenList constructor'''
    # 'do you want to read a book ?'
    # 'aux|do pro|you aux|want inf|to v|read&ZERO det|a n|book ?'
    # '1|5|AUX 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|7|DET 7|5|OBJ 8|5|PUNCT' 
    assert tokens[0].word == "do"
    assert tokens[0].pos == "aux"
    assert tokens[0].dep == 5
    assert tokens[0].rel == "AUX"
    assert tokens[0].head == 5, "same as dep attr"
    assert tokens[0].deprel == "AUX", "same as rel attr"
    assert not tokens[0].is_verb

    assert tokens[1].word == "you"
    assert tokens[1].pos == "pro"
    assert tokens[1].dep == 5
    assert tokens[1].rel == "SUBJ"
    assert not tokens[1].is_verb

    assert tokens[2].word == "want"
    assert tokens[2].pos == "aux"
    assert tokens[2].dep == 5
    assert tokens[2].rel == "AUX"

    assert tokens[4].word == "read"
    assert tokens[4].suffix == "ZERO"
    assert tokens[4].pos == "v"
    assert tokens[4].dep == 0
    assert tokens[4].rel == "ROOT"
    assert tokens[4].is_verb

    assert tokens[7].word == "?"
    assert tokens[7].pos == "?"
    assert tokens[7].dep == 5
    assert tokens[7].rel == "PUNCT"

    for i, word in enumerate('do you want to read a book ?'.split()):
        assert tokens.num(i+1).word == word

@with_setup(setup_tokens)
def test_dependents():
    '''Testing dependent_on method of TokenList'''
    #  do      you      want    to      read     a       book    ?
    #  1       2        3       4       5        6       7       8
    # '1|5|AUX 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|7|DET 7|5|OBJ 8|5|PUNCT' 
    expected = 'do you want to book ?'.split()
    
    assert [t.word for t in tokens.dependent_on(Token(dict(num=5)))] == expected
    assert [t.word for t in tokens.dependent_on(Token(dict(num=7)))] == ['a']

@with_setup(setup_tokens)
def test_properties():
    '''Testing calculated properties of TokenList'''
    assert tokens.words == "do you want to read a book ?".split()
    assert tokens.lemmas == "do you want to read a book ?".split()

@with_setup(setup_tokens)
def test_call_methods():
    '''Testing Token and TokenList call methods'''
    import re
    is_verb = lambda token: re.search(r'v\b', token.pos)
    token = Token(dict(word="jumping", lemma="jump", pos="v"))
    assert token(is_verb)

    is_noun = lambda token: re.search(r'n\b', token.pos)
    has_noun = lambda tokens: any(True for t in tokens if t(is_noun))
    assert tokens(has_noun)
