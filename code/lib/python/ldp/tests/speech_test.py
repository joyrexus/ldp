from ldp.speech import Report, TranscriptReport

speech = Report()
trans = TranscriptReport(22, 6) 

def test_report():
    '''Testing Report class'''
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
