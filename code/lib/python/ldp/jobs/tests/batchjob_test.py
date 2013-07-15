import os
import ldp.jobs
from nose.tools import with_setup

job = None

def setup():
    '''Set up test fixtures'''
    tasks = {
        "alpha": {
            "suspect": "el",
            "suggestions": ["ol"],
            "units" : [{"id": "10", "value": "ten"},
                       {"id": "11", "value": "eleven"},
                       {"id": "12", "value": "twelve"},
                       {"id": "13", "value": "thirteen"}]
        },
        "beta": {
            "suspect": "ee",
            "suggestions": ["ii"],
            "units" : [{"id": "14", "value": "fourteen"},
                       {"id": "15", "value": "fifteen"}]
        }
    }
    global job
    job = ldp.jobs.BatchJob(1, tasks)

@with_setup(setup)
def test_init():
    '''Testing init method'''
    job.set_queue('alpha')
    assert job.queue.name == 'alpha', "current queue is alpha"
    assert job.queue.id(0) == '10', "get id of first element"
    assert job.queue.value(0) == 'ten', "get value of first element"
    assert job.queue.suspect(0) == 'el', "get suspect for first element"
    assert job.queue.suggestions(0) == ['ol'] 
    assert job.queue.SUSPECT == 'el', "get suspect for queue"
    assert job.queue.SUGGESTIONS == ['ol'], "get suggestions for queue"

@with_setup(setup)
def test_set_queue():
    '''Testing set_queue method'''
    job.set_queue('omits')
    assert job.queue.name == 'omits', "queue is now omits"
    job.set_queue('beta')
    assert job.queue.name == 'beta', "queue is now beta"

@with_setup(setup)
def test_set_value():
    '''Testing set_value method'''
    job.set_queue('alpha')
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
    job.set_queue('alpha')
    assert job.queue.tags(0) == [], "first item in queue has no tags"
    job.queue.tag('TEST', 0)
    assert job.queue.tags(0) == ['TEST'], "tag was added to first item"
    # assert job.TAGS == ['TEST'], "added to job tag list"

@with_setup(setup)
def test_modified():
    '''Testing modified property'''
    job.set_queue('alpha')
    assert job.modified == False
    job.queue.set_value('new', 0)
    assert job.modified == True

@with_setup(setup)
def test_set_queue():
    '''Testing set method for setting sub-jobs'''
    job.set_queue('beta')
    assert job.queue.name == "beta"
    assert job.queue.id(0) == '14', "get id of first element"
    assert job.queue.value(0) == 'fourteen', "get value of first element"
    assert job.queue.suspect(0) == 'ee', "get suspect for first element"
    assert job.queue.suggestions(0) == ['ii'] 
    job.set_queue('alpha') 
    assert job.queue.name == "alpha"
    assert job.queue.id(0) == '10', "get id of first element"
    assert job.queue.value(0) == 'ten', "get value of first element"
    assert job.queue.suspect(0) == 'el', "get suspect for first element"
    assert job.queue.suggestions(0) == ['ol'] 

@with_setup(setup)
def test_delete():
    '''Testing delete method'''
    job.set_queue('beta')
    assert job.queue.name == "beta", 'set sub-job to the one named "beta"'
    assert job.queue.id(0) == '14', "get id of first element"
    job.delete('beta')
    assert job.queue.name == "empty"
    assert job.queue.id(0) == None

@with_setup(setup)
def test_count():
    '''Testing count method'''
    assert job.count('alpha') == 4, "unit count is correct"
    assert job.count('beta') == 2, "unit count is correct"

@with_setup(setup)
def test_next():
    '''Testing next method'''
    assert job.next('alpha') == 'beta', 'name following "alpha" is "beta"'
    assert job.next('beta') == 'alpha', 'name following "beta" is "alpha"'

@with_setup(setup)
def test_list():
    '''Testing list property for listing sub-jobs'''
    assert job.list == [('alpha', 4), ('beta', 2)]
    job.set_queue('beta') # set sub-job to the one named "beta"
    assert len(job.queue) == 2
    job.queue.pop_to(job.omits)
    assert len(job.queue) == 0
    assert job.list == [('alpha', 4), ('beta', 0)]

@with_setup(setup)
def test_status():
    '''Testing status property'''
    job.set_queue("alpha")
    assert len(job.queue) == 4, "4 units in current queue"
    job.set_queue("beta")
    assert len(job.queue) == 2, "2 units in current queue"
    assert len(job.edits) == 0
    assert len(job.omits) == 0
    expected = '''  6 units\n  0 edits\n  0 omits'''
    assert job.status == expected
    job.set_queue("alpha")
    job.queue.pop_to(job.edits, 0, 1)
    assert len(job.queue) == 2
    assert len(job.edits) == 2
    assert len(job.omits) == 0
    expected = '''  4 units\n  2 edits\n  0 omits'''
    assert job.status == expected


# test creation and writing of batch job files


def write_setup():
    '''Set up test fixtures'''
    global batch
    batch = ldp.jobs.BatchJob(id=100, issue="spelling", notes=["A", "B"])

@with_setup(write_setup)
def test_set_dataset():
    '''Testing set_dataset method'''
    expected = {'table': 'utterances', 'environ': 'LDP_DB', 'version': [2, 77]}
    batch.set_dataset(table='utterances', version=[2, 77])
    assert batch.dataset == expected

@with_setup(write_setup)
def test_add_task():
    '''Testing add_task method'''
    expected = {
        'reck': {
            'units': [
                {
                    "id": 12223344444, 
                    "column": "p_utts", 
                    "value": "what a reck!",
                    "suspect": "reck",
                    "suggestions": ['wreck', 'rack', 'rock']
                }
            ], 
            'suspect': 'reck',
            'suggestions': ['wreck', 'rack', 'rock']
        }
    }
    units = [{"id": 12223344444, "column": "p_utts", "value": "what a reck!"}]
    batch.add_task("reck", units, suspect="reck", 
                                  suggestions=["wreck", "rack", "rock"])
    assert batch.tasks == expected
    expected = {
        'reck': {
            'units': [
                {
                    "id": 12223344444, 
                    "column": "p_utts", 
                    "value": "what a reck!",
                }
            ], 
        }
    }
    batch.add_task("reck", units)
    assert batch.tasks == expected

batchfile = None

def read_write_setup():
    '''Set up test fixtures'''
    b = ldp.jobs.BatchJob(id=100, issue="spelling", notes=["A", "B"])
    b.set_dataset(table='utterances', version=[2, 77])
    units = [
        {
            "id": 12223344444, 
            "column": "p_utts", 
            "value": "what a reck!"
        },
        {
            "id": 12223344445, 
            "column": "p_utts", 
            "value": "between a reck and a hard place."
        }
    ]
    b.add_task("reck", units, suspect="reck", 
                              suggestions=["wreck", "rack", "rock"])
    path = os.path.dirname(__file__)
    b.write(id=100, issue="spelling", file=path+'/jobfiles/temp.json')
    global batchfile
    batchfile = ldp.jobs.BatchJobFile(path + '/jobfiles/temp.json')

def read_write_teardown():
    '''Tear down test fixtures'''
    batchfile = None
    path = os.path.dirname(__file__)
    os.remove(path + '/jobfiles/temp.json')

@with_setup(setup=read_write_setup, teardown=read_write_teardown)
def test_write():
    '''Testing write method'''
    assert batchfile.id == 100
    assert batchfile.issue == "spelling"
    assert batchfile.notes == ["A", "B"]
    assert batchfile.name == 'temp'
    batchfile.set_queue("reck")
    assert len(batchfile.queue) == 2
    assert batchfile.queue.id(0) == 12223344444
    assert batchfile.queue.id(1) == 12223344445
    assert batchfile.queue.value(0) == "what a reck!"
    assert batchfile.queue.value(1) == "between a reck and a hard place."
    assert batchfile.queue.column(0) == "p_utts"
    assert batchfile.queue.column(1) == "p_utts"
    assert batchfile.queue.suspect(0) == "reck"
    assert batchfile.queue.suspect(1) == "reck"
    assert batchfile.queue.SUSPECT == "reck"
    assert batchfile.queue.suggestions(0) == [u'wreck', u'rack', u'rock']
    assert batchfile.queue.suggestions(1) == [u'wreck', u'rack', u'rock']
    assert batchfile.queue.SUGGESTIONS == [u'wreck', u'rack', u'rock']


@with_setup(setup=read_write_setup, teardown=read_write_teardown)
def test_save():
    '''Testing reading/writing'''
    units = [
        {
            "id": 12223344446, 
            "column": "p_utts", 
            "value": "leck this door."
        },
        {
            "id": 12223344447, 
            "column": "p_utts", 
            "value": "his leck of strength."
        }
    ]
    batchfile.add_task("leck", units, suspect="leck", 
                                      suggestions=["lock", "lack", "lick"])
    batchfile.set_queue("leck")
    assert len(batchfile.queue) == 2
    assert batchfile.queue.id(0) == 12223344446
    assert batchfile.queue.id(1) == 12223344447
    assert batchfile.queue.value(0) == "leck this door."
    assert batchfile.queue.value(1) == "his leck of strength."
    assert batchfile.queue.column(0) == "p_utts"
    assert batchfile.queue.column(1) == "p_utts"
    assert batchfile.queue.suspect(0) == "leck"
    assert batchfile.queue.suspect(1) == "leck"
    assert batchfile.queue.suggestions(0) == ["lock", "lack", "lick"]
    assert batchfile.queue.suggestions(1) == ["lock", "lack", "lick"]
    batchfile.notes = ['New note!']
    batchfile.save(commit=False)
    path = os.path.dirname(__file__)
    f = ldp.jobs.BatchJobFile(path + '/jobfiles/temp.json')
    assert f.notes == ['New note!']
    f.set_queue("leck")
    assert len(f.queue) == 2
    assert f.queue.id(0) == 12223344446
    assert f.queue.id(1) == 12223344447
    assert f.queue.value(0) == "leck this door."
    assert f.queue.value(1) == "his leck of strength."
    assert f.queue.column(0) == "p_utts"
    assert f.queue.column(1) == "p_utts"
    assert f.queue.suspect(0) == "leck"
    assert f.queue.suspect(1) == "leck"
    assert f.queue.suggestions(0) == ["lock", "lack", "lick"]


