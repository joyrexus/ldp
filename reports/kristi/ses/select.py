from datastore.table import Reader

r = Reader('ses.tsv')

def pprint(args):
    print "\t".join(args)

pprint('SUBJ SEX EDU INC RACE ETHN'.split())
for v in r.values('id', 'sex', 'edu', 'income', 'race', 'ethn'):
    pprint(v)
