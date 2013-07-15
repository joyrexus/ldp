'''
Abstract base classes for various grammar matching classes.

'''
from operator import itemgetter


class Matcher(object):
    '''
    Matcher base class to be inherited by grammar matching classes.

    '''
    @property
    def __methods__(self):
        '''Return list of methods.'''
        items = sorted(self.__class__.__dict__.items())
        return [getattr(self, k) for (k,v) in items if not k.startswith('_') 
                                                       and callable(v)]

    @property
    def __synopsis__(self):
        '''Return string synopsis of available methods.'''
        msg = self.__class__.__name__ + '\n' + self.__doc__
        for m in self.__methods__:
            docstring = m.__doc__
            if docstring.startswith('\n'):
                msg += '\n  {0}\n{1}'.format(m.func_name, m.__doc__)
            else:
                msg += '\n  {0}\n\n\t{1}\n'.format(m.func_name, m.__doc__)
        return msg


if __name__ == '__main__':

    match = Matcher()
    print match.__methods__
    print match.__synopsis__
