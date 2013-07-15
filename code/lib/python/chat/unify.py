from collections import defaultdict
from chat import Utt, Mor, Syn
import ldp.data


class Line(dict):
    '''
    Use for tokenizing annotated utterances produced by 
    clan's part-of-speech tagger (``mor``) and grammatical 
    dependency parser (``grasp``).

    '''
    def __init__(self, utt, mor, syn):
        '''
        Initialize a MorphoSyntax Line object.

        Creates a dict representation of the utterance, with each word token's
        numeric index as key and a feature dict as value.

        Such a Line object provides a unified representation of the chat, mor, 
        and syn column values in an utterance line of a transcript.

        '''
        line = defaultdict(dict)
        self.UTT = Utt(utt)
        self.MOR = Mor(mor)
        self.SYN = Syn(syn)
        for i, (utt, mor, syn) in enumerate(zip(self.UTT, self.MOR, self.SYN)):
            line[i+1].update(utt)
            line[i+1].update(mor)
            line[i+1].update(syn)
        dict.__init__(self, line)

    def __getattr__(self, attr):
        def attr_by_index(i):
            '''
            Return attribute for word token with index i.

            The first word token has index = 1, etc.
        
            '''
            try: 
                return self[i][attr]
            except:
                return None
        return attr_by_index

    def set_pos(self, index, tag):
        '''Set part-of-speech (POS) tag of word with index.'''
        self[index]['pos'] = tag

    def set_rel(self, index, tag):
        '''Set dependency relation (REL) tag of word with index.'''
        self[index]['rel'] = tag

    def set_dep(self, index, n):
        '''
        Set dep feature of word with index to n.

        This is specifying that the word token with the specified index 
        number is grammatically depedent on the n-th word token, which serves
        as its head word (grammatical head).

        '''
        self[index]['dep'] = n

    def head(self, i):
        '''
        For word with index i, return index number of the word's grammatical 
        head.

        Alternate name for *dep* (grammatical dependency) feature.
        
        '''
        return self[i]['dep']

    def deprel(self, i):
        '''For word with index i, return dependency relation of word to its
        head.
        
        Alternate name for *rel* (grammatical relation) feature.
        
        '''
        return self[i]['rel']

    @property
    def words(self):
        '''Return each word token in line.'''
        return [str(self[i]['word']) for i in self.keys()]

    @property
    def POS(self):
        '''Return POS (part-of-speech) feature for each token in line.'''
        return [str(self[i]['pos']) for i in self.keys()]

    @property
    def REL(self):
        '''Return REL (grammatical relation) feature for each token in line.'''
        return [str(self[i]['rel']) for i in self.keys()]

    @property
    def DEP(self):
        '''Return DEP (grammatical dependency) feature for each token in line.'''
        return [self[i]['dep'] for i in self.keys()]

    @property
    def valid(self):
        '''
        Return True if all annotations are aligned with word tokens.

        '''
        if not (len(self.UTT) == len(self.MOR)) or \
           not (len(self.UTT) == len(self.SYN)):
            return False
        for i in self.keys():
            if i != self.num(i): return False
        return True

    def __str__(self):
        '''
        Return a formatted representation of word tokens in 
        line and their annotation features.

        The output rendered is in "dependency format", and consists of 7
        fields:

        ID: token counter, starting at 1 for each new sentence
        FORM: word form or punctuation symbol
        LEMMA: lemma or stem of word form
        POSTAG: fine-grained part-of-speech tag
        FEATS: extra features ('_' indicates no extra feature)
        HEAD: head ID of the current token
        DEPREL: dependency relation to the HEAD

        Each field is delimited by a tab character ('\t'). Each sentence is
        delimited by a blank line. The last two fields (HEAD, DEPREL) are
        optional for decoding.
        
        '''
        line = []
        for i in self.keys():
            features = [str(i), self.word(i), self.lemma(i), self.pos(i), '_', 
                        str(self.dep(i)), self.rel(i)]
            line.append("\t".join(features))
        line.append('')
        return "\n".join(line)


class Transcript(object):
    '''
    Provide unified representation of chat, mor, and syn column values in 
    a transcript.
    
    '''
    unify = Line

    def __init__(self, subject, session):
        self.subject = subject
        self.session = session
        self.transcript = ldp.data.Transcript(subject, session)
        self.problems = []

    def __call__(self, speaker="parent"):
        '''Iterator yielding MorphoSyntax Line objects.'''
        return self.__iter__(speaker)

    def __iter__(self, speaker="parent"):
        '''Iterator yielding MorphoSyntax Line objects.'''
        if speaker not in ("parent", "child"):
            raise ValueError('speaker argument must be "parent" or "child"')
        UTT, MOR, SYN = ("c_chat", "c_mor", "c_syn") if speaker is "child" else \
                        ("p_chat", "p_mor", "p_syn")
        columns = "id, {0}, {1}, {2}".format(UTT, MOR, SYN)
        condition = '{0} != ""'.format(SYN)
        for id, utt, mor, syn in self.transcript.select(columns, where=condition):
            if utt and mor and syn:
                line = self.unify(utt, mor, syn)
                if line.valid:
                    yield line
                else:
                    self.problem.append([id, utt, mor, syn])
            else:
                self.problem.append([id, utt, mor, syn])


if __name__ == '__main__':

    utt = 'do you want to read a book ?'
    mor = 'aux|do pro|you aux|want inf|to v|read&ZERO det|a n|book ?'
    syn = '1|5|AUX 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|7|DET 7|5|OBJ 8|5|PUNCT' 

    print Line(utt, mor, syn)

    transcript = Transcript(83, 10)

    for row in transcript(speaker="parent"):
        print row

    if transcript.problems:
        print "{0} problematic lines".format(len(transcript.problems))
