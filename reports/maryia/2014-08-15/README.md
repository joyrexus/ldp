# 2014-08-15 

On Aug 14, 2014, at 4:38 PM, Maryia (Masha) Fedzechkina <mfedze@sas.upenn.edu> wrote:

> I finally extracted the verb lemmas from parental speech. I did the following: I tokenized the `p_mor` column, extracted all tokens that start with 'v', and parsed out the lemmas from there with regular expressions. The regex part seems pretty cumbersome so I'm wondering whether there's a more straightforward way of doing it?  

I would recommend using the [`chat.mor`](https://github.com/joyrexus/ldp/blob/master/code/lib/python/chat/mor.py) module. It’s useful for parsing the morphologically annotated `mor` columns into something more useable, viz. a list of morphological tokens, where each token has the relevant attributes.  For example ...

```python
from chat.mor import Mor

input = "n:prop|Anielle^n:prop|Anielle-POSS^ n|shoe-PL ?"
expected = [
    dict(prefix=None, pos="n:prop", lemma="Anielle", suffix="POSS", irreg=False),
    dict(prefix=None, pos="POSS", lemma="'s", suffix=None, irreg=False),
    dict(prefix=None, pos="n", lemma="shoe", suffix="PL", irreg=False),
    dict(prefix=None, pos="?", lemma="?", suffix=None, irreg=False)
]
assert Mor(input) == expected
```

Usage ...

```python
p_mor = "n:prop|Anielle^n:prop|Anielle-POSS^ n|shoe-PL ?"
mor_tokens = Mor(p_mor)

for token in mor_tokens:
    print token.lemma, token.pos
```

This should print ...

```
Anielle n:prop
's POSS
shoe n
? ?
```

The [`ldp.grammar`](https://github.com/joyrexus/ldp/blob/master/code/lib/python/ldp/grammar/main.py) provides additional functionality.  

```python
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
```

See the docstrings and [tests](https://github.com/joyrexus/ldp/blob/master/code/lib/python/ldp/grammar/tests/main_test.py) for additional usage notes and examples.

The [`ldp.grammar.match.utterance`](https://github.com/joyrexus/ldp/blob/master/code/lib/python/ldp/grammar/match/utterance.py) module might be of interest as well.  Again, the doc-strings and [tests](https://github.com/joyrexus/ldp/tree/master/code/lib/python/ldp/grammar/match/tests) should be useful as a starting point. 
