import re
import time
import datastore.table
from signal import signal, SIGPIPE, SIG_DFL

signal(SIGPIPE,SIG_DFL) # ignore SIG_PIPE and don't throw exceptions on it


class Transcript(datastore.table.Reader):
    """
    Use this class to convert incoming transcript TSV files into canonical
    transcripts that can be inserted into the LDP Dataset.

    """
    def __init__(self, path):
        file = path.split('/')[-1]
        subj, sess = file.split('.')[0:2]
        match = re.search(r'[1-9]\d?', sess)    # extract sess num
        self.subj = int(subj)
        self.sess = int(match.group())
        super(Transcript, self).__init__(path)

    def header(self):
        new = ['id', 'subject', 'session', 'row', 'last_update']
        cols = [self._fix(c) for c in self.columns]
        return new + cols

    def _fix(self, col):
        '''Fix column names if based on old schema.'''
        col = re.sub(r'utts$', 'utts_orig', col)
        return col.replace('_clean', '')

    def _pad(self, value, n):
        '''Pad value with n zeroes.'''
        return str(value).rjust(n, '0')

    def _pk(self, subj, sess, row):
        '''Return unique primary key value based on subject + session + row.'''
        SUBJ = self._pad(subj, 3)
        SESS = self._pad(sess, 2)
        ROW = self._pad(row, 5)
        return ''.join(['1', SUBJ, SESS, ROW])

    def __iter__(self):
        '''Yield prefixed row values with current update time.'''
        row = 0
        now = time.strftime("%x %X").replace('/', '-')
        for v in self.values():
            row += 1
            id = self._pk(self.subj, self.sess, row)
            yield [id, self.subj, self.sess, row, now] + list(v)


if __name__ == '__main__':

    header = True                           # print column header?

    files = sys.argv[1:]
    for f in files:
        t = Transcript(f)
        if header: 
            print "\t".join(t.header())
            header = False                  # only print header once
        for row in t: 
            print "\t".join(str(x) for x in row)
