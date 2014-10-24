from ldp.speech import Report, SubjectReport, TranscriptReport


def test_report():
    '''
    Testing the Report class
    
    '''
    speech = Report()                   # initialize general speech report
    speech.query('subject=22 and session=6')
    child = speech.result(22, 6, 'C')
    assert child['subject'] == 22
    assert child['session'] == 6
    assert child['utterances'] == 1065
    assert child['word_tokens'] == 3283
    assert child['word_types'] == 397
    assert round(child['mlu'], 3) == 3.083
    parent = speech.result(22, 6, 'P')
    assert parent['utterances'] == 1252
    assert parent['word_tokens'] == 5604
    assert parent['word_types'] == 650
    assert round(parent['mlu'], 3) == 4.476

    speech.query('subject=125 and session=11')
    child = speech.result(125, 11, "C")
    assert child['word_tokens'] == 1933
    assert child['word_types'] == 353
    assert child['utterances'] == 499

    speech_uniq_tokens = Report(lemmatize=False)
    speech_uniq_tokens.query('subject=125 and session=11')
    child = speech_uniq_tokens.result(125, 11, "C")
    assert child['word_tokens'] == 1933
    assert child['word_types'] == 400
    assert child['utterances'] == 499


def test_lexicon():
    '''
    Testing lexical tracking feature that can be enabled when querying.

        speech = Report()
        speech.query('subject=125 and session=10', lexicon=True)

    This should enable the tracking of word types used by a speaker ('C' for
    child or 'P' for parent) at a given visit (subj, sess):

        word_types = speech.lexicon[(125, 10, 'P')]

    This return the **set** of word types used by the parent speaker in
    the transcript of the recorded visit for subject 125 at session 10.

    '''
    speech = Report()
    speech.query('subject=125 and session=10', lexicon=True)
    speech.query('subject=125 and session=11', lexicon=True)
    A = speech.lexicon[(125, 10, 'P')]
    B = speech.lexicon[(125, 11, 'P')]
    assert len(A) == 326
    assert len(B) == 271
    B.update(A)                 # union of A and B
    assert len(B) == 457


def test_subject_report():
    '''
    Testing the SubjectReport class.
    
    '''
    speech = Report()
    speech.query('subject=125 and session=11')
    A = speech.result(125, 11, "C")

    subject = SubjectReport(125, min_session=10, max_session=11) 
    subject.query()
    results = subject.results()
    B = results[(125, 11, 'C')]
    assert A['word_tokens'] == B['word_tokens']
    assert A['word_types']  == B['word_types']
    assert A['utterances']  == B['utterances']


def test_cumulative_word_types():
    '''
    Testing counts of cumulative word types.

    '''
    subject = SubjectReport(125, min_session=10, max_session=11) 
    subject.query() 
    results = subject.results()
    A = results[(125, 10, 'P')]
    B = results[(125, 11, 'P')]
    assert A['word_types_cumulative'] == 326
    assert B['word_types_cumulative'] == 457


def test_transcript_report():
    '''
    Testing the TranscriptReport class.
    
    '''
    trans = TranscriptReport(22, 6)     # initialize general speech report

    def test_init():
        '''Testing init of TranscriptReport'''
        assert trans.subject == 22
        assert trans.session == 6
        assert trans.lowercase is True, "utts are lowercased by default"

    def test_child_results():
        '''Testing child speech count results'''
        result = trans.child
        assert result['subject'] == 22
        assert result['session'] == 6
        assert result['utterances'] == 1065
        assert result['word_tokens'] == 3283
        assert result['word_types'] == 397
        assert round(result['mlu'], 3) == 3.083

    def test_parent_results():
        '''Testing parent speech count results'''
        result = trans.parent
        assert result['utterances'] == 1252
        assert result['word_tokens'] == 5604
        assert result['word_types'] == 650
        assert round(result['mlu'], 3) == 4.476

    test_init()
    test_child_results()
    test_parent_results()
