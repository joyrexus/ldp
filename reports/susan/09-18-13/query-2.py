from ldp.gesture import LRB, GestureType
from ldp.data import Utterances, Subjects
from util.count import FeatureCounter

lrb = LRB()
gtype = GestureType()
subjects = Subjects()
utterances = Utterances()
count = FeatureCounter('Subject', 'Session', 'Project', 'Gesture')

P2 = set(subjects.project(2))

columns = 'subject, session, c_lrb, c_g_type'
filter  = 'session in (1,2,3,4,5,8) and c_lrb != ""'

def pprint(args): print "\t".join(args)

for subj, sess, h, g in utterances(columns, filter, limit=''): 
    proj = 2 if subj in P2 else 3
    H = lrb.valid_values(h.upper())
    G = gtype.valid_values(g, subcodes=False)
    for (h, g) in zip(H, G):
        code = "{0}+{1}".format(h, g)
        count(subj, sess, proj, code) 

count.print_report('Gesture')
