'''
Get standard speech counts for all subjects.

'''
from ldp.speech import SpeechCounts
from ldp.data import Subjects

subjects =  [s for s in Subjects().project(2)]
subjects += [s for s in Subjects().project(3)]
keys = 'subject session speaker utterances mlu word_tokens word_types'.split(" ")


def pprint(args):
    print "\t".join(str(x) for x in args)

def get_counts():
    for subj in subjects:
        for sess in range(3, 5):
            speech = SpeechCounts(subj, sess)
            try:
                for counts in (speech.child, speech.parent):
                    pprint([counts[k] for k in keys])
            except: 
                msg = 'Died on subject {0}, session {1}'.format(subj, sess)
                raise Exception(msg)


pprint(keys)
get_counts()
