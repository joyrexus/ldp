import re

class Token(dict):
    '''
    Feature dict for element from a mor string.

    '''
    def __init__(self, tok):
        '''
        Initialize a mor token object.
        
        >>> Token("adj|big-SP")
        {'irreg': False, 'lemma': 'big', 'prefix': None, 'suffix': 'SP', 'pos': 'adj'}

        '''
        prefix, pos, lemma, suffix, irreg = None, None, None, None, False
        if "#" in tok:
            prefix, tok = tok.split("#", 1)
        if "|" in tok:
            pos, tok = tok.split("|", 1)
        else:
            pos, tok = tok, tok
        if "&" in tok:
            irreg = True
            lemma, suffix = tok.split("&", 1)
        elif "-" in tok:
            lemma, suffix = tok.split("-", 1)
        else:
            lemma = tok
        d = dict(prefix=prefix, pos=pos, lemma=lemma, suffix=suffix, irreg=irreg)
        dict.__init__(self, d)

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value


class Parser(object):
    '''
    Use for tokenizing and parsing annotated utterances produced by 
    clan's morphology tagger ("mor").

    '''
    def __call__(self, mor):
        '''
        Parse a mor string into Token objects.

        Return a tuple of tokens.
        
        '''
        return self.parse(mor)

    def parse(self, mor):
        '''
        Parse a mor string into Token objects.

        Return a tuple of tokens.

        '''
        return tuple(Token(x) for x in self.tokenize(mor))

    poss_suffix = re.compile(r'-POSS\b') 
    punc_pt = re.compile(r' [\.\?\!] \b')
    clitic_pt = re.compile(r"(\w+)'s ")

    def tokenize(self, mor):
        '''
        Tokenize a mor string.

        1. Remove unknowns ("unk|xxx").
        2. Split on spaces.
        3. Remove trailing tildes ("pro|he aux|do&PAST~ neg|not").
        4. Replace non-trailing tildes with spaces.
        5. Fix ambiguous tokens and multiply-tagged compounds.
        6. Separate possessive-s as it's own token.
        
        '''
        tokens = []
        match = self.clitic_pt.search(mor)
        if match and match.group(1) != "let":
            new = "{0} v|be ".format(match.group(1))
            mor = self.clitic_pt.sub(new, mor)
        mor = self.punc_pt.sub(' ', mor)
        mor = mor.replace("unk|xxx", "")
        for i in mor.split():
            i = self.fix_token(i)
            i = i.replace("~ ", "")
            i = i.replace("~", " ")
            for j in self.poss_suffix.sub("-POSS POSS|'s", i).split():
                tokens.append(j)
        return tuple(tokens)

    extra_tag = re.compile(r"\+[a-z]+\|")
    poss_pt = re.compile(r"-POSS\^.+")

    def fix_token(self, tok):
        '''
        If ambiguously tagged token, return first option.

        >>> p.fix_token("n:prop|Anielle^n:prop|Anielle-POSS^")
        "n:prop|Anielle"

        If multiply-tagged compound form, return as singly-tagged.
        
        >>> p.fix_token("n|+n|butter+n|fly")
        "n|butter+fly"
        
        '''
        if "|+" in tok: 
            tok = self.extra_tag.sub("+", tok).replace("+", "", 1)
        if "^" in tok:
            if "-POSS^" in tok:
                tok = self.poss_pt.sub("-POSS^", tok)
                if tok.endswith("-POSS^"):
                    tok = tok.split("^")[-2] 
            else:
                tok = tok.split("^")[0] 
        return tok

    def tags(self, mor):
        '''Parse a mor string and return POS tags.'''
        return [m.pos for m in self.parse(mor)]

    def lemmas(self, mor):
        '''Parse a mor string and return lemmas (with prefix).'''
        return [(m.prefix or '') + m.lemma for m in self.parse(mor)]


class Mor(list, Parser):
    '''
    Use for tokenizing annotated utterances produced by 
    clan's part-of-speech tagger (``mor``).

    '''
    def __init__(self, mor):
        '''
        Initialize a mor annotation object.

        Create a list representation of a mor string, where each item is a
        dict of feature annotations for the corresponding utterance token.

        '''
        list.__init__(self, self.parse(mor))


class Converter(Parser):
    '''
    This is an extension of the Parser class, designed to parse mor strings
    into Token objects.

    However, when parsing a mor string, the tag attributes in each of the
    resulting Token objects gets converted from chat-style POS tags to 
    Penn-Treebank-style tags.

    '''
    def __init__(self):
        '''
        Initialize Converter.

        The ``rules`` dict is a dispatcher, with tags as keys and rules 
        for converting the given tag as values.

        The ``mapping`` dict is a simple mapping between tags that can be
        converted without conditional rules.  It's used by the default rule,
        which is used as a fallback if the tag is not observed in the ``rules``
        dict.

        '''
        self.rules = {
            "adj": self.adj_rule,
            "adj:n": self.adj_rule,
            "adj:v": self.adj_rule,
            "adv": self.adv_rule,
            "adv:adj": self.adv_rule,
            "part": self.part_rule,
            "n": self.n_rule,
            "n:adj": self.n_rule,
            "n:v": self.n_rule,
            "v": self.v_rule,
            "v:n": self.v_rule,
        }
        self.mapping = {     
            "adv:wh": "WRB",
            "adv:int": "RB",
            "adv:loc": "RB",
            "adv:tem": "RB",
            "aux": "MD",
            "co": "UH",
            "co:coo": "CC",
            "co:voc": "UH",
            "co:subor": "IN",
            "det": "DT",
            "det:num": "CD",
            "det:wh": "WDT",
            "frn": "FW",
            "inf": "TO",
            "rel": "WDT",
            "int": "UH",
            "n:gerund": "VBG",
            "n:prop": "NNP",
            "n:pt": "NN",
            "neg": "RB",
            "on": "UH",
            "post": "RB",
            "prep": "IN",
            "pro": "PRP",
            "pro:dem": "DT",
            "pro:exist": "EX",
            "pro:indef": "DT",
            "pro:poss": "PRP",
            "pro:poss:det": "PRP$",
            "pro:refl": "PRP",
            "pro:wh": "WP",
            "ptl": "RP",
            "qn": "DT",
            "POSS": "POS",
        }

    def parse(self, mor):
        '''
        Parse a mor string into Token objects.

        Converts chat-style POS tags to Penn-Treebank-style tags.

        Note that ``rules`` is a dictionary used for lexical dispatching.  
        Given a token's tag as key, it returns the appropriate rule for 
        converting that type of tag.
        
        '''
        converted = []
        for tok in super(Converter, self).parse(mor):
            if tok.lemma in ("whose", "to"):
                tok.pos = "WP$" if tok.lemma == "whose" else "TO"
            else: 
                tok = self.rules.get(tok.pos, self.default)(tok)
            converted.append(tok)
        return tuple(converted)

    # rules for converting tag attributes of mor.Token objects

    def default(self, tok):
        '''Convert tag if found in mapping dict or return token unchanged.'''
        tok.pos = self.mapping.get(tok.pos, tok.pos)
        return tok

    def adj_rule(self, tok):
        '''Convert ``adj`` tag.'''
        if tok.suffix == 'CP':
            tok.pos = 'JJR'
        elif tok.suffix == 'SP':
            tok.pos = 'JJS'
        else:
            tok.pos = 'JJ'
        return tok

    def adv_rule(self, tok):
        '''Convert ``adv`` tag.'''
        if tok.suffix == 'CP':
            tok.pos = 'RBR'
        elif tok.suffix == 'SP':
            tok.pos = 'RBS'
        else:
            tok.pos = 'RB'
        return tok

    def part_rule(self, tok):
        '''Convert ``part`` tag.'''
        if tok.suffix == 'PROG':
            tok.pos = 'VBG'
        elif tok.suffix == 'PERF':
            tok.pos = 'VBN'
        else:
            tok.pos = 'JJ'
        return tok

    def n_rule(self, tok):
        '''Convert ``n[:adj|v]`` tags.'''
        tok.pos = 'NNS' if tok.suffix == 'PL' else 'NN'
        return tok

    def v_rule(self, tok):
        '''Convert ``v[:n]`` tags.'''
        if not tok.suffix:
            tok.pos = 'VB'
        elif tok.suffix == 'PROG':
            tok.pos = 'VBG'
        elif tok.suffix == 'ZERO':
            tok.pos = 'VBD'
        elif 'PAST' in tok.suffix:
            tok.pos = 'VBD'
        elif 'PRES' in tok.suffix:
            tok.pos = 'VBP'
        elif tok.suffix == '1S':
            tok.pos = 'VBP'
        elif tok.suffix == 'PL':
            tok.pos = 'VBZ'
        elif tok.suffix == '3S':
            tok.pos = 'VBZ'
        else:
            tok.pos = 'VB'
        return tok


if __name__ == '__main__':

    print Token('adj|big-SP')

    mor_strings = (
        'adj|big-SP',
        'adv:adj|real-LY adv|fast ?',
    )
    for input in mor_strings:
        revised = Parser.poss_suffix.sub("-POSS POSS|'s", input)
        print input, "\n", zip(Parser().tags(revised), Converter().tags(input)), "\n"

