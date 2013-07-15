import os
from chat.file import Writer

w = Writer()

def test_format():
    '''Testing format method.'''
    r = (1022010001, 1, '', 'hello!', '')
    expected = '*MOT:\thello !\n%id:\t1022010001\n%row:\t1\n'
    assert w.format(r) == expected

    r = (1022010001, 1, '', 'hello!', 'bye!')
    M = '*MOT:\thello !\n%id:\t1022010001\n%row:\t1\n'
    C = '*CHI:\tbye !\n%id:\t1022010001\n%row:\t1\n'
    expected = M + C
    assert w.format(r) == expected

def test_fix():
    '''Testing fix method.'''
    assert w.fix("foo-'s ###.") == "foo's xxx ."
    assert w.fix("foo --") == "foo +..."
    assert w.fix("foo +...") == "foo +..."
    assert w.fix("foo?") == "foo ?"
    assert w.fix("foo xxx") == "foo xxx ."
    assert w.fix("ok, foo.") == "okay, foo ."
