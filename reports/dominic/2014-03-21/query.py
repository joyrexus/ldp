import re
from nlp import Tokenizer
from ldp.data import Utterances
from util.count import FeatureCounter

count = FeatureCounter('Subject', 'Session', 'Speaker', 'Word')
utterances = Utterances()
parse = Tokenizer()

words = [word.rstrip() for word in open('words.txt')]
rgx = re.compile(r'\b(?:' + '|'.join(words) + r')\b')

columns = 'subject, session, row, p_utts, c_utts'
where = 'session < 8'

# pretty-print with tab delims
def pprint(*args):
    print '\t'.join(str(x) for x in args)

pprint(*'SUBJ SESS SPKR ROW UTT MATCH'.split(' '))      # header

for subj, sess, row, p, c in utterances(columns, where, project=2):
    for spkr, utt in [('P', p), ('C', c)]:
        matches = rgx.findall(utt)
        for word in matches:
            count(subj, sess, spkr, word)
        if matches:
            pprint(subj, sess, spkr, row, utt, ', '.join(matches))

print
count.print_report('Word')

