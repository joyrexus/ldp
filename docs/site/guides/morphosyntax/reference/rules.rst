**************
Matching Rules
**************

The following are rules for identifying whether an utterance contains a
particular type of morphosyntactic item of interest.

:Author: Hannah Lemonick
:Date: 06-29-12

Preliminaries
=============

List of grammatical relations taken by verbs::

    VERB_REL = ["ROOT", "CSUBJ", "XSUBJ", 
                        "CPRED", "XPRED", 
                        "COMP", "XCOMP", 
                        "CMOD", "XMOD", 
                        "CJCT", "XJCT"]



Word Level
==========

*Word Token Identification Rules*

The following are rules for matching utterances containing word tokens with 
particular morphosyntactic properties (leveraging our existing morphosyntax 
annotation).


1. Simple Nouns
---------------
::

    x.pos.startswith("n") and x.pos is not "neg"


2. Proper Nouns
---------------
::

    x.pos = "n:prop"


3. Plural Nouns
---------------
::

    x.is_noun and x.suffix = "PL"


4. Personal Pronouns
--------------------
::

    x.pos = "pro" and x.lemma is not "it"


5. Past Tense
-------------
::

    x.suffix = "PAST"


6. Infinitive
-------------
::

    x.pos = "inf" and x.rel = "INF"


7. Progressive
--------------
::

    x.suffix = "PROG" and not x.rel.startwith("MOD")

To be cautious, we should use the following rule to catch coordinated
structures as well::

    x.suffix = "PROG" 
        and (x.rel = "MOD" 
             or (x.rel = "COORD" and x has an ancestor, y, where y.rel = "MOD"))

Can we find any examples where this is needed?


8. Third Person Singular Verb
-----------------------------
::

    x.suffix = "3S" and x.lemma != "be"

Hannah and Max originally proposed the following rule, but the above
appears to suffice::

    x.suffix = "3S" and 
        ( (x.is_verb and x.lemma is not "be") or x.pos = "aux" )

Can we find any examples where this more elaborate rule might be needed?


9. Non-Coordinating Conjunction
-------------------------------
::

    x.pos = "conj:subor"
        and x.dep = y.num
        and y.rel is in VERB_REL


10. Clausal Complement
----------------------
::

    x.rel is in ["COMP", "XCOMP"]


11. Clausal Adjunct
-------------------
::

    x.rel is in ["CJCT", "XJCT"]


12. Clausal Predicate
---------------------
::

    x.rel is in ["CPRED", "XPRED"]


13. Clausal Modifier
--------------------
::

    x.rel is in ["CMOD", "XMOD"]


14. Clausal Subject
-------------------
::

    x.rel is in ["CSUBJ", "XSUBJ"]


15. Preposition as Root
-----------------------
::

    x.pos = "prep" 
        and x.rel = "ROOT"
        and if y.dep = x.num
            y.rel is not in ["SUBJ", "CSUBJ", "XSUBJ"]


16. Article-Noun Phrase
-----------------------
::

    x.lemma is in ["a", "the"]
        and x.dep = y.num
        and y.is_noun


17. Non-Article Determiner Noun Phrase
--------------------------------------
::

    x.rel = "DET"
        and x.lemma is not in ["a", "the"]
        and x.dep = y.num
        and y.is_noun


18. Quantifier-Noun Phrase
--------------------------
::

    x.rel = "QUANT"
        and x.dep = y.num
        and y.is_noun


19. Adjective-Noun Phrase
-------------------------
::

    x.pos.startswith("adj")
        and x.rel = "MOD"
        and x.dep = y.num
        and y.is_noun


20. Noun-Noun Phrase
--------------------
::

    x.pos.startswith("n")
        and x.rel = "MOD"
        and x.dep = y.num
        and y.is_noun


21. Verb with Particle
----------------------
::

    x.pos = "ptl"
        and x.dep = y.num
        and y.pos is in ["v", "part"]
        and y.rel is in VERB_REL


22. Adverb Modifying Verb
-------------------------
::

    x.pos.startswith("adv")
        and x.dep = y.num
        and y.pos is in ["v", "part", "aux"]
        and y.rel is in VERB_REL + ["AUX"]


23. Preposition Modifying Verb
------------------------------
::

    x.pos = "prep"
        and x.dep = y.num
        and y.pos is in ["v", "part", "aux"]
        and y.rel is in VERB_REL + ["AUX"]


24. Preposition Modifying Subject Noun
--------------------------------------
::

    x.pos = "prep"
        and x.dep = y.num
        and y.is_noun and y.rel is "SUBJ"


25. Preposition Modifying Non-Subject Noun
------------------------------------------
::

    x.pos = "prep"
        and x.dep = y.num
        and y.is_noun and y.rel is not "SUBJ"

