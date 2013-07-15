from chat.mor import Token, Mor, Parser, Converter

p = Parser()

def init_test():
    '''Test Token init method'''
    tok = Token("n:prop|Anielle")
    expected = dict(prefix=None, pos="n:prop", lemma="Anielle", 
                    suffix=None, irreg=False)
    assert tok == expected
    assert tok.prefix == None
    assert tok.suffix == None
    assert tok.lemma == "Anielle"
    assert tok.pos == "n:prop"

def fix_token_test():
    '''Test fix_token method'''
    tok = "n:prop|Anielle-POSS^"
    assert p.fix_token(tok) ==  "n:prop|Anielle-POSS"
    tok = "n:prop|Anielle^n:prop|Anielle-POSS^"
    assert p.fix_token(tok) ==  "n:prop|Anielle-POSS"
    tok = "v|be&3S^pro:wh|who~v|have&3S^"
    assert p.fix_token(tok) ==  "v|be&3S"
    tok = "n|+n|butter+n|fly"
    assert p.fix_token(tok) ==  "n|butter+fly"
    tok = "n|+v|pull+ptl|up-PL"
    assert p.fix_token(tok) ==  "n|pull+up-PL"
    tok = "n|+n|ice+n|cream+n|truck"
    assert p.fix_token(tok) ==  "n|ice+cream+truck"
    tok = "co|bye+bye"
    assert p.fix_token(tok) ==  "co|bye+bye"
    tok = ("?|kitty+kat")
    assert p.fix_token(tok) ==  "?|kitty+kat"
    tok = ("pro:dem|that~v|be&3S")

def tokenize_test():
    '''Test tokenize method'''
    
    input = "n:prop|Anielle^n:prop|Anielle-POSS^ n|shoe-PL ?"
    expected = "n:prop|Anielle-POSS", "POSS|'s", "n|shoe-PL", "?"
    assert p.tokenize(input) == expected
    
    input = "pro:wh|who~v|be&3S^pro:wh|who~v|have&3S^ n|pen v|be&3S pro:dem|that ?"
    expected = ("pro:wh|who", "v|be&3S", "n|pen", "v|be&3S", "pro:dem|that", "?")
    assert p.tokenize(input) == expected

    input = "pro:dem|that~v|be&3S ."
    expected = ("pro:dem|that", "v|be&3S", ".")
    assert p.tokenize(input) == expected

    input = "co|no pro:dem|that~v|be&3S n:prop|Mama^n:prop|Mama-POSS^ ."
    expected = ("co|no", "pro:dem|that", "v|be&3S", "n:prop|Mama-POSS",
                "POSS|'s", ".")
    assert p.tokenize(input) == expected

    input = "?|three's prep|after det:num|four ."
    expected = ("?|three", "v|be", "prep|after", "det:num|four", ".")
    print  p.tokenize(input)
    assert p.tokenize(input) == expected

def parse_test():
    '''Test parse method'''
    input = "pro|it v|be&3S unk|xxx . "
    expected = (
        dict(prefix=None, pos="pro", lemma="it", suffix=None, irreg=False),
        dict(prefix=None, pos="v", lemma="be", suffix="3S", irreg=True),
        dict(prefix=None, pos=".", lemma=".", suffix=None, irreg=False)
    )
    assert p.parse(input) == expected

    input = "n:prop|Anielle^n:prop|Anielle-POSS^ n|shoe-PL ?"
    expected = (
        dict(prefix=None, pos="n:prop", lemma="Anielle", suffix="POSS", irreg=False),
        dict(prefix=None, pos="POSS", lemma="'s", suffix=None, irreg=False),
        dict(prefix=None, pos="n", lemma="shoe", suffix="PL", irreg=False),
        dict(prefix=None, pos="?", lemma="?", suffix=None, irreg=False)
    )
    assert p.parse(input) == expected

    parse = Parser()    
    assert parse(input) == expected, "parser object is callable"

    input = "pro:wh|who~v|be&3S^pro:wh|who~v|have&3S^ n|pen v|be&3S pro:dem|that ?"
    expected = (
        dict(prefix=None, pos="pro:wh", lemma="who", suffix=None, irreg=False),
        dict(prefix=None, pos="v", lemma="be", suffix="3S", irreg=True),
        dict(prefix=None, pos="n", lemma="pen", suffix=None, irreg=False),
        dict(prefix=None, pos="v", lemma="be", suffix="3S", irreg=True),
        dict(prefix=None, pos="pro:dem", lemma="that", suffix=None, irreg=False),
        dict(prefix=None, pos="?", lemma="?", suffix=None, irreg=False),
    )
    assert parse(input) == expected

    input = "aux|can~neg|not v|get pro:dem|this re#v|thread-PAST n:prop|Zevy ."
    expected = (
        dict(prefix=None, pos="aux", lemma="can", suffix=None, irreg=False),
        dict(prefix=None, pos="neg", lemma="not", suffix=None, irreg=False),
        dict(prefix=None, pos="v", lemma="get", suffix=None, irreg=False),
        dict(prefix=None, pos="pro:dem", lemma="this", suffix=None, irreg=False),
        dict(prefix="re", pos="v", lemma="thread", suffix="PAST", irreg=False),
        dict(prefix=None, pos="n:prop", lemma="Zevy", suffix=None, irreg=False),
        dict(prefix=None, pos=".", lemma=".", suffix=None, irreg=False)
    )
    assert parse(input) == expected

def tags_test():
    '''Test tags method'''
    parse = Parser()
    input = "n:prop|Anielle^n:prop|Anielle-POSS^ n|shoe-PL ?"
    expected = ['n:prop', 'POSS', 'n', '?']
    assert parse.tags(input) == expected

    input = "pro:wh|who~v|be&3S^pro:wh|who~v|have&3S^ n|pen v|be&3S pro:dem|that ?"
    expected = ["pro:wh", "v", "n", "v", "pro:dem", "?"]
    assert parse.tags(input) == expected

    input = "pro|you~v|be&PRES un#part|snap-PERF ."
    expected = ["pro", "v", "part", "."]
    assert parse.tags(input) == expected

def lemmas_test():
    '''Test lemmas method'''
    parse = Parser()
    input = "n:prop|Anielle^n:prop|Anielle-POSS^ n|shoe-PL ?"
    expected = ["Anielle", "'s", "shoe", "?"]
    assert parse.lemmas(input) == expected

    input = "pro:wh|who~v|be&3S^pro:wh|who~v|have&3S^ n|pen v|be&3S pro:dem|that ?"
    expected = ["who", "be", "pen", "be", "that", "?"]
    assert parse.lemmas(input) == expected

    input = "pro|you~v|be&PRES un#part|snap-PERF ."
    expected = ["you", "be", "unsnap", "."]
    assert parse.lemmas(input) == expected

    input = "co|no pro:dem|that~v|be&3S n:prop|Mama^n:prop|Mama-POSS^ ."
    expected = ["no", "that", "be", "Mama", "'s", "."]
    assert parse.lemmas(input) == expected

def convert_test():
    '''Test convert method'''
    c = Converter()
    tok = c.adj_rule(Token('adj|big-SP')) 
    assert tok.pos == 'JJS'

    input = 'adj|big-SP'
    expected = (
        dict(prefix=None, pos="JJS", lemma="big", suffix="SP", irreg=False),
    )
    assert c.parse(input) == expected

    input = 'adj|lovely'
    expected = (
        dict(prefix=None, pos="JJ", lemma="lovely", suffix=None, irreg=False), 
    )
    assert c.parse(input) == expected

    input = 'adj:n|goop-Y'
    expected = (
        dict(prefix=None, pos="JJ", lemma="goop", suffix="Y", irreg=False), 
    )
    assert c.parse(input) == expected

    input = 'adv:adj|real-LY adv|fast ?'
    expected = (
        dict(prefix=None, pos="RB", lemma="real", suffix="LY", irreg=False), 
        dict(prefix=None, pos="RB", lemma="fast", suffix=None, irreg=False), 
        dict(prefix=None, pos="?", lemma="?", suffix=None, irreg=False), 
    )
    assert c.parse(input) == expected

    input = 'adv:loc|here'
    expected = (
        dict(prefix=None, pos="RB", lemma="here", suffix=None, irreg=False), 
    )
    assert c.parse(input) == expected

    input = 'adv:wh|how'
    expected = (
        dict(prefix=None, pos="WRB", lemma="how", suffix=None, irreg=False), 
    )
    assert c.parse(input) == expected

    input = 'n:prop|Zevy-POSS n|nose ?'
    expected = (
        dict(prefix=None, pos="NNP", lemma="Zevy", suffix="POSS", irreg=False), 
        dict(prefix=None, pos="POS", lemma="'s", suffix=None, irreg=False), 
        dict(prefix=None, pos="NN", lemma="nose", suffix=None, irreg=False), 
        dict(prefix=None, pos="?", lemma="?", suffix=None, irreg=False), 
    )
    assert c.parse(input) == expected

    input = 'prep|to n:prop|Mama .'
    expected = (
        dict(prefix=None, pos="TO", lemma="to", suffix=None, irreg=False), 
        dict(prefix=None, pos="NNP", lemma="Mama", suffix=None, irreg=False), 
        dict(prefix=None, pos=".", lemma=".", suffix=None, irreg=False), 
    )
    assert c.parse(input) == expected

    input = 'pro:wh|whose v|turn ?'
    expected = (
        dict(prefix=None, pos="WP$", lemma="whose", suffix=None, irreg=False), 
        dict(prefix=None, pos="VB", lemma="turn", suffix=None, irreg=False), 
        dict(prefix=None, pos="?", lemma="?", suffix=None, irreg=False), 
    )
    assert c.parse(input) == expected
  
    input = 'pro|I~aux|be&1S neg|not part|open-PROG pro:dem|that .'
    expected = (
        dict(prefix=None, pos="PRP", lemma="I", suffix=None, irreg=False), 
        dict(prefix=None, pos="MD", lemma="be", suffix="1S", irreg=True), 
        dict(prefix=None, pos="RB", lemma="not", suffix=None, irreg=False), 
        dict(prefix=None, pos="VBG", lemma="open", suffix="PROG", irreg=False), 
        dict(prefix=None, pos="DT", lemma="that", suffix=None, irreg=False), 
        dict(prefix=None, pos=".", lemma=".", suffix=None, irreg=False), 
    )
    assert c.parse(input) == expected

def mor_test():
    '''Test Mor init method'''
    input = "n:prop|Anielle^n:prop|Anielle-POSS^ n|shoe-PL ?"
    expected = [
        dict(prefix=None, pos="n:prop", lemma="Anielle", suffix="POSS", irreg=False),
        dict(prefix=None, pos="POSS", lemma="'s", suffix=None, irreg=False),
        dict(prefix=None, pos="n", lemma="shoe", suffix="PL", irreg=False),
        dict(prefix=None, pos="?", lemma="?", suffix=None, irreg=False)
    ]
    assert Mor(input) == expected

    input = "co|yes . co|yes ."
    expected = [
        dict(prefix=None, pos="co", lemma="yes", suffix=None, irreg=False),
        dict(prefix=None, pos="co", lemma="yes", suffix=None, irreg=False),
        dict(prefix=None, pos=".", lemma=".", suffix=None, irreg=False),
    ]
    assert Mor(input) == expected
