from chat.mor import Mor

input = "n:prop|Anielle^n:prop|Anielle-POSS^ n|shoe-PL ?"
expected = [
    dict(prefix=None, pos="n:prop", lemma="Anielle", suffix="POSS", irreg=False),
    dict(prefix=None, pos="POSS", lemma="'s", suffix=None, irreg=False),
    dict(prefix=None, pos="n", lemma="shoe", suffix="PL", irreg=False),
    dict(prefix=None, pos="?", lemma="?", suffix=None, irreg=False)
]
assert Mor(input) == expected


### 
# usage ...
#

p_mor = "n:prop|Anielle^n:prop|Anielle-POSS^ n|shoe-PL ?"
mor_tokens = Mor(p_mor)

for token in mor_tokens:
    print token.lemma, token.pos

# should print ...

'''
Anielle n:prop
's POSS
shoe n
? ?
'''
