'''Assortment of decorators.'''

from functools import update_wrapper

def disable(f): 
    '''
    Disable a decorator by re-assigning the decorator's name 
    to this function. For example, to turn off memoization:

    >>> memo = disable

    '''
    return f

def decorator(d):
    '''Make function d a decorator: d wraps a function f.'''
    def _d(f):
        return update_wrapper(d(f), f)
    update_wrapper(_d, d)
    return _d

@decorator
def countcalls(f):
    '''Counts calls made to the function decorated.'''
    def counted(*args):
        counted.calls = getattr(counted, 'calls', 0) + 1
        return f(*args)
    return counted

def test(category):
   def real_decorator(f):
      f.test = True
      f.test_category = category
      return f
   return real_decorator

@decorator
def trace(f):
    '''Trace calls made to function decorated.'''
    spaces = '    '
    def _f(*args):
        signature = '{0}({1})'.format(f.__name__, ', '.join(map(repr, args)))
        indent = trace.level * spaces
        print '{0} --> {1}'.format(indent, signature)
        trace.level += 1
        try:
            result = f(*args)
            indent = (trace.level-1) * spaces
            print '{0} <-- {1} == {2}'.format(indent, signature, result)
        finally:
            trace.level -= 1
        return result
    trace.level = 0
    return _f

@decorator
def memo(f):
    '''
    Memoize a function so that it caches all return values for 
    faster future lookups.

    '''
    def memoized(*args):
        if not getattr(memoized, 'cache', None):
            memoized.cache = {}
        if args in memoized.cache:
            return memoized.cache[args]
        else:
            result = memoized.cache[args] = f(*args)
            return result
    return memoized

def lazy(method):
    '''Method decorator to convert method into a lazy property.'''
    attr = '_' + method.__name__
    @property
    def _lazy(self):
        if not hasattr(self, attr):
            setattr(self, attr, method(self))
        return getattr(self, attr)
    return _lazy

@decorator
def safe(method):
    '''Method decorator to catch any exceptions raised.'''
    def wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except:
            print method.__name__, "didn't like that!\n"
            print "Help for", method.__name__, '...'
            print method.__doc__
    wrapper.__doc__ = method.__doc__
    return wrapper

def aliased(aliased_class):
    """
    Decorator function that *must* be used in combination with @alias
    decorator. This class will make the magic happen!
    @aliased classes will have their aliased method (via @alias) actually
    aliased.
    This method simply iterates over the member attributes of 'aliased_class'
    seeking for those which have an '_aliases' attribute and then defines new
    members in the class using those aliases as mere pointer functions to the
    original ones.

    Usage:
        @aliased
        class MyClass(object):
            @alias('coolMethod', 'myKinkyMethod')
            def boring_method():
                # ...

        i = MyClass()
        i.coolMethod() # equivalent to i.myKinkyMethod() and i.boring_method()

    """
    original_methods = aliased_class.__dict__.copy()
    for name, method in original_methods.iteritems():
        if hasattr(method, '_aliases'):
            # Add the aliases for 'method', but don't override any
            # previously-defined attribute of 'aliased_class'
            try:
                for alias in method._aliases - set(original_methods):
                    setattr(aliased_class, alias, method)
            except TypeError:
                pass
    return aliased_class


class alias(object):
    '''
    Alias class that can be used as a decorator for making methods callable
    through other names (or "aliases").

    Note: This decorator must be used inside an @aliased -decorated class.
    For example, if you want to make the method shout() be also callable as
    yell() and scream(), you can use alias like this:

        @alias('yell', 'scream')
        def shout(message):
            # ....

    '''
    def __init__(self, *aliases):
        self.aliases = set(aliases)

    def __call__(self, f):
        f._aliases = self.aliases
        return f


if __name__ == '__main__':

    print "\nDemo of countcalls, trace, and memo:\n"

    @countcalls
    @trace
    @memo
    def fib(n):
        '''Return fibonacci number for n.'''
        return 1 if n <= 1 else fib(n-1) + fib(n-2)

    fib(8)
    print fib.calls, 'calls made'

    print
    print "\nDemo of alias/aliased:\n"

    @aliased
    class Vehicle(object):

        def __init__(self, brand, model, color):
            self.brand = brand
            self.model = model
            self.color = color

        @alias('modelBrandAndColor', 'getModelBrandAndColour', 'getDescription')
        def model_brand_and_color(self):
            return '{0} {1} {2}'.format(self.color, self.brand, self.model)

    vehicle = Vehicle('Chevrolet', 'Spark', 'black')
    # Now your API looks like your users would want.
    # Any of the following lines is equivalent to the others:
    print vehicle.model_brand_and_color()
    print vehicle.getDescription()
    print vehicle.modelBrandAndColor()
    print vehicle.getModelBrandAndColour()
