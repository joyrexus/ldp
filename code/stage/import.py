#!/usr/bin/env python
'''
import.py - import TSV-formatted transcript files into a sqlite db.

Assumes database has already been created and contains a table named
*utterances* with the set of columns specified in the schema for the 
standard LDP dataset.

'''
import sys
from datastore.sqlite import sqlite

TARGET_DIR = sys.argv[1]

db = sqlite(TARGET_DIR + '/data.db')
db.batch_insert(TARGET_DIR + '/utterances.tsv', 
                table='utterances',
                preview=False)
db.commit()
db.close()
