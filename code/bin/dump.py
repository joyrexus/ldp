#!/usr/bin/env python
'''Use this script to dump chat files from the LDP dataset.'''

from util.argparse import ArgumentParser
from chat.file import Writer
from ldp.data import Transcript

p = ArgumentParser(description=__doc__)
p.add_argument('--subject', type=int, required=True, help='Subject ID')
p.add_argument('--session', type=int, required=True, help='Session ID')
p.add_argument('--out', help='output file')
p.add_argument('dataset', nargs='?', help='sqlite dataset to use instead of default')
args = p.parse_args()

w = Writer(args.out)
t = Transcript(args.subject, args.session, dataset=args.dataset)

rows = t.select('id, row, key, p_utts, c_utts')
w.write(rows)
