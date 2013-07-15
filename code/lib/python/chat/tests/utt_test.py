from chat.utt import Utterance

def init_test():
    '''Testing init method'''
    input = 'do you want to read a book ?'
    expected = [{'word': 'do'}, {'word': 'you'}, {'word': 'want'}, {'word': 'to'}, 
                {'word': 'read'}, {'word': 'a'}, {'word': 'book'}, {'word': '?'}]
    assert Utterance(input) == expected
    
    input = 'do you want to read a xxx ?'
    expected = [{'word': 'do'}, {'word': 'you'}, {'word': 'want'}, {'word': 'to'}, 
                {'word': 'read'}, {'word': 'a'}, {'word': '?'}]
    assert Utterance(input) == expected

    input = "the dog's food ."
    expected = [{'word': 'the'}, {'word': 'dog'}, {'word': "'s"}, 
                {'word': 'food'}, {'word': '.'}]
    assert Utterance(input) == expected

    
