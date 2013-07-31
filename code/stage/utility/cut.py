#!/usr/bin/env python 

'''
cut.py -- cut specified columns from a TSV-formatted file.

Assumes the file contains a header line containing column names, 
of which the columns to be cut are subset.

Modify the columns variable below.

'''
import sys
from datastore.table import Reader

transcripts = sys.argv[1:]
columns = '''id subject session row time line key 
             p_utts_orig p_utts p_form p_lrb p_obj p_gloss p_orient p_mspd 
             c_utts_orig c_utts c_form c_lrb c_obj c_gloss c_orient c_mspd 
             context'''.split()

def pprint(values): print "\t".join(values)

pprint(columns)

for t in transcripts:
    T = Reader(t)
    for row in T.values(*columns): 
        pprint(row)
