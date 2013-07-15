from console import Shell
from util.deco import lazy
from ldp.shell.jobs import Runner

banner = '''
  .-.   .--. .---.
  | |__ | \ \| |-'
  `----'`-'-'`-'  

'''

class Dispatcher(object):
    '''
    Register shells to be run via command name.

    '''
    commands = { "jobs": Runner } 

    @property
    def options(self):
        '''
        Return list of command, description tuples.
        
        Command names are used to dispatch their associated sub-shells.

        '''
        opts = []
        for cmd in sorted(self.commands.keys()):
            Shell = self.commands[cmd]
            opts.append((cmd, Shell.DESC))
        return opts

    def run(self, cmd, *args):
        '''Start shell with associated command.'''
        Shell = self.commands[cmd]
        Shell(*args).run()

   
class Main(Shell):
    '''
    Top-level interactive shell for the LDP project.

    '''
    dispatch = Dispatcher()

    def __init__(self, cmd=None, *args):
        if cmd and cmd in self.dispatch.commands:
                self.dispatch.run(cmd, *args)
        super(Main, self).__init__(prompt='[ldp]: ')
        self.intro = self.color(banner) + self.intro_help

    @lazy
    def intro_help(self):
        msg = 'Type ' + self.color.cyan("jobs") + \
              ' to start the job viewer'
        return msg
                              
    def do_help(self, cmd):
        '''Show help message (for command).'''
        if not cmd:
            print self.intro_help
        super(Main, self).do_help(cmd)

    def do_options(self, line):
        '''List subshells that can be run.'''
        for cmd, desc in self.dispatch.options:
            option = self.color.cyan(cmd) + " - " + desc
            self.puts(option)

    def default(self, cmd):
        '''Run command/subshell if recognized by dispatcher.'''
        if cmd in self.dispatch.commands:
                self.dispatch.run(cmd)
        else:
            print '"{0}" is not a recognized command'.format(cmd)
            self.do_help('')


if __name__ == '__main__':

    # Main('jobs')
    Main().run()
