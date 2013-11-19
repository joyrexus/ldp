from collections import defaultdict as dd

UIDS = set()
DELIMS = dd(int)
TOKENS = dd(int)
types = dd(set)

data = open('data.tsv')
header = data.readline()    # omit header

def pprint(*items):
    '''Pretty-print items.'''
    print "\t".join(str(i) for i in items)

for row in data:
    id, story, page, delims, clauses = row.split('\t')[:5]
    uid = (id, story)
    UIDS.add(uid)
    DELIMS[uid] += int(delims)
    for clause in clauses.split(', '):
        if not clause: continue
        for t in clause.split(' '): # split clause into tokens
            if not t: continue
            if t == 'p':  continue
            TOKENS[uid] += 1        # increment token count for id
            types[uid].add(t)       # add token to set of types for id

pprint('_ID', 'STORY', 'DELIMS', 'TOKENS', 'TYPES')     # report header

for uid in sorted(UIDS):
    tokens = TOKENS[uid]
    delims = DELIMS[uid]
    id, story = uid
    pprint(id, story, delims, tokens, len(types[uid]))
