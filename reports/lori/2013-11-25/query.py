import re
from datetime import time
from ldp import Utterances
from nlp import Words, Tokenizer

hmmss = re.compile('\d:\d\d:\d\d$')
hhmmss = re.compile('\d\d:\d\d:\d\d$')
decimal = re.compile('0\.\d+$')
number = re.compile('\d')
subjects = ','.join(row.rstrip() for row in open('subjects.txt'))
words = Words('words.txt')
tokens = Tokenizer()
utterances = Utterances()

COLUMNS = 'subject, session, time, c_utts, context'
WHERE = '''
    c_utts != "" and
    session > 3 and 
    session < 10 and 
    subject in ({})
    '''.format(subjects)

def convert_time(x):
    '''
    Convert a string containing a decimal time representation from 
    excel to hours, minutes, and seconds.  Return the resulting 
    `datetime` object as a string (`hh:mm:ss`).

    '''
    x = int(float(x) * 24 * 3600) 
    return time(x//3600, (x%3600)//60, x%60).strftime("%H:%M:%S")

def fix_time(t):
    '''
    Convert various strings in various time formats to 
    canoninical form (`hh:mm:ss`) for comparison.

    '''
    if hmmss.match(t):
        return '0' + t
    elif hhmmss.match(t):
        return t
    elif decimal.match(t):
        return convert_time(t)
    else:
        return ''

def make_cond(start, stop, prev=None):
    cond = lambda time: time >= start and time <= stop
    if prev:
        return lambda time: cond(time) or prev(time)
    else:
        return cond
        
ranges = {}
for row in open('times.tsv'):
    if not number.match(row): continue  # skip header
    [subj, sess, start, stop] = row.rstrip().split('\t')
    id = int(subj), int(sess)
    start, stop = fix_time(start), fix_time(stop)
    if ranges.has_key(id):
        prev = ranges[id]
        ranges[id] = make_cond(start, stop, prev)
    else:
        ranges[id] = make_cond(start, stop)

def in_window(subj, sess, time): 
    id = (subj, sess)
    if ranges.has_key(id): return ranges[id](time) 

def pprint(*args):
    print "\t".join(str(x) for x in args)

pprint(*'SUBJECT SESSION TIME CONTEXT UTT MATCHES MATCHED'.split())
def run(limit=''):
    prev_time = '00:00:00'
    prev_id = (24, 4)
    for row in utterances(COLUMNS, WHERE, limit=limit): 
        subj, sess, time, utt, cxt = row
        if not time and prev_id == (subj, sess): time = prev_time
        if in_window(subj, sess, time):
            matched = [t for t in tokens(utt) if t in words]
            matches = len(matched)
            MATCHED = ", ".join(matched)
            if matches: 
                pprint(subj, sess, time, utt, cxt, matches, MATCHED)
        prev_time = time
        prev_id = (subj, sess)

def time_tests():
    assert fix_time('1:00:00') == '01:00:00'
    assert fix_time('01:00:00') == '01:00:00'
    assert fix_time('0.001') == '00:01:26'
    assert in_window(24, 5, '01:12:20'), "is true"
    assert in_window(24, 5, '00:12:20'), "is true"
    assert in_window(24, 4, '00:01:20'), "is true"


if __name__ == '__main__':

    run()
