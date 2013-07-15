from nose.tools import with_setup
from ldp.jobs.main import Unit

unit = {}

def setup():
    data = dict(id="12223344444", value="hello")
    global unit
    unit = Unit(table="utterances", column="p_utts", **data)

@with_setup(setup)
def test_init():
    '''Testing init method'''
    assert unit['table'] == "utterances"
    assert unit['id'] == "12223344444"
    assert unit['value'] == "hello"
    assert unit.table == "utterances"
    assert unit.id == "12223344444"
    assert unit.value == "hello"
    assert unit.modified == False

@with_setup(setup)
def test_value():
    '''Testing value property'''
    unit.value = "bye"
    assert unit.value == "bye"
    assert unit.prior_value == "hello"

@with_setup(setup)
def test_revert():
    '''Testing revert method'''
    unit.value = "goodbye"
    assert unit.value == "goodbye"
    assert unit.prior_value == "hello"
    assert unit.modified == True
    unit.revert()
    assert unit.value == "hello"
    assert unit.prior_value == "goodbye"
    assert unit.modified == False

@with_setup(setup)
def test_regex():
    '''Testing regex method'''
    unit.value = '00 @@ !!'
    assert unit.regex('^\d+', '11') == '11 @@ !!'
    assert unit.regex(' .. ', '_XX_') == '11_XX_!!'
    assert unit.regex('_..$', '_YY') == '11_XX_YY'

@with_setup(setup)
def test_replace():
    '''Testing replace method'''
    unit.value = 'goo good goo good'
    assert unit.replace('goo', 'foo') == 'foo good foo good'
    unit.value = 'goo good goo good'
    assert unit.replace('goo', 'foo', words_only=False) == 'foo food foo food'

@with_setup(setup)
def test_edit():
    '''Testing edit method'''
    unit.value = 'foo far'
    func = lambda x: x.replace('f', 'b')
    assert unit.edit(func) == 'boo bar'

@with_setup(setup)
def test_tags():
    '''Testing tag methods'''
    assert unit.tags == []
    unit.tag('FOO')
    assert unit.tags == ['FOO']
    unit.tag('BAR')
    assert unit.tags == ['FOO', 'BAR']
    del unit.tags
    assert unit.tags == []

@with_setup(setup)
def test_sql():
    '''Testing sql method'''
    unit.value = 'hello'
    expected = "UPDATE utterances SET p_utts='hello' WHERE id=12223344444;"
    assert unit.sql(table='utterances') == expected

def test_init_more():
    '''Testing init method again'''
    data = dict(id="1234", value="foo bar")
    unit = Unit(data, suspect="bar", suggestions=['baz'])
    assert unit.id == "1234"
    assert unit.suspect == "bar"
    assert unit.suggestions == ["baz"]
