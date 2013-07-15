import os
from datetime import datetime
from nose.tools import with_setup
from ldp.jobs import BatchJobFile

job = None

def setup():
    '''Set up test fixtures'''
    path = os.path.dirname(__file__) + '/jobfiles/spelling.json'
    global job
    job = BatchJobFile(path)

@with_setup(setup)
def test_init():
    '''Testing init method'''
    job.set_queue('aachoo')
    assert job.id == 2
    expected = "Correct spelling errors to conform to standard " + \
               "dictionary spellings and transcription conventions."
    assert job.notes == [expected]
    job.units.id(0) == "10280900951"
    job.units.value(0) == "oh aachoo."
    job.queue.id(0) == "10280900951"
    job.queue.value(0) == "oh aachoo."
    job.queue.suspect(0) == "aachoo"
    job.queue.suggestions(0) == ["achoo"]

@with_setup(setup)
def test_info():
    '''Testing info property'''
    assert job.info.startswith('      ID  2')

@with_setup(setup)
def test_tagging():
    'Testing tagging methods'
    job.set_queue("allright")
    assert job.queue.tags(0) == [], "first item in units has no tags"
    job.queue.tag('TEST', 0)
    assert job.queue.tags(0) == ['TEST'], "tag was added to first item"
    assert job.TAGS == ['TEST'], "added to job tag list"
    job.units.pop_to(job.edits, 1)
    job.edits.tag('TEST2', 0)
    assert job.edits.tags(0) == ['TEST2'], "tag was added to first item"
    assert job.TAGS == ['TEST', 'TEST2'], "both tags added to job"
    job.set_queue("aachoo")
    assert job.TAGS == ['TEST2'], "do not show tags associated w/ prev job"

@with_setup(setup)
def test_modified():
    '''Testing modified attribute.'''
    job.set_queue("allright")
    assert job.modified == False
    job.queue.set_value('new', 0)
    assert job.modified == True

@with_setup(setup)
def test_queues():
    '''Testing queue attributes'''
    job.set_queue("allright")
    assert len(job.queue) == 184
    assert len(job.edits) == 0
    job.queue.pop_to(job.edits, 0, 1, 2)
    assert len(job.queue) == 181
    assert len(job.edits) == 3
    job.set_queue("aachoo")
    assert len(job.queue) == 1
    assert len(job.edits) == 3
    job.queue.pop_to(job.edits)
    assert len(job.queue) == 0
    assert len(job.edits) == 4

@with_setup(setup)
def test_notes():
    '''Testing notes attribute'''
    first = 'Correct spelling errors to conform to standard dictionary ' + \
            'spellings and transcription conventions.'
    expected = [first]
    print job.notes
    assert job.notes == expected
    second = 'New note!'
    expected.append(second)
    job.notes.append(second)
    assert job.notes == expected

@with_setup(setup)
def test_stamp():
    '''Testing stamp method'''
    date = datetime.now().isoformat(' ').split()[0]
    job.stamp()
    assert job.editors[-1]['date'].startswith(date)
    assert job.editors[-1]['name'] == os.environ['USER']

@with_setup(setup)
def test_save():
    '''Testing save method'''
    job.set_queue("allright")
    assert job.queue.SUSPECT == "allright"
    assert job.queue.SUGGESTIONS == ["alright"]
    assert len(job.queue) == 184
    assert len(job.edits) == 0
    job.queue.pop_to(job.edits, 0, 1, 2)
    assert len(job.queue) == 181
    assert len(job.edits) == 3
    job.edits.tag('TEST', 0)
    temp = os.path.dirname(__file__) + '/jobfiles/temp.json'
    job.save(temp)
    newjob = BatchJobFile(temp)
    newjob.set_queue("allright")
    assert newjob.queue.SUSPECT == "allright"
    assert newjob.queue.SUGGESTIONS == ["alright"]
    assert len(newjob.queue) == 181
    assert len(newjob.edits) == 3
    newjob.edits.tags(0) == 'TEST'
    os.remove(temp)

@with_setup(setup)
def test_sql_updates():
    '''Testing sql_updates method'''
    expected = "BEGIN TRANSACTION;\n" \
             + "UPDATE utterances SET p_utts='allright Makayla.' " \
             + "WHERE id=10590600663;\nCOMMIT;\n"
    job.set_queue("allright")
    job.units.pop_to(job.edits, 0)
    print job.sql_updates()
    print expected
    assert job.sql_updates() == expected
