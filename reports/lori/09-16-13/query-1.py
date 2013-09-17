import re
from ldp.data import Utterances

U = Utterances()
reading = re.compile(r'\bR\b', re.IGNORECASE)
columns = 'subject, session, time, row, key, p_utts, c_utts, context'
filter = 'session < 8 and key != ""'

def pprint(args):
    print "\t".join(str(x) for x in args)

pprint(columns.upper().split(', '))

for row in U(columns, filter, project=2):
    if reading.search(row[4]): pprint(row)
