'''Tests for nlp.lex module'''

from nlp.lex import Tokenizer, Lemmatizer, Normalizer, IrregularForm

def test_irregulars():
    '''Testing irregulars'''
    irr = IrregularForm()
    print irr.normalize("goes")
    assert irr.normalize("goes") == "go"
    assert irr.normalize("shelves") == "shelf"

def test_expand():
    '''Testing expansions'''
    tok = Tokenizer()
    assert tok.expand("Foo[x3]!") == "Foo Foo Foo!"
    assert tok.expand("Foo [x 3]!") == "Foo Foo Foo!"
    assert tok.expand("Foo [x3]!") == "Foo Foo Foo!"
    assert tok.expand("Foo [x3] bar!") == "Foo Foo Foo bar!"
    assert tok.expand("Foo [x3] bar [x3]!") == "Foo Foo Foo bar bar bar!"
    assert tok.expand("Foo <bar baz>[x2]!") == "Foo bar baz bar baz!" 

def test_tokenize():
    '''Testing the tokenize method'''
    tok = Tokenizer()
    assert tok.tokenize("") == []
    assert tok.tokenize("###") == []
    assert tok.tokenize("###") == []
    assert tok.tokenize("--") == []
    assert tok.tokenize("Foo Bar Baz.") == ["Foo", "Bar", "Baz"]
    assert tok.tokenize("Don't do that!") == ["Don't", "do", "that"]
    assert tok.tokenize("\"Don't do that!\"") == ["Don't", "do", "that"]
    assert tok.tokenize("'Foo' Bar Baz.") == ["Foo", "Bar", "Baz"]
    tok = Tokenizer(split_clitics=True)
    assert tok.tokenize("Don't do that!") == ["Do", "n't", "do", "that"]
    assert tok.tokenize("Foo'll go.") == ["Foo", "'ll", "go"]
    assert tok.tokenize("I'm new.") == ["I", "'m", "new"]
    assert tok.tokenize("He's got to go.") == ["He", "'s", "got", "to", "go"]
    assert tok.tokenize("Foo_Bar Baz.") == ["Foo_Bar", "Baz"]
    assert tok.tokenize("James' friend.") == ["James", "'s", "friend"]
    assert tok.tokenize("Piglet's eyes") == ["Piglet", "'s", "eyes"]
    tok = Tokenizer(nonword=r'[^a-zA-Z\+\'\-\&\@]')
    assert tok.tokenize("Foo_Bar Baz.") == ["Foo", "Bar", "Baz"]

def test_replace():
    '''Testing replacements in tokenization method'''
    tok = Tokenizer()
    assert tok.decontract("hey gimme") == 'hey give me'
    assert tok.decontract("hey let's") == 'hey let_us'
    assert tok.decontract("hey wanna go") == 'hey want to go'
    assert tok.decontract("hey gotta go") == 'hey got to go'
    assert tok.decontract("hey gonna go") == 'hey going to go'
    assert tok.decontract("hey cannot go") == 'hey can not go'
    assert tok.decontract("lookit here") == 'look at here'
    assert tok.tokenize("hey gimme") == ['hey', 'give', 'me']
    assert tok.tokenize("hey let's") == ['hey', 'let_us']
    assert tok.tokenize("hey wanna go") == ['hey', 'want', 'to', 'go']
    assert tok.tokenize("hey gotta go") == ['hey', 'got', 'to', 'go']
    assert tok.tokenize("hey gonna go") == ['hey', 'going', 'to', 'go']
    assert tok.tokenize("hey cannot go") == ['hey', 'can', 'not', 'go']
    assert tok.tokenize("lookit here") == ['look', 'at', 'here']

lem = Lemmatizer()

def test_inflected():
    '''Testing inflections'''
    assert lem.is_inflected("babies") == "s"
    assert lem.is_inflected("baby") is None
    assert lem.is_inflected("walked") == "ed"
    assert lem.is_inflected("walk") is None
    assert lem.is_inflected("running") == "ing"
    assert lem.is_inflected("run") is None
    assert lem.is_inflected("shelves") == "s"

def test_strip_ing():
    '''Testing -ing forms'''
    assert lem.is_geminated("running") == "nning"
    assert lem.strip_suffix("running", "ing") == "run"
    assert lem.is_geminated(u"loving") is None
    assert lem.strip_suffix(u"loving", "ing") == "lov"

def test_rule_params():
    '''Testing rule parameters'''
    assert lem.normalize("loving") == "love"
    # turn off rules in lemmatizer:
    lemm = Lemmatizer(ing_rules=False, irr_rules=False)
    assert lemm.normalize("loving") == "loving"
    assert lemm.normalize("is") == "is"
    assert lemm.normalize("was") == "was"
    assert lemm.normalize("goes") == "go"
    assert lemm.normalize("does") == "does", "'does' handled by irr_rules"

def test_normalize_irr():
    '''Testing irregular word forms'''
    assert lem.normalize("is") == "be"
    assert lem.normalize("was") == "be"
    assert lem.normalize("goes") == "go"
    assert lem.normalize("does") == "do"
    assert lem.normalize("shelves") == "shelf"

def test_normalize_ing():
    '''Testing words ending in -ing'''
    assert lem.normalize("coming") == "come"
    assert lem.normalize("cooking") == "cook"
    assert lem.normalize("making") == "make"
    assert lem.normalize("using") == "use"
    assert lem.normalize("ruling") == "rule"
    assert lem.normalize("making") == "make"
    assert lem.normalize("baking") == "bake"
    assert lem.normalize("taking") == "take"
    assert lem.normalize("shaking") == "shake"
    assert lem.normalize("running") == "run"
    assert lem.normalize("ring") == "ring"
    assert lem.normalize("sing") == "sing"
    assert lem.normalize("during") == "during"
    assert lem.normalize("enduring") == "endure"
    assert lem.normalize("diving") == "dive"
    assert lem.normalize("writing") == "write"
    assert lem.normalize("falling") == "fall"
    assert lem.normalize("drilling") == "drill"
    assert lem.normalize("smelling") == "smell"

def test_normalize_ed():        
    '''Testing words ending in -ed'''
    assert lem.normalize("bed") == "bed"
    assert lem.normalize("fed") == "feed", "fed is irregular"
    assert lem.normalize("led") == "lead", "led is irregular"
    assert lem.normalize("fled") == "flee", "fled is irregular"
    assert lem.normalize("bred") == "breed", "bred is irregular"
    assert lem.normalize("bled") == "bleed", "bled is irregular"
    assert lem.normalize("bleed") == "bleed"
    assert lem.normalize("pleased") == "please"
    assert lem.normalize("scared") == "scare"
    assert lem.normalize("used") == "use"
    assert lem.normalize("tied") == "tie"
    assert lem.normalize("lied") == "lie"
    assert lem.normalize("died") == "die"
    assert lem.normalize("cried") == "cry"
    assert lem.normalize("tried") == "try"
    assert lem.normalize("fried") == "fry"
    assert lem.normalize("freed") == "free"
    assert lem.normalize("fleed") == "flee"
    assert lem.normalize("peed") == "pee"
    assert lem.normalize("feed") == "feed"
    assert lem.normalize("need") == "need"
    assert lem.normalize("deed") == "deed"
    assert lem.normalize("seed") == "seed"
    assert lem.normalize("tired") == "tired"
    assert lem.normalize("wicked") == "wicked"

def test_normalize_s():         
    '''Testing words ending in -s'''
    assert lem.normalize("us") == "us"
    assert lem.normalize("as") == "as"
    assert lem.normalize("bus") == "bus"
    assert lem.normalize("gas") == "gas"
    assert lem.normalize("his") == "his"
    assert lem.normalize("this") == "this"
    assert lem.normalize("tens") == "ten"
    assert lem.normalize("stairs") == "stairs"
    assert lem.normalize("delays") == "delay"
    assert lem.normalize("dress") == "dress"
    assert lem.normalize("tacos") == "taco"
    assert lem.normalize("solos") == "solo"
    assert lem.normalize("pianos") == "piano"
    assert lem.normalize("plateaus") == "plateau"
    assert lem.normalize("taxis") == "taxi" 
    assert lem.normalize("dramas") == "drama"
    assert lem.normalize("pumas") == "puma"
    assert lem.normalize("cheerios") == "cheerio"
    assert lem.normalize("pajamas") == "pajama"
    assert lem.normalize("butterflies") == "butterfly"
    assert lem.normalize("yes") == "yes"
    assert lem.normalize("stairs") == "stairs"
    assert lem.normalize("upstairs") == "upstairs"
    assert lem.normalize("downstairs") == "downstairs"
    for word in "ethos cosmos torus sinus tennis pelvis".split():
        assert lem.normalize(word) == word
    for word in "bias atlas always sideways downstairs".split():
        assert lem.normalize(word) == word

    # tests for -es endings
    assert lem.normalize("scares") == "scare"
    assert lem.normalize("nines") == "nine"
    assert lem.normalize("tenses") == "tense"
    assert lem.normalize("tissues") == "tissue"
    assert lem.normalize("atlases") == "atlas"
    assert lem.normalize("glasses") == "glass"
    assert lem.normalize("ones") == "one"
    assert lem.normalize("eyes") == "eye"
    assert lem.normalize("shoes") == "shoe"
    assert lem.normalize("toes") == "toe"
    assert lem.normalize("potatoes") == "potato"
    assert lem.normalize("kisses") == "kiss"
    assert lem.normalize("trees") == "tree"

    # tests for -ies endings
    assert lem.normalize("ties") == "tie"
    assert lem.normalize("tries") == "try"
    assert lem.normalize("spies") == "spy"
    assert lem.normalize("babies") == "baby"
    assert lem.normalize("ladies") == "lady"
    assert lem.normalize("pennies") == "penny"
    assert lem.normalize("cookies") == "cookie"

    # tests for -ves endings
    assert lem.normalize("halves") == "half", "halves is irregular"
    assert lem.normalize("wives") == "wife", "wives is irregular"
    assert lem.normalize("shelves") == "shelf", "shelves is irregular"
    assert lem.normalize("yourselves") == "yourself", "yourselves is irregular"

def test_compounds():
    '''Testing compound word forms'''
    assert lem.normalize("hotdogs") == "hotdogs"
    assert lem.normalize("hot+dogs") == "hot+dog"
    assert lem.normalize("french+fries") == "french+fry"
    assert lem.normalize("washing+machines") == "washing+machine"

def test_exceptions():
    '''Testing exceptions'''
    exceptions = {"s": ["pants", "mess", "his", "hiss"],
                  "ed": ["seed", "wicked"],
                  "ing": ["morning", "evening", "earring", "nothing"]}
    for type in exceptions:
        for word in exceptions[type]:
            print type, word
            assert lem.normalize(word) == word

def test_full():
    '''Testing typical usage of tokenizer'''
    lemmatize = Lemmatizer()
    tokenize = Tokenizer(split_clitics=True)
    utt = "she's rubbing her feet."
    lemmas = [lemmatize(w) for w in tokenize(utt)]
    assert lemmas == ["she", "'s", "rub", "her", "foot"]
    utt = "saying it doesn't do it."
    lemmas = [lemmatize(w) for w in tokenize(utt)]
    assert lemmas == ["say", "it", "do", "n't", "do", "it"]

def test_normalizer():
    '''Testing typical usage of normalizer'''
    normalize = Normalizer()
    utt = "yeah, she's rubbing her feet."
    assert normalize(utt) == ["yeah", "she", "'s", "rub", "her", "foot"]
    utt = "saying it doesn't do it."
    assert normalize(utt) == ["say", "it", "do", "n't", "do", "it"]
    utt = "it goes here."
    assert normalize(utt) == ["it", "go", "here"]
    utt = "feet foot walk walks walked walking shoes"
    assert normalize(utt) == ["foot", "foot", "walk", "walk", "walk", "walk", "shoe"]
    norm = Normalizer(ed_rules=False, ing_rules=False)
    assert norm(utt) == ["foot", "foot", "walk", "walk", "walked", "walking", "shoe"]
    assert norm("Foo <bar baz>[x2]!") == ["Foo", "bar", "baz", "bar", "baz"]
