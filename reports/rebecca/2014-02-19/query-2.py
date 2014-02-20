import re
from ldp.data import Utterances

talk = re.compile('(talk|say|speak)(s|ing)?|(said|spoke)')
person = re.compile('(P|parent|F|father|sib|sibling|sister|brother)')

utts = Utterances()
columns = 'subject, session, row, p_utts, c_utts, context'
project = 2

def pprint(*args): 
    print "\t".join(str(x) for x in args)

pprint(*columns.split(', '))
for (subj, sess, row, p, c, x) in utts(columns, project=2):
    if talk.search(x) and person.search(x):
        pprint(subj, sess, row, p, c, x)
