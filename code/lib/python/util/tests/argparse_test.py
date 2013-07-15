import util.argparse as argparse

p = argparse.ArgumentParser(description='Test parser')
p.add_argument('--subject', type=int, help='Subject ID')
p.add_argument('--session', type=int, help='Session ID')
args = p.parse_args(['--subject=22', '--session=1'])

def test_version():
    '''Testing version'''
    assert argparse.__version__ == '1.2.1'

def test_arguments():
    '''Testing arguments'''
    assert args.subject == 22
    assert args.session == 1
