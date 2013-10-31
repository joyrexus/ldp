from ldp.data import Utterances

utterances = Utterances()
subjects = [id.rstrip() for id in open('subjects.txt')]

columns = 'id, subject, session, row, c_chat, c_clauses, c_np, context'
where = 'c_chat != "" and session=8'

def pprint(items):
    print "\t".join([str(i) for i in items])

pprint(columns.upper().split(', '))

for u in utterances(columns, where, subjects=subjects, limit=''):
    pprint(u)

