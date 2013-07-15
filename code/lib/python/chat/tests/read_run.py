#!/usr/bin/env python

import os
from chat.file import Reader


file = Reader(os.path.dirname(__file__) + "/sample.cha")

for t in file.tiers: 
    print t

for rec in file.records: 
    print rec

for vals in file.values('syn'):
    print vals

for test, gold in zip(file.values('syn'), file.values('gld')): 
    print 'test:', test
    print 'gold:', gold
