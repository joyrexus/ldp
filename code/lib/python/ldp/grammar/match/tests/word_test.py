from ldp.grammar import TokenList
from ldp.grammar.match import WordMatcher


get = WordMatcher()


def conj_subor_test():
    '''Testing method for matching subordinating conjunctions''' 
    utt = "because he's in a pond ."
    mor = "conj:subor|because pro|he~v|be&3S prep|in det|a n|pond ."
    syn = "1|3|CPZR 2|3|SUBJ 3|0|ROOT 4|3|PRED 5|6|DET 6|4|POBJ 7|3|PUNCT"
    tokens = TokenList(utt, mor, syn)
    result = get.conj_subor(tokens)
    assert result, "we should get a result"
    print result
    assert len(result) == 1, "the result should be 'because'" 
    assert ["because"] == [t.word for t in result]


def verbs_test():
    '''Testing method for matching verbs''' 
    utt = 'I color the dog nose .'
    mor = 'pro|I v|color det|the n|dog n|nose .'
    syn = '1|2|SUBJ 2|0|ROOT 3|5|DET 4|5|MOD 5|2|OBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    result = get.verbs(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "the result should be 'color'" 
    assert ["color"] == [t.word for t in result]


def verbs_aux_test():
    '''Testing method for matching auxiliaries''' 
    utt = "I'll get you more water ."
    mor = "pro|I~aux|will v|get pro|you qn|more n|water ."
    syn = "1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|OBJ2 5|6|QUANT 6|3|OBJ 7|3|PUNCT"
    tokens = TokenList(utt, mor, syn)
    result = get.verbs_aux(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "the result should be 'will'" 
    assert ["will"] == [t.lemma for t in result]


def verbs_past_test():
    '''Testing method for matching past tense verbs''' 
    utt = 'spilled some water .'
    mor = 'v|spill-PAST qn|some n|water .'
    syn = '1|0|ROOT 2|3|QUANT 3|1|OBJ 4|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    result = get.verbs_past(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "there should be one result"
    assert ["spilled"] == [t.word for t in result]


def verbs_progressive_test():
    '''Testing method for matching progressive verbs''' 
    utt = 'he is hitting it.'
    mor = 'pro|he aux|be&3S part|hit-PROG pro|it .' 
    syn = '1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|OBJ 5|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    result = get.verbs_progressive(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "there should be one result"
    assert ["hitting"] == [t.word for t in result]


def verbs_third_singular_test():
    '''Testing method for matching third singular verbs''' 
    utt = 'he hits it.' 
    mor = 'pro|he v|hit-3S pro|it .' 
    syn = '1|2|SUBJ 2|0|ROOT 3|2|OBJ 4|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    result = get.verbs_third_singular(tokens)
    assert result, "there should be a result"
    assert len(result) == 1, "there should be one result"
    assert ["hits"] == [t.word for t in result]

    utt = 'it is going to turn amazing colors .'
    mor = 'pro|it aux|be&3S aux|go-PROG inf|to v|turn adj|amazing n|color-PL .'
    syn = '1|5|SUBJ 2|5|AUX 3|5|AUX 4|5|INF 5|0|ROOT 6|7|MOD 7|5|PRED 8|5|PUNCT'
    tokens = TokenList(utt, mor, syn)
    result = get.verbs_third_singular(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "there should be one match" 
    assert ["is"] == [t.word for t in result], "since 'is' is not the copula"

    utt = "that's the one he wants."
    mor = "pro:dem|that~v|be&3S det|the pro:indef|one pro|he v|want-3S ." 
    syn = "1|2|SUBJ 2|0|ROOT 3|4|DET 4|2|PRED 5|6|SUBJ 7|4|CMOD 8|2|PUNCT"
    tokens = TokenList(utt, mor, syn)
    result = get.verbs_third_singular(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "there should be only one match" 
    assert ["wants"] == [t.word for t in result], "since 'want' is third singular'"
    assert not ["be"] == [t.lemma for t in result], "since 'is' is the copula"


def verbs_morph_misc_test():
    '''Testing method for matching sundry morphologically modified verbs''' 
    utt = 'he is hitting it.'
    mor = 'pro|he aux|be&3S part|hit-PROG pro|it .' 
    syn = '1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|OBJ 5|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    result = get.verbs_morph_misc(tokens)
    assert not result, "we should not get a result"
    assert not ["is", "hitting"] == [t.word for t in result], "because 'is' and 'hitting' are in categories already"

    utt = "I'm painting ."
    mor = "pro|I~aux|be&1S part|paint-PROG ."  
    syn = "1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|PUNCT"
    tokens = TokenList(utt, mor, syn)
    result = get.verbs_morph_misc(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "there should be one result" 
    assert ["be"] == [t.lemma for t in result], "because 'be' is first singular"
    assert not ["paint"] == [t.lemma for t in result], "because 'painting' is progressive"


def verbs_morph_test():
    '''Testing method for matching all morphologically modified verbs'''
    utt = 'he helps me clean .'
    mor = 'pro|he v|help-3S pro|me v|clean .' 
    syn = '1|2|SUBJ 2|0|ROOT 3|2|OBJ 4|2|XCOMP 5|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    result = get.verbs_morph(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "there should be one result" 
    assert ["help"] == [t.lemma for t in result], "because 'helps' is third singular"
    assert not ["clean"] == [t.lemma for t in result], "because clean isn't modified" 
    
    utt = 'I am cleaning .'
    mor = 'pro|I aux|be&1S part|clean-PROG .' 
    syn = '1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|PUNCT'
    tokens = TokenList(utt, mor, syn)
    result = get.verbs_morph(tokens)
    assert result, "we should get a result"
    assert len(result) == 2, "there should be two results" 
    assert ["be", "clean"] == [t.lemma for t in result], "because they are conjugated" 

    utt = "look I'm going to make ."
    mor = "v|look pro|I~aux|be&1S aux|go-PROG inf|to v|make ."
    syn = "1|6|TAG 2|6|SUBJ 3|6|AUX 4|6|AUX 5|6|INF 6|0|ROOT 7|6|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert get.verbs_morph(tokens)


def clausal_complements_test():
    '''Testing method for matching complements.''' 
    utt = 'help me clean it up .'
    mor = 'v|help pro|me v|clean pro|it ptl|up .'
    syn = '1|0|ROOT 2|1|OBJ 3|1|XCOMP 4|3|OBJ 5|3|PTL 6|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    result = get.clausal_complements(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "there should be one result"
    assert ["clean"] == [t.word for t in result]


def clausal_adjuncts_test(): 
    '''Testing method for matching clausal adjuncts.''' 
    utt = "if we're not, we're going to put it away ."
    mor = "conj:subor|if pro|we~v|be&PRES neg|not pro|we~aux|be&PRES aux|go-PROG inf|to v|put&ZERO pro|it ptl|away ."
    syn = "1|3|CPZR 2|3|SUBJ 3|9|CJCT 4|3|NEG 5|9|SUBJ 6|9|AUX 7|9|AUX 8|9|INF 9|0|ROOT 10|9|OBJ 11|9|PTL 12|9|PUNCT"
    tokens = TokenList(utt, mor, syn)
    result = get.clausal_adjuncts(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "there should be one match" 
    assert ["be"] == [t.lemma for t in result]


def clausal_modifiers_test(): 
    '''Testing method for matching clausal modifiers.''' 
    utt = "time to swim ?"
    mor = "n|time inf|to v|swim ?"
    syn = "1|0|ROOT 2|3|INF 3|1|XMOD 4|1|PUNCT"
    tokens = TokenList(utt, mor, syn)
    result = get.clausal_modifiers(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "there should be one match" 
    assert ["swim"] == [t.lemma for t in result]


def clausal_predicates_test(): 
    '''Testing method for matching clausal predicates.''' 
    utt = "because that's what happens . "
    mor = "conj:subor|because pro:dem|that~v|be&3S pro:wh|what v|happen-3S ."
    syn = "1|3|CPZR 2|3|SUBJ 3|0|ROOT 4|5|SUBJ 5|3|CPRED 6|3|PUNCT"
    tokens = TokenList(utt, mor, syn)
    result = get.clausal_predicates(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "there should be one match" 
    assert ["happen"] == [t.lemma for t in result]
    
    utt = "that's because we're going to +..."
    mor = "pro:dem|that~v|be&3S conj:subor|because pro|we~aux|be&PRES aux|go-PROG inf|to +..."
    syn = "1|2|SUBJ 2|0|ROOT 3|7|CPZR 4|7|SUBJ 5|7|AUX 6|7|AUX 7|2|INF-CPRED 8|2|PUNCT"
    tokens = TokenList(utt, mor, syn)
    result = get.clausal_predicates(tokens)
    assert not result, "we should get no result"
    assert not ["to"] == [t.lemma for t in result], "because infinitive is a placeholder and not a full verb"


def clausal_subjects_test(): 
    '''Testing method for matching clausal subjects.''' 
    utt = "whoever can dance the silliest will win ."
    mor = "pro:wh|whoever aux|can v|dance det|the adj|silly-SP aux|will v|win ."
    syn = "1|3|SUBJ 2|3|AUX 3|7|CSUBJ 4|5|DET 5|3|JCT 6|7|AUX 7|0|ROOT 8|7|PUNCT"
    tokens = TokenList(utt, mor, syn)
    result = get.clausal_subjects(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "there should be one match" 
    assert ["dance"] == [t.lemma for t in result]


def pronouns_personal_test():
    '''Testing method for matching personal pronouns'''
    utt = 'I hit it.'
    mor = 'pro|I v|hit pro|it .' 
    syn = '1|2|SUBJ 2|0|ROOT 3|2|OBJ 4|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    result = get.pronouns_personal(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "there should be one match" 
    assert ["I"] == [t.word for t in result]


def pronouns_demonstrative_test():
    '''Testing method for matching demonstrative pronouns'''
    utt = 'does that fit?' 
    mor = 'aux|do&3S pro:dem|that v|fit ?'
    syn = '1|3|AUX 2|3|SUBJ 3|0|ROOT 4|3|PUNCT' 
    tokens = TokenList(utt, mor, syn)
    result = get.pronouns_demonstrative(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "there should be one match" 
    assert ["that"] == [t.word for t in result]


def pronouns_possessive_test():
    '''Testing method for matching possessive pronouns'''
    utt = 'I took hers.' 
    mor = 'pro|I v|took pro:poss|hers .' 
    syn = '1|2|SUBJ 2|0|ROOT 3|2|OBJ 4|2|PUNCT '
    tokens = TokenList(utt, mor, syn)
    result = get.pronouns_possessive(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "there should be one match" 
    assert ["hers"] == [t.word for t in result]


def pronouns_misc_test():
    '''Testing method for matching misc prounouns'''
    utt = 'I hit myself.'
    mor = 'pro|I v|hit pro:refl|myself .' 
    syn = '1|2|SUBJ 2|0|ROOT 3|2|OBJ 4|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    result = get.pronouns_misc(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "there should be one match" 
    assert ["myself"] == [t.word for t in result]

    utt = "if there's one and you take it away, what's left?"   
    mor = '''conj:subor|if pro:exist|there v|be&3S pro:indef|one conj:coo|and 
             pro|you v|take pro|it adv|away pro:wh|what v|be&3S adj|left ?'''
    syn = '''1|3|CPZR 2|3|ESUBJ 3|5|COORD-CJCT 4|3|PRED 5|11|CJCT 6|7|SUBJ 
             7|5|COORD-CJCT 8|7|OBJ 9|7|JCT 10|11|SUBJ 11|0|ROOT 12|11|PRED 13|11|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    result = get.pronouns_misc(tokens)
    assert result, "we should get a result"
    assert len(result) == 3, "there should be three matches" 
    assert ["there", "one", "what"] == [t.word for t in result]


def pronouns_it_test():
    '''Testing method for matching impersonal pronoun'''
    utt = 'I color it.'
    mor = 'pro|I v|color pro|it .' 
    syn = '1|2|SUBJ 2|0|ROOT 3|2|OBJ 4|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    result = get.pronouns_it(tokens)
    assert result, "we should get a result"
    assert len(result) == 1, "there should be one match"
    assert ["it"] == [t.word for t in result]


def pronouns_test():
    '''Testing method for matching all pronouns'''
    utt = 'I color it.'
    mor = 'pro|I v|color pro|it .' 
    syn = '1|2|SUBJ 2|0|ROOT 3|2|OBJ 4|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    result = get.pronouns(tokens)
    assert result, "we should get a result"
    assert len(result) == 2, "there should be two matches"
    assert ["I", "it"] == [t.word for t in result]


def nouns_plural_test():
    '''Testing method for counting plural nouns'''
    utt = 'I think his teeth look like a beaver .'
    mor = 'pro|I v|think pro:poss:det|his n|tooth&PL v|look prep|like det|a n|beaver .'
    syn = '1|2|SUBJ 2|0|ROOT 3|4|DET 4|5|SUBJ 5|2|COMP 6|5|PRED 7|8|DET 8|6|OBJ 9|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    result = get.nouns_plural(tokens)
    assert result, "should not be empty"
    assert len(result) == 1, "should have only one match"
    assert ["tooth"] == [t.lemma for t in result]

    utt = '''Kevin we need to buy more straight pieces .'''
    mor = '''n:prop|Kevin pro|we aux|need inf|to v|buy qn|more 
             adj|straight n|piece-PL .'''
    syn = '''1|5|VOC 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|8|QUANT 
             7|8|MOD 8|5|OBJ 9|5|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    plurals = [t.word for t in get.nouns_plural(tokens)] 
    assert plurals, "should not be empty"
    assert len(plurals) == 1, "should only have one match"
    assert 'pieces' in plurals, "since 'pieces' is plural"
    assert not 'Kevin' in plurals, "since 'Kevin' is not plural"
    assert not 'we' in plurals, "since 'we' is not plural"


def nouns_basic_test():
    '''Testing method for counting basic nouns'''
    utt = 'I color the dog nose .'
    mor = 'pro|I v|color det|the n|dog n|nose .'
    syn = '1|2|SUBJ 2|0|ROOT 3|5|DET 4|5|MOD 5|2|OBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    result = get.nouns_basic(tokens)
    assert result, "we should get a result"
    assert len(result) == 2, "the result should not include the pronoun"
    assert ["dog", "nose"] == [t.word for t in result]

    utt = 'the swimming .'
    mor = 'det|the n:gerund|swim-GERUND .'
    syn = '1|2|DET 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert ["swimming"] == [t.word for t in get.nouns(tokens)]

    utt = "what's this ?"
    mor = "pro:wh|what~v|be&3S pro:dem|this ?"
    syn = "1|2|PRED 2|0|ROOT 3|2|SUBJ 4|2|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert ["what", "this"] == [t.word for t in get.nouns(tokens)]


def nouns_proper_test():
    '''Testing method for counting proper nouns'''
    utt = '''Kevin we need to buy more straight pieces .'''
    mor = '''n:prop|Kevin pro|we aux|need inf|to v|buy qn|more 
             adj|straight n|piece-PL .'''
    syn = '''1|5|VOC 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|8|QUANT 
             7|8|MOD 8|5|OBJ 9|5|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    result = get.nouns_proper(tokens)
    assert result, "we should get a result"
    assert len(result) == 1
    assert ["Kevin"] == [t.word for t in result]

    utt = 'that the wrong one Mom .'
    mor = 'pro:dem|that det|the adj|wrong pro:indef|one n:prop|Mom .'
    syn = '1|4|SUBJ 2|4|DET 3|4|MOD 4|0|ROOT 5|4|VOC 6|4|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert ["Mom"] == [t.word for t in get.nouns_proper(tokens)]


def nouns_test():
    '''Testing method for counting nouns'''
    utt = 'I color the dog nose .'
    mor = 'pro|I v|color det|the n|dog n|nose .'
    syn = '1|2|SUBJ 2|0|ROOT 3|5|DET 4|5|MOD 5|2|OBJ 6|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    result = get.nouns(tokens)
    assert result, "we should get a result"
    assert len(result) == 3, "the result should contain three nouns"
    assert ["I", "dog", "nose"] == [t.word for t in result]

    utt = '''Kevin we need to buy more straight pieces .'''
    mor = '''n:prop|Kevin pro|we aux|need inf|to v|buy qn|more 
             adj|straight n|piece-PL .'''
    syn = '''1|5|VOC 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|8|QUANT 
             7|8|MOD 8|5|OBJ 9|5|PUNCT'''
    tokens = TokenList(utt, mor, syn)
    result = get.nouns(tokens)
    assert result, "we should get a result"
    assert ["Kevin", "we", "pieces"] == [t.word for t in result]

    utt = 'dog eat people food .'
    mor = 'n|dog v|eat n|person&PL n|food .'
    syn = '1|2|SUBJ 2|0|ROOT 3|4|MOD 4|2|OBJ 5|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert ["dog", "people", "food"] == [t.word for t in get.nouns(tokens)]

    utt = 'house shoes .'
    mor = 'n|house n|shoe-PL .'
    syn = '1|2|MOD 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert ["house", "shoes"] == [t.word for t in get.nouns(tokens)]

    utt = 'little .'
    mor = 'adj|little .'
    syn = '1|0|ROOT 2|1|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert not get.nouns(tokens), "we should not get a result here"

    utt = 'the swimming .'
    mor = 'det|the n:gerund|swim-GERUND .'
    syn = '1|2|DET 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert ["swimming"] == [t.word for t in get.nouns(tokens)]

    utt = "let's do dancing ."
    mor = "aux|let's v|do n:gerund|dance-GERUND ."
    syn = "1|2|AUX 2|0|ROOT 3|2|OBJ 4|2|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert ["dancing"] == [t.word for t in get.nouns(tokens)]

    utt = "I'm good at doing it."
    mor = "pro|I v|be&1S adj|good prep|at n:gerund|do-GERUND pro|it ."
    syn = "1|2|SUBJ 2|0|ROOT 3|2|PRED 4|3|JCT 5|4|POBJ 6|4|POBJ 7|2|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert ["I", "doing", "it"] == [t.word for t in get.nouns(tokens)]

    utt = 'what button, this one ?'
    mor = 'det:wh|what n|button det|this pro:indef|one ?'
    syn = '1|2|DET 2|0|ROOT-NV 3|4|DET 4|2|JCT 5|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert ["button", "one"] == [t.word for t in get.nouns(tokens)]
    
    utt = 'what games ?'
    mor = 'det:wh|what n|game-PL ?'
    syn = '1|2|DET 2|0|ROOT-NV 3|2|PUNCT'
    tokens = TokenList(utt, mor, syn)
    assert ["games"] == [t.word for t in get.nouns(tokens)]

    utt = "what's this ?"
    mor = "pro:wh|what~v|be&3S pro:dem|this ?"
    syn = "1|2|PRED 2|0|ROOT 3|2|SUBJ 4|2|PUNCT"
    tokens = TokenList(utt, mor, syn)
    assert ["what", "this"] == [t.word for t in get.nouns(tokens)]
