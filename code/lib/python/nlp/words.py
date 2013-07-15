from __future__ import with_statement
import os

CWD = os.path.dirname(os.path.abspath(__file__))
WORDS_DIR = os.path.join(CWD, "words")

class WordList(dict):
    '''
    Useful for testing whether a word is in a wordlist file.

    A wordlist file is a plain text file containing either one word 
    per line or one word and value per line separated by a "|" 
    (e.g., "ran|run").
    
    The default word list is ``words/english.txt`` and it contains one 
    word per line. 

        >>> from nlp.words import WordList
        >>> words = WordList()
        >>> words.dog 
        True
        >>> words.baz
        False
        >>> 'dog' in words
        True
        >>> 'baz' in words
        False
        >>> words['dog']
        True
        >>> words['baz']
        False
        >>> words.add('baz')
        >>> words['baz']
        True
    
    As an example of a wordlist file containing both words and values, 
    consider ``words/irregular/noun.txt``. This file contains irregular 
    noun forms where each irregular form is followed by its base/dictonary 
    form (e.g., "feet|foot").

        >>> path = os.environ["LDP_LIB"] + '/python/nlp/words/'
        >>> words = WordList(path + 'irregular/noun.txt')
        >>> words.feet
        'foot'
        >>> words.foot
        False

    '''
    def __init__(self, *wordlists):
        '''Initialize wordlists.'''
        self.new = []
        WORDS = {}
        if not wordlists: 
            wordlists = [os.path.join(WORDS_DIR, "english.txt")]
        self.files = wordlists
        for list in wordlists:
            try:
                with open(list) as words:
                    for word in words:
                        word = word.rstrip()
                        if "|" in word:
                            word, value = word.split("|")
                            WORDS[word] = value
                        else:
                            WORDS[word] = True
            except IOError:
                raise IOError("{0} does not exist!".format(list))
        dict.__init__(self, WORDS)

    def check(self, word):
        '''Return True if word in WordList.'''
        return self.__getattr__(word)

    def add(self, word, value=True):
        '''Add word (and value) to active WordList.'''
        if word not in self:
            self[word] = value
            self.new.append(word)

    def __call__(self, word):
        '''Add word (and value) to active WordList.'''
        self.add(word)

    def __getattr__(self, word):
        '''Lookup word as attribute.'''
        return self.get(word, False)

    def commit(self):
        '''Write any new words to first wordlist file.'''
        with open(self.files[0], 'a') as wordlist:
            for word in self.new:
                wordlist.write(word + "\n")


class Words(set):
    '''
    Lightweight version of WordList.

    Useful for testing whether a word is a recognized 
    dictionary word or in a wordlist file.

    '''
    def __init__(self, *wordlists):
        '''Initialize wordlists.'''
        if not wordlists: 
            default = os.path.join(WORDS_DIR, "english.txt")
            wordlists = [default]
        words = (w.rstrip() for list in wordlists for w in open(list)) 
        set.__init__(self, words)

    def __getattr__(self, word):
        '''Lookup word as attribute.'''
        return word in self


if __name__ == '__main__':

    words = Words('words/numbers.txt')
    assert "hundred" in words
    assert "two" in words

    '''
    words = Words()
    assert "hit" in words
    assert words.hit

    nums = WordList('words/integers.txt')
    for i in range(20):
        print i, nums[str(i)]

    words = WordList('words/irregular/noun.txt', 'words/irregular/verb.txt')
    assert words.feet == 'foot'
    assert words.ran == 'run'

    words = WordList('words/test.txt')
    assert words.baz is False
    assert words.dog is True
    words('biz')    # add "biz" to wordlist
    assert words['biz'] is True
    words.commit()  # write new words added to wordlist
    words = WordList('words/test.txt')
    assert words['biz'] is True
    assert words.biz is True

    assert words.check('foo bar baz')
    assert words.alpha == 'beta'

    words = WordList('words/test.txt')
    assert words.biz
    '''
