import os
from chat.file import Reader

file = Reader(os.path.dirname(__file__) + "/sample.cha")

def test_tiers():
    '''Testing tiers attribute'''
    assert file.tiers == ['gld', 'mor', 'row', 'speaker', 'syn', 'utt']

def test_records():
    '''Testing records method'''
    assert len(file.records) == 10 

def test_values():
    '''Testing values method'''
    assert len([i for i in file.values('syn')]) == 10
