from ldp.data import Utterances

utterances = Utterances()

columns = 'id, subject, session, row, c_chat, c_mor, context'
where = 'c_chat != "" and session=8'

def pprint(items):
    print "\t".join([str(i) for i in items])

pprint(columns.upper().split(', '))

for u in utterances(columns, where, limit=''):
    pprint(u)

