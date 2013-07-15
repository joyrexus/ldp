import os
from datastore import sqlite, AttributeRowFactory

db = sqlite(os.environ['LDP_DB'], row_factory=AttributeRowFactory)

for row in db('subjects', limit=1):
    print row
    print row[0]
    print row['id']
    print row.id
    print row.values("id", "dob", "sex")
    for i in row: print i

db.close()

'''
db = sqlite(os.environ['LDP_DB']) 

db.show('subjects')

db.show('subjects', columns='id, sex, dob', limit=5)

print db.tables
print db.columns('subjects')

for id, sex, dob in db.select('subjects', 
                                columns='id, sex, dob',
                                where='project=2'):
    print id, sex, dob

'''

from datastore import Reader

r = Reader('tests/tsv/init.tsv')
# print r.rows
# print r.column('name')
for v in r.values('name', 'age'):
    print v
'''
print r
for row in r: print row
print r.insert_sql(table='sample')
print r.batch_insert_sql(table='sample')
print r.batch_update_sql(table='sample')
'''
