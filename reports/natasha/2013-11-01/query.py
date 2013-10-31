#!/usr/bin/env python
import sys
from ldp.data import Utterances

utterances = Utterances()
subjects = '83 40 49'.split(' ')
columns = [col.rstrip() for col in open('columns.txt')]

sess_cond = ''
if len(sys.argv) > 1:
    sess = sys.argv[-1]
    sess_cond = ' and session = ' + sess

COLUMNS = ', '.join(columns)
CONDITIONS = '(p_utts != "" or c_utts != "")' + sess_cond
LIMIT = ''

def pprint(args):
    try:
        print '\t'.join(str(x) for x in args)
    except:
        for x in args:
            try:
                print x,
            except:
                print x.encode('ascii', 'ignore'),
        print

pprint(columns)

for row in utterances(COLUMNS, CONDITIONS, LIMIT, subjects=subjects):
    pprint(row)
