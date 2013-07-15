import os
from datastore.sqlite import sqlite, AttributeRowFactory


class Dataset(sqlite):
    '''Abstract base class for querying LDP dataset.'''

    table_name = None       # specify in subclass

    def __init__(self, path=None, **kw):
        path = path if path else os.environ['LDP_DB']
        super(Dataset, self).__init__(path, **kw)

    def __repr__(self):
        return 'LDP Dataset'

    def select(self, columns='*', where='', limit='', table=None):
        '''Select columns from table name of subclass.

        Return an iterator of rows.
        
        '''
        table = table if table else self.table_name
        if not table:
            msg = 'table_name attr must be set in subclass!'
            raise NotImplementedError(msg)
        return super(Dataset, self).select(table, columns, where, limit)

    def count(self, columns='', where='', limit='', table=None):
        '''Count records matching where clause, grouped by columns.'''
        table = table if table else self.table_name
        if columns:
            if where:
                where += ' group by ' + columns
            else:
                where = '1 group by ' + columns
            columns += ', count(*)'
        else:
            columns = 'count(*)'
        self.show(columns, where, limit)

    def total(self, where, **kw):
        '''Total rows matching where clause.'''
        return self.select('count(id)', where=where, **kw).fetchone()[0]

    def update(self, id, table=None, **kw):
        '''Update row id of table with remaining column/value args.'''
        table = table if table else self.table_name
        str_eq = '{0}="{1}"'    # wrap quotes around string values
        num_eq = '{0}={1}'
        map = []
        for column, value in kw.items():
            if type(value) is str:
                map.append(str_eq.format(column, value))
            else:
                map.append(num_eq.format(column, value))
        update_st = '''UPDATE {0} SET {1} WHERE id={2}'''
        update_st = update_st.format(table, ", ".join(map), id)
        return self.execute(update_st)


class Subjects(Dataset):
    '''Query subjects.'''

    table_name = 'subjects'

    def project(self, i):
        '''Return iterator with ids of subjects for specified project num.'''
        return (i[0] for i in self.select('id', where='project={0}'.format(i)))

    def at_session(self, i, project=None):
        '''Return iterator with ids of subjects visited at session.'''
        where = 'session={0} and completed=1'.format(i)
        if project:
             subjs = "subject in (select id from subjects where project={0})"
             where += " and " + subjs.format(project)
        return (i[0] for i in self.select('subject', where=where,
                                                     table='visits'))


class Subject(Dataset):
    '''Get info for a particular subject.'''

    table_name = 'subjects'

    def __getattr__(self, name):
        '''
        Return a function taking a single argument *id*.

        This allows one to access all column values for a particular 
        subject id as attributes.

        >>> subject = Subject()
        >>> subject(22)
        Row(control=0, ethn=u'N', lesion=u'', project=2, dob=u'2001-05-10', 
            sex=u'F', note=u'', race=u'WH', active=1, id=22)
        >>> subject.project(22)
        2
        >>> subject.dob(22)
        2001-05-10

        '''
        return lambda id: getattr(self(id), name)

    def __call__(self, id):
        self.row_factory(AttributeRowFactory)
        condition = 'id={0}'.format(id)
        self.select(where=condition)
        return self.fetchone()


class Transcripts(Dataset):
    '''Query transcript info.'''

    table_name = 'transcripts'

    def exists(self, subject, session):
        where = 'subject={0} and session={1}'.format(subject, session)
        return True if self.select('count(id)', where=where).fetchone()[0] \
                    else False


class Transcript(Dataset):
    '''Query utterances of a transcript.'''

    table_name = 'utterances'
    queued = False                 # set to True after executing a query

    def __init__(self, subject, session, dataset=None):
        self.subject = subject
        self.session = session
        super(Transcript, self).__init__(dataset)

    def __iter__(self):
        if self.queued:
            return self.cur
        else:
            self.row_factory(AttributeRowFactory)
            self.select()
            return self.cur

    def select(self, columns='*', where='', limit=''):
        '''Select columns from utterances table.'''
        self.queued = True
        t = "subject={0} and session={1}".format(self.subject, self.session)
        if where:
            if 'subject' in where or 'session' in where:
                msg = "Do not include subject or session parameters!"
                raise ValueError(msg)
            where = '{0} and {1}'.format(t, where)
        else:
            where = t
        return super(Transcript, self).select(columns, where, 
                                              limit, 'utterances')


class Utterances(Dataset):
    '''Query utterances.'''

    table_name = 'utterances'

    def subj_constraint(self, project='', subjects=[]):
        '''Return subject constraint for utterance selection.
        
        The subject constraint is a formatted string for a sql select
        statement's where clause.  It constrains the selection to utterances
        by the specified subjects or the subjects of the specified project (2
        or 3).

        '''
        if project:
            subjects = [str(x) for x in Subjects().project(project)]
        elif subjects:
            subjects = [str(x) for x in subjects]
        if subjects:
            return 'subject in ({0})'.format(','.join(subjects))

    def select(self, columns='*', where='', limit='', project='', subjects=[]):
        '''Select columns from table name of subclass.'''
        constraint = self.subj_constraint(project, subjects) 
        where = " and ".join(x for x in (where, constraint) if x)
        return super(Utterances, self).select(columns, where, limit)

    def match(self, pattern, columns='p_utts, c_utts', where='', limit=''):
        '''Select utterances matching pattern.'''
        p = r"p_utts regexp '{0}' or c_utts regexp '{0}'".format(pattern)
        if where:
            where = '{0} and {1}'.format(p, where)
        else:
            where = p
        return self.select(columns, where, limit)

    def contains(self, pattern, *args, **kwargs):
        '''Select utterances containing pattern.'''
        pattern = r'.*{0}'.format(pattern)
        return self.match(pattern, *args, **kwargs)

    def context(self, id, window=5, columns='p_utts, c_utts, context'):
        '''Show context of utterance id.'''
        lo = id - window
        hi = id + window
        constraints = 'id > {0} and id < {1}'.format(lo, hi)
        return self.select(columns, where=constraints)


if __name__ == '__main__':

    subject = Subject()
    print subject(22)
    print subject.project(22)
    print subject.dob(22)

    utts = Utterances()
    utts.show('subject, session, row, p_mor', 'session < 2', limit=5,
              subjects=[24, 33])

    '''
    utts = Utterances()
    for u in utts.context(10290900403):
        print u

    for row in Transcript(22, 10):
        print row.subject, row.session, row.c_utts
        print row.values('subject, session, c_utts')

    trans = Transcript(22, 10)
    print
    print 'Count of all c_g_type values:'
    trans.count('c_g_type')
    print
    print 'Count of all c_g_type values where child utt starts with "h":'
    trans.count('c_g_type', where='c_utts like "h%"')
    print
    print 'Count of all rows where child utt starts with "h":'
    trans.count(where='c_utts like "h%"')
    print 'Ditto:'
    print
    print trans.total('c_utts like "h%"')

    utts = Utterances()
    utts.count('subject, session', where='subject=22 and session=10')

    trans = Transcript(22, 10)
    trans.show('subject, session, c_utts', 10)

    for subj, sess, utt in trans.select('subject, session, c_utts', 10):
        print subj, sess, utt

    for row in Transcript(22, 10):
        print row.subject, row.session, row.c_utts

    for row in Transcript(22, 10):
        print row.values('subject, session, c_utts')

    subjects = Subjects()
    for i in subjects.at_session(1, project=2): print i

    utts = Utterances()
    utts.show('subject, session, row, p_mor', 'session > 8', limit=5)

    for u in utts.contains(r'---', columns='subject, session', limit=1):
        print u
    
    '''
