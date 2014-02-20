'''
This was used to convert `td-pl.tsv` to `reading.tsv`

'''
from datastore.table import Reader
from collections import defaultdict

columns = 'SUBJ SESS AGE WJ GM'.split()

outcomes = Reader('td-pl.tsv')
subjects = defaultdict(dict)

def pprint(*args):
    print "\t".join(args)

pprint(*columns)

for row in outcomes:
    subj = row['SUBJ']
    wj1, gm1 = row['READ1'], row['READ3']
    wj2, gm2 = row['READ2'], row['READ4']
    pprint(subj, "22", "102", wj1, gm1) 
    pprint(subj, "25", "114", wj2, gm2) 
                         
