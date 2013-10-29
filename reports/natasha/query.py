from ldp.data import Utterances

utterances = Utterances()
subjects = '24 29 33 37 42 43 44 48 50 62 74 77 78 84 88 92 103 105'.split(' ')
columns = [col.rstrip() for col in open('columns.txt')]

COLUMNS = ', '.join(columns)
CONDITIONS = 'p_utts != "" or c_utts != ""'
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
