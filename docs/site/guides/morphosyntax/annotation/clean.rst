.. _mg-clean:

*********************
Prepping a transcript
*********************

Prior to adding any part-of-speech annotation, you will need to clean up a few
things in the transcript to make it conform to the CHAT transcription standards.
This is necessary for the morphosyntax programs to properly parse and tag the
transcripts.  The following steps explain how to prep your transcript prior to
running the MOR and POST commands.

.. _mg-clean-1:

1. Remove disfluencies and repetitions
======================================

Speakers will often repeat or stumble over a word or phrase.  When this happens,
remove the repeated or unintended words, leaving only the necessary and/or
intentional parts of the utterance.  To find repetitions and disfluencies, search
for the ``#`` symbol, which denotes a pause or a re-casting of an utterance.

The general rules to follow are:

	* Use only the words that were spoken.
	* From those words, leave only those that the speaker intended to say.
		* When determining whether something was intended or not, give preference to what was spoken last.
	* From those words, give the speaker as much credit as possible for complex constructions while making the most grammatically coherent sentence.

For instance, if you search for ``#`` and see::

	*CHI:	I # I # I want the ball .
	*MOT:	give him the bowl # ball .

remove the repetitions of ``I`` and the accidental use of ``bowl`` to make it::

	*CHI:	I want the ball .
	*MOT:	give him the ball .

In general, you will want to preserve what is said to the right of ``#``, as this is probably what the speaker intended to say.  For instance::

	*MOT:	he brought # he took it .

would be cleaned up as::

	*MOT:	he took it .

However, you also want to give them as much credit for complex constructions as possible given the words that they spoke.  This means that if a speaker said::

	*CHI:	this fire+truck has # it drives real fast .

you would want to give them credit for the more complex noun phrase structure and would thus retain ``this fire+truck``, while removing the accidental use of ``has`` and the grammatically redundant and less complex use of ``it``::

	*CHI:	this fire+truck drives real fast .

.. note::

	You will not always need to remove words for every instance of ``#``.  Sometimes this simply denotes a pause in the speech, and not a repetition or re-casting of the utterance.

.. _mg-clean-1-1:

1.1. Remove utterances consisting only of ``#``
-----------------------------------------------

Occasionally you will come across an utterance that has no words in it, only the
``#`` symbol.  When you do, delete that speech tier, as well as its
corresponding %row and %id tiers.  For instance, in the following::

	*MOT:   sure .
	%id:    10850900151
	%row:   151
	*MOT:   #
	%id:    10850900152
	%row:   152
	*CHI:   seven, eight, nine, eleven, twelve +...
	%id:    10850900153
	%row:   153

Row 152 should be removed, resulting in the following::

	*MOT:   sure .
	%id:    10850900151
	%row:   151
	*CHI:   seven, eight, nine, eleven, twelve +...
	%id:    10850900153
	%row:   153


.. _mg-clean-2:

2. Find and remove repeated words and phrases
=============================================

Not all repeated words and phrases are transcribed with the ``#`` symbol.  This
is especially true when the words are spoken rapidly and/or intentionally.
However, we still want to reduce repeated words and phrases to only the necessary
elements.  Therefore, even when a speaker intends to repeat a word (for emphasis
or during word play, for example), remove all but one instance of it.

.. note::

	A repetition should not be removed if it is grammatically correct.  For instance, "I know that that isn't right" and "if you throw it it will break" are grammatically correct and the repetitions of "that" and "it" are therefore not removed.

There are two ways to find repetitions:

.. _mg-clean-2-1:

2.1. Use the *tn* shortcut in VI to find single-word repetitions
----------------------------------------------------------------

If you have downloaded and set up your :ref:`.vimrc file <mg-setup-4>`, you can
simply press the key combination *tn* when viewing the file with the VI editor.
This will execute a search for any single word that is repeated.  When you are
finished removing the repetitions in one utterance, you can find the next by
pressing *n*.

.. _mg-clean-2-2:

2.2. Use the program **dis** to find repeated words and phrases
---------------------------------------------------------------

To find repeated words and phrases using **dis**, open a second terminal window
and navigate to the directory containing the file you are working on (for example,
*$REPO/chat/proj_2/coders/max*).  Then, run the program **dis** by typing::

	dis 123.09.cha

This will print a list of row numbers on which repeated words or phrases are
found.  For instance, the following shows that there is a repetition on rows 57
and 276.::

	dis 123.09.cha

	%row:	57
	%row:	276

You can use the ``-p`` switch to print the entire utterance as well, or the
``-v`` switch to print the repeated words or phrases.::

	dis -p 123.09.cha

	*CHI:	this is for for Daddy .
	%row:	57
	*MOT:	you have to, have to eat some more vegetables .
	%row:	276


	dis -v 123.09.cha

	Repetition: for
	%row:	57
	Repetition: have to
	%row:	276

You will then have to find these rows in the file you are working on and remove
all but one instance of the repeated word or phrase.

.. _mg-clean-3:

3. Add an ``&`` symbol to the beginning of non-words
====================================================

Find all instances of "oh", "uh", "um", "ooh", and "ah" and affix the ``&``
symbol to the beginning (i.e. ``&oh``, ``&uh``, ``&um``, etc.).  Also affix ``&``
to the beginning of every instance of "xxx", the symbol for unintelligible
speech.  We do this so that these words are not counted as word types and tokens
and do not contribute to a speaker's Mean Length of Utterance (MLU).

If you are using the VI text editor and have :ref:`set up the .vimrc file <mg-setup-4>`,
simply type the key combination *\`c* (that is the symbol on the same key as the
~ symbol) to invoke a search and replace command that will execute this process for you.

.. _mg-clean-4:

4. Ensure that "Mom", "Dad", etc. are properly capitalized
==========================================================

Due to formatting and/or transcriber error, you may sometimes come across family
relationship terms that do not have the proper capitalization.  As specified in
:ref:`section 6.2.2 <tg-6-2-2>` of the Transcription Guide, "Mom", "Dad",
"Grandma", and other such terms should be capitalized when used as a proper noun
(e.g. "hey Mom, can you open this?") and lower-case when used as a common noun
(e.g. "my dad is stronger than your dad.").  There are two VI shortcuts to help
you find potential problem cases.

.. _mg-clean-4-1:

4.1. Find incorrectly lower-case family terms using the *\`m* shortcut
----------------------------------------------------------------------

If you have :ref:`set up the .vimrc file <mg-setup-4>`, you can press the
shortcut *\`m* (that is the symbol on the same key as the ~ symbol) to search
the transcript for family terms that may be incorrectly transcribed in
lower-case.  Hitting this shortcut will find each instance of the following
words that matches a certain pattern:

	* mom | mommy | mama
	* dad | daddy | dada
	* grandpa
	* grandma
	* papa
	* nana

When a match is found, you will be presented with a prompt in the bottom left of
the screen, asking if you want to capitalize the highlighted word.  If you think
the word should be capitalized, hit **y**; if not, hit **n**.  If you want to
capitalize all matches, hit **a** (you can probably safely do this, since most
matches should in fact be capitalized).  If you want to quit searching and
replacing, hit **q**.

.. _mg-clean-4-2:

4.2. Find incorrectly capitalized family terms using the *\`d* shortcut
-----------------------------------------------------------------------

If you have :ref:`set up the .vimrc file <mg-setup-4>`, you can press the
shortcut *\`d* (that is the symbol on the same key as the ~ symbol) to search
the transcript for family terms that may be incorrectly capitalized.  Hitting
this shortcut will find each instance of the following words that matches a
certain pattern:

	* Mom | Mommy | Mama
	* Dad | Daddy | Dada
	* Grandpa
	* Grandma
	* Papa
	* Nana

When a match is found, you will be presented with a prompt in the bottom left of
the screen, asking if you want to lower-case the highlighted word.  If you think
the word should be transcribed in lower-case, hit **y**; if not, hit **n**.  If
you want to lower-case all matches, hit **a** (you can probably safely do this,
since most matches should be lower-case).  If you want to quit searching and
replacing, hit **q**.

.. _mg-clean-5:

5. Search for and correct common mistakes using the *\`v* shortcut
==================================================================

If you have :ref:`set up the .vimrc file <mg-setup-4>`, you can press the
shortcut *\`v* (that is the symbol on the same key as the ~ symbol) to search the
transcript for a list of common mistakes and patterns that need your attention.
This shortcut will search for the following things:

	#) Phrases that need or might need to be joined by a *+*.
	#) Phrases that need or might need to be changed or written with an apostrophe
	#) Two capitalized words in a row (might signify a name that should be joined by a *+*).
	#) Punctuation placed in the middle of an utterance.
	#) Repetitions marked by *[xN]*.
	#) Single quotes (apostrophes) used as quotation marks.
	#) Apostrophes in proper nouns.
	#) Misuse of the *@l* marker.
	#) A space at the beginning of any of the tiers (may cause formatting issues later).
	#) Utterances missing punctuation.

.. _mg-clean-5-1:

5.1. Phrases that need or might need to be joined by a *+*
----------------------------------------------------------

This shortcut will search for the phrases "kind of", "sort of", "of course", "at
all", "what if", "a lot", "at least", and "as well."  If these phrases are used
adverbially as a fixed expression (e.g. "kind of quiet around here", "are you
hungry at all?", "I like that a lot") replace the space with plus sign (e.g.
"kind+of quiet around here", "are you hungry at+all?", "I like that a+lot").  If
they are not used adverbially (e.g. "what kind of toy is that?", "I see him at
all the concerts", "that's a lot of food"), leave them as they are.  See
:ref:`Section 6.5.1 <tg-6-5-1>` of the transcription guide for more on these
phrases.

The shortcut also searches for the phrases "because of", "instead of", "except
for", and "in case".  If any of these phrases are being used as a preposition or
a subordinating conjunction, join them with a *+*.  For example:

+---------------+----------------------------------------+------------------------------------------------+
| Phrase        | Preposition example                    | Conjunction example                            |
+===============+========================================+================================================+
| because of    | I stubbed my toe because+of this mess. | N/A                                            |
+---------------+----------------------------------------+------------------------------------------------+
| instead of    | do you want milk instead+of juice?     | instead+of watching t+v, let's read a book.    |
+---------------+----------------------------------------+------------------------------------------------+
| except for    | I did all my homework except+for math. | it's like a plane except+for it goes in space. |
+---------------+----------------------------------------+------------------------------------------------+
| in case       | N/A                                    | let's bring a jacket in+case it gets cold.     |
+---------------+----------------------------------------+------------------------------------------------+

Additionally, the shortcut searches for the following fixed phrases, which
should be joined with a *+*.

	* thank you 
	* bless you 
	* excuse me|you 
	* pretty please
	* you're welcome 
	* how about 
	* what about and 
	* how come

.. _mg-clean-5-2:

5.2. Phrases that need or might need to be changed or written with an apostrophe
--------------------------------------------------------------------------------

For whatever reason, some words are written as two words that should either be one word or should be joined with an apostrophe.  Make the following changes if the shortcut finds these phrases::

	all right	=>	alright (when used in the same sense as "okay")
	is got		=>	has got (this was due to an older script we use to run that expanded
					   's, but sometimes expanded it to the wrong thing)
	let us		=>	let's

.. _mg-clean-5-3:

5.3. Two capitalized words in a row
-----------------------------------

If you find two capitalized words in a row, determine whether they are meant to be part of a single proper noun.  For instance, if you found "let's talk to Aunt Judy", you would want to combine "Aunt" and "Judy" following the rules in :ref:`Section 6.5 <tg-6-5>` and :ref:`6.6 <tg-6-6>` of the transcription guide (i.e. "let's talk to Aunt+Judy").

This part of the shortcut tends to match things that often don't need to be fixed, for example "Mom, I want a donut" or "did you talk to Judy, David?".  Leave these words separated and capitalized.

.. _mg-clean-5-4:

5.4. Punctuation placed in the middle of an utterance
-----------------------------------------------------

Sometimes, especially in earlier transcripts, you will find a sentence-final punctuation mark (. ! ?) in the middle of an utterance.  This is incorrect according to :ref:`rule 3.1 <tg-3-1>` of the transcription guide and will confuse the syntax software.  Remove these punctuation marks, replacing with a comma if appropriate.  You may also have to lower-case the word following the punctuation if it is not a proper noun.

For example::

	come here.  Let me put on your coat .	=>	come here, let me put on your coat .
	be quiet!  Mommy is talking .		=>	be quiet, Mommy is talking .
	where are you going?  asked the bear .	=>	where are you going, asked the bear .
	
.. _mg-clean-5-5:

5.5. Repetitions marked by *[xN]*
---------------------------------

Words and phrases that are repeated three or fewer times are simply transcribed with a dash or pound sign between repetitions (e.g. "let's # let's # let's play this").  Four or more repetitions are transcribed using the notation *[xN]* where N is the number of times the word or phrase is repeated.  If you find this construction, remove the brackets and everything inside (since we don't care about repeated words anyway).

Repeated phrases are written in angle brackets (*<>*).  If you find a repeated phrase, remove the angle brackets from around the phrase.

For example::

	no[x7], I don't want to !		=>	no, I don't want to !
	<I'm going to>[x5] play with my train .	=>	I'm going to play with my train .

.. _mg-clean-5-6:

5.6. Single quotes (apostrophes) used as quotation marks
--------------------------------------------------------

While we never use quotation marks in our transcripts now, you will sometimes see them in older transcripts.  Double quotes (") are usually removed automatically, but it's harder to remove single quotes ('), since these are also used in contractions.  The shortcut will search for a single quote that does not follow a letter character, and is thus probably being used as a quotation mark, not an apostrophe.  You may also have to remove punctuation associated with the quoted part of the utterance.

For example::

	'help!' he cried .		=>	help, he cried .
	Mom said 'oh no you don't' .	=>	Mom said, oh no you don't .

.. _mg-clean-5-7:

5.7. Apostrophes in proper nouns
--------------------------------

Similarly, apostrophes are never supposed to appear in proper nouns, even those that would have one in standard written English (e.g. Reese's Pieces should be Reeses+Pieces).  If the shortcut finds an apostrophe in a proper noun, simply remove it.

.. _mg-clean-5.8:

5.8. Misuse of the *@l* marker
------------------------------

When converting transcripts from our transcription format to the CHAT transcription format, the pronoun "I" and the indefinite article "a" sometimes get tagged as the letter "i" and the letter "a".  If the shortcut finds any instances of *i@l* or *a@l*, determine whether they are in fact letters.  If they are not, remove the *@l* tag and capitalize *i*.

Also during the converting process, some newer transcripts mistakenly have two *@l* tags.  If you find an instance of this, simply remove one of the tags.

For example::

	a@l is a letter.  Leave it alone:
		a@l is for apple .	=>	a@l is for apple .

	a@l is an article.  Change it:
		do you have a@l b@l ?	=>	do you have a b@l ?

	i@l is a letter.  Leave it alone:
		give me an i@l !	=>	give me an i@l !

	i@l is a pronoun.  Change it:
		no, i@l am not .	=>	no, I am not .

	Too many @l tags.  Remove one:
		a@l@l is for apple .	=>	a@l is for apple .

.. _mg-clean-5-9:

5.9. A space at the beginning of the tier
-----------------------------------------

Sometimes a speech tier will have an errant space after the first tab and before the utterance starts.  If this happens, simply remove the extra space.

.. _mg-clean-5-10:

5.10. Utterances missing punctuation
------------------------------------

Sometimes a speech tier will be missing an utterance-final marker (either
typical punctuation marks or the symbol *+...*).  If you find such an utterance,
add the appropriate mark at the end, remembering to separate it from the last
word with a space.

.. _mg-clean-6:

6. Run **caps** to verify that capitalized words are proper nouns and are correctly formatted
=============================================================================================

For whatever reason, transcripts sometimes contain capitalized words that are actually common nouns.  They may also contain proper nouns that are sometimes capitalized and sometimes lower-case.  To ensure that all capitalized words are actually proper nouns and that there are not lower-case instances of proper nouns, run the program **caps**.  This will print out a list of all capitalized words, as well as an indicator if one of those words also has lower-case instances.::

	Alice_In_Wonderland
	Connect_Four
	Dad		-->	check lower case
	Dora
	Grant		-->	check lower case
	Ick
	Lady		-->	check lower case
	Laura
	Mom
	Twentythree

If you see something in the list that looks like it should not be a proper noun, go back into the transcript and fix it.  For example, "Twentythree" and "Ick" are not proper nouns and need to be lower-cased and possibly reformatted, i.e. ``twenty+three`` and ``ick``.

If you see something in the list that has a "check lower case" indicator, go back into the transcript and make sure that the lower-case instances are correct.  If not, capitalize those instances.  For example, "Grant" and "Lady" (from "Lady and the Tramp") are proper names.  However, when we convert from our transcription format to the CHAT transcription format, sentence-initial words that are recognized by the CLAN lexicon are lower-cased, in this case erroneously, so you could capitalize those words.

Not all lower-case instances need to be capitalized, however.  For example, "Dad" can have a proper noun usage and a common noun usage.  When used in place of a name ("did you see Dad in the garage?"), "Dad" should be capitalized.  When used as a common noun ("my dad is taller than your dad"), it should remain lower-case.  Thus you can have upper- and lower-case instances of some words in the same transcript.

After you go through the list and make the necessary changes to the transcript, run **caps** again until the list contains only correctly formatted proper nouns, and all the lower-case indicators have been confirmed.  For example, after making all of the necessary changes, the list would now look like this::

	Alice_In_Wonderland
	Connect_Four
	Dad		-->	check lower case
	Dora
	Grant
	Lady
	Laura
	Mom

The program **caps** will also print a list of words that have an ampersand in front of them (except for "oh", "uh", "um", "ooh", "ah", and "xxx" which always have an ampersand).  This list also includes a comment if there is an un-ampersanded instance of an ampersanded word::

	Ampersanded words:

	&bitiba         -->     check for unampersanded instances
	&chickeny
	&phwoosh

If you see something in the list that looks like it should be counted as a real word, go back into the transcript and remove the ampersand.  For instance, although "chickeny" is not a dictionary word, it is formed with the -y suffix of :ref:`rule 6.11 <tg-6-11>`.  Since we want to count it as a word, remove the ampersand from all instances of "chickeny" in the transcript.

The utterances "phwoosh" and "bitiba", on the other hand, do not qualify as words, and so should retain the ampersand.  However, "bitiba" has unampersanded instances in the transcript that must be ampersanded.

After making the changes to these ampersanded words, run **caps** again and verify that these words are correctly transcribed.  Repeat this process until you are satisfied that everything is properly formatted.  For example, after making all of the necessary changes, the list would now look like this::

	Ampersanded words:

	&bitiba
	&phwoosh

.. note::

	See :ref:`Section 6.1 <tg-6-1>` for more on what should have the *&* symbol.
