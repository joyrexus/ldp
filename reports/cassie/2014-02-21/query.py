import sys
from ldp.data import Utterances
from ldp.grammar import TokenList
from collections import defaultdict as dd

vtoks = dd(int)
vtyps = dd(dict)

utts = Utterances()
columns = 'id, subject, session, p_utts, p_mor, c_utts, c_mor'
where = 'c_mor != "" or p_mor != ""'

for row in utts(columns, where, project=2, limit=''):
    id, subj, sess, p, p_mor, c, c_mor = row
    for spkr, utt, mor in [('P', p, p_mor), ('C', c, c_mor)]:
        if mor:
            try:
                tokens = TokenList(utt, mor)
            except IndexError:
                sys.stderr.write("problem parsing row {}: {}".format(id, mor)) 
            verbs = [t.lemma for t in tokens if t.pos.startswith('v')]
            for v in verbs:
                vtoks[subj, sess, spkr] += 1
                vtyps[subj, sess, spkr][v] = 1


def pprint(*args):
    print "\t".join(str(x) for x in args)


pprint(*'SUBJ SESS SPKR VTYPS VTOKS'.split(' '))
for id in vtoks:
    SUBJ, SESS, SPKR = id
    VTYPS = len(vtyps[id].items())
    pprint(SUBJ, SESS, SPKR, VTYPS, vtoks[id])

