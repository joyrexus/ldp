import re
from ldp.data import Utterances

pattern = r'\bones?\b'
numword = re.compile(pattern, re.IGNORECASE)
utts = Utterances()
columns = 'subject, session, row, p_utts, c_utts, context'
where = 'session in (5, 6, 7)'

def pprint(*args): 
    print "\t".join(str(x) for x in args)

pprint(*'subject session row speaker utterance context'.upper().split())

for subj, sess, row, p, c, ctx in utts(columns, where, limit=''):
    for spkr, utt in [('P', p), ('C', c)]:
        if numword.search(utt):
            pprint(subj, sess, row, spkr, utt, ctx)
