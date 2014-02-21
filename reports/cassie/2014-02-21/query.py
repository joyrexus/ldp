from ldp.data import Utterances
from ldp.grammar import TokenList

utts = Utterances()
columns = 'subject, session, p_utts, p_mor, c_utts, c_mor'

for subj, sess, p, p_mor, c, c_mor in utts(columns, project=2, limit=1000):
    for spkr, utt, mor in [('P', p, p_mor), ('C', c, c_mor)]:
        if mor:
            tokens = TokenList(utt, mor)
            verb_count = sum(t.pos.startswith('v') for t in tokens)
            if verb_count:
                print subj, sess, spkr, 

