from datastore.sqlite import sqlite

db = sqlite('temp.db')

column = 'c_utts'
pattern = r'.*\d'

select_st = 'select id, {0} from utterances where {0} regexp "{1}";'

db.execute(select_st.format(column, pattern))

for id, utt in db:
    print utt
