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
WHERE = 'p_g_type like "%R%"'

def convert(x):
    return str(x) if type(x) is int else x.encode('utf-8', 'ignore')

def pprint(args):
    try:
        print "\t".join(str(i) for i in args)
    except UnicodeEncodeError:
        print "\t".join(convert(i) for i in args)

pprint(columns) # header

def query(condition='', limit=''):
    for row in utterances(COLUMNS, condition, project=2, limit=limit):
        # if row['p_g_type'] != 'R.met': pprint(row)
        pprint(row)

# query(condition='p_g_type like "%R%"')
query(condition='p_form like "%iconic%"')
# query(condition='p_g_type like "%R%" and not p_form like "%iconic%"')
# query(condition='p_form like "%iconic%" and not p_g_type like "%R%"')
