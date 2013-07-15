import os
import re
import sys
import cmd
import textwrap
from console.color import TextColor


def textarg(method):
    '''
    Decorator for interactive shell commands that take single text arg.
    
    An empty string is returned if no alpha chars are found in the 
    default line arg. The method might then prompt for user input.

    This is used to catch and filter out index/numeric args for our 
    shell commands that do not take index args.

    '''
    word = re.compile(r'[A-Za-z]')
    def wrapped(self, line):
        text = line if word.search(line) else ''
        return method(self, text)
    wrapped.__doc__ = method.__doc__
    return wrapped

def noargs(method):
    '''Decorator for interactive shell commands that do not take any args.'''
    def wrapped(self, line):
        return method(self)
    wrapped.__doc__ = method.__doc__
    return wrapped

def indexargs(method):
    '''
    Decorator for interactive shell commands that need their 
    line (string) argument converted to indices (positive integers).
    
    '''
    integer_string = re.compile(r'^\d+$')
    def wrapped(self, line):
        indices = [int(i) for i in line.split()]
        return method(self, *indices)
    wrapped.__doc__ = method.__doc__
    return wrapped


class Shell(cmd.Cmd, object):
    '''
    Base class for creating interactive shells.
    
    '''
    def __init__(self, prompt='~ ', intro='', default_color='WHITE'):
        super(Shell, self).__init__()
        color = TextColor(default_color)
        self.color = color
        self.quiet = False
        self.prompt = prompt
        self.intro = intro or "Type " + color.cyan("?") + " for help"

    @property
    def prompt(self):
        '''Return formatted prompt.'''
        return self.PROMPT

    @prompt.setter
    def prompt(self, new):
        '''Set prompt to new.'''
        self.indent = len(new)
        spaces = ' ' * (self.indent - 2)
        self.PROMPT = self.color.yellow(new)
        self.CMD_PROMPT = self.color.yellow(spaces + ': ')
        self.OUT_PROMPT = self.color.yellow(spaces + '>')
        self.IN_PROMPT  = self.color.yellow(spaces + '< ')

    def run(self):
        '''Start interactive shell.'''
        self.cmdloop(self.intro)

    def puts(self, text, prompt='', indent=0):
        '''Print text to stdout.'''
        if prompt:
            spaces = ' ' * (indent or self.indent)
            print spaces + prompt + text
        else:
            print self.wrap(text)

    def wrap(self, text, width=80, indent=0):
        '''Wrap text with indent.'''
        spaces = ' ' * (indent or self.indent)
        return textwrap.fill(text, width, initial_indent=spaces,
                                          subsequent_indent=spaces)

    def highlight(self, sub, text, color='RED', words_only=True):
        '''Highlight substring sub in text.'''
        if words_only:
            word = r'\b{0}\b'.format(sub)
            return re.sub(word, self.color(sub, color), text)
        else:
            return text.replace(sub, self.color(sub, color))

    def helper(self, text, indent=0):
        '''Print help message if quiet mode is off.'''
        if not self.quiet:
            spaces = ' ' * (indent or self.indent)
            print self.color("{0}[{1}]".format(spaces, text))

    def get_input(self, help=''):
        '''Prompt for input with optional help message.'''
        if help: 
            help = "{1:>{0}}".format(self.indent - 3, help)
        prompt = self.color(help) + self.color.yellow(" < ")
        response = raw_input(prompt)
        return response

    def bool_input(self, question):
        '''
        Prompt with question requiring yes or no response.

        Return True if response is yes.

        '''
        y = self.color.cyan("y")
        n = self.color.cyan("n")
        prompt = "{0} ({1} or {2}): ".format(question, y, n)
        response = raw_input(prompt)
        if response.startswith('y'): return True

    @noargs
    def do_clear(self):
        '''Clear the screen.'''
        sys.stdout.write(os.popen('clear').read())

    @noargs
    def do_quiet(self):
        '''Turn off/on quiet mode.

            >>> quiet [on|off]

        '''
        if choice == 'off':
            self.quiet = False
            print self.color.white('[quiet mode off]')
        else:
            self.quiet = True
            print self.color.white('[quiet mode on]')

    @noargs
    def do_shell(self):
        '''Run a shell command.'''
        print os.popen(line).read()

    @noargs
    def do_EOF(self):
        '''Quit with ^D.'''
        print
        return True

    @noargs
    def do_quit(self):
        '''Quit.'''
        return True


if __name__ == '__main__':

    shell = Shell()
    shell.run()
