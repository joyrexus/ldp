***************
Word Categories
***************


====
Noun
====

All nouns of any kind, comprising the following subcategories:

Proper Noun
-----------

All proper nouns.

	has POS tag n:prop

* James
* Legos
* I speak German.

Negative Examples:

* I am a german woman.


Basic Noun
----------

All morphological nouns, including gerunds, excluding proper nouns and pronouns.

	has POS tag that starts with n: and is not neg or n:prop

Examples:
  
* chair
* The **writing** is on the wall.

Negative Examples:

* I want **some**. 
* I like **writing**.


Pronoun
-------

All pronouns of any kind, comprising all of the following subcategories:

Personal Pronoun
++++++++++++++++

Personal pronouns, excluding reflexives, possessives, and the impersonal pronoun.
	has POS tag pro and is not "it" 

* you
* them

Negative Examples:

* your
* it 
* himself

Demonstrative Pronoun
+++++++++++++++++++++

Demonstrative pronouns.

	has POS tag pro:dem

Examples:

* those
* I want *that*

Negative examples:

* *That* one.

Possessive Pronoun
++++++++++++++++++

Possessive pronouns, used as nominals and not determiners.

	has POS tag pro:poss and is not pro:poss:det

Examples:

* It's *hers*.

Negative examples:

* *Her* bike.

Impersonal Pronoun
++++++++++++++++++

All instances of the impersonal pronoun 'it'.
	
	has lemma 'it'

* *It*'s him.


Miscellaneous Pronoun
+++++++++++++++++++++

All pronouns which do not fall into the preceding specific categories of pronoun.

	has POS tag pro:indef, pro:exist, pro:refl, or pro:wh

* That *one*.
* *There* are three.
* *Himself*.


====
Verb
====

All verbs of all kinds, comprising the following categories:


Auxiliary Verb
---------------

All auxiliary verbs, including modals.

	has POS aux

*  I *was* running.
*  I *want* to go.

Basic Verb
----------

Verbs which are marked as full verbs or which are participles serving the role of a full verb, excluding the copula.

	has POS that begins with v *or* has POS part and one of the verbal GRs (CSUBJ, XSUBJ, CPRED, XPRED, CMOD, XMOD, COMP, XCOMP, CJCT, XJCT, ROOT)

* I was *running*.
* I *ran*.

Copula
------

The copula (the verb "to be") anytime it appears in the transcript.  This does not include auxilliary "be".

	has POS 'v' and lemma "be"	

* I *am* a doctor. 
* It *'s* nice *to be* friends.


===========
Conjunction
===========


Subordinating Conjunction
-------------------------

Number of uses of a conjunction other than {and, or, but}

* I went **because** I wanted to.
* **Before** he went, he saw me.

n.b.:  This count includes occasional cases where the conjunction does not introduce a clause, usually because the speaker halted mid-sentence.

* I don't think so **because** --


Dangling Coordinator
--------------------

Number of times that a coordinator appears, but does not actually coordinate two or more items.

* **And** then I went.
* **Or** not.

