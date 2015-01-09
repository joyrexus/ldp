#!/usr/bin/env python 
'''
Generate a unique primary key ID based on a combination of 
subject, session, and row (optionally) IDs.

'''
import sys

class PrimaryKey(object):
    '''
    Generate a unique primary key ID based on a combination of 
    subject, session, and row (optionally) IDs.

    '''
    def _pad(self, value, n):
        '''Pad `value` with zeros to make an n-character string.'''
        return str(value).rjust(n, '0')

    def __call__(self, subject, session, row=None):
        '''
        Return an 11-digit unique primary key value based on subject 
        + session + row.
    
        The `row` argument is optional.  If not given, a 6-digit 
        primary key for a transcript/visit is generated based on 
        the subject and session IDs given.

        >>> pk = PrimaryKey()
        >>> pk(subject=2, session=3, row=4)
        10020300004
        >>> pk(subject=222, session=33, row=4444)
        12223304444

        '''
        SUBJ = self._pad(subject, 3)
        SESS = self._pad(session, 2)
        ROW = self._pad(row, 5) if row else ''
        return int(''.join(['1', SUBJ, SESS, ROW]))

    def convert(self, filename):
        '''
        Given the name of a file containing subject and session 
        (and optionally row) IDs in the first 2 (or 3) columns,
        parse each line, add a unique ID column (as the first column) 
        and print the result.

        '''
        for row in open(filename):
            subj, sess = row.split('\t')[0:2]
            if subj.isdigit():
                print self.__call__(subj, sess) + "\t" + row.rstrip()
            else:
                print "id\t" + row.rstrip()


if __name__ == '__main__':

    pk = PrimaryKey()
    # args = sys.argv[1:]
    # print pk(*args)
    assert pk(subject=22, session=33, row=44) == 10223300044
    assert pk(subject=22, session="33", row=44) == 10223300044

