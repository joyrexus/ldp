import os
from nose.tools import raises
from ldp.data import Dataset, Transcript, Subject, Utterances

ds = Dataset(":memory:")

ds.execute("CREATE TABLE people(id INTEGER PRIMARY KEY, name, age)")
ds.con.executescript("""
    INSERT INTO people VALUES (1, 'John', 20);
    INSERT INTO people VALUES (2, 'Mary', 24);
    INSERT INTO people VALUES (3, 'Raul', 33);
    INSERT INTO people VALUES (4, 'Jones', 38);
    INSERT INTO people VALUES (5, 'William', 18);
    """)

def test_misc():
    assert ds.schema() == {'people': ['id', 'name', 'age']}
    assert ds.tables == ['people']
    assert ds.columns('people') == ['id', 'name', 'age']
    assert ds.path == ":memory:"

def test_execute():
    '''Testing execute method'''
    ds.execute('select * from people')
    person = ds.cur.fetchone()
    assert person['id'] == 1
    assert person['name'] == 'John'
    assert person['age'] == 20

def test_select():
    '''Testing select method'''
    ds.select(table='people')
    person = ds.cur.fetchone()
    assert person['id'] == 1
    assert person['name'] == 'John'
    assert person['age'] == 20
    ds.select(table='people', where='age > 35')
    person = ds.cur.fetchone()
    assert person['name'] == 'Jones'
    assert person['age'] == 38

def test_insert():
    '''Testing insert method'''
    ds.insert('people', id=6, name="Sawyer", age=40)
    ds.select(table='people', where='name="Sawyer"')
    person = ds.cur.fetchone()
    assert person['id'] == 6
    assert person['name'] == 'Sawyer'
    assert person['age'] == 40

def test_update():
    '''Testing update method'''
    ds.update(table='people', id=5, age=20, name="Bill")
    ds.select(table='people', where='id=5')
    person = ds.cur.fetchone()
    assert person['id'] == 5
    assert person['name'] == 'Bill'
    assert person['age'] == 20

@raises(Exception)
def test_close():
    '''Testing close method'''
    ds.con.close()
    ds.select('people'), 'Raise exception since connection is closed'

d = Dataset()   # default to $LDP_DB

def test_default():
    '''Testing default parameters'''
    assert d.path == os.environ['LDP_DB']
    c = ['id', 'protocol', 'alias', 'grade', 'season', 'desc'] 
    assert d.columns('sessions') == c
    t = ['subjects', 'sessions', 'visits', 'transcripts', 'utterances', 'log']
    assert d.tables == t

def test_total():
    '''Testing total method'''
    where = 'subject=38 and session=10 and c_mor like "%1S%"'
    assert d.total(where, table='utterances') == 14
    t = Transcript(38, 10)
    assert t.total('c_mor like "%1S%"') == 14

def test_subject():
    '''Testing Subject class'''
    subject = Subject()
    result = subject(22).__repr__()
    result.startswith("Row(control=0, sex=u'F'")
    assert subject.project(22) == 2
    assert subject.dob(22) == '2001-05-10'

def test_subj_constraint():
    '''Testing subject constraint method in Utterances class'''
    utts = Utterances()
    result = utts.subj_constraint(subjects=[22, 100])
    expect = 'subject in (22,100)'
    assert result == expect
    result = utts.subj_constraint(project=2)
    assert result.startswith('subject in (22,24,')
    result = utts.subj_constraint(project=3)
    assert result.startswith('subject in (30,32,')
