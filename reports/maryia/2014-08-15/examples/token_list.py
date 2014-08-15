from  ldp.grammar import TokenList

utt = 'do you want to read a book ?'
mor = 'aux|do pro|you aux|want inf|to v|read&ZERO det|a n|book ?'
syn = '1|5|AUX 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|7|DET 7|5|OBJ 8|5|PUNCT' 

tokens = TokenList(utt, mor, syn)
print tokens
print tokens.words
print tokens.lemmas
assert tokens.num(1).word == 'do'

for t in tokens: 
    if t.is_verb: 
        print t.lemma, t.pos



