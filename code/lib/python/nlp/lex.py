'''
nlp.lex - basic lexical utilities for anglo text.

Use for tokenizing, lemmatizing, and normaling text strings.

'''
import re, os
from nlp.words import WordList, WORDS_DIR

def memo(f):
    "Memoize function f."
    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    memoized.cache = cache
    return memoized


class IrregularForm(object):
    '''Use for normalizing irregular word forms.'''

    def __init__(self):
        verb_file = WORDS_DIR + "/irregular/verb.txt"
        noun_file = WORDS_DIR + "/irregular/noun.txt"
        self.words = WordList(verb_file, noun_file)

    def normalize(self, word):
        '''
        Return normalized word form if present, otherwise return 
        original form.

        '''
        return self.words.get(word, word)


class Tokenizer(object):
    '''Use for splitting strings into word tokens.'''

    def __init__(self, split_clitics=False, nonword=r'[^a-zA-Z\+\'\-\&\@\_]'):
        self.split_clitics = split_clitics
        self.nonword_pt = re.compile(nonword)

    contractions = "let's|gimme|gotta|gonna|wanna|cannot|lookit"
    contraction_pt = re.compile(r"\b(" + contractions + ")")
    clitic_pt = re.compile(r"(n't|'(m|s|d|ll|re|ve))$")
    poss_plural_pt = re.compile(r"s'\s")
    letter = re.compile(r'\w')

    def __call__(self, s):
        '''Return the list of word tokens in string.'''
        return self.tokenize(s)

    def tokenize(self, s):
        '''Return the list of word tokens in string.'''
        words = []
        if self.contraction_pt.search(s):
            s = self.decontract(s)
        if self.poss_plural_pt.search(s):
            s = s.replace("s'", "s's")
        if '[x' in s:
            s = self.expand(s)
        for word in self.nonword_pt.split(s):
            if word.startswith("'"): word = word[1:]
            if word.endswith("'"): word = word[:-1]
            if not word or not self.letter.search(word): continue 
            if self.split_clitics and self.clitic_pt.search(word):
                match = self.clitic_pt.search(word)
                clitic = match.group()
                n = len(clitic)
                words.extend([word[:-n], clitic])
            else:
                words.append(word)
        return words

    def decontract(self, x):
        x = x.replace("let's", "let_us")
        x = x.replace('gotta', 'got to')
        x = x.replace('gonna', 'going to')
        x = x.replace('wanna', 'want to')
        x = x.replace('gimme', 'give me')
        x = x.replace('cannot', 'can not')
        x = x.replace('lookit', 'look at')
        return x

    count_pt = r'\s?\[x\s?(\d+)\]'
    word_rep_pt = re.compile(r'(\w+)' + count_pt)
    phrase_rep_pt = re.compile(r'<(.*?)>' + count_pt)

    def expand(self, string):
        '''Expand the word repetitions indicated by `[x#]` annotation.

        "Foo [x3]" => "Foo Foo Foo"
        "<Foo bar>[x2]" => "Foo bar Foo bar"

        '''
        for p in [self.word_rep_pt, self.phrase_rep_pt]:
            iter = p.finditer(string)
            for m in iter:
                reps = int(m.group(2))
                new = ' '.join([m.group(1)] * reps)
                string = p.sub(new, string, count=1)
        return string


class Lemmatizer(object):
    '''Custom lemmatizer for normalizing inflected and irregular word forms.'''

    # Inflection rule exceptions
    exceptions = {"s": ["bus", "yes", "does", "his", "hers", "mess", "hiss", 
                        "woods", "stairs", "tights", "pants", "shorts", "jeans"],
                  "ed": ["fled", "wicked", "tired",
                         "reed", "weed", "feed", "need", "seed"],
                  "ing": ["morning", "evening", "earring", "nothing"]}

    # Patterns
    vowel = r'[aeiou]'
    nonvowel = r'[^aeiou]'
    consonant = r'[bcdfghjklmnpqrstvwxz]'

    # Regex
    # pattern for geminated words such as "running":
    gem = re.compile(r'(?P<gem>[pbmtdnrgsvz])(?P=gem)(?P<suffix>ed|ing)')

    def __init__(self, s_rules=True, ed_rules=True, ing_rules=True, 
                                                    irr_rules=True):
        '''Defaults to using all rules.

        s_rules: normalize words ending in "s"
        ed_rules: normalize words ending in "ed"
        ing_rules: normalize words ending in "ing"
        irr_rules: normalize irregular words
        
        '''
        self.spell = WordList()
        suffixes = []
        if s_rules: suffixes.append("s")
        if ed_rules: suffixes.append("ed")
        if ing_rules: suffixes.append("ing")
        self.inflection = re.compile(r"(?:" + "|".join(suffixes) + r")$")
        self.irregular = False
        if irr_rules:
            self.irregular = IrregularForm()

    def __call__(self, word):
        '''Normalize word based on selected rules.'''
        return self.normalize(word)

    def normalize(self, word):
        '''Normalize word based on selected rules.'''
        if self.irregular:
            result = self.irregular.normalize(word)
            if result != word:
                return result
        inflection = self.is_inflected(word)
        if inflection:
            if "+" in word:
                (base, end) = word.rsplit("+", 1)
                normalize = getattr(self, "normalize_" + inflection)
                return base + "+" + normalize(end)
            else:
                normalize = getattr(self, "normalize_" + inflection)
                return normalize(word)
        else:
            return word

    def normalize_s(self, word):
        if len(word) < 3 or word in self.exceptions["s"]:
            return word
        stem = self.strip_suffix(word, "s")
        if self.spell.check(stem):
            return stem
        if word.endswith("ies"):
            stem = word[:-3]
            if self.spell.check(stem + "y"):
                return stem + "y"
        if word.endswith("ves"):
            if len(word) < 5:
                return word
            stem = word[:-3]
            if self.spell.check(stem + "f"):
                return stem + "f"
        if word.endswith("es"):
            stem = word[:-2]
            if self.spell.check(stem):
                return stem
        return word

    def normalize_ed(self, word):
        if len(word) < 4 or word in self.exceptions["ed"]:
            return word
        stem = self.strip_suffix(word, "ed")
        if word.endswith("ied") and stem not in ["ti", "li", "di"]:
            stem = word[:-3]
            if self.spell.check(stem + 'y'):
                return stem + 'y'
            else:
                return word
        if self.spell.check(stem) and stem not in ["us", "ti", "fe", "bl", 
                                                     "pleas", "scar"]:
            return stem
        elif self.spell.check(stem + 'e'):
            return stem + 'e'
        else:
            return word

    def normalize_ing(self, word):
        if len(word) < 5 or word in self.exceptions["ing"]:
            return word
        stem = self.strip_suffix(word, "ing")
        if self.spell.check(stem) and stem not in ["us", "com", "div", "writ"]:
            return stem
        elif self.spell.check(stem + 'e'):
            return stem + 'e'
        else:
            return word

    def is_inflected(self, word):
        '''Return inflectional morpheme if word is inflected or plural.'''
        match = self.inflection.search(word)
        if match:
            return match.group()

    def is_geminated(self, word):
        '''Test to see if a word is geminated.'''
        match = self.gem.search(word)
        if match:
            return match.group()

    def strip_suffix(self, word, suffix):
        '''Try to intelligently strip off suffix.'''
        n = len(suffix)
        if self.is_geminated(word):
            return word[:-(n+1)]
        else:
            return word[:-n]


class Normalizer(object):
    '''
    Tokenize and optionally lemmatize a string of words. 
    
    '''
    def __init__(self, split_clitics=True, 
                       nonword=r'[^a-zA-Z\+\'\-\&\@\_]', 
                       lemmas=True,                 # do not lemmatize if False 
                       **kwargs):
        self.tokens = Tokenizer(split_clitics, nonword)
        self.lemmatize = Lemmatizer(**kwargs)
        self.lemmas = lemmas                        # return lemmatized forms 
                       
    def __call__(self, utt):
        '''Tokenize an utterance and optionally return a list of lemmas.'''
        if self.lemmas:
            return [self.lemmatize(t) for t in self.tokens(utt)]
        else:
            return self.tokens(utt)
