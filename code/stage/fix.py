#!/usr/bin/env python 
'''
fix.py - lowercase firstword in utterance if it's a dictionary word.

'''
import os
import re
import sys
import nlp.lex
import nlp.words
from datastore.sqlite import sqlite

# set testing to False to commit changes
testing = False

TARGET_DIR = sys.argv[1]
db = sqlite(TARGET_DIR + '/data.db')

namefile = os.environ["LDP_LIB"] + '/python/nlp/words/names.txt'
names = nlp.words.WordList(namefile)
dictionary = nlp.words.WordList()
lem = nlp.lex.Lemmatizer()

for speaker in ['c', 'p']:

    column = '{0}_utts'.format(speaker)
    pattern = r'\W*[A-Z]'

    select_st = 'select id, {0} from utterances where {0} regexp "{1}";'
    update_st = 'update utterances set {0} = ? where id = ?;'.format(column)

    db.execute(select_st.format(column, pattern))

    firstword_pt = re.compile(r'\W*([A-Z]\w+)[\,\.\?\!\s]')

    updates = []

    for id, utt in db:
        m = firstword_pt.match(utt)
        if not m:
            continue
        word = m.group(1)
        if word in names:
            continue
        if lem.normalize(word.lower()) in dictionary:
            p = re.compile(r"{0}\b".format(word))
            fixed = p.sub(word.lower(), utt)
            updates.append((fixed, id))

    if testing:
        for u in updates: print u
    else:
        db.con.executemany(update_st, updates)
        db.commit()
