import re
from ldp.data import Utterances

U = Utterances()
words = re.compile(r'\b(build|block|lego)', re.IGNORECASE)
columns = 'subject, session, time, row, key, c_utts, context'
filter = 'session > 3 and session < 10'

def pprint(args):
    print "\t".join(str(x) for x in args)

pprint(columns.upper().split(', '))

for row in U(columns, filter, project=2):
    if words.search(row[5]): pprint(row)

