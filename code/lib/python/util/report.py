# -*- coding: utf-8 -*-
'''Basic printing and reporting utilities.'''

def tostring(x):
    '''
    Convert a unicode string, normal string or number value to 
    a UTF-8-encoded string.
    
    '''
    return (x if type(x) is unicode else str(x)).encode('utf8')

def stringify(x, sep="\t"):
    '''
    Convert a string or number value (or array/dict comprised 
    of such values) to a UTF-8-encoded string.

    The values of a list and the tuples of a dict get separated by 
    the separator arg (default is a tab) in the resulting string.

    '''
    if type(x) is list or type(x) is tuple:
        return sep.join(tostring(v) for v in x)
    elif type(x) is dict:
        pair = lambda k, v: "({0}, {1})".format(tostring(k), tostring(v))
        return sep.join(pair(k,v) for k,v in x.items())
    else:
        return tostring(x)

def pprint(*values):
    '''
    Helper for stringifying a list of arguments.
    
        >>> pprint(1, 2, 'x', u'é')
        '1\t2\tx\té'

    '''
    print stringify(values)



if __name__ == '__main__':

    assert tostring(1) is '1'
    assert tostring('x') is 'x'
    assert tostring(u'x') is 'x'
    assert tostring(u'é') == 'é'
    assert stringify(1) is '1'
    assert stringify('x') is 'x'
    assert stringify(u'x') is 'x'
    assert stringify(u'é') == 'é'
    arr = [1, 2, 'x', u'é']
    assert stringify(arr) == "1\t2\tx\té"
    dic = {'a': 4, 2: "two", u'é': u'étan'}
    assert stringify(dic, sep=", ") == '(a, 4), (é, étan), (2, two)'
    pprint(1, 2, 'x', u'é')

