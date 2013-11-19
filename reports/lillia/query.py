from util.count import FeatureCounter
from ldp import Utterances
from nlp import Words, Normalizer

corpus = Utterances()
normalize = Normalizer()

columns = 'session, c_utts, c_mor'
conditions = 'c_mor != "" and session > 10'

count = FeatureCounter("Lemma", "Session")

for sess, utt, mor in corpus(columns, where=conditions, project=2):
    lemmas = normalize(utt)
    tokens = mor.split(' ')
    words = utt.split(' ')
    sess = str(sess)

    for lemma, pos in zip(lemmas, tokens):
        if pos.startswith('v'):
            print lemma, pos
