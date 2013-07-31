#!/usr/bin/env python 
'''
copy.py - copy utts column to utts_orig column.

'''
import sys
from datastore.sqlite import sqlite

TARGET_DIR = sys.argv[1]
db = sqlite(TARGET_DIR + '/data.db')

update_st = 'UPDATE utterances SET {0}_utts = {0}_utts_orig'
# update_st = 'UPDATE utterances SET {0}_utts_orig = {0}_utts'

for speaker in ['p', 'c']:
    db.execute(update_st.format(speaker))
    db.commit()
