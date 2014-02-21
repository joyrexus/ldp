from ldp.data import Utterances
from ldp.gesture import GestureType
from collections import defaultdict as dd

seen = dd(set)
count = dd(int)
parse = GestureType()
utts = Utterances()
columns = 'subject, session, row, c_g_type'
where = 'c_g_type != ""'

for subj, sess, row, gt in utts(columns, where=where, project=2, limit=''):
    codes = parse(gt, subcodes=False)
    if 'R' in codes: 
        seen[subj].add(sess)
        count[subj, sess] += sum(x=='R' for x in codes)

def pprint(*args):
    print "\t".join(str(x) for x in args)

pprint('SUBJ', 'ONSET', 'COUNT')
for subj in sorted(seen):
    onset = min(seen[subj])
    pprint(subj, onset, count[subj, onset])
