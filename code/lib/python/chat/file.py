'''Read in and write out chat files.'''

import os, re, sys

class Reader(object):
    '''
    Read in a chat file.
     
    '''
    def __init__(self, file):
        self.file = file
        self.records = []
        self._parse(file)
        self.tiers = sorted(self.records[0].keys())

    def _parse(self, file):
        '''Parse chat file into records.

        Each record gets stored as a dict. For example, suppose we have the
        following record in a chat file (an utterance with dependent tiers):

            *MOT:   I think we need some +...
            %row:   12
            %mor:   pro|I v|think pro|we v|need pro:indef|some +...
            %syn:   1|2|SUBJ 2|0|ROOT 3|4|SUBJ 4|2|COMP 5|4|OBJ 6|2|PUNCT 

        This record would get parsed and stored as a dict:

            {'utt': 'I think we need some +...', 
            'speaker': 'MOT', 
            'row': '12',
            'mor': 'pro|I v|think pro|we v|need pro:indef|some +...', 
            'syn': '1|2|SUBJ 2|0|ROOT 3|4|SUBJ 4|2|COMP 5|4|OBJ 6|2|PUNCT'}
        
        '''
        with open(file) as f:
            for rec in f.read().split("*"):
                if rec.startswith("@"): continue
                rec = rec.rstrip("\n")
                record = {}
                for line in rec.split("\n"):
                    if line.startswith("@"): continue
                    (tier, value) = line.rstrip().split("\t", 1)
                    if tier.startswith("%"):
                        tier = tier.strip("%:")
                    else:
                        spkr = tier.strip(":")
                        record['speaker'] = spkr
                        tier = 'utt'
                    record[tier] = value
                if record:
                    self.records.append(record)

    def values(self, *tiers):
        '''Yield tuple of values for specified tiers.'''
        if not tiers:
            tiers = self.tiers
        for rec in self.records:
            yield tuple(rec.get(tier, "") for tier in tiers)

    def pprint(self, *tiers, **kwargs):
        '''Pretty-print the values for specified tiers.'''
        if not tiers:
            tiers = self.tiers
        sep = kwargs.get("separator", "\t")
        print sep.join(str(tier).upper() for tier in tiers)
        for rec in self.values(*tiers):
            print sep.join(str(value) for value in rec)


class Writer(object):
    '''
    Write out chat files.
     
    '''
    def __init__(self, out=None):
        hdr = (os.path.dirname(__file__) or '.') + '/header.txt'
        self.header = open(hdr, 'r').read()
        self.out = open(out, 'a') if out else sys.stdout

    def write(self, rows):
        '''Write out rows as chat tiers.

        *rows* should be an iter of 5-tuples: 
        [(UID, ROW, KEY, P_UTT, C_UTT), ... ]
        
        
        '''
        self.out.write(self.header)
        for r in rows:
            self.out.write(self.format(r))
        self.out.write('@End\n')

    word_pt = re.compile(r'\w')

    def format(self, r, fix=True):
        '''Format row as chat tiers.

        *r* should be a 5-tuple: (UID, ROW, KEY, P_UTT, C_UTT)

        '''
        uid, row, key, p, c = r     # unpack row
        spk, utt = '', ''           # speaker and utterance
        P, C = '', ''               # Parent and Child tiers
        tiers = "*{0}:\t{1}\n%id:\t{2}\n%row:\t{3}\n"   # tier format

        if not self.word_pt.search(p) and not self.word_pt.search(c):
            return ''
        if p:
            spk = 'FAT' if 'F' in key else 'MOT'
            utt = p
            if fix: utt = self.fix(utt)
            P = tiers.format(spk, utt, uid, row)
        if c:
            spk = 'CHI'
            utt = c
            if fix: utt = self.fix(utt)
            C = tiers.format(spk, utt, uid, row)
        return P + C

    term_pt = re.compile(r'([^\.])([\?\!\.])$')
    term_dash_pt = re.compile(r' --$')
    dash_pt = re.compile(r'--+')
    ok_pt = re.compile(r'\bok\b')

    def fix(self, utt):
        '''Fix utterance so that it conforms to chat conventions.

        * separate punctuation from last word token ("Foo!" > "Foo !")
        * replace terminal dashes with chat-style ellipses ("+...")
        * replace all other dashes with pound sign ("#")
        * remove quotes
        * remove dash from possessive ("Foo-'s bar" > "Foo's bar")
        * change ambiguous utterance sign ("###" > "xxx")
        
        '''
        utt = self.term_pt.sub(r'\1 \2', utt)
        utt = self.term_dash_pt.sub(' +...', utt)
        utt = self.dash_pt.sub('#', utt)
        utt = self.ok_pt.sub('okay', utt)
        utt = utt.replace('"', '')
        utt = utt.replace("-'s", "'s")
        utt = utt.replace("###", "xxx")
        if utt.endswith("xxx"): utt = utt + " ."
        return utt


if __name__ == '__main__':

    file = Reader('tests/sample.cha')
    file.pprint('speaker', 'row', 'utt', 'mor')
    
    '''
    w = Writer()
    rows = [(1022010001, 1, '', 'hello!', ''),
            (1022010002, 2, '', 'hello!', ''),
            (1022010003, 3, '', 'hello!', '')]
    w.write(rows)
    '''
