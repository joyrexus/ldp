from nlp.words import Words, WordList, WORDS_DIR
import os

def test_words():
    '''Testing simple Words class'''
    words = Words()
    assert 'dog' in words
    assert 'dogs' in words
    assert 'baz' not in words
    assert 'wrestl' not in words
    assert 'wrestle' in words
    assert 'wrestled' in words
    assert words.dog is True
    assert words.dogs is True
    assert words.baz is False
    assert words.wrestl is False
    assert words.wrestle is True
    assert words.wrestled is True

words = WordList()

def test_words_dir():
    '''Testing WORDS_DIR constant'''
    assert WORDS_DIR == os.environ['LDP_LIB'] + '/python/nlp/words' or \
                        os.environ['LDP_LIB'] + '/nlp/words'

def test_init():
    '''Testing init method with multiple wordlists'''
    words = WordList(WORDS_DIR + '/irregular/noun.txt', 
                     WORDS_DIR + '/irregular/verb.txt')
    assert words.feet == 'foot'
    assert words.ran == 'run'

def test_check():
    '''Testing check method'''
    assert words.check('dog') is True
    assert words.check('dogs') is True
    assert words.check('ran') is True
    assert words.check('run') is True
    assert words.check('runs') is True
    assert words.check('runn') is False
    assert words.check('running') is True
    assert words.check('baz') is False
    assert words.check("wrestling") is True
    assert words.check("wrestled") is True
    assert words.check("wrestle") is True
    assert words.check("wrestl") is False
    assert words.check("shelves") is True
    assert words.check("shelve") is True
    assert words.check("shelv") is False

def test_contains():
    '''Testing contains method'''
    assert 'dog' in words
    assert 'dogs' in words
    assert 'baz' not in words
    assert 'wrestl' not in words
    assert 'wrestle' in words
    assert 'wrestled' in words

def test_getitem():
    '''Testing getitem method'''
    nums = WordList(WORDS_DIR + "/integers.txt")
    assert nums['1'] == "one"
    assert nums['2'] == "two"

def test_getattr():
    '''Testing getattr method'''
    assert words.dog is True
    assert words.baz is False

def test_add():
    '''Testing add method'''
    testwords = WordList(WORDS_DIR + "/test.txt")
    assert 'baz' not in testwords
    testwords.add('baz')    # add "baz" to active word list
    assert 'baz' in testwords, '"baz" was added to WordList'

def test_call():
    '''Testing call method'''
    assert 'baz' not in words
    words('baz')            # add "baz" to active word list
    assert 'baz' in words, '"baz" was added to WordList'

def test_len():
    '''Testing length method'''
    w = WordList(WORDS_DIR + "/test.txt")
    assert len(w) == 4

def test_valued():
    '''Testing word lists with values'''
    words = WordList(WORDS_DIR + "/irregular/noun.txt")
    assert words.feet == "foot"
    assert words.foot == False, "since not an irregular form"

