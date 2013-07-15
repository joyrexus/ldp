from ldp.grammar import Token
from ldp.grammar.match.token import TokenMatcher


match = TokenMatcher()


def verb_copula_test():
    '''Test copula matching methods'''
    t = Token(dict(word="is", 
                   lemma="be", 
                   suffix="3S",
                   pos="v", 
                   rel="CMOD"))
    assert match.verb_copula(t)
    
    t = Token(dict(word="is", lemma="be", pos="aux", rel="AUX"))
    assert not match.verb_copula(t)

def verb_test():
    '''Test verb matching methods'''
    t = Token(dict(word="married", 
                   lemma="marry", 
                   suffix="PERF",
                   pos="part", 
                   rel="PRED"))
    assert not match.verb_basic(t)
    assert not match.verb(t)
    
    t = Token(dict(word="is", lemma="be", pos="aux", rel="AUX"))
    assert not match.verb_basic(t)
    assert match.verb(t)
    
    # part|marry-PERF
    t = Token(dict(word="married", 
                   lemma="marry", 
                   suffix="PERF",
                   pos="part", 
                   rel="ROOT"))
    assert match.verb_basic(t)
    assert match.verb(t)
    
    t = Token(dict(word="jumping", 
                   lemma="jump", 
                   pos="part", 
                   rel='MOD'))
    assert not match.verb_basic(t)


def pronoun_test():
    '''Test pronoun matching method'''
    t = Token(dict(word="there", pos="pro:exist", rel="ESUBJ"))
    assert match.pronoun(t)

    t = Token(dict(word="him", pos="pro", rel="OBJ2"))
    assert match.pronoun(t)
    
    t = Token(dict(word="her", pos="pro:poss:det", rel="DET"))
    assert not match.pronoun(t)


def noun_test():
    '''Test noun matching methods'''
    t = Token(dict(word="mom", pos="n", rel="MOD"))
    assert match.noun_basic(t)
    assert match.noun(t)

    t = Token(dict(word="running", pos="n:gerund", rel="SUBJ"))
    assert match.noun_basic(t)
    assert match.noun(t)

    t = Token(dict(word="Mom", pos="n:prop", rel="VOC"))
    assert not match.noun_basic(t)
    assert match.noun(t)

    t = Token(dict(word="her", pos="pro", rel="OBJ"))
    assert not match.noun_basic(t)
    assert match.noun(t)

