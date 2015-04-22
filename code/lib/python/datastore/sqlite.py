'''
datastore.sqlite - a sqlite3 wrapper.

'''
import os
import re
import sqlite3
from datastore.table import Reader


class AttributeRowFactory(object):
    '''
    Use this in place of default `sqlite.Row` factory for various
    conveniences (albeit expensive).
    
        >>> db = sqlite(os.environ['DB'], row_factory=AttributeRowFactory)
        >>> for subj in db('subjects', limit=1):
        ...     print subj.values("id", "dob", "sex")
        [22, u'2001-05-10', u'F']
        >>> for subj in db('subjects', limit=1):
        ...     print subj.dob
        '2001-05-10'

    '''
    def __init__(self, *args): self(*args)

    def __call__(self, cursor, row):
        d = dict((col[0], row[i]) for i, col in enumerate(cursor.description))
        self.__dict__.update(d)
        return self

    def __repr__(self):
        args = ['{0}={1}'.format(k, repr(v)) for k, v in self.__dict__.items()]
        return 'Row({0})'.format(', '.join(args))

    def __getitem__(self, i):
        if type(i) is int:
            return self.__dict__.items()[i]
        else:
            return self.__getattribute__(i)

    def __iter__(self):
        return self.__dict__.iteritems()

    def values(self, *columns):
        '''
        Return a list of values for column names in row.

        >>> db = sqlite(os.environ['DB'], row_factory=AttributeRowFactory)
        >>> for subj in db('subjects', limit=1):
        ...     print subj.values("id", "dob", "sex")
        [22, u'2001-05-10', u'F']

        '''
        return [self.__getattribute__(col) for col in columns]


class sqlite(object):
    '''
    A simple sqlite3 wrapper.
    
    '''
    def __init__(self, path=':memory:', row_factory=sqlite3.Row):
        con = sqlite3.connect(path)
        con.row_factory = row_factory
        con.text_factory = lambda x: unicode(x, "utf-8", "ignore")
        con.create_function("regexp", 2, self.regexp)
        self.con = con
        self.cur = self.con.cursor()
        q = 'select name from sqlite_master where type="table"'
        if row_factory is AttributeRowFactory:
            self.tables = [i.name for i in con.execute(q)]
        else:
            self.tables = [i[0] for i in con.execute(q)]
        self.path = path

    def row_factory(self, factory):
        '''Change row factory default from sqlite.Row.'''
        self.cur.row_factory = factory

    def execute(self, *args):
        self.cur.execute(*args)

    def commit(self):
        '''Commit any changes.'''
        self.con.commit()

    def close(self):
        '''Close the cursor and connection.'''
        self.cur.close()
        self.con.close()

    def __iter__(self):
        '''Iterator that yields rows in cursor.'''
        return self.cur

    def __call__(self, table, *args, **kwargs):
        '''Yield row from table.'''
        self.select(table, *args, **kwargs)
        return self

    def regexp(self, expr, item):
        '''Create the function "regexp" for the REGEXP operator of sqlite'''
        r = re.compile(str(expr))
        return item and r.match(item) is not None

    def select(self, table, columns='*', where='', limit=''):
        '''Select columns from table with constraints.'''
        if where:
            where = ' where {0}'.format(where)
        if limit:
            limit = ' limit {0}'.format(limit)
        q = 'select {0} from {1}'.format(columns, table) + where + limit
        self.cur.execute(q)
        return self

    def fetchone(self):
        '''Return first row in cursor.'''
        return self.cur.fetchone()

    def encode(self, i):
        '''Encode input as byte string or utf-8 for printing.'''
        try:
            return str(i)
        except UnicodeEncodeError:
            return i.encode('utf-8', 'replace')

    def pprint(self, separator="\t", header=True):
        '''Pretty-print rows in cursor.'''
        if header:
            print separator.join([i[0] for i in self.cur.description])
        for row in self.cur:
            print separator.join(self.encode(i) for i in row)

    def show(self, *args, **kwargs):
        '''Pretty-print columns from table with constraints.'''
        self.select(*args, **kwargs)
        self.pprint()

    def columns(self, table=None):
        if table is None: 
            table = self.table_name
        self.execute('select * from {0} limit 1'.format(table))
        return [i[0] for i in self.cur.description]

    def schema(self):
        '''Return dict with tables as keys and columns as values.'''
        if not self.tables:
            q = 'select name from sqlite_master where type="table"'
            self.tables = [i[0] for i in self.con.execute(q)]
        schema = {}
        for t in self.tables:
            schema[t] = self.columns(t)
        return schema

    def _format(self, value):
        '''Return string values with surrounding quotes.'''
        if value is None:
            return 'NULL'
        elif type(value) in (str, unicode):
            return '"{0}"'.format(value)
        elif type(value) in (int, float, long, bool):
            return "{0}".format(value)
        else:
            return value

    def valid_table(self, table):
        '''Raise exception if table is not a valid table name.'''
        if table not in self.tables:
            msg = '"{0}" is not a table in this database!'.format(table)
            raise NameError(msg)
        return True

    def valid_column(self, column, table):
        '''Raise exception if column is not a valid column name in table.'''
        if column not in self.columns(table):
            msg = '"{0}" is not a column in {1}!'.format(column, table)
            raise NameError(msg)
        return True

    def insert(self, table, preview=False, **kw):
        '''Insert into table the keyword column/value pairs.'''
        self.valid_table(table)
        columns = kw.keys()
        for col in columns: 
            self.valid_column(col, table)
        cols = ', '.join(columns)
        vals = ', '.join(self._format(i) for i in kw.values())
        q = 'INSERT INTO {0} ({1}) VALUES ({2})'.format(table, cols, vals)
        if preview:
            return q
        else:
            return self.con.execute(q)

    def batch_insert(self, filename, table, preview=False):
        '''
        Batch insert column values from filename into table.

        If *preview* is True, print the sql statement that will be used 
        for inserting and the table of values from *filename*
        
        *filename* should be a TSV file with a column header line with 
        column names corresponding to the column names in the target 
        database table.

        For example, suppose we have a file ``insert.tsv``:

            id  name  age
            1   John  20
            2   Mary  24

        We'd like to insert this table of values into the "people" table of 
        our company database.  To preview the insertion:

            >>> from datastore import sqlite
            >>> ds = sqlite('company.db') 
            >>> ds.batch_insert('insert.tsv', table="people", preview=True)
            INSERT INTO people (id, name, age) VALUES (:id, :name, :age);
            id  name    age
            1   John    20
            2   Mary    24
        
        '''
        data = Reader(filename)
        self.valid_table(table)
        for col in data.columns: 
            self.valid_column(col, table)
        insert_st = data.insert_sql(table)
        if preview:
            print insert_st
            print data
        else:
            try:
                self.cur.executemany(insert_st, data.rows)
            except sqlite3.IntegrityError as err:
                print insert_st
                print err
                for row in data.rows:
                    print row
                    self.insert(table, **row) ## try inserting row by row
                                              ##  to find problematic row
                raise SystemExit

    def update(self, table, pk='id', preview=False, **kw):
        '''Update row in table with keyword column/value pairs.'''
        self.valid_table(table)
        for col in kw.keys(): self.valid_column(col, table)
        eq = '{0} = {1}'
        pk_eq = eq.format(pk, kw[pk])
        vals = ', '.join(self._format(i) for i in kw.values())
        assignments = []
        for col, val in kw.items():
            if col == pk: continue
            assignments.append(eq.format(col, self._format(val)))
        cols_eq = ', '.join(assignments)            
        q = 'UPDATE {0} SET {1} WHERE {2};'.format(table, cols_eq, pk_eq)
        if preview:
            return q
        else:
            return self.con.execute(q)

    def batch_update(self, filename, table, pk='id', preview=False):
        '''
        Batch update column values from filename into table.

        If *preview* is True, print the sql statement that will be used 
        for updating and the table of values from *filename*
        
        *filename* should be a TSV file with a header line having 
        column names corresponding to the column names in the target 
        database table.

        The *pk* argument should reference the primary key to use for each
        update in the WHERE clause ("WHERE id = :id"). For example, consider 
        the following update file:

        For example, suppose we have a file ``update.tsv``:

            id  name  age
            1   John  21
            2   Mary  25
        
        We'd like to update the existing values in the "people" table of 
        our company database with these new values.  To preview the update:

            >>> from datastore import sqlite
            >>> ds = sqlite('company.db') 
            >>> ds.batch_update('update.tsv', table="people", preview=True)
            UPDATE people SET name = :name, age = :age WHERE id = :id;
            id  name    age
            1   John    21
            2   Mary    25

        '''
        data = Reader(filename)
        self.valid_table(table)
        for col in data.columns: 
            self.valid_column(col, table)
        update_st = data.update_sql(table)
        if preview:
            print update_st
            print data
        else:
            self.cur.executemany(update_st, data.rows)


if __name__ == '__main__':

    db = sqlite(os.environ['LDP_DB'], row_factory=AttributeRowFactory)

    for row in db('subjects', limit=1):
        print row
        print row[0]
        print row['id']
        print row.id
        print row.values("id", "dob", "sex")
        for i in row: print i

    db.close()

    '''
    db = sqlite(os.environ['LDP_DB']) 

    db.show('subjects')

    db.show('subjects', columns='id, sex, dob', limit=5)

    print db.tables
    print db.columns('subjects')

    for id, sex, dob in db.select('subjects', 
                                  columns='id, sex, dob',
                                  where='project=2'):
        print id, sex, dob

    '''

