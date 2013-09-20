from ldp.gesture import LRB
from ldp.data import Utterances, Subjects
from collections import defaultdict as dd

lrb = LRB()
subjects = Subjects()
utterances = Utterances()
count = dd(lambda: dd(int))
P2 = set(subjects.project(2))

codes = 'L R B'.split()
columns = 'subject, session, c_lrb'
filter  = 'session in (1,2,3,4,5,8) and c_lrb != ""'

def pprint(args): print "\t".join(str(x) for x in args)

for subj, sess, h in utterances(columns, filter, limit=''): 
    proj = 2 if subj in P2 else 3
    H = set(h for h in lrb.valid_values(h.upper())) # no repeats
    for h in H:
        if h in codes: count[subj, sess, proj][h] += 1

pprint('Subject Session Project'.split() + [x for x in codes])

for id in sorted(count):
    subj, sess, proj = id
    results = [count[id][x] for x in codes]
    pprint([subj, sess, proj] + results)
    
