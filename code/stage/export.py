#!/usr/bin/env python 
import sys
from ldp.data import Utterances

TARGET_DIR = sys.argv[1]
Utterances(TARGET_DIR + '/data.db').show()
