import os
import json
from ldp.jobs.main import *
from collections import defaultdict


class BatchJob(Job):
    '''
    A batch job contains multiple tasks.

    '''
    def __init__(self, id, tasks={}, edits=[], omits=[], **kwargs):
        self.id = id
        self.tasks = tasks or defaultdict(dict)
        for task in tasks:
            units = tasks[task]['units']
            # add other task keys as attributes to each task's units queue
            other = dict([(str(k), v) for k, v in tasks[task].items() 
                          if k != 'units'])
            self.tasks[task]['units'] = Units(task, units, **other)
        self.units = Units("units")             # empty queue
        self.edits = Units("edits", edits)
        self.omits = Units("omits", omits)
        self.queue = self.units                 # empty queue
        self.__dict__.update(kwargs)

    def __repr__(self):
        return json.dumps(self.__dict__, indent=2)

    def set_queue(self, name):
        '''Set active queue to name.'''
        if name in self.tasks:
            self.units = self.tasks[name]['units']
            self.queue = self.units
        elif name in ('units', 'edits', 'omits'):
            self.queue = getattr(self, name)
        else:
            print name, 'is not a valid option!'
            return 0
        return 1

    def delete(self, task):
        '''Delete task.'''
        if self.queue.name == task:
            self.queue = Units("empty")
        if task in self.tasks:
            del self.tasks[task]

    def count(self, task):
        '''Get unit count of task.'''
        if task in self.tasks:
            return len(self.tasks[task]['units'])

    def next(self, task):
        '''Return name of task following specified task.'''
        if task in self.tasks:
            names = sorted(self.tasks.keys())
            i = names.index(task)
            next = names[0] if i+1 == len(names) else names[i+1]
            if next != task:
                return next     # next task
            else:
                return None     # none left!
        else:
            return 'edits'

    @property
    def list(self):
        '''
        Return list of tuples containing task names and counts.

        Each tuple contains a task name and the number of units 
        remaining in that task's queue.

        '''
        return [(task, self.count(task)) for task in sorted(self.tasks.keys())]

    @property
    def status(self):
        '''Return status of current batch job (unit counts of each queue).'''
        counts = []
        for q in ['edits', 'omits']:
            count = len(getattr(self, q))
            counts.append("{0:>3} {1}".format(count, q))
        units = 0
        for job, count in self.list:
            units += count
        counts.insert(0, "{0:>3} {1}".format(units, "units"))
        return "\n".join(counts)

    def set_dataset(self, table, version=[], environ='LDP_DB'):
        '''
        Set the dataset attribute.

        environ - env variable with path for LDP sqlite-db file
        version - version of LDP database used
        table - name of database table containing column
        
        '''
        self.dataset = dict(environ=environ, version=version, table=table)

    def add_example(self, old, new):
        '''
        Append example to examples attribute.
        
        old - a sample pre-edited value
        new - the corresponding corrected/post-edited value

        >>> b.add_example(old="aachoo", new="achoo")
        >>> b.examples
        [{"old": "reck", "new": "wreck"}]

        '''
        if not hasattr(self, 'examples'): self.examples = []
        self.examples.append(dict(old=old, new=new))

    def add_task(self, name, units, **kwargs):
        '''
        Add task to dict of tasks.

        name - name of task (which can be same as suspect)
        units - list of dicts each containing id, column, and value keys
        kwargs - additional attribute/values to be added to task

        >>> units = [
            {"id": 12223344444, "column": "p_utts", "value": "what a reck!"}
            {"id": 12223344444, "column": "c_utts", "value": "reck on!"}
        ]
        >>> b.add_task("reck", units, suspect="reck", 
                                      suggestions=["wreck", "rack", "rock"])

        '''
        units = Units(name, units, **kwargs)
        self.tasks[name] = dict(units=units, **kwargs)

    def write(self, file=None, **kwargs):
        '''Write to file (path + filename).'''
        if not file: 
            file = self.file
        assert file.endswith('.json')
        self.kind = "BatchSuspectSubstring"
        self.author = os.environ['USER']
        self.created = str(datetime.datetime.today())
        self.__dict__.update(kwargs)
        for attr in ('id', 'issue'):
            if not hasattr(self, attr): 
                raise AttributeError("Please specify {0} parameter!")
        for attr in ('tags', 'notes', 'examples', 'editors', 'edits', 'omits'):
            if not hasattr(self, attr): setattr(self, attr, [])
        if not hasattr(self, 'dataset'):
            raise AttributeError("Use set_dataset() to specify dataset info!")
        if not hasattr(self, 'tasks'):
            raise AttributeError("Use add_task() to add tasks!")
        with open(file, 'w') as file:
            if hasattr(self, 'queue'): del self.queue
            file.write(repr(self))


class BatchJobFile(BatchJob, JobFile):
    '''
    Initialize batch job file serialized as a json file.

    A batch job contains multiple tasks.

    '''
    required_keys = ['id', 'kind', 'dataset', 'editors', 'tasks', 
                     'edits', 'omits']

    def __init__(self, file, **kwargs):
        self.file = file
        self.name = os.path.basename(file).split('.')[0]
        if not os.path.exists(file):
            super(BatchJobFile, self).__init__(**kwargs)
        else:
            data = json.load(open(file))
            for key in self.required_keys: assert key in data
            self.KEYS = data.keys()                 # save original keys
            self.__dict__.update(data)
            super(BatchJobFile, self).__init__(self.id, self.tasks, 
                                                        self.edits,
                                                        self.omits)


if __name__ == '__main__':

    batch = BatchJob(100, issue="issue", notes=["description here"])
    batch.set_dataset(table='utterances', version=[2, 77])
    units = [
        {"id": 12223344444, "column": "p_utts", "value": "what a reck!"},
        {"id": 12223344445, "column": "p_utts", 
                            "value": "between a reck and a hard place."}
    ]
    batch.add_task("reck", units, suspect="reck", 
                                  suggestions=["wreck", "rack", "rock"])
    print batch.tasks

    '''
    path = os.path.dirname(__file__)
    batch.write(path + 'tests/jobfiles/temp.json')

    job = BatchJobFile(path + 'tests/jobfiles/temp.json')
    print job.name
    job.set_queue("reck")
    print len(job.queue)
    print job.queue.id(0)
    print job.queue.value(0)
    print job.queue.column(0)
    print job.queue.suspect(0)
    print job.queue.SUSPECT
    print job.queue.suggestions(0)
    print job.queue.SUGGESTIONS
    '''
