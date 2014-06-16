from ldp.data import Utterances

verbose = False
utterances = Utterances()
visits = [x.rstrip().split('\t') for x in open('visits.txt')]

columns = 'id, time, row, c_utts, p_utts'

def stringify(args):
    return '\t'.join(str(x) for x in args)

for subj, sess in visits:
    print 'output/{}.{:0>2}.xls ...'.format(subj, sess)
    with open('output/{}.{:0>2}.xls'.format(subj, sess), 'w') as f:
        header = stringify(('_' + columns.upper()).split(', ')) + '\n'
        f.write(header)
        cond = 'subject={} and session={}'.format(subj, sess)
        for row in utterances(columns, cond, limit=''):
            if verbose: print stringify(row)
            f.write(stringify(row) + '\n')

