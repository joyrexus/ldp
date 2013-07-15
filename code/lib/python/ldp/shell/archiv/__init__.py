import os
from ldp.shell.job import Viewer
from console import Shell
from util.deco import *


class Runner(object):
    '''
    Use to register various subshells to be run 
    via the top-level ldp shell

    '''
    jobs = Viewer()     # job viewer shell

    shells = {
        "jobs": {
            "shell": jobs, 
            "help": "start job viewer",
            "intro": "jobs to do ...\n"
        }
    } 

    def options(self):
        '''Return list of shells that can be run.'''
        return self.shells.keys()

    def help(self, name):
        '''Return help message for shell with name.'''
        return self.shells[name]["help"]

    def run(self, name, intro=True):
        '''Start shell with name.'''
        if intro:
            print self.shells[name]["intro"]
        self.shells[name]["shell"].run()


banner = '''
  .-.   .--. .---.
  | |__ | \ \| |-'
  `----'`-'-'`-'  

'''
   
class LDP(Shell):

    runner = Runner()

    def __init__(self, cmd=None, path=None):
        if path:
            self.PATH = path
        elif 'LDP' in os.environ:
            self.PATH = os.environ['LDP']
        if cmd and cmd in self.runner.options():
                self.runner.run(cmd)
        super(LDP, self).__init__(prompt='[ldp]: ')
        self.intro = self.color(banner) + self.intro

    @lazy
    def intro_help(self):
        msg = 'Type ' + self.color.cyan("jobs") + \
              ' to start the job viewer'
        return msg
                              
    def do_help(self, line):
        '''Show help message.'''
        if not line:
            print self.intro_help
        super(LDP, self).do_help(line)

    def do_options(self, line):
        '''List subshells that can be run.'''
        for opt in self.runner.options():
            help = self.runner.help(opt)
            option = self.color.cyan(opt) + " - " + help
            self.puts(option)

    def default(self, cmd):
        if cmd in self.runner.options():
                self.runner.run(cmd, intro=False)
        else:
            print '"{0}" is not a recognized command'.format(cmd)
            self.do_help('')


if __name__ == '__main__':

    shell = LDP()
    shell.run()
