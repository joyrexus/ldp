from __future__ import division
from nlp import Normalizer
from ldp.data import Utterances, Transcript
from collections import defaultdict as dd
import re


class Report(object):
    '''
    Calculate child and parent speech counts.

    Pass the `query` method a set of conditions (using
    the syntax of WHERE clause from a SQL statement)
    to specify which transcripts will be queried.

        >>> speech = Report()
        >>> speech.query('session=11')
        >>> speech.query('subject=22 and session=5')
        >>> speech.query('session=5', project=2)
        >>> speech.query('session=5', subjects=[22, 23, 24])

    Use the `result` method to get the speech counts 
    for a particular (subject, session, speaker).

        >>> speech.result(125, 11, 'P')
        { 'subject': 125,
          'session': 11, 
          'speaker': 'P', 
          'utterances': 199,
          'word_tokens': 936, 
          'word_types': 271, 
          'mlu': 4.703517587939698 }

    Use the `report` method to print a report of all 
    the speech counts for all transcripts queried.

        >>> speech.report(header=True)

    Call the object directly to query and report:

        >>> speech('session=10')

    '''
    letter = re.compile(r'\w')

    def __init__(self, lowercase=True, lemmatize=True, dataset=None):
        self.normalize = Normalizer(lemmas=lemmatize)
        self.utterances = Utterances(dataset)
        self.lowercase = lowercase
        self.dataset = dataset
        self.toks = dd(int)
        self.utts = dd(int)
        self.words = dd(lambda: dd(int))
        self.trans = dd(int)

    def __call__(self, conditions=None, limit='', project='', subjects=[]):
        '''
        Call object directly to run a query and print a report.
        
            >>> speech = Report()
            >>> speech('subject=22 and session=5')
            >>> speech('session=5', project=2)
            >>> speech('session=5', subjects=[22, 23, 24])
        '''
        self.query(conditions, limit, project, subjects)
        self.report()

    def query(self, conditions=None, limit='', project='', subjects=[]):
        '''
        Query the dataset of utterances with given conditions.

        `conditions` - "where" clause of a SQL statement
        `limit` - limit the number of utterances to query

            >>> speech = Report()
            >>> speech.query('subject=125 and session=11', limit=100)

        '''
        columns = 'subject, session, p_utts, c_utts'

        for subj, sess, p, c in self.utterances(columns, 
                                                conditions,
                                                limit, 
                                                project, 
                                                subjects):
            self.trans[subj, sess] = 1
            for spkr, utt in [('P', p), ('C', c)]:
                if not utt: continue
                id = (subj, sess, spkr)
                if self.lowercase: utt = utt.lower()
                if self.letter.search(utt):
                    self.utts[id] += 1
                for word in self.normalize(utt):
                    self.toks[id] += 1
                    self.words[id][word] += 1

        return self

    def result(self, subj, sess, spkr, returnArray=False):
        '''
        Return a dict of results for the specified 
        (subject, session, speaker).

        `subj` - subject ID
        `sess` - session ID (1 to 12)
        `spkr` - speaker ID ("P for parent or "C" for child)

        '''
        id = (subj, sess, spkr)
        UTT = self.utts[id]
        TOK = self.toks[id]
        TYP = len(self.words[id])
        MLU = TOK/UTT if UTT else '-'
        if returnArray:
            return [subj, sess, spkr, UTT, TOK, TYP, MLU]
        else:
            return dict(subject=subj,
                        session=sess,
                        speaker=spkr, 
                        utterances=UTT, 
                        word_tokens=TOK, 
                        word_types=TYP, 
                        mlu=MLU)

    def report(self, header=True):
        '''
        Print a report showing the number of utterances, word
        tokens, word types, and MLU for each (subj, sess, spkr).

        The report will only contain results after first querying
        the dataset.

        '''
        def pprint(*args):
            print "\t".join(str(x) for x in args)

        if header:
            pprint(*'subj sess spkr UTT TOK TYP MLU'.split(" "))

        for subj, sess in sorted(self.trans):
            for spkr in ['P', 'C']:
                id = (subj, sess, spkr)
                UTT = self.utts[id]
                TOK = self.toks[id]
                TYP = len(self.words[id])
                MLU = TOK/UTT if UTT else '-'
                pprint(subj, sess, spkr, UTT, TOK, TYP, MLU)


class TranscriptReport(object):
    '''
    Calculate child or parent speech counts for a given transcript.

    '''
    normalize = Normalizer()
    letter = re.compile(r'\w')

    def __init__(self, subject, session, lowercase=True, dataset=None):
        self.subject = subject
        self.session = session
        self.lowercase = lowercase
        self.dataset = dataset

    @property
    def child(self):
        '''Return child speech counts.'''
        return self.results('child')

    @property
    def parent(self):
        '''Return parent speech counts.'''
        return self.results('parent')

    def results(self, speaker):
        '''
        Return a dict of results for the specified speaker.

        '''
        column = None
        words = dd(int)
        UTT = 0
        TOK = 0
        if speaker == 'parent':
            column = 'p_utts'
        elif speaker == 'child':
            column = 'c_utts'

        for row in Transcript(self.subject, self.session, self.dataset):
            utt = getattr(row, column)
            if not utt: continue
            if self.lowercase: utt = utt.lower()
            UTT += 1 if self.letter.search(utt) else 0
            for w in self.normalize(utt):
                TOK += 1
                words[w] += 1

        TYP = len(words)
        MLU = TOK/UTT if UTT else '-'

        return dict(subject=self.subject, 
                    session=self.session, 
                    speaker="P" if speaker == "parent" else "C", 
                    utterances=UTT, 
                    word_tokens=TOK, 
                    word_types=TYP, 
                    mlu=MLU)


if __name__ == '__main__':

    speech = Report()
    speech.query('subject=125 and session=11')

    trans = TranscriptReport(125, 11) 
    assert trans.child == speech.result(125, 11, "C")
    assert trans.parent == speech.result(125, 11, "P")
