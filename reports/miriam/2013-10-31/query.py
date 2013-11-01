from ldp.speech import Report

speech = Report()
speech.query('session in (8, 9)', project=2)
columns = 'subject session mlu'.split(' ')      # columns to print

def pprint(args):                               # pretty-print
    print "\t".join(str(i) for i in args)

pprint(c.upper() for c in columns)              # header

for subj, sess in sorted(speech.trans):         # iterate over transcript IDs
    row = speech.result(subj, sess, 'C')        # get child result
    pprint(row[i] for i in columns)             # pretty-print specified cols

