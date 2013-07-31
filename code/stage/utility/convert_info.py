#!/usr/bin/env python 
'''
convert.py - convert (subject, session) values to a unique ID.

This is a simple script for converting a TSV file containing info to update the
LDP dataset's `transcripts` table.

The input file is expected to have its first two columns be `subject` and
`session`.  It generates a unique ID based on the (subject, session) values in
those columns and replaces those values with the resulting ID:

    (subject, session) -> id
    (22, 7)            -> 102207

The resulting output can be used to generate a TSV-file compatible with our
`tsv2sql` utility -- i.e., you can convert a TSV-file to a sql update or insert
file.

Input column format:

    subject session ...

Output column format:

    id ...

'''
import sys
from ldp.util import PrimaryKey

pk = PrimaryKey()

def pprint(*args):
    print "\t".join(str(x) for x in args)

for line in open(sys.argv[1]):
    subj, sess = line.split("\t")[:2]
    cols = line.rstrip().split("\t")[2:]
    if subj.startswith('subj'): 
        pprint('id', *cols)
        continue
    id = pk(subj, sess)
    pprint(id, *cols)

