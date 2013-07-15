import os
import re
import json
import readline
import subprocess
from glob import glob
from pprint import pprint, pformat
from collections import defaultdict

from util.deco import *
from console.shell import *
from ldp.jobs import Context, BatchJobFile


#  If you prefer vi-style editing when prompted for input, add ...
#       bind -v
#  ... to ~/.editrc (config file for the os x readline/editline lib)
#
#  We previously set readline to use vi-style editing with ...
#       readline.parse_and_bind("bind -v")  
#  ... but users on os x versions < 10.5 had issues.


@aliased
class Runner(Shell):
    '''
    Interactive shell to list job options and start particular jobs.

    The job options presented are based on the files with a .json 
    extension found in the default job directory or the optional path 
    specified in the init path argument.

    '''
    DESC = 'list job options and start particular jobs'
    PATH = os.environ['LDP'] + '/data/jobs'
    jobfiles = {}

    def __init__(self, path=None):
        if path:
            self.PATH = path
        elif 'LDP_JOBS' in os.environ:
            self.PATH = os.environ['LDP_JOBS']
        elif 'LDP_DATA' in os.environ:
            self.PATH = os.environ['LDP_DATA'] + '/jobs'
        files = glob(self.PATH + '/*.json')
        for file in files:
            name = os.path.basename(file).split('.')[0]
            self.jobfiles[name] = file
        super(Runner, self).__init__('[jobs]: ')
        self.intro = self.do_options('', indent=7)

    @property
    def options(self):
        '''Return list of job name, issue tuples.'''
        return [(name, self.issue(name)) for name in self.jobfiles.keys()]

    @alias('do_jobs')
    def do_options(self, line, indent=None):
        '''List job options.'''
        print "jobs to do ...\n",
        for name in self.jobfiles.keys():
            option = self.color.blue(name) + ' - ' + self.issue(name)
            self.puts(option, indent=indent)
        print
        self.help_start()

    def issue(self, name):
        '''Return issue for job with name.'''
        if name in self.jobfiles:
            with open(self.jobfiles[name]) as file:
                job = json.load(file)
                return job['issue']

    def kind(self, name):
        '''Return kind of job for job with name.'''
        if name in self.jobfiles:
            return json.load(open(self.jobfiles[name]))['kind']

    def info(self, name):
        '''Return info for a particular job.'''
        job = JobFile(self.jobfiles[name])
        return job.info

    def do_info(self, name):
        '''Print info about a particular job.'''
        if not name:
            print "Please specify a job"
            self.do_options('')
        else:
            print self.info(name)

    def help_info(self):
        cmd = self.color.cyan('info ') + self.color.blue('{job}')
        print "Type", cmd, "for details about a job"

    def do_start(self, job):
        '''Start job with name.'''
        if job in self.jobfiles:
            if self.kind(job).startswith('Batch'):
                job = BatchJobFile(self.jobfiles[job])
            else:
                print 'Oops! The job editor cannot edit this kind of job file.'
                # job = JobFile(self.jobfiles[job])
            Editor(job).run()
        else:
            print job, 'is not a valid job name!'

    def help_start(self):
        cmd = self.color.cyan('start ') + self.color.blue('{job}')
        print "Type", cmd, "to start a job"


def indexargs(method):
    '''
    Decorator for interactive shell commands that need their 
    line (string) argument converted to indices (positive integers).

    This is typically used for passing the index numbers of specific
    elements within a sequence to commands that work on sequences.

    In the decorator implementation below we assume that decorated methods
    have an active queue (self.job.queue), a current "page" of visible 
    items within the queue (self.job.queue), and that the page has an
    indices property (self.job.queue.page.indices) which returns a set 
    of valid indices for the current page.

    '''
    integer_string = re.compile(r'^\d+$')
    num_range = re.compile(r'^(\d+)-(\d+)$')
    def wrapped(self, line):
        index = []                                  # indices for current page
        indices = []                                
        valid = lambda i: integer_string.match(i)
        num_cmp = lambda x, y: x - y
        if hasattr(self, 'job'):
            index = self.job.queue.page.indices     # indices for current page
            valid = lambda i: integer_string.match(i) and int(i) in index
        if "-" in line:
            for arg in line.split():
                if valid(arg):
                    indices.append(int(arg))
                elif "-" in arg:
                    match = num_range.match(arg)
                    start, stop = int(match.group(1)), int(match.group(2))
                    for i in range(start, stop+1):
                        if valid(str(i)): indices.append(i)
                indices = sorted(indices, cmp=num_cmp)
        else:
            indices = [int(i) for i in line.split() if valid(i)] or index
        return method(self, *indices)
    wrapped.__doc__ = method.__doc__
    return wrapped


@aliased
class Editor(Shell):
    '''
    Interactive shell for editing job files.

    '''
    viz_qsize_max = 30                          # maximum number of queued items shown
    edit_cache = defaultdict(lambda: None)      # cache of unit values by id

    def __init__(self, job):
        super(Editor, self).__init__()
        self.job = job
        self.tags = set(self.job.tags)
        self.context = Context(self.job.dataset['environ'])
        self.set_prompt(self.job.name)
        self.set_intro()

    def set_intro(self):
        tip = "Type " + self.color.blue('tasks') + " to list tasks"
        self.intro = "\n\n".join([self.job.info, tip])

    def set_prompt(self, text):
        '''Set the input prompt.'''
        self.prompt = '[{0}]: '.format(text)

    @lazy
    def intro_help(self):
        '''Intro help message.'''
        intro = '''
        tasks - show tasks to do.
        edits - show edited units.
        omits - show omitted units.
        notes - show notes.
        tags - show tags.

        save - save changes.
        quit - quit current job.

        list [TASK] - show list of tasks (or units within TASK).
        note [TEXT] - add note to current job.

        To work on a task, you need to list it. If a task contains more 
        than 30 units you can use "prev" or "next" to move forward or 
        back through the unit queue.

        Each unit will have an index number.  The following commands take
        indices as optional arguments. For example, "context 5 8" will show 
        the speech context of units 5 and 8, whereas "context" alone will 
        show the context of all visible units. Be careful to specify the 
        units if you do not want to affect them all.

        tag - add tag.
        edit - edit full line.
        replace - replace suspect/highlighted word.
        sub - substitute OLD with NEW.

        undo/revert - revert to previous value.
        commit - move edited units to edits
        omit - move units to omits

        context - show speech context of unit(s).
        inspect - show details of unit(s).'''
        return intro

    @textarg
    def do_help(self, command):
        '''Show help (for a particular command if specified).'''
        if not command:
            print self.intro_help
        super(Editor, self).do_help(command)

    @noargs
    def do_units(self):
        '''Show units in current queue.'''
        self.show()

    @noargs
    def do_edits(self):
        '''Show edits.'''
        self.list('edits')

    @noargs
    def do_omits(self):
        '''Show omits.'''
        self.list('omits')

    @noargs
    def do_tags(self):
        '''Show tags.'''
        for tag in sorted(self.tags):
            self.puts(tag)

    @noargs
    def do_examples(self):
        '''Show examples.'''
        for e in self.job.examples:
            old = e['old']
            new = e['new']
            self.puts(self.color.red(old) + " => " + self.color.green(new))

    @noargs
    def do_notes(self):
        '''Show notes associated with job file.'''
        for note in self.job.notes:
            print
            self.puts(note)
        print

    @textarg
    def do_note(self, text):
        '''Add text to list of notes.'''
        if not text:
            readline.clear_history()
            try:
                text = raw_input(self.IN_PROMPT)
            except KeyboardInterrupt:
                print
                return
        self.job.notes.append(text)

    @property
    def viz_qsize(self):
        '''Visible queue size (number of elements shown).'''
        max = self.viz_qsize_max
        size = len(self.job.queue) 
        return size if (size < max) else max

    @viz_qsize.setter
    def viz_qsize(self, x):
        'Set maximum visible queue size (number of elements shown).'
        self.viz_qsize_max = x

    @alias('do_tasks')
    @textarg
    def do_list(self, name):
        '''
        Show list of tasks to do.

        If task name is given, show units in task queue.

        '''
        if name:
            self.list(name)
        elif self.job.tasks:
            print "{0:>20} (COUNT)".format('NAME')
            for name, count in self.job.list:
                print "{0:>20} ({1})".format(name, count)
            print
            print 'Type ' + self.color.cyan("list ")    \
                          + self.color.blue("{task}") + \
                          ' to list the units in a particular task'
        else:
            print "No tasks remaining!"

    def list(self, name):
        '''Set queue to task with name and show units.'''
        if self.job.set_queue(name):
            self.job.queue.page_size = self.viz_qsize
            self.set_prompt(name)
            self.show()

    def show(self, highlight=None, color='RED', clear=True):
        '''Show range of units in current queue with their indices.'''
        if clear: 
            self.do_clear('')
        if not self.job.queue: 
            return
        else:
            print self.prompt
        print "   ID  VALUE"
        E = self.color.blue('E')                        # edit marker
        for i, unit in self.job.queue.page():
            key = (unit.id, unit.column)
            if key in self.edit_cache:
                unit.value = self.edit_cache[key]       # replace orig if edited
            substring = highlight or unit.suspect
            stat = E if unit.modified else ' '
            value = self.highlight(substring, unit.value, color)
            tags = unit.tags or ''
            i = self.color("{0:>3} ".format(i))
            print stat, i, value, self.color(tags)
        print

    @noargs
    def do_next(self):
        '''Show next page of items in queue.'''
        self.job.queue.page.next()
        self.show()

    @noargs
    def do_prev(self):
        '''Show previous page of items in queue.'''
        self.job.queue.page.prev()
        self.show()

    def next_if_empty(self):
        '''Switch to next queue if queue is empty.'''
        name = self.job.queue.name
        if len(self.job.queue) == 0: 
            next = self.job.next(name)
            self.job.delete(name)
            if next:
                self.list(next)
            else:
                print "Congratulations!!!" 
                print "You have finished all the tasks in this job."
                self.list('edits')
        else:
            self.list(name)

    @indexargs
    def do_inspect(self, *indices):
        '''Inspect units from active queue.'''
        for i in indices:
            unit = self.job.queue.get(i)
            pprint(unit, indent=2)

    @indexargs
    def do_context(self, *indices):
        '''Show speech context for units.'''
        for i in indices:
            id = self.job.queue.id(i)
            if id:
                suspect = self.job.queue.suspect(i)
                P = self.color("   P")
                C = self.color("   C")
                for p, c, x in self.context(id):
                    if p: print P, self.highlight(suspect, p)
                    if c: print C, self.highlight(suspect, c)
                    if x: print self.color("     " + x)
                print

    @alias('do_e')
    @indexargs
    def do_edit(self, *indices):
        '''Edit line values of units.'''
        for i in indices:
            value = self.job.queue.value(i)
            readline.clear_history()
            readline.add_history(value)
            print self.OUT_PROMPT, value
            try:
                edited = raw_input(self.IN_PROMPT)
                if edited:
                    self.job.queue.set_value(edited, i)
            except KeyboardInterrupt:
                print
        print self.OUT_PROMPT, "..."
        self.show(clear=False)

    @alias('do_r')
    @indexargs
    def do_replace(self, *indices):
        '''Replace suspect word in units.'''
        if self.job.queue.name in ("edits", "omits"):
            print "Try", self.color.cyan("sub"), "instead"
            return None
        readline.clear_history()
        for word in reversed(self.job.queue.SUGGESTIONS): 
            readline.add_history(word)
        try:
            new = raw_input(self.IN_PROMPT)
            old = self.job.queue.SUSPECT
            self.job.queue.replace(old, new, *indices)
            print self.OUT_PROMPT, "..."
        except KeyboardInterrupt:
            print
        self.show(clear=False)

    @indexargs
    def do_sub(self, *indices):
        '''Find and substitute a word in units.'''
        readline.clear_history()
        readline.add_history(self.job.queue.SUSPECT)
        old = self.get_input('OLD')
        for word in self.job.queue.SUGGESTIONS: 
            readline.add_history(word)
        new = self.get_input('NEW')
        self.job.queue.replace(old, new, *indices)
        print self.OUT_PROMPT, "..."
        self.show(clear=False)

    @indexargs
    def do_regex(self, *indices):
        '''Find and substitute a regular expression pattern in units.'''
        readline.clear_history()
        readline.add_history(self.job.queue.SUSPECT)
        old = self.get_input('OLD')
        for word in self.job.queue.SUGGESTIONS: 
            readline.add_history(word)
        new = self.get_input('NEW')
        self.job.queue.regex(old, new, *indices)
        print self.OUT_PROMPT, "..."
        self.show(clear=False)

    @alias('do_undo')
    @indexargs
    def do_revert(self, *indices):
        '''Revert units to prior values.'''
        if len(indices) == self.job.queue.page.size:
            if self.bool_input("Revert all units to their previous values?"):
                self.job.queue.revert(*indices)
                self.show()
        else:
            self.job.queue.revert(*indices)
            self.show()

    @indexargs
    def do_commit(self, *indices):
        '''Commit units that have been edited.

        Units that have been edited are marked by an "E". When committed
        they get moved to the edits queue.
        
        '''
        edited = [i for i in indices if self.job.queue.modified(i)]
        self.update_edit_cache(*edited)
        self.job.queue.pop_to(self.job.edits, *edited)
        self.next_if_empty()

    def update_edit_cache(self, *indices):
        '''
        For each indiced item in current queue, cache column values 
        hashed by their id.
        
        '''
        for i in indices:
            id = self.job.queue.id(i)
            col = self.job.queue.column(i)
            self.edit_cache[(id, col)] = self.job.queue.value(i)

    @indexargs
    def do_omit(self, *indices):
        '''Omit units from active queue.'''
        self.job.queue.pop_to(self.job.omits, *indices)
        self.next_if_empty()

    @indexargs
    def do_tag(self, *indices):
        '''Tag units in active queue.'''
        readline.clear_history()
        for tag in self.tags:
            readline.add_history(tag)
        try:
            text = raw_input(self.IN_PROMPT)
            self.tags.add(text)
            self.job.queue.tag(text, *indices)
            print self.OUT_PROMPT, "...\n"
        except KeyboardInterrupt:
            print
        self.show()

    @indexargs
    def do_untag(self, *indices):
        '''Remove tags on units in active queue.'''
        self.job.queue.untag(*indices)
        self.show()

    @textarg
    def do_save(self, file):
        '''Save any changes made.'''
        print "Saving changes"
        tags = sorted(self.tags)
        self.job.save(file, tags, commit=False)

    def bool_input(self, question):
        y = self.color.cyan("y")
        n = self.color.cyan("n")
        prompt = "{0} ({1} or {2}): ".format(question, y, n)
        response = raw_input(prompt)
        if response.startswith('y'): return True

    @noargs
    def do_quit(self):
        '''Quit editor.'''
        if self.job.modified:
            if self.bool_input("Save changes?"):
                self.do_save('')
                print "Committing changes"
                self.job.commit()
        if not self.job.tasks:
            print "There are no more tasks remaining in this job."
            if self.bool_input("Commit updates to data repository?"):
                self.job.save_sql_updates(commit=True)
                self.job.complete()
        return True


if __name__ == '__main__':

    '''
    Runner().run()
    '''
    job = BatchJobFile('../jobs/tests/jobfiles/scratch.json')
    e = Editor(job)
    e.run()

