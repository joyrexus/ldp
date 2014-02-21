import re

class GestureMixin(object):
    '''
    Mixin class for other gesture column utility classes.

    '''
    sep = r'[;/]'                               # seperator
    rep = r'\([Xx](\d+)\)'                      # repetition indicator
    code = ''
    subcode = ''

    def __init__(self):
        repcode = r'({0}){1}'.format(self.code, self.rep)   # repeated code
        compound = r'({0})({1}{0})*$'.format(self.code, self.sep)

        self.REP = re.compile(self.rep)                       # repetition indicator
        self.SEP = re.compile(self.sep)                       # seperator
        self.CODE = re.compile(r'({0})$'.format(self.code))   # valid code
        self.SUBCODE = re.compile(self.subcode)               # subcode (".b" in "E.b")
        self.REPCODE = re.compile(repcode)                    # repeated code
        self.COMPOUND = re.compile(compound)                  # compound code

    def __call__(self, *args, **kwargs):
        '''Return list of individual values.'''
        return self.parse(*args, **kwargs)

    def parse(self, v, expand=True, subcodes=True):
        '''
        Return list of individual values.

        expand - expand abbreviated repeating codes if True
        subcodes - omit subcodes from values if False
    
        >>> gs = GestureSpeechRelation()
        >>> gs.values("X;E (x3)") == ['X','E','E','E']
        >>> gs.values("X;E (x3)", expand=False) == ['X','E(x3)']
        >>> gs.values("E.b") == ['E.b']
        >>> gs.values("E.b", subcodes=False) == ['E']

        '''
        v = v.replace(' ', '')
        if not subcodes:
            v = self.SUBCODE.sub('', v)
        if expand and self.expandable(v):
            return self.expand(v) 
        else:
            values = [x for x in self.SEP.split(v) if x]
            return values

    def expand(self, v):
        '''
        Expand repeated codes that are in abbreviated form.

        >>> gs = GestureSpeechRelation()
        >>> gs.expand("E (x3)") == ['E', 'E', 'E']

        '''
        values = []
        for x in self.SEP.split(v):
            if self.expandable(x):
                match = self.REPCODE.search(x)
                if match:
                    code = match.group(1)
                    n = match.group(2)
                    values.extend([code] * int(n))
                else:
                    values.append(x)
            else:
                values.append(x)
        return values

    def expandable(self, v):
        return True if self.REP.search(v) else False

    def compound(self, v):
        return True if self.SEP.search(v) else False

    def valid(self, v):
        '''True if all values are valid.'''
        return all(self.CODE.match(x) for x in self.parse(v))

    def valid_values(self, v, **kwargs):
        '''Return list of valid values.'''
        return [x for x in self.parse(v, **kwargs) if self.CODE.match(x)]

    def invalid_values(self, v, **kwargs):
        '''Return list of invalid values.'''
        return [x for x in self.parse(v, **kwargs) if not self.CODE.match(x)]


class GestureForm(GestureMixin):
    '''
    Utility for working with the gesture-form column values.

    '''
    sep = r'\s*[\+\-\/\.]\s*'                   # separator


class GestureType(GestureMixin):
    '''
    Utility for working with the gesture-type column values.

    '''
    # Patterns for each valid code
    d = r'(?:DP(?:\.nl)?|DS|DSDP)'              # deictic
    r = r'R(?:.(?:a|d|m|met)(?:\.(?:e|pp))?)?'  # representational / iconic
    c = 'C'                                     # conventional
    e = 'E'                                     # emphatic
    g = 'G'                                     # give
    s = 'S'                                     # sign
    f = 'FA'                                    # functional act

    r_sub = r'(?:a|d|m|met)(?:\.(?:e|pp))?'     # representational subcode
    d_sub = r'nl'                               # deictic subcode
    valid_subcode = r'\.({0})?'.format(r_sub +'|'+ d_sub)   # valid subcode

    sep = r'\s*[;/]\s*'                         # separator
    code = r'C|E|G|S|FA|{0}|{1}'.format(d, r)   # valid code
    subcode = r'\.[a-z]+(?:\.[a-z]+)?'          # pattern of optional subcode


class GestureSpeechRelation(GestureMixin):
    '''
    Utility for working with the gesture-speech-relation column values.

    '''
    # Patterns for each valid code
    add = r'ADD(?:\.(?:a|d|f|p|q|s|met|n[rs]|err(?:\.s)?))?'
    emphasize = r'E(?:\.b)?'
    reinforce = r'RF(?:\.[adp])?'
    elaborate = r'ELAB\.[ab]'
    other = r'FA|DA|MS|UC|X'

    code = '|'.join([add, emphasize, reinforce, elaborate, other])
    subcode = r'\.[a-z]+(?:\.s)?'


class GestureGloss:
    '''
    Utility for working with the gesture gloss column values.

    Eve's rules for normalizing glosses.
    
    If gloss ...
    * starts with "give", return "give"
    * starts with take, return None
    * contains possessive -'s form, delete it and preceding words
    * contains common adjectives (colors, sizes, etc.), delete them
    * contains prepositional phrases, delete them (except for "of ...")

    '''
    sep = re.compile(r'\s*[\+\-\/\.]\s*')

    startwords = "give take hold"
    preps = "with for in on"
    colors = "red blue green brown purple yellow orange pink"
    sizes = "big small large tiny"
    ordinals = "first second third fourth"

    descriptors = " ".join([colors, sizes, ordinals]).split()
    verbiage = re.compile(r"\b({0})\b".format("|".join(descriptors)))

    keywords = descriptors + " ".join([startwords, preps]).split()
    kw = re.compile(r"\b({0})\b".format("|".join(keywords)))

    spaces = re.compile(r"\s\s+")           # extra spaces
    paren = re.compile(r"\s+\(.+?\)")       # parenthetical comment
    prep = re.compile(r"\s+\b({0})\b\s+.*$".format(preps.replace(" ","|")))
                                            # prep phrase and following
    poss = re.compile(r"^.*\b\w+'s\s+")     # possessive form and preceding

    def parse(self, value):
        '''Return list of individual gloss values.'''
        return [g for g in self.sep.split(value.lower())]

    def has_keyword(self, gloss):
        '''Check if gloss contains a keyword before trying to apply rules.'''
        return self.kw.search(gloss) and True

    def delete_parens(self, gloss):
        '''Delete parenthetical comments.'''
        return self.paren.sub('', gloss)

    def delete_possessive(self, gloss):
        '''Delete everything preceding possessive -'s form.'''
        return self.poss.sub('', gloss)

    def normalize(self, gloss):
        '''Apply normalization rules to gloss.'''
        if "(" in gloss:
            gloss = self.delete_parens(gloss)
        if self.kw.search(gloss):
            if gloss.startswith("give"):
                return "give"
            if gloss.startswith("take"):
                return ""
            gloss = self.verbiage.sub(" ", gloss)
            gloss = self.prep.sub("", gloss)
        if "'s " in gloss:
            gloss = self.delete_possessive(gloss)
        return self.spaces.sub(" ", gloss.strip())

    def parse_and_norm(self, value):
        '''Parse gloss and return list of normalized values.'''
        return [self.normalize(g) for g in self.parse(value)]


if __name__ == '__main__':

    gg = GestureGloss()
    assert gg.parse('x + y + z') == 'x y z'.split()
    assert gg.has_keyword('foo in bar')
    assert gg.has_keyword('the big jar')
    assert gg.normalize('the big jar') == 'the jar'
    assert gg.normalize('the big brown jar') == 'the jar'
    assert gg.normalize('give the ball') == 'give'
    assert gg.normalize("this is mom's big ball") == 'ball'
    assert gg.normalize("foo in bar") == 'foo'
    assert gg.normalize("foo with bar") == 'foo'
    assert gg.normalize("foo with bar (baz)") == 'foo'
    assert gg.normalize("mom's foo with bar") == 'foo'
    assert gg.parse_and_norm("foo with bar. foo with bar") == ['foo', 'foo']
    assert gg.parse_and_norm("foo with bar. mom's foo") == ['foo', 'foo']
    assert gg.parse_and_norm("mom's foo in bar") == ['foo']
    assert gg.parse_and_norm("mom's (nice) foo in bar") == ['foo']

    gs = GestureSpeechRelation()
    assert gs.valid('X')
    assert not gs.valid('Y')
    assert gs.valid('X;X')
    assert not gs.compound('X')
    assert gs.compound('X;X')
    assert gs.parse('X;X;FA') == ['X', 'X', 'FA']
    assert gs('X;X;E.b (x3)') == ['X', 'X', 'E.b', 'E.b', 'E.b']
    assert gs('X;X;E.b (x3)', subcodes=False) == ['X', 'X', 'E', 'E', 'E']
    assert gs(u'') == []

    gt = GestureType()
    assert not gt.valid('X')
    assert gt.valid('E')
    assert gt.valid('G;G')
    assert not gt.compound('E')
    assert not gt.compound('DP.nl')
    assert gt.compound('E;E')
    assert gt.parse('E;G;FA') == ['E', 'G', 'FA']
    assert gt('DS;DP.nl;E (x3)') == ['DS', 'DP.nl', 'E', 'E', 'E']
    assert gt('DS;DP.nl (x2);E (x3)') == ['DS', 'DP.nl', 'DP.nl', 'E', 'E', 'E']
    assert gt('DS;DP.nl (x2);E (x3)', subcodes=False) == 'DS DP DP E E E'.split()
    assert gt(u'') == []
    assert gt('DS;DP.nl;E (x3)', subcodes=False) == 'DS DP E E E'.split()
