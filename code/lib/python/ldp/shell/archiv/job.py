import os
import re
import json
import readline
import subprocess
import ldp.data
from glob import glob
from pprint import pformat
from datetime import datetime

from console import Shell
from util.list import Queue
from util.deco import *


# readline.parse_and_bind("bind -v")  # add vi bindings


class Job(object):

    def __init__(self, jobfile):
        self.file = jobfile
        self.name = os.path.basename(jobfile).split('.')[0]
        job = json.load(open(jobfile))
        self.KEYS = job.keys()
        for qname in ['units', 'edits', 'omits']:
            job[qname] = Queue(qname, job[qname])   # convert to queues
        self.__dict__.update(job)
        self.LDP_DB = os.environ[self.dataset['environ']]
        self.QUEUE = self.units                     # active queue

    def __repr__(self):
        '''Return a string representation of job with main attributes.'''
        args = ['{0}={1}'.format(k, repr(v)) for k, v in self.__dict__.items()
               if type(v) is not Queue]
        return 'Job(\n\t{0}\n)'.format(',\n\t'.join(args))

    @property
    def active_queue_name(self):
        '''Get name of active queue ("units", "edits", or "omits").'''
        return self.QUEUE.name

    def set_active_queue(self, name):
        '''Set active queue ("units", "edits", or "omits").'''
        self.QUEUE = getattr(self, name)

    def get_value(self, i):
        '''Get value of unit with index i in current queue.'''
        if len(self.QUEUE) > i:
            return self.QUEUE[i]['value']

    def set_value(self, i, value):
        '''Set value of unit with index i in current queue.'''
        if len(self.QUEUE) > i:
            self.QUEUE[i]['value'] = value

    def unit_count(self, qname=None):
        '''Return count of units in queue.'''
        if qname:
            q = getattr(self, qname)
        else:
            q = self.QUEUE
        return len(q)

    def tag(self, i, text):
        '''Add tag to unit with index i in current queue.'''
        if text not in self.tags:
            self.tags.append(text)
        if 'tags' in self.QUEUE[i]:
            self.QUEUE[i]['tags'].append(text)
        else:
            self.QUEUE[i]['tags'] = [text]

    @property
    def modified(self):
        '''Returns True if job was modified.'''
        if self.tags or self.edits or self.omits:
            return True

    @property
    def info(self):
        '''Return basic info about job.'''
        items = []
        for key in ['type', 'issue', 'author', 'dataset']:
            value = getattr(self, key)
            if type(value) is unicode:
                value = str(value)
            else:
                value = pformat(value, width=30, indent=4)
            items.append("{0:>8}  {1}".format(key.upper(), value))
        return "\n".join(items)

    @property
    def status(self):
        '''Return status of current job.'''
        items = []
        for q in ['units', 'edits', 'omits']:
            qcount = "{0:>3} {1}".format(len(getattr(self, q)), q)
            items.append(qcount)
        return "\n".join(items)

    def stamp(self):
        '''Append username and timestamp to list of editors.'''
        name = os.environ['USER']
        date = datetime.today()
        self.editors.append(dict(name=name, date=str(date)))

    def save(self, jobfile=None, commit=True):
        '''Save changes to jobfile.'''
        if jobfile:
            commit = False
            if not jobfile.endswith(".json"):
                jobfile += ".json"
        else:
            jobfile = self.file
        self.stamp()
        data = {}
        for key in self.KEYS:
            data[key] = getattr(self, key)      # only dump original keys
        with open(jobfile, 'w') as file:
            file.write(json.dumps(data, indent=2))
        if commit:
            self.commit()

    def commit(self):
        '''Commit changes to jobfile in repo.'''
        user = os.environ['USER']
        svn_msg = '{0} modified {1}'.format(user, self.file)
        svn_cmd = 'svn commit {0} -m "{1}"'.format(self.file, svn_msg)
        subprocess.call(svn_cmd, shell=True)


class Viewer(Shell):

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
        super(Viewer, self).__init__('[jobs]: ')
        self.intro = None

    def preloop(self): 
        self.do_options('', indent=7)

    def do_options(self, line, indent=None):
        '''List job options.'''
        for name in self.jobfiles.keys():
            option = self.color.blue(name) + ' - ' + self.issue(name)
            self.puts(option, indent=indent)
        print
        self.help_start()

    def issue(self, name):
        '''Return info for a particular job.'''
        job = Job(self.jobfiles[name])
        return job.issue

    def info(self, name):
        '''Return info for a particular job.'''
        job = Job(self.jobfiles[name])
        return job.info

    def do_info(self, name):
        '''Print info about a particular job.'''
        if not name:
            print "Please specify a job"
            self.do_options('')
        else:
            print self.info(name)

    def help_info(self):
        print self.color("Type ")           + \
              self.color.cyan('info ')      + \
              self.color.blue('{job}')      + \
              self.color(" for details about a job")

    def do_start(self, name):
        '''Start a particular job.'''
        if name in self.jobfiles:
            e = Editor(self.jobfiles[name])
            e.run()
        else:
            print name, 'is not a valid job name!'

    def help_start(self):
        print self.color("Type ")           + \
              self.color.cyan('start ')     + \
              self.color.blue('{job}')      + \
              self.color(" to start a job")


@aliased
class Editor(Shell):

    flag = re.compile(r'\s+(--\w+|-\w)\s+')
    integer_string = re.compile(r'^\d+$')

    # edit options    OPT  ACTION
    EDIT_OPT_DICT = { "r": "redo previous",
                      "e": "edit line",
                      "c": "context",
                      "t": "tag",
                      "o": "omit",
                      "q": "quit" }

    def __init__(self, jobfile):
        self.job = Job(jobfile)
        prompt = '[job.{0}]: '.format(self.job.name)
        super(Editor, self).__init__(prompt)
        self.utts = ldp.data.Utterances(self.job.LDP_DB)
        self.quiet = False                         # extra help messages
        self.EDIT_OPTS = self.format_opts(self.EDIT_OPT_DICT)

    def format_opts(self, opts):
        'Format a dict of options into a nice looking string.'
        f = ''
        for opt, val in opts.items():
            opt = self.color.cyan(opt)
            val = self.color.white(val)
            f += "    {0} {1}\n".format(opt, val)
        return f

    def isnum(self, i):
        if self.integer_string.match(i): return True

    def reformat(self, unit):
        '''Reformat unit value with suspects highlighted.'''
        value = unit['value']
        for suspect in unit['suspects']:
            value = self.highlight(suspect, value)
        tags = ''
        if 'tags' in unit:
            tags = self.color(repr(unit['tags']))
        return value, tags

    @safe
    def do_show(self, qname, start=0, stop=20, header=False):
        '''Show range of units, edits, or omits.'''
        queue = getattr(self.job, qname)
        if not queue: return
        if len(queue) < (stop - start): 
            stop = len(queue)
        if header:
            print self.color(" [ {0} ]".format(qname))
        print " ID VALUE"
        for i in range(start, stop):
            value, tags = self.reformat(queue[i])
            i = self.color("{0:>3}".format(i))
            print i, value, tags
        print

    @lazy
    def intro_help(self):
        a = 'Type ...\n  '                                          + \
            self.color.cyan("units")                                + \
            ' to see the queue of units to be evaluated\n  '        + \
            self.color.cyan("edits") + ' for units edited\n  '      + \
            self.color.cyan("omits") + ' for units ommitted\n\n'
        b = 'You can ' + self.color.cyan('edit') + ', '             \
                       + self.color.cyan('omit') + ', or '          \
                       + self.color.cyan('tag') + ' units.\n\n'
        c = 'Type ' + self.color.cyan("help ")                      \
                    + self.color.blue("{edit|omit|tag}")            \
                    + ' for details.'
        return a + b + c

    @lazy
    def extra_help(self):
        msg = 'Type ' + self.color.cyan("notes") + \
              ', ' + self.color.cyan("examples") + \
              ', or ' + self.color.cyan("status") + \
              ' for details about this job.'
        return msg
                              
    def do_help(self, line):
        '''Show help message.'''
        if not line:
            print self.intro_help
        super(Editor, self).do_help(line)
        if not line:
            print self.extra_help

    def do_info(self, line):
        '''Show info about current job.'''
        print self.job.info
        print
        print self.extra_help

    def do_note(self, note):
        '''Add note to notes.'''
        self.job.notes.append(line)

    def do_notes(self, line):
        '''Show notes about current job.'''
        for note in self.job.notes:
            print
            print self.wrap(note, indent=4)
        print

    def do_tags(self, line):
        '''Show tagset associated with this job.'''
        for t in self.job.tags:
            print t

    def do_examples(self, line):
        '''Show examples for current job.'''
        for e in self.job.examples:
            old = self.color("    {0}".format(e['old']), 'RED')
            new = self.color(e['new'], 'GREEN')
            print old, " => ", new

    def do_status(self, line):
        '''Show status of current job.'''
        print self.job.status

    @alias('do_U')
    def do_units(self, line):
        '''Show pending units.'''
        self.job.set_active_queue('units')
        self.do_show('units')

    @alias('do_E')
    def do_edits(self, line):
        '''Show edited units.'''
        self.job.set_active_queue('edits')
        self.do_show('edits')

    @alias('do_O')
    def do_omits(self, line):
        '''Show omitted units.'''
        self.job.set_active_queue('omits')
        self.do_show('omits')

    @alias('do_i')
    def do_inspect(self, i):
        '''Show full details of unit.

            >>> inspect 3
        
        '''
        unit = self.job.QUEUE[int(i)]
        print pformat(unit, width=20)

    @alias('do_c')
    def do_context(self, i):
        '''Show speech context of unit.

            >>> context 3
        
        '''
        unit = self.job.QUEUE[int(i)]
        P = self.color("   P")
        C = self.color("   C")
        for p, c, x in self.utts.context(unit['id']):
            if p: print P, p
            if c: print C, c
            if x: print self.color("    " + x)

    @alias('do_o')
    def do_omit(self, args):
        '''Omit units from current queue.
        
            >>> omit 1 2
            >>> omit 1 2 3 -t "review later"
            >>> omit 4 5 6 -t CHECK:SPELLING

        '''
        q = self.job.QUEUE
        nums = [int(i) for i in args.split() if self.isnum(i)]
        if q.name is not 'omits':
            self.do_tag(args)
            q.pop_to(self.job.omits, *nums)
            self.do_show(q.name, header=True)

    @alias('do_r')
    def do_redo(self, nums):
        '''Move units IDs from current queue to units-queue.'''
        q = self.job.QUEUE
        nums = [int(i) for i in nums.split() if self.isnum(i)]
        if q.name is not 'units':
            q.pop_to(self.job.units, *nums)
            self.do_show(q.name, header=True)

    @alias('do_t')
    def do_tag(self, args):
        '''Add tag to unit(s).
        
            >>> tag 2 4 6 -t AMBIGUOUS
            >>> tag 1 2 3 -t "unsure of spelling"

        '''
        # PROMPT IF TAG NOT GIVEN !!!
        args = self.flag.split(args)
        nums = [int(i) for i in args[0].split() if self.isnum(i)]
        if len(args) > 2:
            tag = args[2]
            for i in nums:
                self.job.tag(i, tag)

    def do_untag(self, nums):
        '''Remove tags from unit(s).

            >>> untag 2 4 6

        '''
        q = self.job.QUEUE
        nums = [int(i) for i in nums.split() if self.isnum(i)]
        for i in nums:
            if 'tags' in q[i]:
                del q[i]['tags']

    @alias('do_e')
    def do_edit(self, nums):
        '''Edit unit IDs.

            >>> edit [IDs]
        
        '''
        q = self.job.QUEUE
        self._previous = (None, None)         # reset cache
        if q.name is not 'units':
            items = ', '.join(nums.split())
            print 'Sorry, you can only edit items in [units].'
            if nums:
                print 'Use "redo {0}" to move {1} '.format(nums, items) + \
                      'back to the [units] for editing.'
            self.do_show(q.name, header=True) 
            return None
        if nums:
            nums = [int(i) for i in nums.split() if self.isnum(i)]
        else:
            nums = range(len(q))
        omits = []  # track indices of units to move to omits
        edits = []  # track indices of units to move to edits
        for i in nums:
            status = self.edit(i)
            if status == 'redo':
                status = self.edit(i)
            if status == 'quit':
                break
            elif status == 'edit':
                edits.append(i)
            elif status == 'omit':
                omits.append(i)
        for i in edits:
            self.job.edits.append(q[i])
        for i in omits:
            self.job.omits.append(q[i])
        indices = edits + omits
        q.popm(*indices)

    @safe
    def edit(self, i):
        '''Edit unit i.'''
        suspects = self.job.units[i]['suspects']    # suspect substrings
        value = self.job.units[i]['value']          # unit value
        newval = ''
        status = None

        for suspect in suspects:
            print self.OUT_PROMPT, self.highlight(suspect, value)
            new = raw_input(self.IN_PROMPT)
            if new:
                newval = value.replace(suspect, new)
                print self.OUT_PROMPT, self.highlight(new, newval, 'GREEN')
                print
                status = 'edit'
            else:
                while True:
                    input = raw_input(self.CMD_PROMPT)
                    if input in ("?", "h", "help"):
                        print self.EDIT_OPTS,
                        input = raw_input(self.CMD_PROMPT)
                    if not input:
                        return None                             # do nothing
                    elif input == 'q':
                        return 'quit'
                    elif input == 'r':
                        _i, _value = self._previous           
                        if not _value:
                            self.helper("no previous value stored!")
                            continue
                        self.job.units[_i]['value'] = _value    # restore prev
                        self.edit(_i)                       # redo edit
                        return 'redo'
                    elif input.startswith('o'):             # omit unit
                        if '-t' in input:
                            self.do_tag(str(i) + input.replace("o", "", 1))
                        print
                        return 'omit'
                    elif input == 'c':
                        self.do_context(i)
                        status = None
                    elif input.startswith('t'):
                        self.do_tag("{0} -{1}".format(i, input))
                        status = None
                    elif input == 'e':
                        self.helper("use up arrow to get existing line", 4)
                        readline.add_history(value)
                        newval = raw_input(self.IN_PROMPT)
                        if newval:
                            print self.OUT_PROMPT, newval
                            print
                            status = 'edit'
                            break

        if status == 'edit':
            self._previous = (i, value)         # store prev index, value
            self.job.units[i]['value'] = newval
            # self.job.set_value(i, newval)
        return status

    def do_save(self, filename):
        '''Save any edits made.'''
        self.helper("Saving changes")
        self.job.save(filename, commit=False)

    def do_commit(self, line):
        '''Commit any edits made.'''
        self.helper("Committing changes")
        self.job.commit()

    @alias('do_q', 'do_quit')
    def do_EOF(self, line):
        '''Quit job editor.'''
        if self.job.modified:
            print self.color("Save changes? (") + \
                  self.color.cyan("y")          + \
                  self.color(" or ")            + \
                  self.color.cyan("n")          + \
                  self.color(")"),
            response = raw_input(self.color('~ '))
            if response.startswith('y'):
                self.do_save('')
                self.do_commit('')
        return True


if __name__ == '__main__':

    Viewer().run()

    '''
    job = Job('tests/jobs/times.json')
    print job.info
    print job.status
    e = Editor('tests/jobs/times.json')
    e.run()
    '''
