'''
Test suite for ldp.util module.

'''
from ldp.util import *

def test_pk():
    '''Testing primary-key/unique-id generator.'''
    pk = PrimaryKey()
    assert pk(subject=22, session=33, row=44) == 10223300044
    assert pk(subject=2, session=3, row=4) == 10020300004
    assert pk(subject=222, session=33, row=4444) == 12223304444
