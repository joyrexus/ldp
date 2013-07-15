from nose.tools import with_setup
from ldp.jobs.main import Units

units = None

def setup():
    '''Set up test fixtures'''
    data = [{"id": "10", "value": "ten", "column": "p_utts"},
            {"id": "11", "value": "eleven", "column": "p_utts"},
            {"id": "12", "value": "twelve", "column": "p_utts"},
            {"id": "13", "value": "thirteen", "column": "p_utts"}]
    global units
    units = Units('units', data)

@with_setup(setup)
def test_init():
    '''Testing init and accessor methods'''
    assert units.id(0) == "10"
    assert units.value(0) == "ten"
    assert units.id(1) == "11"
    assert units.value(1) == "eleven"

@with_setup(setup)
def test_set_value():
    '''Testing set_value method'''
    assert units.value(0) == "ten"
    assert units.value(1) == "eleven"
    units.set_value('number', 0, 1)
    assert units.value(0) == "number"
    assert units.value(1) == "number"
    units.revert(0, 1)
    assert units.value(0) == "ten"
    assert units.value(1) == "eleven"

@with_setup(setup)
def test_pop_to():
    '''Testing pop_to method'''
    assert units.id(0) == "10"
    assert units.value(0) == "ten"
    assert units.id(1) == "11"
    assert units.value(1) == "eleven"
    omits = Units('omits')
    assert len(units) == 4
    assert len(omits) == 0
    units.pop_to(omits, 0, 1)
    assert omits.id(0) == "11"
    assert omits.value(0) == "eleven"
    assert omits.id(1) == "10"
    assert omits.value(1) == "ten"
    assert len(units) == 2
    assert len(omits) == 2

@with_setup(setup)
def test_replace():
    '''Testing replace method'''
    assert units.modified(0) == False
    assert units.modified(1) == False
    units.replace('ten', 'tin', 0, 1)
    assert units.value(0) == "tin"
    assert units.prior_value(0) == "ten"
    assert units.modified(0) == True
    assert units.value(1) == "eleven"
    assert units.prior_value(1) == None
    assert units.modified(1) == False

@with_setup(setup)
def test_regex():
    '''Testing regex method'''
    assert units.modified(0) == False
    assert units.modified(1) == False
    units.regex('\we', '_e', 0, 1)
    assert units.value(0) == "_en"
    assert units.value(1) == "e_e_en"
    units.revert(0, 1)
    assert units.value(0) == "ten"
    assert units.value(1) == "eleven"

@with_setup(setup)
def test_revert():
    '''Testing revert method'''
    assert units.modified(0) == False
    assert units.modified(1) == False
    units.replace('ten', 'tin', 0, 1)
    assert units.value(0) == "tin"
    assert units.value(1) == "eleven"
    units.revert(0, 1)
    assert units.value(0) == "ten"
    assert units.value(1) == "eleven"

@with_setup(setup)
def test_edit():
    '''Testing edit method'''
    func = lambda x: x.upper()
    units.edit(func, 0, 1)
    assert units.value(0) == "TEN"
    assert units.value(1) == "ELEVEN"
    units.revert(0, 1)
    assert units.value(0) == "ten"
    assert units.value(1) == "eleven"

@with_setup(setup)
def test_tags():
    '''Testing tag method'''
    assert units.tags(0) == []
    assert units.tags(1) == []
    units.tag('FOO', 0, 1)
    assert units.tags(0) == ['FOO']
    assert units.tags(1) == ['FOO']
    units.tag('BAR', 0, 1)
    units.tag('BAZ', 1)
    assert units.tags(0) == ['FOO', 'BAR']
    assert units.tags(1) == ['FOO', 'BAR', 'BAZ']
    assert units.TAGS == set(['BAR', 'BAZ', 'FOO']), "all tags returned"
    units.untag(0, 1)
    print units.tags(0)
    assert units.tags(0) == []
    assert units.tags(1) == []

def test_sql():
    '''Testing sql method'''
    print units.sql(table='utterances')
    updates = ["UPDATE utterances SET p_utts='ten' WHERE id=10;",
               "UPDATE utterances SET p_utts='eleven' WHERE id=11;",
               "UPDATE utterances SET p_utts='twelve' WHERE id=12;",
               "UPDATE utterances SET p_utts='thirteen' WHERE id=13;"]
    expected = "\n".join(updates) + "\n"
    assert units.sql(table='utterances') == expected

@with_setup(setup)
def test_modified():
    '''Testing modified attribute'''
    assert units.MODIFIED == False
    assert units.modified(0) == False
    units.set_value('number', 0, 1)
    assert units.modified(0) == True
    assert units.MODIFIED == True

def test_getattr():
    '''Testing getattr method'''
    data = [{"id": "10", "value": "ten", "suspect": "bar"},
            {"id": "11", "value": "eleven", "suspect": "bar"},
            {"id": "12", "value": "twelve", "suspect": "bar"},
            {"id": "13", "value": "thirteen", "suspect": "bar"}]
    units = Units('units', data)
    assert units.id(0) == "10"
    assert units.value(0) == "ten"
    assert units.suspect(0) == "bar"
    assert units.id(1) == "11"
    assert units.value(1) == "eleven"
    assert units.suspect(1) == "bar"
