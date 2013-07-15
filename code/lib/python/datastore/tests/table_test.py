'''
Tests for datastore.table

'''
import os
from datastore.table import Reader

tsv_dir = os.path.dirname(__file__) + '/tsv/'
r = Reader(tsv_dir + 'init.tsv')

def test_columns():
    '''Testing columns attribute'''
    assert r.columns == ['id', 'name', 'age']

def test_insert():
    '''Testing insert_sql method'''
    expected = 'INSERT INTO people (id, name, age) VALUES (:id, :name, :age);'
    assert r.insert_sql(table='people') == expected

def test_update():
    '''Testing update_sql method'''
    expected = 'UPDATE people SET name = :name, age = :age WHERE id = :id;'
    assert r.update_sql(table='people') == expected

def test_convert_quotes():
    '''Testing convert_quotes method'''
    before_a = """i'd love foo's bar."""
    before_b = """foo's bar's."""
    after_a = """i''d love foo''s bar."""
    after_b = """foo''s bar''s."""
    dict_before = dict(a=before_a, b=before_b)
    dict_after = dict(a=after_a, b=after_b)
    assert r.convert_quotes(dict_before) == dict_after

batch_insert_string = '''BEGIN TRANSACTION;
INSERT INTO people (id, name, age) VALUES ('1', 'John', '20');
INSERT INTO people (id, name, age) VALUES ('2', 'Mary', '24');
INSERT INTO people (id, name, age) VALUES ('3', 'Raul', '33');
INSERT INTO people (id, name, age) VALUES ('4', 'Jones', '38');
COMMIT;'''

batch_insert_qstring = """BEGIN TRANSACTION;
INSERT INTO utterances (id, utt) VALUES ('1', 'foo''s "bar".');
INSERT INTO utterances (id, utt) VALUES ('2', '''foo''s bar''.');
COMMIT;"""

def test_batch_insert():
    '''Testing batch_insert_sql method'''
    assert r.batch_insert_sql(table='people') == batch_insert_string
    q = Reader(tsv_dir + 'quotes.tsv')
    assert q.batch_insert_sql(table='utterances') == batch_insert_qstring

batch_update_string = '''BEGIN TRANSACTION;
UPDATE people SET name = 'John', age = '20' WHERE id = 1;
UPDATE people SET name = 'Mary', age = '24' WHERE id = 2;
UPDATE people SET name = 'Raul', age = '33' WHERE id = 3;
UPDATE people SET name = 'Jones', age = '38' WHERE id = 4;
COMMIT;'''

batch_update_qstring = """BEGIN TRANSACTION;
UPDATE utterances SET utt = 'foo''s "bar".' WHERE id = 1;
UPDATE utterances SET utt = '''foo''s bar''.' WHERE id = 2;
COMMIT;"""

def test_batch_update():
    '''Testing batch_update_sql method'''
    r = Reader(tsv_dir + 'init.tsv')
    assert r.batch_update_sql(table='people') == batch_update_string
    q = Reader(tsv_dir + 'quotes.tsv')
    assert q.batch_update_sql(table='utterances') == batch_update_qstring
