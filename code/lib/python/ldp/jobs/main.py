import os
import re
import json
import datetime
import subprocess
from pprint import pformat
from util.list import Queue


class Unit(dict):
    '''
    Implements a dictionary like interface with special accessors for 
    the keys: value, prior_value, and tags.

        >>> unit = Unit(id=10, value="foo")
        >>> unit.id
        10
        >>> unit.value
        "foo"
        >>> unit.value = "bar"
        >>> unit.value
        "bar"
        >>> unit.prior_value
        "foo"
        >>> unit.revert()
        >>> unit.value
        "foo"
        >>> unit.tags
        []
        >>> unit.tag('TAG')
        >>> unit.tags
        ['TAG']

    '''
    def __init__(self, *args, **kwargs):
        # if 'tags' not in kwargs: kwargs['tags'] = []
        dict.__init__(self, *args, **kwargs)
        self.__dict__.update(*args, **kwargs)
        self.orig_value = self['value']

    def __getattr__(self, name):
        '''Return None if attribute does not exist.'''
        return None

    @property
    def modified(self):
        '''Return True if unit value was modified.'''
        return self['value'] != self.orig_value

    @property
    def value(self):
        '''Get unit value.'''
        return self['value']

    @value.setter
    def value(self, new):
        '''Set unit value and store priorious.'''
        self.prior_value = self['value']
        self['value'] = new

    @property
    def prior_value(self):
        '''Get prior unit value.'''
        if 'prior_value' in self:
            return self['prior_value']

    @prior_value.setter
    def prior_value(self, new):
        '''Set prior unit value.'''
        self['prior_value'] = new

    @property
    def tags(self):
        '''Get unit tags.'''
        if "tags" not in self:
            self['tags'] = []
        return self['tags']

    @tags.setter
    def tags(self, new):
        '''Append new tag to tag list.'''
        self['tags'].append(new)

    @tags.deleter
    def tags(self):
        '''Delete tag list.'''
        self['tags'] = []

    def revert(self):
        '''Set unit value to prior value.'''
        if self.prior_value:
            self.value = self.prior_value

    def regex(self, old, new):
        '''Replace old pattern with new pattern in value and return result.'''
        value = re.sub(old, new, self.value)
        if value != self.value: self.value = value
        return self.value

    def replace(self, old, new, words_only=True):
        '''Replace old string with new string in value and return result.'''
        if words_only:
            old = r'\b{0}\b'.format(old)
            value = re.sub(old, new, self.value)
        else:
            value = self.value.replace(old, new)
        if value != self.value:
            self.value = value
        return self.value

    def edit(self, func):
        '''Apply edit function to unit value and return result.'''
        self.value = func(self.value)
        return self.value

    def tag(self, text):
        '''Append tag to tags attribute.'''
        self.tags.append(text)

    def sql(self, table, column=None):
        '''Return sql update statement.'''
        sql = "UPDATE {0} SET {1}='{2}' WHERE id={3};"
        value = self.value.replace("'", "''")
        if not column:
            column = self.column
        return sql.format(table, column, value, self.id)


def delta(method):
    '''Sets MODIFIED attribute to true when calling decorated methods.'''
    def wrapped(self, *args, **kwargs):
        self.MODIFIED = True
        return method(self, *args, **kwargs)
    return wrapped


class Units(Queue):
    '''
    Provides a list like interface to a collection of unit dicts.

    '''
    def __init__(self, name, unit_dicts=[], **kwargs):
        units = [Unit(i, **kwargs) for i in unit_dicts]
        super(Units, self).__init__(name, units)
        self.SUSPECT = ''
        self.SUGGESTIONS = []
        self.MODIFIED = False
        self.TAGS = set()
        for key, value in kwargs.items():       
            setattr(self, key.upper(), value)   # uppercase extra keywords

    def __getattr__(self, name):
        '''
        If attribute name doesn't exist, return a function taking 
        a single argument i. 
        
        This allows us to access unit attributes by index number
        without knowing in advance all the attributes a unit might
        have.

        *name* - name of a unit attribute
        *i* - index of unit in queue from which to get attribute

        >>> unit_a = dict(id=10, value="foo bar", suspect="bar")
        >>> unit_a = dict(id=11, value="foo baz", suspect="baz")
        >>> units = Units('units', [unit_a, unit_b])
        >>> units.id(0), units.suspect(0)
        (10, "bar")

        '''
        return lambda i: self[i][name] if i < len(self) else None

    def get(self, i):
        '''Return unit with index.'''
        return self[i]

    def value(self, i):
        '''Return value of unit with index.'''
        return self[i].value

    def tags(self, i):
        '''Return tag list of unit with index.'''
        return self[i].tags

    def modified(self, i):
        '''Return modification status of unit with index.'''
        return self[i].modified

    def prior_value(self, i):
        '''Return prior value of unit with index.'''
        return self[i].prior_value

    @delta
    def set_value(self, new, *indices):
        '''Set value of units with indices to new.'''
        indices = indices or range(len(self))
        for i in indices:
            self[i].value = new

    @delta
    def revert(self, *indices):
        '''Revert units with given index numbers to their prior values.'''
        indices = indices or range(len(self))
        for i in indices:
            self[i].revert()

    @delta
    def regex(self, old, new, *indices):
        '''Replace old with new in values of all units with given indices.'''
        indices = indices or range(len(self))
        for i in indices:
            self[i].regex(old, new)

    @delta
    def replace(self, old, new, *indices):
        '''Replace old with new in values of all units with given indices.'''
        indices = indices or range(len(self))
        for i in indices:
            self[i].replace(old, new)

    @delta
    def edit(self, func, *indices):
        '''Apply edit func to all unit values with given index numbers.'''
        indices = indices or range(len(self))
        for i in indices:
            self[i].edit(func)

    @delta
    def tag(self, text, *indices):
        '''Add new tag to units with given index numbers.'''
        indices = indices or range(len(self))
        for i in indices:
            self[i].tag(text)
        self.TAGS.add(text)

    @delta
    def untag(self, *indices):
        ''' all units with given index numbers.'''
        indices = indices or range(len(self))
        for i in indices:
            del self[i].tags

    def sql(self, table, *indices):
        '''Return sql update statement for units with given index numbers.'''
        indices = indices or range(len(self))
        sql = ''
        for i in indices:
            sql += self[i].sql(table) + "\n"
        return sql


class Job(object):
    '''
    Manage queues of units, omits, and edits.

    '''
    def __init__(self, id, units=[], edits=[], omits=[]):
        self._id = id
        self.units = Units("units", units)
        self.edits = Units("edits", edits)
        self.omits = Units("omits", omits)
        self.queue = self.units

    def set_queue(self, name):
        '''Set active queue to name.'''
        self.queue = getattr(self, name, self.units)

    @property
    def TAGS(self):
        '''Return any tags applied.'''
        return sorted(self.units.TAGS | self.edits.TAGS | self.omits.TAGS)

    @property
    def modified(self):
        '''Return True if any queue was modified.'''
        return self.units.MODIFIED or \
               self.omits.MODIFIED or \
               self.edits.MODIFIED

    @property
    def status(self):
        '''Return status of current job (unit counts of each queue).'''
        counts = []
        for q in ['units', 'edits', 'omits']:
            count = len(getattr(self, q))
            counts.append("{0:>3} {1}".format(count, q))
        return "\n".join(counts)


class JobFile(Job):
    '''
    Convert standard job file to JobFile.

    '''
    required_keys = ['id', 'kind', 'issue', 'dataset', 'author', 
                     'editors', 'tags', 'notes', 'examples',
                     'units', 'edits', 'omits']

    def __init__(self, file):
        self.file = file
        self.name = os.path.basename(file).split('.')[0]
        data = json.load(open(file))
        for key in self.required_keys: 
            assert key in data
        self.KEYS = data.keys()                         # save original keys
        self.__dict__.update(data)
        super(JobFile, self).__init__(self.id, units=self.units, 
                                               edits=self.edits,
                                               omits=self.omits)

    @property
    def info(self):
        '''Return basic info about job.'''
        info = []
        for key in ['id', 'kind', 'issue', 'author', 'notes']:
            value = getattr(self, key)
            if type(value) is unicode:
                value = str(value)
            else:
                value = pformat(value, width=30, indent=4)
            info.append("{0:>8}  {1}".format(key.upper(), value))
        return "\n".join(info)

    def stamp(self):
        '''Append username and timestamp to list of editors.'''
        name = os.environ['USER']
        date = datetime.datetime.today()
        self.editors.append(dict(name=name, date=str(date)))

    def save(self, file=None, tags=[], commit=True):
        '''Save changes to job.'''
        if file:
            commit = False
            if not file.endswith(".json"):
                file += ".json"
        else:
            file = self.file
        self.stamp()
        data = {}
        if hasattr(self, 'KEYS'):
            for key in self.KEYS:
                data[key] = getattr(self, key)      # only dump original keys
        else:
            data = self
        if tags:
            data['tags'] = tags
        with open(file, 'w') as file:
            file.write(json.dumps(data, indent=2))
        if commit:
            self.commit()

    def commit(self, file=None):
        '''Commit changes to file in repo.'''
        if not file:
            file = self.file
        user = os.environ['USER']
        svn_msg = '{0} modified {1}'.format(user, file)
        svn_cmd = 'svn commit {0} -m "{1}"'.format(file, svn_msg)
        subprocess.call(svn_cmd, shell=True)

    def sql_updates(self, table=None):
        '''
        Return sql update statements for all edits.

        That is, convert the id and value of each unit in the current
        edits queue into a sql update statement of the form ...

            UPDATE :table SET :column=:value WHERE id=:id

        '''
        table = table if table else self.dataset['table']
        sql = "BEGIN TRANSACTION;\n{0}COMMIT;\n"
        return sql.format(self.edits.sql(table))

    def save_sql_updates(self, file=None, append=False, commit=False):
        '''
        Save all edits to a sql update file.

        See sql_updates() method for details.

        If you want to append a set of update statements to an existing
        sql update file be sure to set append to True!

        '''
        if not file:
            if commit:
                LDP_DATA = os.environ['LDP_DATA']
                table = self.dataset['table']
                vers = str(self.dataset['version'][0])
                name = self.name + '.sql'
                file = os.path.join(LDP_DATA, 'tables', table, 
                                    'updates', vers, name)
            else:
                file = file or self.file.replace(".json", ".sql")
        elif not file.endswith(".sql"):
            file += ".sql"
        mode = 'a' if append else 'w'
        with open(file, mode) as f:
            f.write(self.sql_updates())
        if commit:
            svn_cmd = 'svn add {0}'.format(file)
            subprocess.call(svn_cmd, shell=True)
            self.commit(file)

    def complete(self):
        '''Move job file to completed directory.'''
        LDP_DATA = os.environ['LDP_DATA']
        JOBS = os.path.join(LDP_DATA, 'jobs')
        dirpath = os.path.join(LDP_DATA, 'jobs', 'complete')
        svn_cmd = 'svn move {0} {1}'.format(self.file, dirpath)
        subprocess.call(svn_cmd, shell=True)
        user = os.environ['USER']
        svn_msg = '{0} completed {1}'.format(user, self.file)
        svn_cmd = 'svn commit {0} -m "{1}"'.format(JOBS, svn_msg)
        subprocess.call(svn_cmd, shell=True)


if __name__ == '__main__':

    path = os.path.dirname(__file__) or '.'
    job = JobFile(path + '/tests/jobfiles/times.json')
    print job.info
    job.queue.pop_to(job.edits, 0, 1)
    job.save_sql_updates(commit=True)
