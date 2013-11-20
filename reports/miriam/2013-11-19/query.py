from ldp.data import Utterances
from ldp.gesture import GestureType

gtypes = GestureType()
utterances = Utterances()
columns = '''
    id 
    subject 
    session 
    row 
    time 
    key
    p_utts
    p_form
    p_lrb
    p_obj
    p_gloss
    p_orient
    p_mspd
    p_g_type
    p_gs_rel
'''.split()
COLUMNS = ', '.join(columns)
WHERE = 'p_g_type like "%D%" and session < 11'

def convert(x):
    return str(x) if type(x) is int else x.encode('utf-8', 'ignore')

def pprint(args):
    try:
        print "\t".join(str(i) for i in args)
    except UnicodeEncodeError:
        print "\t".join(convert(i) for i in args)

pprint(columns) # header

for row in utterances(COLUMNS, WHERE, project=2):
    pprint(row)
