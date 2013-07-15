import re
from nlp import Tokenizer


class Utterance(list):
    '''
    Use for tokenizing utterances.
    
    '''
    tokenize = Tokenizer(split_clitics=True)

    unknown = re.compile(r"\bxxx(?:'s)?\b")

    def __init__(self, utt):
        '''
        Initialize an Utt object.

        Create a dict representation of the utterance, with each word token's
        numeric index as key and a feature dict as value.

        '''
        words = []
        if utt:
            utt = self.unknown.sub("", utt)
            punct = utt.split()[-1]
            words = self.tokenize(utt.replace("+...", "")) + [punct]
        list.__init__(self, [dict(word=w) for w in words if not w.startswith("&")])


if __name__ == '__main__':

    input = "the dog's food ."
    print Utterance(input)
