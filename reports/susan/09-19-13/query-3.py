from ldp.gesture import LRB
from ldp.gesture import GestureSpeechRelation as GSR
from ldp.data import Utterances, Subjects
from collections import defaultdict as dd

lrb = LRB()
gsr = GSR()
subjects = Subjects()
utterances = Utterances()
count = dd(lambda: dd(int))
P2 = set(subjects.project(2))

gcodes = set()
hcodes = 'L R B'.split()
columns = 'subject, session, c_lrb, c_gs_rel'
filter  = 'session in (1,2,3,4,5,8) and c_lrb != ""'

def pprint(args): print "\t".join(str(x) for x in args)

for subj, sess, h, g in utterances(columns, filter, limit=''): 
    proj = 2 if subj in P2 else 3
    H = lrb.valid_values(h.upper())
    G = gsr.valid_values(g, subcodes=False)
    pairs = set(p for p in zip(H, G))           # no repeats
    for h, g in pairs:
        if h in hcodes: 
            gcodes.add(g)
            count[subj, sess, proj, g][h] += 1


pprint('Subject Session Project GSR'.split() + hcodes)

for id in sorted(count):
    subj, sess, proj, g = id
    results = [count[id][h] for h in hcodes]
    pprint([subj, sess, proj, g] + results)
    
