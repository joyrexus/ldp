from ldp.shell.main import Dispatcher

dispatch = Dispatcher()

def test_options():
    '''Testing options property'''
    expected = [('jobs', 'list job options and start particular jobs')]
    assert dispatch.options == expected
