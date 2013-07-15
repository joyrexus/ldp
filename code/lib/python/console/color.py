'''Utilities for creating colorful terminal-based apps.'''


class TextColor(object):
    '''
    ANSI color formatting for output in terminal.
    
        >>> color = TextColor(default='CYAN')
        >>> color('hi')
        hi
        >>> color.red('hi')
        hi
        >>> color.colorize('hi', 'RED')
        hi
        >>> color.colorize('hi', highlight='RED')
        hi
        >>> color.RED + 'hi' + color.RESET
        hi

    '''
    COLORS = ("BLACK", "RED", "GREEN", "YELLOW", "BLUE", 
              "MAGENTA", "CYAN", "WHITE")
    code = '\033[{0};{1}m'      # alternately '\x1B[{0}m'

    COLOR = dict(zip(COLORS, [code.format(0, i) for i in range(30, 38)]))
    BRIGHT = dict(zip(COLORS, [code.format(1, i) for i in range(30, 38)]))
    HIGHLIGHT = dict(zip(COLORS, [code.format(0, i) for i in range(40, 48)]))
    RESET = code.format(0, 0)

    def __init__(self, default="BLACK"):
        self.default = default
        self.__dict__.update(self.COLOR)

    def __call__(self, *args, **kwargs):
        return self.colorize(*args, **kwargs)

    def __getattr__(self, color):
        return lambda text: self.colorize(text, color.upper())

    def colorize(self, text, color=None, bright=None, highlight=None):
        if not color:
            color = self.default
        if highlight:
            text = "{0}{1}{2}".format(self.HIGHLIGHT[color], text, 
                                      self.RESET)
        if bright:
            text = "{0}{1}{2}".format(self.BRIGHT[color], text, 
                                      self.RESET)
        else:
            text = "{0}{1}{2}".format(self.COLOR[color], text, 
                                      self.RESET)
        return text

if __name__ == '__main__':

    color = TextColor('YELLOW')

    print color('hi')
    print color.red('hi')
    print color.cyan('hi')
    print color.magenta('hi')

    for name in color.COLORS:
        print color.colorize('hi', name)
        print color.colorize('hi', name, highlight=True)
        print color.colorize('hi', name, bright=True)

    print color.BLUE + 'hi' + color.RESET
    print '\033[1;31m' + 'hi' + color.RESET
