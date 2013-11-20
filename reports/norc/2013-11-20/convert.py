from nlp import Normalizer
import re

word = re.compile(r'\w')
coded = re.compile(r'(d/k|n/r)', re.IGNORECASE)
parens = re.compile(r'\s?(\([^\)]+?\))')
brackets = re.compile(r'\s?(\[[^\]]+?\])')
lemmas = Normalizer()

def pprint(*items):
    print "\t".join(str(i) for i in items)

pprint(*'ID STORY PAGE DELIM CLAUSES TOKENS TEXT'.split(' '))

for line in open('data.tsv'):
    columns = line.rstrip().split('\t')
    id = columns[0]
    if id == 'SU_ID': continue
    A = columns[1:6]        # story A
    B = columns[11:16]      # story B
    for story, pages in [('A', A), ('B', B)]:
        for page, text in enumerate(pages):
            page += 1
            utts = text
            if coded.search(text):
                utts = coded.sub('', text)
            if brackets.search(text):
                utts = brackets.sub('', text)
            if parens.search(text):
                utts = parens.sub('', text)
            delims = utts.count('|')
            parts = utts.lower().split('|')   # split text into parts
            words = [" ".join(lemmas(t)) for t in parts if word.search(t)]
            tokens = ", ".join(words)
            pprint(id, story, page, delims, tokens, text)
