import re
from ldp.data import Utterances
from nlp.lex import Tokenizer
from util.count import FeatureCounter

utts = Utterances()
tokenize = Tokenizer()
count = FeatureCounter('Subject', 'Session', 'Speaker')
columns = 'subject, session, key, c_utts, p_utts'

wordchar = re.compile(r'\w')
grandmother = re.compile(r'G')
father = re.compile(r'F|@')


for subj, sess, key, c, p in utts(columns, 
                                  where='session in ("11", "12")',
                                  limit='', 
                                  project=2):
    for spkr, utt in [('CHILD', c), ('MOTHER', p)]:
        if spkr == 'MOTHER':
            if father.search(key): 
                spkr = 'FATHER'
            elif grandmother.search(key): 
                spkr = 'GRANDMOTHER'
        for t in tokenize(utt):
            if wordchar.search(t): count(subj, sess, spkr)

count.print_report('Speaker')
