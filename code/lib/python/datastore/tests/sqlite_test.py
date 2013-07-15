'''
Tests for datastore.sqlite

'''
import os
from datastore import sqlite
from nose.tools import raises

db = sqlite(":memory:")

db.execute("CREATE TABLE people(id INTEGER PRIMARY KEY, name, age INTEGER)")
db.con.executescript("""
    INSERT INTO people VALUES (1, 'John', 20);
    INSERT INTO people VALUES (2, 'Mary', 24);
    INSERT INTO people VALUES (3, 'Raul', 33);
    INSERT INTO people VALUES (4, 'Jones', 38);
    """)
    
def test_props():
    '''Tesing db properties'''
    assert db.schema() == {'people': ['id', 'name', 'age']}
    assert db.tables == ['people']
    assert db.columns('people') == ['id', 'name', 'age']
    assert db.path == ":memory:"

def test_execute():
    '''Testing execute method'''
    db.execute('select * from people')
    person = db.cur.fetchone()
    assert person['name'] == 'John'
    assert person['age'] == 20

def test_select():
    '''Testing select method'''
    db.select('people')
    person = db.cur.fetchone()
    assert person['name'] == 'John'
    assert person['age'] == 20
    db.select('people', where='age > 35')
    person = db.cur.fetchone()
    assert person['name'] == 'Jones'
    assert person['age'] == 38

def test_regexp():
    '''Testing regular expression matching'''
    select_st = 'select id, name from people where name regexp "^M";'
    db.execute(select_st)
    person = db.cur.fetchone()
    assert person['name'] == 'Mary'

def test_valid_table():
    '''Testing valid_table method with valid table'''
    assert db.valid_table('people') == True

@raises(NameError)
def test_invalid_table():
    '''Testing valid_table method with invalid table name'''
    db.valid_table('orders')

def test_valid_column():
    '''Testing valid_column method with valid column name'''
    assert db.valid_column('age', table='people') == True

@raises(NameError)
def test_invalid_column():
    '''Testing check_column_name method with invalid column'''
    db.valid_column('sex', table='people')

def test_insert():
    '''Testing insert method'''
    i = 'INSERT INTO people (age, id, name) VALUES (40, 5, "Sawyer")'
    assert db.insert('people', id=5, name="Sawyer", age=40, preview=True) == i
    db.insert('people', id=5, name="Sawyer", age=40)
    db.select('people', where='name = "Sawyer"')
    person = db.cur.fetchone()
    assert person['name'] == 'Sawyer'
    assert person['age'] == 40

def test_batch_insert():
    '''Testing batch_insert method'''
    file = os.path.dirname(__file__) + '/tsv/insert.tsv'
    db.batch_insert(file, table='people')
    db.select('people', where='name="William"')
    person = db.cur.fetchone()
    assert person['name'] == 'William'
    assert person['age'] == 22

def test_update():
    '''Testing update method'''
    expected = 'UPDATE people SET age = 30 WHERE id = 1;'
    assert db.update('people', id=1, age=30, preview=True) == expected
    expected = 'UPDATE people SET name = "Jack" WHERE id = 1;'
    assert db.update('people', id=1, name="Jack", preview=True) == expected
    db.update('people', id=1, name="Jack")
    db.select('people', where='id = 1')
    person = db.cur.fetchone()
    assert person['name'] == 'Jack'

def test_batch_update():
    '''Testing batch_update method'''
    file = os.path.dirname(__file__) + '/tsv/update.tsv'
    db.batch_update(file, table='people')
    db.select('people', where='name="Bill"')
    person = db.cur.fetchone()
    assert person['name'] == 'Bill'
    assert person['age'] == 22
    db.select('people', where='name="Amy"')
    person = db.cur.fetchone()
    assert person['name'] == 'Amy'
    assert person['age'] == 28
