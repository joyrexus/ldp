'''
datastore.table - a simple data table reader and utils.

'''
import sys
from string import Template
from csv import DictReader


class Reader(object):
    '''
    Read in a TSV (tab-separated values) file as an array of dicts.

    The file should include a header line consisting of column names.

    Each dict represents a row in the table, with column names as keys.

    '''
    def __init__(self, filename, delimiter="\t"):
        file = sys.stdin if filename == '-' else open(filename)
        reader = DictReader(file, delimiter=delimiter)
        self.rows = (r for r in reader)
        self.columns = reader.fieldnames
        self.filename = filename

    def __iter__(self):
        '''Yield row values.'''
        for row in self.rows:
            yield row

    def __str__(self):
        '''Pretty print the table.'''
        lines = ["\t".join(self.columns)]
        for row in self.values():
            lines.append("\t".join(row))
        return "\n".join(lines)

    def values(self, *columns):
        '''Yield column values of rows.'''
        if not columns:
            columns = self.columns
        for r in self.rows:
            yield tuple(r[col] or '' for col in columns)

    def column(self, name):
        '''Return list of all values for column name.'''
        return [row[name] for row in self.rows]

    def convert_quotes(self, d):
        '''
        Convert inner single quotes of dict values to sql standard.

        So, a dict value of ...
        
            "i'd love foo's bar."

        ... will be converted to ...
            
            "i''d love foo''s bar."

        This allows the dict values to be embedded within single-quotes
        within a SQL statement:

        UPDATE utterances SET p_utts = 'i''d love foo''s bar.' WHERE id = 5;
        
        '''
        return dict([(k,(v or "").replace("'", "''")) for k,v in d.items()])

    def insert_sql(self, table):
        '''Return sql statement for batch inserting into table.

        For example, if we read in a data file called "insert.tsv" which
        had columns for "id", "name", and "age":

            >>> r = Reader('insert.tsv')
            >>> insert_st = r.insert_sql(table='people')
            >>> insert_st
            INSERT INTO people (id, name, age) VALUES (:id, :name, :age);

        The resulting sql statement embeds named parameters. Such 
        statements can be used with the execute method of the sqlite3 
        API cursor object: 

            >>> import sqlite3
            >>> con = sqlite3.connect('data.db')
            >>> cur = con.cursor()
            >>> cur.execute(insert_st, {"id": 2, "name": "Mary", "age": 22})

        Likewise with the executemany method:

            >>> cur.executemany(insert_st, r.rows)

        '''
        insert_st = 'INSERT INTO {0} ({1}) VALUES ({2});'
        vals = ", ".join(':{0}'.format(c) for c in self.columns)
        cols = ", ".join(self.columns)
        return insert_st.format(table, cols, vals)

    def batch_insert_sql(self, table):
        '''Return string of sql statements for batch insert into table.'''
        insert_st = 'INSERT INTO {0} ({1}) VALUES ({2});'
        vals = ", ".join("'${0}'".format(c) for c in self.columns)
        cols = ", ".join(self.columns)
        temp = Template(insert_st.format(table, cols, vals))
        inserts = ['BEGIN TRANSACTION;']
        for dict in self.rows:
            dict = self.convert_quotes(dict)
            inserts.append(temp.substitute(dict))
        inserts.append('COMMIT;')
        return "\n".join(inserts)

    def update_sql(self, table, pk='id'):
        '''Return sql statement for batch updating table.

        pk - primary key to use for updating.
        
        For example, if we read in a data file called "update.tsv" which
        had columns for "id", "name", and "age":

            >>> r = Reader('update.tsv')
            >>> update_st = r.update_sql(table='people')
            UPDATE people SET name = :name, age = :age WHERE id = :id;

        '''
        update_st = 'UPDATE {0} SET {1} WHERE {2} = :{2};'
        eq = '{0} = :{1}'
        columns = [c for c in self.columns if not c == pk]
        mapping = ", ".join(eq.format(c, c) for c in columns)
        return update_st.format(table, mapping, pk)

    def batch_update_sql(self, table, pk='id'):
        '''Return string of sql statements for batch updating table.

        pk - primary key to use for updating.
        
        '''
        eq = "{0} = '${1}'"
        update_st = 'UPDATE {0} SET {1} WHERE {2} = ${2};'
        columns = [c for c in self.columns if not c == pk]
        mapping = ", ".join(eq.format(c, c) for c in columns)
        temp = Template(update_st.format(table, mapping, pk))
        updates = ['BEGIN TRANSACTION;']
        for dict in self.rows:
            if not pk in dict: continue
            dict = self.convert_quotes(dict)
            updates.append(temp.substitute(dict))
        updates.append('COMMIT;')
        return "\n".join(updates)


if __name__ == '__main__':

    r = Reader('tests/tsv/init.tsv')
    # print r.rows
    # print r.column('name')
    for v in r.values('name', 'age'):
        print v
    '''
    print r
    for row in r: print row
    print r.insert_sql(table='sample')
    print r.batch_insert_sql(table='sample')
    print r.batch_update_sql(table='sample')
    '''
