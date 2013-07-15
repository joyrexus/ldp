.. |to| raw:: html

	<b><em>to</em></b>

.. |be| raw:: html

	<b><em>be</em></b>

.. |is| raw:: html

	<b><em>is</em></b>

.. |all| raw:: html

	<b><em>all</em></b>

.. |verbing| raw:: html

	<b><em>to be</em></b> + <b><em>done/finished</b></em> + <b>VERB<em>ing</em></b>

.. |done_finished| raw:: html

	<b><em>done/finished</b></em>

.. |to_study| raw:: html

	<b><em>to study</em></b>

.. |you| raw:: html

	<b><em>you</em></b>

.. |do_you_think| raw:: html

	<b><em>do you think</em></b>

.. |good_at| raw:: html

	<b><em>good at</em></b>

.. _mg-problems:

***************
Common problems
***************

After you have prepped a transcript and generated flags to catch probable errors,
you are ready to correct the morphosyntactic tagging.  The flags will point out
common problems, but it can't catch everything.  You don't have to correct only
those problems that are flagged; while you're looking at a flagged utterance, go
ahead and make sure everything in it is correct.  Likewise, if you happen to spot
a mistake in an unflagged utterance, you can fix that too (don't make a point to
look at unflagged utterances, but if your eye wanders and you happen to see some
mistakes, feel free to correct them).  The rule names should provide a clue as to
what may have been mistagged and will require your attention.

You will inevitably encounter some utterances which don't have an immediately
obvious solution.  There's a good chance that these problems have come up before
and have already been discussed.  This section outlines those troublesome
utterances and constructions and provides the conventions that have been
established to deal with them.  If you are ever stumped by an utterance, check
here to see if there is already a conventional solution for it.

.. _mg-problems-doc-abbrevs:

Abbreviations
=============

The following abbreviations are used in this document::

	POS		Part-of-speech (the tags found on the mor tier)
	GR		Grammatical Relationship (the tags found on the syn tier)
	NP  		Noun Phrase
	VP		Verb Phrase
	PP  		Prepositional Phrase

.. _mg-problems-pos:

Part of speech
==============

.. _mg-problems-go-to-sleep:

The phrase *go to sleep*
------------------------

The phrase "go to sleep" is coded as ``v|go prep|to n|sleep`` (as opposed
to something like ``v|go inf|to v|sleep``).  This is because it is
analogous to "go to bed", which is unambiguously a prepositional phrase.

Example::

	I want to go to bed .
	pro|I aux|want inf|to v|go prep|to n|bed .
	1|4|SUBJ 2|4|AUX 3|4|INF 4|0|ROOT 5|4|JCT 6|5|POBJ 7|4|PUNCT 

	I want to go to sleep .
	pro|I aux|want inf|to v|go prep|to n|sleep .
	1|4|SUBJ 2|4|AUX 3|4|INF 4|0|ROOT 5|4|JCT 6|5|POBJ 7|4|PUNCT 


.. _mg-problems-syntax:

Syntax
======

.. _mg-problems-v-np-to-v:

**V NP** |to| **V**
-------------------

The construction **V NP** |to| **V** (e.g. I want you to want me) can occur with a large
number of verbs in the first position and essentially limitless range of verbs in the
second position.  The **NP** is almost always an ``OBJ`` or ``PRED`` to the first verb,
and the |to| **V** phrase may be an ``XMOD`` to the **NP**, or an ``XJCT`` or ``XCOMP``
to the first verb.  The ``XCOMP`` scenario is by far the most common.

.. _mg-problems-v-np-to-v-xcomp:

``XCOMP``
#########

If the **NP** is semantically the subject of the |to| **V** phrase, mark the
**NP** as an ``OBJ`` or ``PRED`` to the first verb and mark the second verb as an
``XCOMP`` to the first verb.  We mark the **NP** as being dependent on the first verb
even though it is semantically the subject of the second verb because it is
inflected as though it were the object of the first verb, which is only seen
when the **NP** is a pronoun (e.g. "I need him to call me", not "I need he to
call me").

Example::

	I need him to call me .
	pro|I v|need pro|him inf|to v|call pro|me .
	1|2|SUBJ 2|0|ROOT 3|2|OBJ 4|5|INF 5|2|XCOMP 6|5|OBJ 7|2|PUNCT

	I want Buzz to come .
	pro|I v|want n:prop|Buzz inf|to v|come . 
	1|2|SUBJ 2|0|ROOT 3|2|OBJ 4|5|INF 5|2|XCOMP 6|2|PUNCT 

.. _mg-problems-v-np-to-v-xmod:

``XMOD``
########

If the **NP** is semantically an object of the second verb or the object of a
preposition dependent on that verb, mark the second verb as an ``XMOD`` to the
**NP**.  In the latter case, although the preposition will be marked ``prep`` on
the mor tier, the **NP** will not be a ``POBJ`` on the syn tier, so the preposition
will not have an explicitly marked ``POBJ``.

Example::

	those are big shoes to fill .
	pro:dem|those v|be&PRES adj|big n|shoe-PL inf|to v|fill .
	1|2|SUBJ 2|0|ROOT 3|4|MOD 4|2|PRED 5|6|INF 6|4|XMOD 7|2|PUNCT

	I need a sheet to write on .
	pro|I v|need det|a n|sheet inf|to v|write prep|on .
	1|2|SUBJ 2|0|ROOT 3|4|DET 4|2|OBJ 5|6|INF 6|4|XMOD 7|6|JCT 8|2|PUNCT

.. _mg-problems-v-np-to-v-xjct:

``XJCT``
########

If the **NP** is semantically unrelated to the |to| **V** phrase, (i.e.
semantically not an obligatory argument to any part of the second verb phrase),
mark it as an ``XJCT``. 

Example::

	I need caffeine to study .
	pro|I v|need n|caffeine inf|to v|study .
	1|2|SUBJ 2|0|ROOT 3|2|OBJ 4|5|INF 5|2|XJCT 6|2|PUNCT

	I'm climbing the wall to go save him .
	pro|I~aux|be&1S part|climb-PROG det|the n|wall inf|to v|go v|save pro|him . 
	1|3|SUBJ 2|3|AUX 3|0|ROOT 4|5|DET 5|3|OBJ 6|7|INF 7|8|SRL 8|3|XJCT 9|8|OBJ 10|3|PUNCT 


A good test to see whether a |to| **V** phrase should be an ``XJCT`` or not is to
add "in order" before the "to" and see if it makes sense and means the same thing.

Example::

	1a. I need you to study.
	1b. I need you in order to study.

	2a. I need caffeine to study.
	2b. I need caffeine in order to study.

The sentence *1b* is the same as *1a* with "in order" added to it.  While *1b*
does have a meaning, it is not the same as that of *1a*.  On the other hand, *2b*
is *2a* with "in order" added to it.  Since the meaning of *2b* is the same as
that of *2a*, you should mark |to_study| as ``XJCT``.

.. _mg-problems-v-np-v:

**V NP V**
----------

Very similar to **V NP** |to| **V** is the construction **V NP V** (e.g. make him
come here).  With this construction, however, the **NP** is only ever the semantic
subject of the second **VP**, and thus that **VP** is always coded as ``XCOMP``.
The most common verbs that introduce this construction are "make", "let", "help"
and the sensing verbs "see", "hear", and "feel".

Example::

	make that guy come here .
	v|make det|that n|guy v|come adv:loc|here .
	1|0|ROOT 2|3|DET 3|1|OBJ 4|1|XCOMP 5|4|JCT 6|1|PUNCT

	can you help me move this ?
	aux|can pro|you v|help pro|me v|move pro:dem|this ?
	1|3|AUX 2|3|SUBJ 3|0|ROOT 4|3|OBJ 5|3|XCOMP 6|5|OBJ 7|3|PUNCT

	I heard my phone ring .
	pro|I v|hear&PAST pro:poss:det|my n|phone v|ring .
	1|2|SUBJ 2|0|ROOT 3|4|DET 4|2|OBJ 5|2|XCOMP 6|2|PUNCT

.. _mg-problems-aux-gr:

``AUX`` and ``INF`` as head of a verb cluster
---------------------------------------------

If an auxiliary is acting in place of a full verb, add ``AUX-`` to the
beginning of what the GR would normally be.  Likewise, if an infinitive
is taking the place of a full verb, add ``INF-`` to the beginning.  Even
though an infinitive is obviously marking a non-finite verb, you can
still have ``INF-COMP`` or ``INF-CJCT`` if the first part of the verb
cluster is inflected (e.g. "he said he *is going to*" where *is going to*
is the verb cluster).

Example::

	yes I can .
	co|yes pro|I aux|can .
	1|3|COM 2|3|SUBJ 3|0|AUX-ROOT 4|3|PUNCT

	I don't want to .
	pro|I aux|do~neg|not aux|want inf|to .
	1|5|SUBJ 2|5|AUX 3|2|NEG 4|5|AUX 5|0|INF-ROOT 6|5|PUNCT

	I said I will .
	pro|I v|say&PAST pro|I aux|will .
	1|2|SUBJ 2|0|ROOT 3|4|SUBJ 4|2|AUX-COMP 5|2|PUNCT

	I said I don't want to .
	pro|I v|say&PAST pro|I aux|do~neg|not aux|want inf|to .
	1|2|SUBJ 2|0|ROOT 3|7|SUBJ 4|7|AUX 5|4|NEG 6|7|AUX 7|2|INF-COMP 8|2|PUNCT

.. _mg-problems-det-gr:

``DET`` as the head of a noun phrase
------------------------------------

Similar to ``AUX-`` and ``INF-``, if a determiner is taking the place of
a complete NP, add ``DET-`` to the beginning of the GR.  Note that this
only happens in incomplete or partially unintelligible utterances, or
when children misuse a possessive pronoun in place of a regular pronoun.
If it's possible to analyze a word as a ``pro:dem`` instead of as a
``det`` (e.g. "that" or "those"), use the ``pro:dem``.  If the only
option for the word is a ``det``, however, then add ``DET-`` to the GR.

Example::

	look at that dog .
	v|look ptl|at det|that n|dog .
	1|0|ROOT 2|1|PTL 3|4|DET 4|1|OBJ 5|1|PUNCT
	(Since the complete NP is there, "that" is a DET and "dog" is OBJ)

	look at that ### .
	v|look ptl|at pro:dem|that .
	1|0|ROOT 2|1|PTL 3|1|OBJ 4|1|PUNCT
	(Since the complete NP is missing, "that" is now OBJ.  Since it
	 has a pro:dem entry, however, we use pro:dem|that and do not add DET-)

	look at the dog .
	v|look ptl|at det|the n|dog .
	1|0|ROOT 2|1|PTL 3|4|DET 4|1|OBJ 5|1|PUNCT
	(Since the complete NP is there, "the" is a DET and "dog" is OBJ)

	look at the ### .
	v|look ptl|at det|the .
	1|0|ROOT 2|1|PTL 3|1|DET-OBJ 4|1|PUNCT
	(Since the complete NP is missing, "the" is now OBJ.  Since it
	 has only the one POS entry, det|the, add DET- to the GR)

The only words that just have a determiner entry, and thus would require
``DET-`` at the beggining of a GR are::

	the
	a
	an
	my
	your
	their
	our
	its

NOTE: We make an exception for numbers (which have POS ``det:num``), which
do not require anything added to the front of the GR.

.. _mg-problems-det-as-jct:

``det`` used as ``JCT``
-----------------------

There is one time when a ``det`` is not used as an actual determiner,
but we do not use the ``DET-`` tag, and that is with non-standard/babyish
uses of "a".  When "a" is used in some non-standard way (e.g. "a me want
it", "I'm a go over here"), leave its POS as ``det|a``, but change its GR to
``JCT``.  This way, it won't add to the count of NPs and won't affect the
number of clauses.

Example::

	I'm a go over here .
	pro|I~aux|be&1S det|a v|go prep|over adv:loc|here .
	1|4|SUBJ 2|4|AUX 3|4|JCT 4|0|ROOT 5|4|JCT 6|5|POBJ 7|4|PUNCT

	a look up microscopic creatures .
	det|a v|look ptl|up adj|microscopic n|creature-PL . 
	1|2|JCT 2|0|ROOT 3|2|PTL 4|5|MOD 5|2|OBJ 6|2|PUNCT 

.. _mg-problems-apposition:

Nominals in apposition
----------------------

When there are two nominals in apposition, the first phrase is the head
and the second is a ``MOD`` to the first.

Example::

	my friend Paul is here .
	pro:poss:det|my n|friend n:prop|Paul v|be&3S adv:loc|here .
	1|2|DET 2|4|SUBJ 3|2|MOD 4|0|ROOT 5|4|PRED 6|4|PUNCT

This rule encompasses phrases like "the number three", "the letter b",
or "the year two+thousand".

Example::

	can you find the letter b@l ?
	aux|can pro|you v|find det|the n|letter n:let|b ?
	1|3|AUX 2|3|SUBJ 3|0|ROOT 4|5|DET 5|3|OBJ 6|5|MOD 7|3|PUNCT

	you were born in the year two+thousand .
	pro|you aux|be&PAST part|bear&PERF prep|in det|the n|year det:num|two+thousand .
	1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|JCT 5|6|DET 6|4|POBJ 7|6|MOD 8|3|PUNCT

.. _mg-problems-pro-as-det:

Pronouns used as determiners
----------------------------

Sometimes a pronoun (e.g. me) is used like a possessive pronoun (e.g. my).
If that happens, code everything else as though the ``pro`` were indeed a
``pro:poss:det``.  However, instead of coding the ``pro`` as a ``DET``, mark
it as a ``MOD``.  A ``pro`` can only be used in this way if the head of the
NP has no other determiner, although it may have a ``MOD`` or a ``QUANT``.

Although this pattern is often used for non-standard English (e.g. "now
where's me toothpick?", "you won't catch them bad guys"), it is also 
frequently used in the standard English construction |you| **NP**, the
most common example of which is "you guys".

Example::

	you guys are noisy .
	pro|you n|guy-PL v|be&PRES adj|noisy .
	1|2|MOD 2|3|SUBJ 3|0|ROOT 4|3|PRED 5|3|PUNCT

	that's not it, you silly goose .
	pro:dem|that~v|be&3S neg|not pro|it pro|you adj|silly n|goose .
	1|2|SUBJ 2|0|ROOT 3|2|NEG 4|2|PRED 5|7|MOD 6|7|MOD 7|2|VOC 8|2|PUNCT

	them three ninjas are sneaky .
	pro|them det:num|three n|ninja-PL v|be&PRES adj|sneaky .
	1|3|MOD 2|3|QUANT 3|4|SUBJ 4|0|ROOT 5|4|PRED 6|4|PUNCT

	him bike is fast .
	pro|him n|bike v|be&3S adj|fast .
	1|2|MOD 2|3|SUBJ 3|0|ROOT 4|3|PRED 5|3|PUNCT

.. _mg-problems-no-copula:

Missing copulae
---------------

If there is a pronoun followed by an NP that *does* include a ``DET``,
this is probably a clause that is missing a copula (e.g. "you a silly
goose", "them the ninjas").  In this case, mark what would have been
the ``PRED`` as the ``ROOT`` (or whatever the head of that clause would
be).  Keep what would have been the ``SUBJ`` as the ``SUBJ``, but make
it dependent on what was formerly the ``PRED``.

Example::

	you are a silly goose .
	pro|you v|be&PRES det|a adj|silly n|goose .
	1|2|SUBJ 2|0|ROOT 3|5|DET 4|5|MOD 5|2|PRED 6|2|PUNCT

	you a silly goose .
	pro|you det|a adj|silly n|goose .
	1|4|SUBJ 2|4|DET 3|4|MOD 4|0|ROOT 5|4|PUNCT

	I thought them were the ninjas .
	pro|I v|think&PAST pro|them v|be&PAST det|the n|ninja-PL .
	1|2|SUBJ 2|0|ROOT 3|4|SUBJ 4|2|COMP 5|6|DET 6|4|PRED 7|2|PUNCT

	I thought them the ninjas .
	pro|I v|think&PAST pro|them det|the n|ninja-PL .
	1|2|SUBJ 2|0|ROOT 3|5|SUBJ 4|5|DET 5|2|COMP 6|2|PUNCT

The last example is obviously non-standard English, but it would
be the same format, and more clearly a missing-copula construction,
if the pronoun had been "they" instead of "them".

ADD MORE ABOUT MISSING COPULAE HEREHEREHERE

.. _mg-problems-no-copula-vs-post-mod:

Missing copula vs. post-positioned ``MOD``
------------------------------------------

If you encounter an NP followed by a locative adverb or a PP, it may be a missing
copula construction, but it may also be an NP with a post-positioned ``MOD`` or a
sentence fragment containing an NP and a ``JCT``.  You must use the context of the
utterance to determine how it's being used.  The utterance "that guy in the car",
for example, could be any of of those constructions:

Example::

	Missing Copula:

	(playing with toy figures)
	\*MOT:	where is this guy going to be ?
	\*CHI:	that guy in the car .
	%mor:	det|that n|guy prep|in det|the n|car .
	%syn:	1|2|DET 2|3|SUBJ 3|0|ROOT 4|5|DET 5|3|POBJ 6|3|PUNCT

	Post-positioned MOD:

	\*CHI:	now he's sleeping .
	\*MOT:	who's sleeping ?
	\*CHI:	that guy in the car .
	%mor:	det|that n|guy prep|in det|the n|car .
	%syn:	1|2|DET 2|0|ROOT 3|2|MOD 4|5|DET 5|3|POBJ 6|2|PUNCT

	Sentence fragment with JCT:

	\*MOT:	should we put this guy in the car or that guy in the car ?
	\*CHI:	that guy in the car .
	%mor:	det|that n|guy prep|in det|the n|car .
	%syn:	1|2|DET 2|0|ROOT 3|2|JCT 4|5|DET 5|3|POBJ 6|2|PUNCT

.. _mg-problems-thing-post-mod:

Post-positioned ``MOD``\s after *-thing*, *-body*, and *-one* words
-------------------------------------------------------------------

In general, the only post-positioned ``MOD``\s (that is, where the ``MOD``
comes after the NP) will be prepositional phrases (e.g. the guy *in the car*).
The major exception, however, is when the noun phrase is one of the
*-thing*, *-body*, or *-one* words (i.e. nothing, something, anything,
everything, nobody, somebody, anybody, everybody, noone, someone,
anyone, everyone), in which case the ``MOD`` following may be any adjective
or the word "else" with POS ``post``.

Example::

	do you want something else ?
	aux|do pro|you v|want pro:indef|anything post|else ?
	1|3|AUX 2|3|SUBJ 3|0|ROOT 4|3|OBJ 5|4|MOD 6|3|PUNCT

	you can't have anything sweet .
	pro|you aux|can~neg|not v|have pro:indef|anything adj|sweet .
	1|4|SUBJ 2|4|AUX 3|2|NEG 4|0|ROOT 5|4|OBJ 6|5|MOD 7|4|PUNCT

	there's nobody cooler than him .
	pro:exist|there~v|be&3S pro:indef|nobody adj|cool-CP prep|than pro|him .
	1|2|ESUBJ 2|0|ROOT 3|2|PRED 4|3|MOD 5|4|JCT 6|5|POBJ 7|2|PUNCT

	everyone else can go .
	pro:indef|everyone post|else aux|can v|go .
	1|4|SUBJ 2|1|MOD 3|4|AUX 4|0|ROOT 5|4|PUNCT

.. _mg-problems-subj-after-verb:

``SUBJ`` after ``ROOT``
-----------------------
	
Naturally, in a standard declarative utterance, the ``SUBJ`` comes
before the ``ROOT``.  A common exception to this happens when the words
"here/there" are used in conjunction with the verbs "be/come/go".
In those cases, the ``JCT`` or ``PRED`` (whichever GR "here/there" is
fulfilling) comes first, followed by the verb, followed by the ``SUBJ``.

Example::

	here comes the car .
	adv:loc|here v|come-3S det|the n|car .
	1|2|JCT 2|0|ROOT 3|4|DET 4|2|SUBJ 5|2|PUNCT

	there goes my baby .
	adv:loc|there v|go-3S pro:poss:det|my n|baby .
	1|2|JCT 2|0|ROOT 3|4|DET 4|2|SUBJ 5|2|PUNCT

	here's your doll .
	adv:loc|here~v|be&3S pro:poss:det|your n|doll .
	1|2|PRED 2|0|ROOT 3|4|DET 4|2|SUBJ 5|2|PUNCT

Unless "here/there" is used with "be/come/go", any nominal coming
after the verb is almost definitely an ``OBJ`` (unless you think
there's a very good reason that the thing coming after is a ``SUBJ``,
but it's unlikely).

.. _mg-problems-post-quant:

Post-positioned quantifiers
---------------------------

Quantifiers usually precede the NP they are quantifying (e.g. "all my children",
"both candidates"), but it's possible for the quantifier to come after the
quantified NP, especially when that NP is the ``SUBJ`` ("my children all want to
come").  The quantifier can even be separated by an auxiliary or a copula ("my
children are all adults now", "my children can all ride unicycles").

Example::

	we both are tired .
	pro|we qn|both v|be&PRES part|tire-PERF .
	1|3|SUBJ 2|1|QUANT 3|0|ROOT 4|3|PRED 5|3|PUNCT

	we are both tired .
	pro|we v|be&PRES qn|both part|tire-PERF .
	1|2|SUBJ 2|0|ROOT 3|1|QUANT 4|2|PRED 5|2|PUNCT

	the guests will each receive a copy .
	det|the n|guest-PL aux|will qn|each v|receive det|a n|copy .
	1|2|DET 2|5|SUBJ 3|5|AUX 4|2|QUANT 5|0|ROOT 6|7|DET 7|5|OBJ 8|5|PUNCT

	I'll show them all .
	pro|I~aux|will v|show pro|them qn|all .
	1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|OBJ 5|4|QUANT 6|3|PUNCT

.. _mg-problems-part-pred-vs-passive:

Perfect participle as ``PRED`` vs. passive construction
-------------------------------------------------------

At some point you will probably encounter a construction like **NP** |be| **PART**
(e.g. "the toy was broken") and you will have to decide whether it should be coded
as a copula construction (i.e.  ``1|2|DET 2|3|SUBJ 3|0|ROOT 4|3|PRED``) or as a
passive construction (i.e. ``1|2|DET 2|4|SUBJ 3|4|AUX 4|0|ROOT``).

Example::

	Copula:
		the toy was broken .
		det|the n|toy v|be&PAST&13S part|break&PERF .
		1|2|DET 2|3|SUBJ 3|0|ROOT 4|3|PRED 5|3|PUNCT

	Passive:
		the toy was broken .
		det|the n|toy aux|be&PAST&13S part|break&PERF .
		1|2|DET 2|4|SUBJ 3|4|AUX 4|0|ROOT 5|4|PUNCT

Notice that in the copula construction, "be" is marked as a full verb on the mor
tier, as well as being marked ``ROOT`` (or another verbish GR) on the syn tier
and the participle is a ``PRED`` to "be".  In a passive construction, "be" is
marked ``aux`` on the mor tier and ``AUX`` on the syn tier, while the participle
takes over the verbish GR on the syn tier.

So how do you decide which way to code it?  It depends on the context and what you
think the meaning of the sentence is.

.. _mg-problems-part-pred:

As ``PRED``
###########

If the utterance is meant to describe the state of something at a given timepoint,
you probably want to use the copula construction::

	Copula:
		*MOT:	do you want to look at the painting ?

		*CHI:	where is it ?

		*MOT:	it is attached to the wall .
		%mor:	pro|it v|be&3S part|attach-PERF prep|to det|the n|wall .
		%syn:	1|2|SUBJ 2|0|ROOT 3|2|PRED 4|3|JCT 5|6|DET 6|4|POBJ 7|2|PUNCT

In the previous exchange, the mother reports the state of the picture as being
attached to the wall.  The painting does not undergo any change and is not acted
upon.  You can also see how the utterance in question would be coded as a copula
construction.

.. _mg-problems-part-passive:

As passive construction
#######################

If, on the other hand, the utterance is describing a process or an event that
something experienced, you probably want to use the passive construction::

	Passive:
		*MOT:	when the painter finishes, he frames his painting .

		*CHI:	and then what happens ?

		*MOT:	it is attached to the wall .
		%mor:	pro|it aux|be&3S part|attach-PERF prep|to det|the n|wall .
		%syn:	1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|JCT 5|6|DET 6|4|POBJ 7|3|PUNCT

In the previous exchange, the mother describes a process that the painting undergoes,
namely somebody attaching the painting to the wall.  Again, you can see how the
utterance would be coded, this time as a passive construction.

More examples::

	Copula:
		*CHI:	why did he look like a chicken ?

		*MOT:	he was covered in feathers .
		%mor:	pro|he v|be&PAST&13S part|cover-PERF prep|in n|feather-PL .
		%syn:	1|2|SUBJ 2|0|ROOT 3|2|PRED 4|3|JCT 5|4|POBJ 6|2|PUNCT

	Passive:
		*CHI:	what happened after they tarred him ?

		*MOT:	he was covered in feathers .
		%mor:	pro|he aux|be&PAST&13S part|cover-PERF prep|in n|feather-PL .
		%syn:	1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|JCT 5|4|POBJ 6|3|PUNCT

Now that you know the actual reasons for choosing copula vs.  passive
constructions, it may also be useful to know that passive constructions come up
much less frequently in our data than copula constructions do.

.. _mg-problems-compound-preps:

Compound (multi-word) prepositions
----------------------------------

You will sometimes encounter "compound prepositions" comprising either two
``prep``\s or an ``adv``/``adv:loc`` followed by a ``prep`` (usually "of" or
"to").  When this happens, the first part is the head of the construction (and
thus is the ``JCT`` or ``PRED`` or whatever GR to something else), while the
second part is a ``JCT`` to the first part.  The most common examples of these
"compound prepositions" are "out of" and "next to".

Example::

	take the sandwich out of the bag .
	v|take det|the n|sandwich adv:loc|out prep|of det|the n|bag .
	1|0|ROOT 2|3|DET 3|1|OBJ 4|1|JCT 5|4|JCT 6|7|DET 7|5|POBJ 8|1|PUNCT

	put it next to the table .
	v|put pro|it adv|next prep|to det|the n|table .
	1|0|ROOT 2|1|OBJ 3|1|LOC 4|3|JCT 5|6|DET 6|4|POBJ 7|1|PUNCT

	I want to sit next to you .
	pro|I aux|want inf|to v|sit adv|next prep|to pro|you .
	1|4|SUBJ 2|4|AUX 3|4|INF 4|0|ROOT 5|4|JCT 6|5|JCT 7|6|POBJ 8|4|PUNCT

.. _mg-problems-pp-as-pobj:

Prepositional phrase as object of another preposition
-----------------------------------------------------

Although it doesn't happen very often, you may encounter a preposition whose
argument is not an NP but a PP (e.g. for in the house).  Code these the same way
you would code compound prepositions, with the first ``prep`` being the ``PRED``,
``JCT``, etc. and the second ``prep`` being a ``JCT`` to the first.

Example::

	the little ones are for in the house .
	det|the adj|little pro:indef|one-PL v|be&PRES prep|for prep|in det|the n|JCT .
	1|3|DET 2|3|MOD 3|4|SUBJ 4|0|ROOT 5|4|PRED 6|5|JCT 7|8|DET 8|6|POBJ 9|4|PUNCT

	here is your snacks from around the world .
	adv:loc|here v|be&3S pro:poss:det|your n|snack-PL prep|from prep|around det|the n|world .
	1|2|PRED 2|0|ROOT 3|4|DET 4|2|SUBJ 5|4|MOD 6|5|JCT 7|8|DET 8|6|POBJ 9|2|PUNCT

.. _mg-problems-dangling-coord:

Dangling ``COORD``\s
--------------------

If you have two independent clauses joined by a coordinating conjunction,
each of those clauses is a ``COORD`` dependent on the conjucntion, which
takes over as ``ROOT`` of the utterance.  If you have a coordinating
conjunction that's only "coordinating" one clause, it still takes over as
the ``ROOT`` while the one clause is a ``COORD`` dependent on the
conjunction.

Example::

	I will always love you .
	pro|I aux|will adv|always v|love pro|you .
	1|4|SUBJ 2|4|AUX 3|4|JCT 4|0|ROOT 5|4|OBJ 6|4|PUNCT

	and I will always love you .
	conj:coo|and pro|I aux|will adv|always v|love pro|you .
	1|0|ROOT 2|5|SUBJ 3|5|AUX 4|5|JCT 5|1|COORD 6|5|OBJ 7|1|PUNCT

	I'd like to tell you .
	pro|I~aux|will&COND aux|like inf|to v|tell pro|you .
	1|5|SUBJ 2|5|AUX 3|5|AUX 4|5|INF 5|0|ROOT 6|5|OBJ 7|5|PUNCT

	I'd like to tell you but +..
	pro|I~aux|will&COND aux|like inf|to v|tell pro|you conj:coo|but +..
	1|5|SUBJ 2|5|AUX 3|5|AUX 4|5|INF 5|7|COORD 6|5|OBJ 7|0|ROOT 8|7|PUNCT

This also includes a phrase that itself comprises two coordinated clauses.  The
head of the coordinated phrase, which in this case is a coordinator, is still the
``COORD`` dependent on the dangling coordinator.

Example::

	I'll love him and walk him every day .
	pro|I~aux|will v|love pro|him conj:coo|and v|walk pro|him qn|every n|day .
	1|3|SUBJ 2|3|AUX 3|5|COORD 4|3|OBJ 5|0|ROOT 6|5|COORD 7|6|OBJ 8|9|QUANT 9|6|JCT 10|5|PUNCT

	and I'll love him and walk him every day .
	conj:coo|and pro|I~aux|will v|love pro|him conj:coo|and v|walk pro|him qn|every n|day .
	1|0|ROOT 2|4|SUBJ 3|4|AUX 4|6|COORD 5|4|OBJ 6|1|COORD 7|6|COORD 8|7|OBJ 9|10|QUANT 10|7|JCT 11|1|PUNCT

.. _mg-problems-pred-words:

When to use ``PRED``
--------------------

A ``PRED`` is used to give information about the state or condition of the
``SUBJ``.  A ``PRED`` can be just about any part-of-speech, most commonly ``n``,
``n:prop``, ``adj``, ``adv:loc``, and ``prep``.  In incomplete utterances, they
may even be ``det``.  The most common verb with which a ``PRED`` occurs is "be",
but can also occur with the verbs "get", "seem", "appear", and verbs of sensing,
or rather of being sensed (i.e. sound, look, smell, taste, feel).

Example::

	he is very smart .
	pro|he v|be&3S adv:int|very adj|smart .
	1|2|SUBJ 2|0|ROOT 3|4|JCT 4|2|PRED 5|2|PUNCT
	
	are they in the car ?
	v|be&PRES pro|they prep|in det|the n|car ?
	1|0|ROOT 2|1|SUBJ 3|1|PRED 4|5|DET 5|3|POBJ 6|1|PUNCT

	it seems friendly .
	pro|it v|seem-3S adj:n|friend-LY .
	1|2|SUBJ 2|0|ROOT 3|2|PRED 4|2|PUNCT

	this tastes kind+of funny .
	pro:dem|this v|taste-3S adv|kind+of adj|funny .
	1|2|SUBJ 2|0|ROOT 3|4|JCT 4|2|PRED 5|2|PUNCT

	I don't feel good .
	pro|I aux|do~neg|not v|feel adj|good .
	1|4|SUBJ 2|4|AUX 3|2|NEG 4|0|ROOT 5|4|PRED 6|4|PUNCT

	she looks like a good student .
	pro|she v|look-3S prep|like det|a adj|good n|student .
	1|2|SUBJ 2|0|ROOT 3|2|PRED 4|6|DET 5|6|MOD 6|3|POBJ 7|2|PUNCT

``PRED`` may also occur with the verbs "make", "want", and "need" after the
``OBJ`` of the verb.  Only use a ``PRED``, however, if you could insert the
word(s) "(to) be" between the ``OBJ`` and the ``PRED`` and maintain the same
meaning.

Example::

	Good:
	      make that one red 	=> 	make that one be red

	      he wants that over here 	=>	he wants that to be over here

	      I need you very quiet	=>	I need you to be very quiet

	Bad:
	      (where should we make our cake?)
	      let's make it over here	=>	let's make it be over here

	      I want that for my car	=>	I want that to be for my car

	      she needs you real quick	=>	she needs you to be real quick


In the first set of examples, you can add "(to) be" between the ``OBJ`` and the
adjective or PP and the meaning remains the same, so that ``adj`` or PP should
be marked ``PRED``.  In the second set of examples, while the utterances with
"to be" are grammatical, they do not mean the same thing as the utterances
without "to be", so those PPs and ``adv``\s should be coded as ``JCT``.

Example::

	make that one red .
	v|make det|that pro:indef|one adj|red .
	1|0|ROOT 2|3|DET 3|1|OBJ 4|1|PRED 5|1|PUNCT

	I need you in here right now .
	pro|I v|need pro|you prep|in adv:loc|here adv|right adv|now .
	1|2|SUBJ 2|0|ROOT 3|2|OBJ 4|2|PRED 5|4|POBJ 6|7|JCT 7|2|JCT 8|2|PUNCT

	let's make him the captain .
	aux|let's v|make pro|him det|the n|captain .
	1|2|AUX 2|0|ROOT 3|2|OBJ 4|5|DET 5|2|PRED 6|2|PUNCT

	(where should be make this ?)
	let's make it over here .
	aux|let's v|make pro|it prep|over adv:loc|here .
	1|2|AUX 2|0|ROOT 3|2|OBJ 4|2|PRED 5|4|POBJ 6|2|PUNCT

Notice that in order for one of these three verbs to have a ``PRED``, it must
also have an ``OBJ`` that comes first.

.. _mg-problems-tags:

Using the ``TAG`` GR
--------------------
	
The ``TAG`` code is used on the syn tier for the head of a verb cluster that is
either a full verb/participle or an auxiliary on the mor tier, but that should
not be counted as adding to the number of clauses of the utterance.  There are
three occasions when you will use the ``TAG`` code on the syn tier:

	#) Negated auxiliary/copula tags (e.g. he's fast, isn't he?)
	#) Sentence fragments containing a full verb.  These are sometimes
	   properly transcribed utterances (e.g. this goes on top, see?).
	#) Full sentences with no grammatical connection that are on the
	   same line as another utterance.  These are the result of incorrect
	   transcription (e.g. let's go, we're late.)

.. _mg-problems-tags-negated:

Negated auxiliary/copula tags
#############################

These are a valid construction in standard English, but we don't want these
phrases to add to the complexity (i.e. clause count) of the utterance, so we
mark them as ``TAG``.  The ``TAG`` is dependent on whatever phrase the auxiliary
or copula is referencing, usually the ``ROOT``.

Example::

	he's fast, isn't he ?
	pro|he~v|be&3S adj|fast v|be&3S~neg|not pro|he ?
	1|2|SUBJ 2|0|ROOT 3|2|PRED 4|2|TAG 5|4|NEG 6|4|SUBJ 7|2|PUNCT

	she was laughing a+lot, wasn't she ?
	pro|she aux|be&PAST&13S part|laugh-PROG adv|a+lot aux|be&PAST&13S~neg|not pro|she ?
	1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|JCT 5|3|TAG 6|5|NEG 7|5|SUBJ 8|3|PUNCT

	I thought gosh he's fast, isn't he ?
	pro|I v|think&PAST co|gosh pro|he~v|be&3S adj|fast v|be&3S~neg|not pro|he ?
	1|2|SUBJ 2|0|ROOT 3|5|COM 4|5|SUBJ 5|2|COMP 6|5|PRED 7|5|TAG 8|7|NEG 9|7|SUBJ 10|2|PUNCT

.. _mg-problems-tags-fragment:

Sentence fragment with full verb
################################

While these types of utterances aren't technically considered one sentence
in standard English, our transcription rules allow some verbs with no
arguments (or sometimes one object argument, so long as the verb is in
imperative form) to be transcribed on the same line (see `Rule 4.9 <tg-4-9>`).
However, we still don't want these verbs to add to the complexity/clause
count, so we mark them as ``TAG``.  These are almost always dependent on
``ROOT`` or, in the case of coordinated clauses, on the closest head of an
independent clause (I can't think of when it wouldn't be, but if you think
there's a good reason for something not to be dependent on ``ROOT``, it's not
prohibited).

Example::

	this goes on top, see ?
	pro:dem|this v|go-3S prep|on n|top v|see ?
	1|2|SUBJ 2|0|ROOT 3|2|JCT 4|3|POBJ 5|2|TAG 6|2|PUNCT

	remember, we have to go to practice .
	v|remember pro|we aux|have inf|to v|go prep|to n|practice .
	1|5|TAG 2|5|SUBJ 3|5|AUX 4|5|INF 5|0|ROOT 6|5|JCT 7|6|POBJ 8|5|PUNCT

.. _mg-problems-tags-full:

Full sentence with no grammatical connection
############################################

Unfortunately, transcribers are not perfect, and sometimes you will see
an utterance that does not conform to our transcription rules regarding
utterance boundaries.  While we can make slight changes to single words
which are clearly typos (e.g. "its in the box" => "it's in the box", or
"do you have they're number" => "do you have their number"), we cannot
split an utterance into two utterances.  So if you encounter something
like "let's go, we're late" you'll have to make do with what you have.

There are two options for dealing with an extraneous clause like this:
mark it as ``TAG``, so that it doesn't add to the clause count, or mark it
as ``CJCT``/``XJCT``, so that it does add to the clause count.  In general,
I mark phrases like this as a ``CJCT``/``XJCT`` if it seems more
semantically meaningful, and as ``TAG`` if it seems more like a throw-away
phrase that doesn't carry much meaning.  By throw-away, I mean things like
"I know", "you know (what)", "I guess", "that's right", "you're right",
"let's go", etc.  If you come across two unconnected, semantically meaningful
utterances on the same line, in general just mark the first one as ``ROOT``
and the second as ``CJCT``/``XJCT`` (again, unless you think there's a good
reason to do it the other way around; there's no rule against it).

Example::

	Throw-away phrases, mark as TAG:

	let's go, we're late .
	aux|let's v|go pro|we~v|be&PRES adj|late .
	1|2|AUX 2|4|TAG 3|4|SUBJ 4|0|ROOT 5|4|PRED 6|4|PUNCT

	you know what, we already have that .
	pro|you v|know pro:wh|what pro|we adv|already v|have pro:dem|that .
	1|2|SUBJ 2|6|TAG 3|2|OBJ 4|6|SUBJ 5|6|JCT 6|0|ROOT 7|6|OBJ 8|6|PUNCT

	there's always next year, I guess .
	pro:exist|there~v|be&3S adv|always adj|next n|year pro|I v|guess .
	1|2|ESUBJ 2|0|ROOT 3|2|JCT 4|5|MOD 5|2|PRED 6|7|SUBJ 7|2|TAG 8|2|PUNCT

	Semantically meaningful phrases, mark as CJCT/XJCT:

	you can't go there, Mark is in there .
	pro|you aux|can~neg|not v|go adv:loc|there n:prop|Mark v|be&3S prep|in adv:loc|there .
	1|4|SUBJ 2|4|AUX 3|2|NEG 4|0|ROOT 5|4|JCT 6|7|SUBJ 7|4|CJCT 8|7|PRED 9|8|POBJ 10|4|PUNCT

	he'll go in the car, you take the train .
	pro|he~aux|will v|go prep|in det|the n|car pro|you v|take det|the n|train .
	1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|JCT 5|6|DET 6|4|POBJ 7|8|SUBJ 8|3|CJCT 9|10|DET 10|8|OBJ 11|3|PUNCT

.. _mg-problems-done-verbing:

The phrase |verbing|
--------------------

The very common construction |verbing| (e.g. he is done working) is coded
such that |done_finished| is a ``PRED`` of |be| and the ``part|verb-PROG``
is an ``XCOMP`` of |done_finished|.

Example::

	she is done singing .
	pro|she v|be&3S part|do&PERF part|sing-PROG .
	1|2|SUBJ 2|0|ROOT 3|2|PRED 4|3|XCOMP 5|2|PUNCT

	are you finished eating ?
	v|be&PRES pro|you part|finish-PERF part|eat-PROG ?
	1|0|ROOT 2|1|SUBJ 3|1|PRED 4|3|XCOMP 5|1|PUNCT

	you can nap when she's done recording .
	pro|you aux|can v|nap conj:subor|when pro|she~v|be&3S part|do&PERF part|record-PROG .
	1|3|SUBJ 2|3|AUX 3|0|ROOT 4|6|CPZR 5|6|SUBJ 6|3|CJCT 7|6|PRED 8|7|XCOMP 9|3|PUNCT

.. _mg-problems-qn-vs-pro-indef:

Quantifiers and *quantifier + of* phrases
-----------------------------------------

The following words can be used to quantify a noun phrase in two different ways,
but with slightly different coding used in each case::

	all, any, both, each, either, enough, few, half,
	many, more, most, much, plenty, several, some

If any of these words is followed directly by a noun phrase, mark it as ``qn`` on
the mor tier and ``QUANT`` on the syn tier, dependent on the head of the NP.

Example::

	give me all your money .
	v|give pro|me qn|all pro:poss:det|your n|money .
	1|0|ROOT 2|1|OBJ2 3|5|QUANT 4|5|DET 5|1|OBJ 6|1|PUNCT

	some kids don't like chocolate .
	qn|some n|kid-PL aux|do~neg|not v|like n|chocolate .
	1|2|QUANT 2|5|SUBJ 3|5|AUX 4|3|NEG 5|0|ROOT 6|5|OBJ 7|5|PUNCT

If, however, there is the preposition "of" between the word and the NP, mark the
word as ``pro:indef`` on the mor tier and whatever the GR of the NP would have
been on the syn tier (e.g. ``OBJ`` or ``SUBJ``).  Then, mark "of" as a ``MOD`` to
the ``pro:indef``, and mark the head of the NP as a ``POBJ`` to "of".

Example::

	give me all of your money .
	v|give pro|me pro:indef|all prep|of pro:poss:det|your n|money .
	1|0|ROOT 2|1|OBJ2 3|1|OBJ 4|3|MOD 5|6|DET 6|4|POBJ 7|1|PUNCT

	some of the kids don't like chocolate .
	pro:indef|some prep|of det|the n|kid-PL aux|do~neg|not v|like n|chocolate .
	1|7|SUBJ 2|1|MOD 3|4|DET 4|2|POBJ 5|7|AUX 6|5|NEG 7|0|ROOT 8|7|OBJ 9|7|PUNCT

.. _mg-problems-voc:

When to use ``VOC``
-------------------

Any time a word is used as a vocative (that is, when it identifies to whom an
utterance is addressed), code it as ``VOC``.  Common vocatives include "honey",
"sweetie", and "sir".  These words, when used in this sense, get the POS code
``co:voc`` and the GR code ``VOC``:

Example::

	do you want some more, sweetie ?
	aux|do pro|you v|want qn|some pro:indef|more co:voc|sweetie ?
	1|3|AUX 2|3|SUBJ 3|0|ROOT 4|5|QUANT 5|3|OBJ 6|3|VOC 7|3|PUNCT
	
	honey, I can't understand you .
	co:voc|honey pro|I aux|can~neg|not v|understand pro|you .
	1|5|VOC 2|5|SUBJ 3|5|AUX 4|3|NEG 5|0|ROOT 6|5|OBJ 7|5|PUNCT

Proper nouns are also very frequently used as vocatives, especially the proper
nouns "Mom/Mommy" and "Dad/Daddy," although any proper noun can be used as a
vocative.  In fact, any noun can be used as a vocative, though common nouns are
less likely to be used in that way, although it does happen (especially when kids
are talking to their toys).

Example::

	Mom, can I have some more ?
	n:prop|Mom aux|can pro|I v|have qn|some pro:indef|more ?
	1|4|VOC 2|4|AUX 3|4|SUBJ 4|0|ROOT 5|6|QUANT 6|4|OBJ 7|4|PUNCT

	you've had enough, David .
	pro|you~aux|have part|have&PERF pro:indef|enough n:prop|David .
	1|3|SUBJ 2|3|AUX 3|0|ROOT 4|3|OBJ 5|3|VOC 6|3|PUNCT

	come here, ball !
	v|come adv:loc|here n|ball !
	1|0|ROOT 2|1|JCT 3|1|VOC 4|1|PUNCT

	horsie, wake up !
	n|horse-DIM v|wake ptl|up !
	1|2|VOC 2|0|ROOT 3|2|PTL 4|2|PUNCT

.. _mg-problems-nps:

Structure of a noun phrase
--------------------------

A noun phrase can consist of the base noun plus a ``DET``, a ``QUANT``,
or both.  (e.g. all my friends, those two guys).  There should never be
two ``DET``\s; if there are, you should probably just delete the first one
on the assumption that it was an error or, if the speaker is the child and
the first ``DET`` is "a", mark it as a ``JCT`` (e.g. "a this one, Mommy";
see `"det" used as "JCT" <mg-problems-det-as-jct>`).  This is because young
children often use "a" in non-standard ways, and we want to track that.

Standard English does allow two quantifiers to be used in the same noun
phrase.  However, we only code them both as ``QUANT`` to the noun if one
has the POS code ``quant`` and the other has ``det:num``.  If, however,
two words with POS code ``quant`` are used, we mark the first one as a
``JCT`` to the second, which is a ``QUANT`` to the noun.
GIVE A REASON HEREHEREHERE!!!

Example::

	all my friends are coming .
	qn|all pro:poss:det|my n|friend-PL aux|be&PRES part|come-PROG .
	1|3|QUANT 2|3|DET 3|5|SUBJ 4|5|AUX 5|0|ROOT 6|5|PUNCT

	those two guys are my friends .
	det|thos det:num|two n|guy-PL v|be&PRES pro:poss:det|my n|friend-PL .
	1|3|DET 2|3|QUANT 3|4|SUBJ 4|0|ROOT 5|6|DET 6|4|PRED 7|4|PUNCT

	do it one more time .
	v|do pro|it det:num|one qn|more n|time .
	1|0|ROOT 2|1|OBJ 3|5|QUANT 4|5|QUANT 5|1|JCT 6|1|PUNCT

	hold up all five fingers .
	v|hold ptl|up qn|all det:num|five n|finger-PL .
	1|0|ROOT 2|1|PTL 3|5|QUANT 4|5|QUANT 5|1|OBJ 6|1|PUNCT

	give me some more chips .
	v|give pro|me qn|some qn|more n|chip-PL .
	1|0|ROOT 2|1|OBJ 3|4|JCT 4|5|QUANT 5|1|OBJ 6|1|PUNCT

.. _mg-problems-wh-comp:

``COMP``\s and ``CPRED``\s introduce by WH-words
------------------------------------------------

You will frequently see a subordinate clause introduced by a WH-word (i.e. who,
what, where, when, why, how).  If you see this, code the clause as a ``COMP``
(or ``CPRED``, and very occasionally ``CSUBJ``, if the matrix verb is "be") and
code the WH-word as though it were part of the subordinate clause.  DO NOT code
the WH-word as part of the matrix clause and then code the subordinate clause as
a ``CMOD``/``CJCT`` to the WH-word.

Example::

	I know who you are talking about .
	pro|I v|know pro:wh|who pro|you aux|be&PRES part|talk-PROG prep|about .
	1|2|SUBJ 2|0|ROOT 3|7|POBJ 4|6|SUBJ 5|6|AUX 6|2|COMP 7|6|JCT 8|2|PUNCT

	I'll do what I want .
	pro|I~aux|will v|do pro:wh|what pro|I v|want .
	1|3|SUBJ 2|3|AUX 3|0|ROOT 4|6|OBJ 5|6|SUBJ 6|3|COMP 7|3|PUNCT

	he knows how you make it .
	pro|he v|know-3S adv:wh|how pro|you v|make pro|it .
	1|2|SUBJ 2|0|ROOT 3|5|JCT 4|5|SUBJ 5|2|COMP 6|5|OBJ 7|2|PUNCT

	that is why I won't go .
	pro:dem v|be&3S adv:wh|why pro|I aux|will~neg|not v|go .
	1|2|SUBJ 2|0|ROOT 3|7|JCT 4|7|SUBJ 5|7|AUX 6|5|NEG 7|2|CPRED 8|2|PUNCT

	this is what I need .
	pro:dem|this v|be&3S pro:wh|what pro|I v|need .
	1|2|SUBJ 2|0|ROOT 3|5|OBJ 4|5|SUBJ 5|2|CPRED 6|2|PUNCT

	here is how you do it .
	adv:loc|here v|be&3S adv:wh|how pro|you v|do pro|it .
	1|2|PRED 2|0|ROOT 3|5|JCT 4|5|SUBJ 5|2|CSUBJ 6|5|OBJ 7|2|PUNCT

If, however, the WH-word is replaced with a normal noun phrase, you *should* code
the noun phrase as part of the matrix clause and code the subordinate clause as a
``CMOD`` to the noun phrase.

Example::

	I know the guy you are talking about .
	pro|I v|know det|the n|guy pro|you aux|be&PRES part|talk-PROG prep|about .
	1|2|SUBJ 2|0|ROOT 3|4|DET 4|2|OBJ 5|7|SUBJ 6|7|AUX 7|4|CMOD 8|7|JCT 9|2|PUNCT

	that is the reason I won't go .
	pro:dem v|be&3S det|the n|reason pro|I aux|will~neg|not v|go .
	1|2|SUBJ 2|0|ROOT 3|4|DET 4|2|PRED 5|8|SUBJ 6|8|AUX 7|6|NEG 8|4|CMOD 9|2|PUNCT

	here is the way you do it .
	adv:loc|here v|be&3S det|the n|way pro|you v|do pro|it .
	1|2|PRED 2|0|ROOT 3|4|DET 4|2|SUBJ 5|6|SUBJ 6|4|CMOD 7|6|OBJ 8|2|PUNCT

Although these constructions are very similar and it may seem strange to code
them in different ways, there is one very important difference.  While you could
insert a relativizer (i.e. "that" or "who") after an NP (i.e. I know the guy
*who* you are talking about, that is the reason *that* I won't go), you cannot do
the same with a WH-word introducing the clause (i.e. \*I know who *that* you are
talking about, \*that is why *that* I won't go).  So, when there is a normal noun
phrase, we can assume that the relativizer is just implied, but still code it as
a relative clause.  With the WH-words, however, relative clauses are not allowed,
so we must code them differently.

.. _mg-problems-all-csubj:

|all| **NP VERB** |is|
----------------------

Very similar to complements introduced by WH-words are subjects introduced by the
word "all" (e.g. "all you have to do is try your best").  Strangely enough, we
treat this construction as an exception to the last rule; while you can insert
a relativizer after "that" (e.g. "all *that* you have to do is try your best"), we
don't code it as a relative clause, but rather similar to the way we would code it
with WH-words.  That is to say, "all" takes whatever GR it serves in the first
clause (in this case ``OBJ``), while the entire clause serves as the ``CSUBJ`` to
the main clause.  Unfortunately, the only reason for this is that this is what the
coders under the old system did.

Example::

	all you have to do is try your best .
	pro:indef|all pro|you aux|have inf|to v|do v|be&3S v|try pro:poss:det|your n|best .
	1|5|OBJ 2|5|SUBJ 3|5|AUX 4|5|INF 5|6|CSUBJ 6|0|ROOT 7|6|XPRED 8|9|DET 9|7|OBJ 10|6|PUNCT

	all I'm saying is you shouldn't have done that .
	pro:indef|all pro|I~aux|be&1S part|say-PROG v|be&3S pro|you aux|should~neg|not aux|have part|do&PERF pro:dem|that .
	1|4|OBJ 2|4|SUBJ 3|4|AUX 4|5|CSUBJ 5|0|ROOT 6|10|SUBJ 7|10|AUX 8|7|NEG 9|10|AUX 10|5|CPRED 11|10|OBJ 12|5|PUNCT

	all he is is a dirty rotten scoundrel .
	pro:indef|all pro|he v|be&3S v|be&3S det|a adj|dirty adj|rotten n|scoundrel .
	1|3|PRED 2|3|SUBJ 3|4|CSUBJ 4|0|ROOT 5|8|DET 6|8|MOD 7|8|MOD 8|4|PRED 9|4|PUNCT

.. _mg-problems-adj-to-verb:

The phrase |be| **ADJ** |to| **VERB**
-------------------------------------

In the construction |be| **ADJ** |to| **VERB**, the **ADJ** is always a ``PRED``
to "be" while the **VERB** is an ``XJCT`` to "be".

Example::

	it is hard to bake a cake .
	pro|it v|be&3S adj|hard inf|to v|bake det|a n|cake .
	1|2|SUBJ 2|0|ROOT 3|2|PRED 4|5|INF 5|2|XJCT 6|7|DET 7|5|OBJ 8|2|PUNCT

	it wasn't easy to do .
	pro|it v|be&PAST&13S~neg|not adj|easy inf|to v|do .
	1|2|SUBJ 2|0|ROOT 3|2|NEG 4|2|PRED 5|6|INF 6|2|XJCT 7|2|PUNCT

.. _mg-problems-good-at:

The phrase |good_at| **VERBing**
--------------------------------

In an utterance like "you are good at hiding", we do not want the phrase "at hiding"
to contribute to the number of clauses in the utterance.  Thus "good" should be a ``PRED``
, "at" should be a preposition and a ``JCT`` to "good", and the verb (in this case "hiding")
should be coded as ``n:gerund|hide-GERUND`` and should be a ``POBJ`` dependent on "to".

Example::

    you are good at hiding .
    pro|you v|be&PRES adj|good prep|at n:gerund|hide-GERUND .
    1|2|SUBJ 2|0|ROOT 3|2|PRED 4|3|JCT 5|4|POBJ 6|2|PUNCT

.. _mg-problems-clause-as-pobj:

Clauses used as objects of prepositions
---------------------------------------

.. _mg-problems-do-you-think:

**WH-word** |do_you_think| **CLAUSE**
-------------------------------------

The phrase **WH-word** |do_you_think| **CLAUSE** comes up frequently (e.g. "what
do you think this is?", "where do you think he is going?").  There are obviously
two clauses, but it may not be clear at first which is the ``ROOT`` and which the
subordinate clause.  The easiest way to figure this out is to restructure the
utterance to make it a declarative sentence.  Thus, "what do you think this is?"
becomes "you (do) think this is what?".  Now it's easier to see that "think" is
``ROOT``, while "is" is a ``COMP`` and "what" is the ``PRED`` of "is", even though
they are not adjacent.

Example::

	what do you think this is ?
	pro:wh|what aux|do pro|you v|think pro:dem|this v|be&3S ?
	1|6|PRED 2|4|AUX 3|4|AUX 4|0|ROOT 5|6|SUBJ 6|4|COMP 7|4|PUNCT

	where do you think he is going ?
	adv:wh|where aux|do pro|you v|think pro|he aux|be&3S part|go-PROG ?
	1|7|JCT 2|4|AUX 3|4|SUBJ 4|0|ROOT 5|7|SUBJ 6|7|AUX 7|4|COMP 8|4|PUNCT

Using the sentence restructuring trick, you will always find that "do you think"
(or any variation of that, such as "does he think") will be the ``ROOT`` and the
other clause will be its ``COMP``.  You can also use this trick any time there is
an interrogative sentence and it's unclear what each word's GR is or, if there
are multiple clauses, which clause is the ``ROOT``.
