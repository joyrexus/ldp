import re
import chat.unify


class PosTagConverter(object):
    '''
    Use to convert part-of-speech tags from CHAT to CoNLL style.

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
            "det:num": self.det_num_rule,
            "n": self.n_rule,
            "n:adj": self.n_rule,
            "n:let": self.n_let_rule,
            "n:v": self.n_rule,
            "part": self.part_rule,
            "qn": self.qn_rule,
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
            "co:voc": "UH",
            "conj:coo": "CC",
            "conj:subor": "IN",
            "det": "DT",
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
            "POSS": "POS",
        }

    def __call__(self, line):
        '''Alias for convert method.'''
        return self.convert(line)

    nominal = re.compile(r'det|n(:[a-z:]+)?|pro(:[a-z:]+)?')

    def convert(self, line):
        '''
        Converts POS tags from CHAT to Penn-Treebank style.

        For each indexed word token (i) in line, converts the POS tag based on
        the mapping dict or rule dispatcher.
        
        '''
        for i in line:
            tag = line.pos(i)   # original tag
            if line.word(i) in ("more", "less") \
               and line.dep(i) > 0 \
               and line.pos(line.dep(i)) \
               and self.nominal.match(line.pos(line.dep(i))):
                    tag = 'JJR'
            elif line.word(i) in ("most", "least") \
               and line.pos(line.dep(i)) \
               and self.nominal.match(line.pos(line.dep(i))):
                    tag = 'JJS'
            elif line.lemma(i) == "whose": 
                tag = 'WP$'
            elif line.lemma(i) == "to": 
                tag = 'TO'
            else: 
                tag = self.rules.get(line.pos(i), self.default)(i, line)
            line.set_pos(i, tag)

    def default(self, i, line):
        '''
        Return new POS tag for i-th word in line if found in mapping dict.
        
        '''
        return self.mapping.get(line.pos(i), line.pos(i))

    def adj_rule(self, i, line):
        '''Convert ``adj`` tag of i-th word in line.'''
        tag = 'JJ'  # default
        if line.suffix(i) == 'CP':
            tag = 'JJR'
        elif line.suffix(i) == 'SP':
            tag = 'JJS'
        return tag

    def adv_rule(self, i, line):
        '''Convert ``adv`` tag of i-th word in line.'''
        tag = 'RB'  # default
        if line.suffix(i) == 'CP':
            tag = 'RBR'
            if line.lemma(i) == 'late' and not \
               line.lemma(line.dep(i)) == 'than': 
                tag = 'RB'
        elif line.suffix(i) == 'SP':
            tag = 'RBS'
        return tag

    def part_rule(self, i, line):
        '''Convert ``part`` tag of i-th word in line.'''
        tag = 'JJ'  # default
        if line.suffix(i) == 'PROG':
            tag = 'VBG'
        elif line.suffix(i) == 'PERF':
            tag = 'VBN'
        return tag

    def qn_rule(self, i, line):
        '''Convert ``qn`` tag of i-th word in line.'''
        tag = 'DT'  # default
        for j in range(i, len(line)):
            if line.pos(j) in ('qn', 'det:num', 'pro:poss:det') and \
               line.dep(j) == line.dep(i):
                tag = 'PDT'
        return tag

    def n_rule(self, i, line):
        '''Convert ``n[:adj|v]`` tag of i-th word in line.'''
        return 'NNS' if line.suffix(i) == 'PL' else 'NN'

    def n_let_rule(self, i, line):
        '''Convert ``n:let`` tag of i-th word in line.'''
        return 'LS' if line.rel(i) == 'ENUM' else 'NN'

    def det_num_rule(self, i, line):
        '''Convert ``det:num`` tag of i-th word in line.'''
        return 'LS' if line.rel(i) == 'ENUM' else 'CD'

    def v_rule(self, i, line):
        '''Convert ``v[:n]`` tag of i-th word in line.'''
        tag = 'VB'  # default
        if not line.suffix(i):
            tag = 'VB'
        elif line.suffix(i) == 'PROG':
            tag = 'VBG'
        elif line.suffix(i) == 'ZERO':
            tag = 'VBD'
        elif 'PAST' in line.suffix(i):
            tag = 'VBD'
        elif 'PRES' in line.suffix(i):
            tag = 'VBP'
        elif line.suffix(i) == '1S':
            tag = 'VBP'
        elif line.suffix(i) == 'PL':
            tag = 'VBZ'
        elif line.suffix(i) == '3S':
            tag = 'VBZ'
        return tag


class RelTagConverter(object):
    '''
    Use to convert tags for grammatical dependency relations from CHAT 
    to CoNLL style.

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
            "PUNCT": self.punct_rule,
            "IOBJ": self.iobj_rule,
            "MOD": self.mod_rule,
            "JCT": self.jct_rule,
        }
        self.mapping = {     
            "SUBJ": "SBJ",
            "CSUBJ": "SBJ",
            "XSUBJ": "SBJ",
            "OBJ": "OBJ",
            "OBJ2": "OBJ",
            "COMP": "OBJ",
            "XCOMP": "OPRD",
            "PRED": "PRD",
            "CPRED": "PRD",
            "XPRED": "PRD",
            "NEG": "ADV",
            "DET": "NMOD",
            "POBJ": "PMOD",
            "PTL": "PRT",
            "COM": "DEP",
            "TAG": "DEP",
            "VOC": "VOC",
            "ROOT": "ROOT",
            "ROOT-NV": "ROOT",
            "QUANT": "NMOD",
            "LOC": "PUT",
            "CMOD": "NMOD",
            "XMOD": "NMOD",
            "XJCT": "ADV",
        }

    def __call__(self, line, orig):
        '''Alias for convert method.'''
        return self.convert(line, orig)

    def convert(self, line, orig):
        '''
        Converts REL tags from CHAT to CoNLL style.

        For each indexed word token (i) in line, converts the REL tag based on
        the mapping dict or rule dispatcher.
        
        '''
        for i in line:
            if line.rel(i) == 'CPZR':
                self.cpzr_rule(i, line, orig)
            elif line.rel(i) in ('AUX', 'SRL'):
                self.aux_srl_rule(i, line, orig)
            elif line.rel(i) == 'INF':
                self.inf_rule(i, line, orig)
            if line.rel(i).startswith('COORD-'):
                self.coord_rule(i, line, orig)
            tag = line.rel(i)   # original tag
            tag = self.rules.get(tag, self.default)(i, line, orig)
            line.set_rel(i, tag)

    def default(self, i, line, orig):
        '''
        Return new REL tag for i-th word in line if found in mapping dict.
        
        '''
        return self.mapping.get(line.rel(i), line.rel(i))

    def punct_rule(self, i, line, orig):
        '''
        Modify rel tag and dep num of i-th word.

        This rule is triggered with the i-th word has a rel of PUNCT
        (i.e., the i-th item in the line is a form of punctuation).

        The rule merely ensures that punctuation always depends on the 
        ROOT word and returns "P" for the new rel tag.

        '''
        for k in line:
            if line.rel(k) == 'ROOT':
                line.set_dep(i, k)
        return 'P'

    def iobj_rule(self, i, line, orig):
        '''Convert IOBJ tag of i-th word in line.'''
        return 'BNF' if line.word(i) == "for" else 'DTV'

    def mod_rule(self, i, line, orig):
        '''Convert MOD tag of i-th word in line.'''
        return 'SUFFIX' if orig.pos(i) == "POSS" else 'NMOD'

    nominal = re.compile(r'det|n(:[a-z:]+)?|pro(:[a-z:]+)?')
    verbal = re.compile(r'v(:n)?|part|aux|inf')

    def jct_rule(self, i, line, orig):
        '''Convert JCT tag of i-th word in line.'''
        tag = 'ADV' # default
        if line.word(i) in ("to", "from"):
            tag = 'DIR'
        elif line.word(i) in ("in", "at") or orig.pos(i) == 'adv:loc':
            tag = 'LOC'
        elif line.word(i) in ("before", "after") or orig.pos(i) == 'adv:tem':
            tag = 'TMP'
        elif line.word(i).endswith("ly"):
            tag = 'MNR'
        elif not (self.nominal.match(orig.pos(line.dep(i))) \
          or self.verbal.match(orig.pos(line.dep(i)))):
            tag = 'AMOD'
        return tag

    def coord_rule(self, i, line, orig):
        '''
        Convert various features of line if i-th word is a coordinator.

        This rule is triggered if the rel feature of the i-th word 
        starts with "COORD".

        '''
        # find headword of word
        d = line.dep(i)
        # if headword is itself a COORD, run coord_rule on it
        if line.rel(d).startswith("COORD") and orig.pos(d) == "conj:coo":
            self.coord_rule(d, line, orig)
        # find indices of words with rel = COORD[-GR] sharing same dep
        sharing_d = [j for j in line if (line.dep(j) == d)
                                    and (line.rel(j).startswith('COORD'))]
        # if any of the other dependent words are a COORD, parse that
        # COORD structure and update the dependent word to the new head
        for j in range(len(sharing_d)):
           sharing_d[j] = self.check_coord(sharing_d[j], line, orig)
        # set rel of first COORD word to rel of headword
        line.set_rel(i, line.rel(d))
        # set dep of first COORD word to dep of headword
        line.set_dep(i, line.dep(d))
        # set rel of headword to "COORD"
        if i < d:
            line.set_rel(d, 'COORD')
        # ... unless headword comes before i-th word, then set rel to "DEP"
        elif d < i:
            line.set_rel(d, 'DEP')
        # set dep of headword to i-th word
        line.set_dep(d, i)
        for j in sharing_d:
            if j == i:
                pass
            elif orig.pos(j) == "conj:coo":
                line.set_rel(j, "COORD")
            else:
                line.set_rel(j, "CONJ")

    def check_coord(self, i, line, orig):
        '''
        Check whether the i-th word is the head of a COORD structure.  If it is, convert
        the structure to CoNLL format and return the word number of the new head.  If it
        is not the head, return the unchanged word number.

        '''
        if line.rel(i) == "COORD":
            # find indices of words with rel = COORD[-GR] dependent on word
            sharing_d = [j for j in line if (line.dep(j) == i)
                                    and (line.rel(j).startswith('COORD'))]
            # if any of the dependent words are a COORD, parse that
            # COORD structure and update the dependent word to the new head
            for j in range(len(sharing_d)):
                sharing_d[j] = self.check_coord(sharing_d[j], line, orig)
            if len(sharing_d) > 0:
                # set first dependent word's GR to this GR
                line.set_rel(sharing_d[0], line.rel(i))
                # set first dependent word's headword to this headword
                line.set_dep(sharing_d[0], line.dep(i))
                # set this word's headword to be first elem of sharing_d
                line.set_dep(i, sharing_d[0])
                for j in range(1, len(sharing_d)):
                    line.set_rel(sharing_d[j], 'CONJ')
                return sharing_d[0]
            else:
                return i
        else:
            return i

    cpzr_map = {'before': "TMP",
                'after': "TMP", 
                'by': "MNR", 
                'because': "PRP", 
                'for': "PRP"}

    def cpzr_rule(self, i, line, orig):
        '''
        Convert various features of line if i-th word has a CPZR rel feature.
        
        '''
        # set rel of i-th word (w/ CPZR tag) to the rel of its head
        d = line.dep(i)
        line.set_rel(i, line.rel(d))
        # set dep of i-th word (w/ CPZR tag) to the dep of its head
        line.set_dep(i, line.dep(d))
        # set rel of orig head to SUB
        line.set_rel(d, 'SUB')
        # set dep of orig head to i-th word
        line.set_dep(d, i)
        # modify rel of i-th word if pos was conj:subor and head was X/CJCT
        if orig.rel(d) in ('CJCT', 'XJCT') and orig.pos(i) == 'conj:subor':
            tag = self.cpzr_map.get(line.word(i), 'ADV')
            line.set_rel(i, tag)

    def aux_srl_rule(self, i, line, orig):
        '''
        Convert various features of line if i-th word has a
        rel feature of AUX or SRL.

        If a word prior to the i-th word had such a rel feature, we don't do
        anything as the required conversion will have already been completed.
        
        '''
        for p in range(1, i):   # word indices prior to i-th word
            if line.rel(p) in ('AUX', 'SRL'): return None 
        d = line.dep(i)     # shared dep word num
        # find indices of words with rel = AUX or SRL sharing same dep
        sharing_d = [j for j in line if (line.dep(j) == d)
                                    and (line.rel(j) in ('AUX', 'SRL'))]
        # set rel of first word to rel of their shared dep
        first = sharing_d[0]
        line.set_rel(first, line.rel(d))
        # set dep of first word to dep of their shared dep
        line.set_dep(first, line.dep(d))
        # set dep of the rest (as well as shared dep) to word num of preceding
        sharing_d.append(d)
        chain = sorted(sharing_d)           # chain of words to be modified
        for x, y in zip(chain, chain[1:]):  # get words of chain pairwise
            line.set_dep(y, x)              # set dep of y to that of prior (x)
        for k in chain[1:]:
            line.set_rel(k, 'VC')           # set rel of remaining to VC
        # set deps of other words prior to and dependent on d to first
        max = d if d > i else i
        for k in set(range(1, max)) - set(chain):
            if line.dep(k) == d and not line.rel(k) == 'INF':
                line.set_dep(k, first)

    def inf_rule(self, i, line, orig):
        '''
        Convert various features of line if i-th word has an INF rel feature.
        
        '''
        d = line.dep(i)                 # find head dependency
        line.set_rel(i, line.rel(d))    # set rel to rel of head
        line.set_dep(i, line.dep(d))    # set dep to dep of head
        line.set_dep(d, i)              # set dep of head to i
        line.set_rel(d, 'IM')           # set rel of head to "IM"
        for j in range(1, i):           # for all prior words 
            if line.dep(j) == d:        #   if dependent on former head
                line.set_dep(j, i)      #     set dep to i


class Line(chat.unify.Line):
    '''
    Use for tokenizing annotated utterances produced by 
    clan's part-of-speech tagger (``mor``) and grammatical 
    dependency parser (``grasp``).

    '''
    convert_pos = PosTagConverter()
    convert_rel = RelTagConverter()

    def __init__(self, utt, mor, syn):
        '''
        Initialize a MorphoSyntax Line object.

        Creates a dict representation of the utterance, with each word token's
        numeric index as key and a feature dict as value.

        That is, a Line object is comprised of word token indices mapping to
        that word's morphosyntactic features (word, lemma, pos, dep, rel, etc).

        { 1: FEATURE-DICT-1, 
          2: FEATURE-DICT-2,
          ...
          N: FEATURE-DICT-N }

        Such a Line object provides a unified representation of the chat, mor, 
        and syn column values in an utterance line of a transcript.

        Note that POS and REL tags are converted from CHAT to CoNLL style.

        '''
        super(Line, self).__init__(utt, mor, syn)
        orig = chat.unify.Line(utt, mor, syn)
        self.convert_pos(self)
        self.convert_rel(self, orig)    # convert self based on unconverted features
        dict.__init__(self)


class Transcript(chat.unify.Transcript):
    '''
    Provide unified representation of chat, mor, and syn column values in 
    a transcript.
    
    '''
    unify = Line


if __name__ == '__main__':

    utt = 'do you want to read a book ?'
    mor = 'aux|do pro|you aux|want inf|to v|read&ZERO det|a n|book ?'
    syn = '1|5|AUX 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|7|DET 7|5|OBJ 8|5|PUNCT' 

    print Line(utt, mor, syn)

    '''
    transcript = Transcript(83, 10)

    for row in transcript(speaker="parent"):
        print row

    if transcript.problems:
        print "{0} problematic lines".format(len(transcript.problems))
    '''

