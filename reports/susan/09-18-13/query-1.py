from ldp.gesture import LRB
from ldp.data import Utterances, Subjects
from util.count import FeatureCounter

lrb = LRB()
subjects = Subjects()
utterances = Utterances()
count = FeatureCounter('Subject', 'Session', 'Project', 'LRB')

P2 = set(subjects.project(2))

columns = 'subject, session, c_lrb, c_g_type'
filter  = 'session in (1,2,3,4,5,8) and c_lrb != ""'

def pprint(args): print "\t".join(args)

for subj, sess, h, g in utterances(columns, filter, limit=''): 
    proj = 2 if subj in P2 else 3
    for h in lrb.valid_values(h.upper()): 
        count(subj, sess, proj, h) 

count.print_report('LRB')

