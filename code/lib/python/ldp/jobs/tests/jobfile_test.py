import os
from datetime import datetime
from nose.tools import with_setup
from ldp.jobs import JobFile

job = None

def setup():
    '''Set up test fixtures.'''
    path = os.path.dirname(__file__) + '/jobfiles/times.json'
    global job
    job = JobFile(path)

@with_setup(setup)
def test_init():
    '''Testing init method'''
    assert job.id == 1
    expected = 'Convert conventionally transcribed time formats ' + \
               'to our transcription standard.'
    assert job.notes == [expected]
    job.units.value(0) == '8:30?'

@with_setup(setup)
def test_info():
    '''Testing info property'''
    assert job.info.startswith('      ID  1')

@with_setup(setup)
def test_tagging():
    '''Testing tagging methods'''
    assert job.units.tags(0) == [], "first item in units has no tags"
    job.units.tag('FOO', 0)
    assert job.units.tags(0) == ['FOO'], "tag was added to first item"
    assert job.TAGS == ['FOO'], "added to job tag list"
    job.units.pop_to(job.edits, 1)
    job.edits.tag('BAR', 0)
    assert job.edits.tags(0) == ['BAR'], "tag was added to first item"
    assert job.TAGS == ['BAR', 'FOO'], "both tags added to job"

@with_setup(setup)
def test_modified():
    '''Testing modified attribute.'''
    assert job.modified == False
    job.queue.set_value('new', 0)
    assert job.modified == True

@with_setup(setup)
def test_queues():
    '''Testing queue attributes'''
    assert len(job.units) == 15
    assert len(job.edits) == 0
    job.units.pop_to(job.edits, 0, 1, 2)
    assert len(job.units) == 12
    assert len(job.edits) == 3

@with_setup(setup)
def test_notes():
    '''Testing notes attribute'''
    first = 'Convert conventionally transcribed time formats ' + \
            'to our transcription standard.'
    expected = [first]
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
    assert len(job.units) == 15
    assert len(job.edits) == 0
    job.units.pop_to(job.edits, 0, 1, 2)
    assert len(job.units) == 12
    assert len(job.edits) == 3
    temp = os.path.dirname(__file__) + '/jobfiles/temp.json'
    job.save(temp)
    job2 = JobFile(temp)
    assert len(job2.units) == 12
    assert len(job2.edits) == 3
    first = 'Convert conventionally transcribed time formats ' + \
            'to our transcription standard.'
    expected = [first]
    assert job2.notes == expected
    second = 'New note'
    expected.append(second)
    job2.notes.append(second)
    job2.save(temp)
    job3 = JobFile(temp)
    assert job3.notes == expected
    os.remove(temp)

@with_setup(setup)
def test_sql_updates():
    '''Testing sql_updates method'''
    sql_a = "UPDATE utterances SET p_utts='09:05.' WHERE id=10300600667;\n"
    sql_b = "UPDATE utterances SET p_utts='8:30?' WHERE id=10290900403;\n"
    expected = "BEGIN TRANSACTION;\n{0}{1}COMMIT;\n".format(sql_a, sql_b)
    job.units.pop_to(job.edits, 0, 1)
    print job.sql_updates()
    print expected
    assert job.sql_updates() == expected

