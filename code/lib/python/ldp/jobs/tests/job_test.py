from nose.tools import with_setup
from ldp.jobs import Job

job = None

def setup():
    '''Set up test fixtures'''
    data = [{"id": "10", "value": "ten"},
            {"id": "11", "value": "eleven"},
            {"id": "12", "value": "twelve"},
            {"id": "13", "value": "thirteen"}]
    global job
    job = Job(id=1, units=data)

@with_setup(setup)
def test_init():
    '''Testing init method'''
    assert job.queue.name == 'units', "default queue is units"

@with_setup(setup)
def test_set_queue():
    '''Testing set_queue method'''
    job.set_queue('omits')
    assert job.queue.name == 'omits', "queue is now omits"
    job.set_queue('units')
    assert job.queue.name == 'units', "queue is now units"

@with_setup(setup)
def test_set_value():
    '''Testing set_value method'''
    assert job.queue.id(0) == "10"
    assert job.queue.value(0) == "ten"
    assert job.queue.id(1) == "11"
    assert job.queue.value(1) == "eleven"
    job.queue.set_value('number', 0, 1)
    assert job.queue.value(0) == "number"
    assert job.queue.value(1) == "number"

@with_setup(setup)
def test_tagging():
    '''Testing tagging methods'''
    assert job.units.tags(0) == [], "first item in units has no tags"
    job.units.tag('FOO', 0)
    assert job.units.tags(0) == ['FOO'], "tag was added to first item"
    assert job.units.TAGS == set(['FOO']), "added to units tag list"
    assert job.TAGS == ['FOO'], "added to job tag list"
    job.units.tag('BAR', 1)
    assert job.units.tags(1) == ['BAR'], "tag was added to first item"
    print job.units.TAGS
    assert job.units.TAGS == set(['BAR', 'FOO']), "added to units tag list"
    assert job.TAGS == ['BAR', 'FOO'], "added to job tag list"

@with_setup(setup)
def test_modified():
    '''Testing modified property'''
    assert job.modified == False
    job.queue.set_value('new', 0)
    assert job.modified == True

@with_setup(setup)
def test_status():
    '''Testing status property'''
    assert len(job.units) == 4
    assert len(job.edits) == 0
    assert len(job.omits) == 0
    expected = '''  4 units\n  0 edits\n  0 omits'''
    assert job.status == expected
    job.units.pop_to(job.edits, 0, 1)
    assert len(job.units) == 2
    assert len(job.edits) == 2
    assert len(job.omits) == 0
    expected = '''  2 units\n  2 edits\n  0 omits'''
    assert job.status == expected
