from nlp import Normalizer
import re

word = re.compile(r'\w')
coded = re.compile(r'(d/k|n/r)', re.IGNORECASE)
parens = re.compile(r'\s?(\([^\)]+?\))')
brackets = re.compile(r'\s?(\[[^\]]+?\])')
lemmas = Normalizer()

def pprint(*items):
    print "\t".join(str(i) for i in items)

pprint(*'ID STORY DELIM CLAUSES'.split(' '))

for line in open('data.tsv'):
    columns = line.rstrip().split('\t')
    id = columns[0]
    if id == 'SU_ID': continue
    A = columns[1:6]        # story A
    A_clauses = columns[7]  # story A clauses
    B = columns[11:16]      # story B
    B_clauses = 0
    if len(columns) > 17: B_clauses = columns[17] # story B clauses
    for story, pages, CLAUSES in [('A', A, A_clauses), ('B', B, B_clauses)]:
        DELIMS = 0
        for text in pages: DELIMS += text.count('|')
        pprint(id, story, DELIMS, CLAUSES)
