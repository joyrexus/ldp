.. _tg-6:

***********************
6. Spelling Conventions
***********************

The following spelling conventions are designed to help Jason's computer programs and the CHAT software arrive at the right counts of word types, word tokens, and MLU, as well as carry out syntactic analysis.  It is therefore important to use all of the spelling conventions consistently in your transcripts.

.. _tg-6-1:

6.1 Transcribe only conventionally recognized words
===================================================

Do not transcribe any words that are not dictionary words and not included in our :ref:`list of standardized spellings <tg-spelling>` without using one of the symbols in :ref:`6.1.1 <tg-6-1-1>` or :ref:`6.1.2 <tg-6-1-2>`.

.. _tg-6-1-1:

6.1.1 Use the ``@`` symbol for idiosyncratic words
--------------------------------------------------

The ``@`` symbol marks words as being somehow non-standard or non-conventional. Use this symbol when you are transcribing a word that is not a proper noun, a dictionary word, or on our list of standardized spellings, but you still want it to be counted as a word when we compute things like word types and word tokens. A situation where you would have to transcribe such a word is when a child or a family has their own, idiosyncratic word for something. For example, in one of our families, the word "bishienoolie" means "butt". It should be transcribed as ``bishienoolie@``, with no space between the word and the ``@`` symbol. That way, it gets counted as a word, but the computer knows not to look for it in the dictionary. If a lot of kids or families start using the same non-standard term, then we can add it to our list of conventional spellings so that our computer programs will recognize it. See :ref:`Sections 6.4 <tg-6-4>` and :ref:`6.10 <tg-6-10>` for more on the related symbols ``@l`` for letters and ``@f`` for foreign words. 

.. _tg-6-1-2:

6.1.2 Use the ``&`` symbol for non-word sounds
----------------------------------------------

The ``&`` symbol marks things as not being words. As you will learn in this section, there are times when you will transcribe syllables (when speakers are sounding a word out, for example), alphabet sounds, creative rhyming, and other things that should not be added to our types and tokens counts. For example, a child might say "run, fun, zun, grun!" just to be cute. You would transcribe this as ``run, fun, &zun &grun!``.

.. note::

	The ``&`` symbol appears before the word while the ``@`` symbols appears after the word.

.. _tg-6-2:

6.2 Every utterance must end with proper marking
================================================

Every utterance must have either a terminal punctuation mark (``.``, ``!``, ``?``), a pair of dashes (``--``) or three number signs (``###``) at the end. Do not end utterances with commas, colons, semi-colons, or with nothing at all. Do not put punctuation of any kind after ``###`` in your transcript (for more on the ``###`` symbol, see :ref:`Section 7 <tg-7>`). For questions and exclamations use standard punctuation:

+----------------------------------+
| *p_utts*                         |
+==================================+
| did you remember to put it away? |
+----------------------------------+
| that one?                        |
+----------------------------------+
| good job!                        |
+----------------------------------+
| go put it on the --              |
+----------------------------------+
| Mom, can I ###                   |
+----------------------------------+

.. _tg-6-2-1:

6.2.1 Only capitalize proper nouns and the pronoun ``I``
--------------------------------------------------------

Only proper nouns (including ``Mom`` and ``Dad``, see :ref:`Section 6.5.1 <tg-6-5-1>`) and the pronoun ``I`` may be capitalized. Everything else, including words at the beginning of an utterance and the word ``ok`` (which was formerly transcribed as ``Ok``), must be transcribed in lower-case. This includes nationalities, abbreviations and acronyms that are commonly written in upper-case. Thus "German" should be transcribed ``german``, "American, should be transcribed ``american``, "TV" should be transcribed ``t+v``, and "CD" should be transcribed ``c+d``. State and country names are still considered proper nouns (for example, ``a citizen of Germany is a german citizen``).  Proper nouns that are abbreviations are still capitalized. Thus "NFL" and "CBS" would be transcribed as ``N_F_L`` and ``C_B_S``, respectively.


.. note::

	Rule 6.2.1 marks a break with the old conventions, in which the initial word of each utterance was capitalized.  This rule was changed to facilitate automatic part-of-speech tagging, which uses capitalization to signify a proper noun.  Determining whether the initial word was a proper noun and thus should have been capitalized was posing a problem during the conversion from our transcription format to the format used by the part-of-speech tagger. 

.. _tg-6-2-2:

6.2.2 "Mom" and "Dad" are usually capitalized
-------------------------------------------------

The words "Mom" ("Mommy", etc.) and "Dad" ("Daddy", etc.) get capitalized if used while addressing the mother or father or if used as a name. If used as a common noun, it is transcribed lowercase. 

+------------------------------------------+
| *c_utts*                                 |
+==========================================+
| Mom, I want that one!                    |
+------------------------------------------+
| where's Daddy, Mommy?                    |
+------------------------------------------+
| moms and dads love each other very much. |
+------------------------------------------+
| is your mom here?                        |
+------------------------------------------+

.. _tg-6-3:

6.3 Repeated words and phrases
==============================

For words and phrases that are repeated many times (as a result of either a series of false starts or an intentional repetition) within the same utterance, use the notation described in :ref:`Sections 6.3.1 <tg-6-3-1>` and :ref:`6.3.2 <tg-6-3-2>`.

.. _tg-6-3-1:

6.3.1 Use two dashes ``--`` for three or fewer repetitions
----------------------------------------------------------

If the word or phrase is repeated three or fewer times, type the word out one to three times with two dashes surrounded by spaces ( ``--`` ) in between. For example you would transcribe ``I want -- I want -- I want more milk!`` if the speaker repeats the phrase "I want" three times. You would transcribe ``where -- where -- where is my ninja?`` if the speaker repeats the word "where" three times.

.. _tg-6-3-2:

6.3.2 Use the form ``word[xN]`` for N > 3 repetitions
------------------------------------------------------------

If the word or phrase is repeated four or more times, type the word once and indicate the number of repetitions in brackets ``[]``. For example, if a child says "where" four times before getting to "is my ninja?" you would type ``where[x4] is my ninja?``. If a multi-word phrase has been repeated, indicate the scope of the repetition in angle brackets ``< >``, like this: ``<I want>[x4] more milk!`` so that we know that more than just the last word has been repeated. For both cases, be sure there is no space between the bracket and the preceding character.

.. _tg-6-4:

6.4 Use the ``@l`` symbol for letter names
==========================================

If speakers are spelling out words, type the letters they say in lowercase, followed immediately by the symbol ``@l``, putting a space between each letter. For example, you might type ``ball is spelled b@l a@l l@l l@l.``. 

.. _tg-6-4-1:

6.4.1 Use ``<letter>s@l`` for plural letters
--------------------------------------------

If speakers use the plural of a letter, transcribe the plural suffix before the ``@l`` symbol. For example, ``can you find any more rs@l?``.

.. _tg-6-4-2:

6.4.2 Use ``<letter>-'s@l`` for possessive letters
--------------------------------------------------

Believe it or not, this occasionally happens. For example, a mother might say
``the g-'s@l downstroke is drawn this way.`` (Meaning `the downstroke of the letter g@l is drawn this way.`) Or if a kid has some of those magnetic letters that stick on a refrigerator they might say ``oh no, a-'s@l magnet came off!``. (Meaning `the magnet on the letter e@l came off.` Note that this is in accord with rule :ref:`6.8 <tg-6-8>` for transcribing possessives.

.. _tg-6-4-3:

6.4.3 Use ``<letter>@ln`` for letters when spelling names
---------------------------------------------------------

If a speaker is spelling out sensitive information, the individual letters are tagged ``@ln``.  This would come into play any time someone is spelling a name we would normally use the ``@n`` symbol to anonymize (refer to :ref:`6.12 <tg-6-12>` for clarification).  For example, if the child is spelling ``Mary``, the letters would be tagged ``m@ln a@ln r@ln y@ln``.

.. _tg-6-5:

6.5 Transcribe compound nouns with plus signs ``+``
===================================================

Compound nouns also get smooshed together, with plus signs (``+``) between words. For example, ``ice+cream``, ``play+ground``, ``desk+top``, ``rocking+chair``, ``police+car``, ``laundry+bag``, etc.  If you are unsure of whether a word is a compound, check the `Oxford English Dictionary <http://www.oed.com>`_.  If the OED has an entry for that combination of words, regardless of whether it's written as one word, a hyphenated word, or two words, transcribe it with a plus sign.  If there are no entries for that combination of words, transcribe them separately.

+---------------+------------------------+-----------------------+
| Search for:   | OED Entry:             | Transcribe as:        |
+===============+========================+=======================+
| play ground   | playground             | ``play+ground``       |
+---------------+------------------------+-----------------------+
| ice cream     | ice-cream              | ``ice+cream``         |
+---------------+------------------------+-----------------------+
| police car    | police car             | ``police+car``        |
+---------------+------------------------+-----------------------+
| train track   | *There Are No Results* | ``train track``       |
+---------------+------------------------+-----------------------+

.. note::

        Prior to Version 1.5.2, word combinations that were written as separate words on the OED were transcribed as separate words, while word combinations that were written as one word or hyphenated would be transcribed with a plus.

Multi-word proper nouns also get smooshed together with plus signs between words and each new word capitalized. For example, type ``George+Bush``, ``United+States``, ``Hokey+Pokey``, and ``Mrs+Robinson`` as single words.

.. _tg-6-5-1:

6.5.1 Plus signs for idiomatic phrases
---------------------------------------

Some idiomatic phrases are also written with plus signs. These include ``of+course``, ``how+come``, ``how+about``
, ``hows+about``, ``where+abouts``, ``what+about``, ``sort+of``, ``kind+of``, and ``a+lot``.  All of these, with the exception
of "kind of", "sort of", and "a lot", will always be transcribed with a plus sign.

The phrases "kind of", "sort of", and "a lot" can function in two ways: as a noun phrase with prepositional modifier ("what kind of animal", "a lot of cake") or as an adverbial modifier ("kind of noisy", "I like it a lot").  Only plus these phrases when they are used as an adverbial modifier. To test this, try replacing the phrase with a synonymous one-word adverb (for "kind of" and "sort of", try "rather"; for "a lot", try "frequently" or "considerably"). If you can replace it and it makes sense, transcribe it with plus signs. If it does not make sense, transcribe it as separate words.

+-----------------------+---------------------------------+------------+----------------------+
| What you hear:        | Replace with one-word synonym:  |  Evaluate: | Transcribe as:       |
+=======================+=================================+============+======================+
| "It's getting kind of | "It's getting rather dark out." |  Good!     | it's getting kind+of |
| dark out."            |                                 |            | dark out.            |
+-----------------------+---------------------------------+------------+----------------------+
| "What kind of animal  | "What rather animal is that?"   |  Bad!      | what kind of animal  |
| is that?"             |                                 |            | is that?             |
+-----------------------+---------------------------------+------------+----------------------+
| "I eat cake a lot."   | "I eat cake frequently."	  |  Good!     | I eat cake a+lot     |
+-----------------------+---------------------------------+------------+----------------------+
| "I eat a lot of	| "I eat frequently of cake." or  |  Bad!      | I eat a lot of cake  |
| cake."		| "I eat considerably of cake."   |            |                      |
+-----------------------+---------------------------------+------------+----------------------+

.. _tg-6-5-2:

6.5.2 Other uses for plus signs
--------------------------------

The following types of phrases are also written with plus signs between words: Brand names (e.g. ``Kool+Aid``, ``Q+Tip``), foreign phrases used as fixed expressions (e.g. ``cul+de+sac``, ``non+sequitur``), abbreviations (e.g. ``t+v``, ``x+ray``), and catch phrases (e.g. ``yabba+dabba+doo``, ``ho+ho+ho``).

Not all catchphrases require plus signs.  Only use a plus sign when the phrase is wordlike, as in ``bippity+boppity+boo`` but not when it contains complex internal structure, as in ``I've made a huge mistake!``.

.. _tg-6-6:

6.6 Use underscores to connect multi-word titles
================================================

In most cases, we use the plus sign (``+``) to connect compound word forms. (See :ref:`Sections 6.5 <tg-6-5>` for help in considering what's a compound word.) 

However, the names and titles of some things are not happily thought of as single lexical units. For example, the book titles "The Cat In The Hat" and "The Boy Who Cried Wolf" are comprised of multiple words, each of which can be found in a standard dictionary. So, instead of using the plus connector to mark the combination of these words as a single lexical unit, we instead use an underscore to indicate that they are more loosely linked. The individual words have an independent meaning, but together they form the name or title of something: ``The_Cat_In_The_Hat``, ``The_Boy_Who_Cried_Wolf``.

Consider how the titles of some things are better thought of as single lexical units. The TV shows "South Park" and "Sesame Street", like two-word brand names, could certainly be considered single lexical units. To avoid some ambiguity here, for cases like "The Matrix", we recommend that you use a plus connector for all two word names/titles and use your best judgment for titles comprised of three or more words.

In general, *if a title is comprised of three or more words and most of the words in the title are normal dictionary words, use an underscore to connect the title.* 

Perhaps the following general rules of thumb and list of examples will help clarify these guidelines:

Use a plus (``+``) to tightly connect most proper names:

* Toy+Story
* South+Park
* The+Matrix
* Monty+Python
* Magnum+P+I
* Tic+Tac+Toe

Use an underscore (``_``) to loosely connect longer titles:

* Dora_The_Explorer
* The_Giving_Tree 
* The_Cat_In_The_Hat
* Hide_And_Go_Seek

If there is a compound word (``Three+D``) or proper name (``Toy+Story``) within a title ("Toy Story Two"), use both connectors as appropriate: 

* Toy+Story_Two
* Jackass_Three+D
* Monty+Python_And_The_Holy_Grail
* South+Park_Bigger_Louder_And_Uncut

For questionable cases, consult our :ref:`Spelling Conventions <tg-spelling>` page.

.. _tg-6-7:

6.7 Do not use apostrophes in proper nouns and certain fixed phrases
====================================================================

Do not use apostrophes for words like "Valentine's Day" or "o'clock".  Instead, transcribe these as ``Valentines_Day`` and ``oclock``.  We don't want the computer to accidentally count those as possessives or contractions, which is what will happen if it sees an apostrophe somewhere.

.. _tg-6-8:

6.8 Transcribe possesive marker as ``-'s``
==========================================

The apostrophe-s ('s) that's used for both possesives ("John's shoe") and contracted "is", "has", or "does" ("John's running") can appear ambiguous to a computer program that's trying to identify different parts of speech. To make it less ambiguous, place a dash (``-``) before the ``'s`` whenever you're transcribing the possessive apostrophe-s (``-'s``). For example, transcribe ``John's got Sue-'s dog`` or ``Fred's about to get on John-'s nerves``. 

.. _tg-6-8-1:

6.8.1 Transcribe plural possessive markers as ``-'``
----------------------------------------------------

If a possessive apostrophe is used in conjunction with a plural "s" marking (as in "his brothers' toys"), still place a dash before the apostrophe even though no "s" follows it (e.g. ``his brothers-' toys``). 

.. _tg-6-9:

6.9 Spell out numbers
=====================

There are several conventions to follow when transcribing numbers:

	* All numbers in speech should be transcribed as words, not as digits.
	* For numbers composed of two or more number words, separate each part with a plus sign (e.g. ``thirty+four``, ``one+hundred``).
		* The teens qualify as single words and thus do not have a plus sign (e.g. ``fourteen``, NOT ``four+teen``).
		* If "a" is used in place of "one" at the beginning of a number, use a plus sign (e.g. ``a+hundred+and+one``, ``a+million``).
	* Numbers containing fractions are also transcribed as one word connected by plus signs (e.g. ``two+and+a+half``, ``three+and+two+sixths``).
	* If a speaker pronounces the number zero as "oh," transcribe it as the letter ``o``.
	* "AM" and "PM" should be written ``a+m`` and ``p+m`` and attached to whatever precedes them with a plus sign (e.g. ``nine+a+m``).
	* When number words precede units, the units are separate from the numbers.

+-----------------------------+--------------------------------+
| If you hear:                | Transcribe it as:              |
+=============================+================================+
| It's four-thirty            | it's four+thirty.              |
+-----------------------------+--------------------------------+
| That costs $4.75            | that costs four+seventy+five.  |
+-----------------------------+--------------------------------+
| It must be ninety-five      | it must be ninety+five         |
| degrees in here!            | degrees in here.               |
+-----------------------------+--------------------------------+
| That'll be 150 dollars      | that'll be a+hundred+and+fifty |
|			      | dollars			       |
+-----------------------------+--------------------------------+
| This bottle holds 7.5 mL    | this bottle holds              |
|                             | seven+point+five milliliters.  |
+-----------------------------+--------------------------------+
| Let's leave tomorrow at     | let's leave tomorrow at        |
| 9:30 am.                    | nine+thirty+a+m.               |
+-----------------------------+--------------------------------+
| Two thousand and five       | two+thousand+and+five.         |
+-----------------------------+--------------------------------+
| You live at 503 Circle      | you live at five+o+three       |
| Drive.                      | Circle_Drive.                  |
+-----------------------------+--------------------------------+
| We need 1 and 3/4 of a cup. | we need one+and+three+quarters |
|                             | of a cup.                      |
+-----------------------------+--------------------------------+
| My watch says 5:06          | my watch says five+o+six.      |
+-----------------------------+--------------------------------+

6.9.1 Spell out made-up numbers
-------------------------------

	* Treat made-up numbers like real numbers, transcribing the full words and connecting words with a plus sign (e.g. ``three+hundred+million+billion+thirty+fifty+eighty+two``).

.. _tg-6-10:

6.10 Use the ``@f`` symbol for foreign words
============================================

If you encounter foreign language words in an otherwise English utterance, you can transcribe them if you know what they are and what they mean.  If the entire utterance is in a foreign language, see :ref:`Section 2.1.3 <tg-2-1-3>`.  Mark foreign words by putting the ``@f`` symbol after the word and the letter ``l`` in the *key* column.  If you cannot easily transcribe and translate words from a foreign language, transcribe the words as ``###`` and note the presence of foreign language words with an ``l`` in the *key* column.  Make a note on the Info page as well, including the language being spoken. None of the kids in our study are being raised bilingually, so you will never see more than a couple of foreign-language words in a transcript, and these are usually (though not always) picked up from Dora the Explorer or something similar and not learned by a native speaker.

+-------+-------------------------+
| *key* | *p_utts*                |
+=======+=========================+
| l     | but you didn't abre@f   |
|       | the gate.               |
+-------+-------------------------+
| l     | you need to say abre@f. |
+-------+-------------------------+

.. _tg-6-11:

6.11 Use ``ie`` for diminutive nouns, ``y`` for adverbs
=======================================================

It is possible to make diminutive forms of many nouns (e.g. "doggie", "birdie"), as well as adjectival/adverbial forms of many words (e.g. "cheesy", "poopy").  If you encounter a diminutive or adjectival/adverbial form that cannot be found in the `OED <http://www.oed.com>`_ or the :ref:`LDP recognized word list <tg-spelling>`, use the ``ie`` suffix to make a diminutive noun ("fish" -> "fishie"; ``that's a cute little fishie.``) and the ``y`` suffix to make an adjective/adverb ("fish" -> "fishy"; ``this water tastes fishy.``).  

.. _tg-6-12:

6.12 Use the ``@n`` symbol for names that require anonymization
===============================================================

Any time a word conveys sensitive or identifying information about the child, attach the tag ``@n`` to the end of the word.  This applies to family member's names, friends' names, nicknames, schools, banks, playgrounds, neighborhoods, and basically anything that might hint at the identity of the subjects.  This rule still applies even if names are already included in the cast field of the transcript.  Generic or non-identifying names, like the names of fictional characters or large cities (Sesame Street or Chicago), don't require this tag.  The ``@n`` tag will make it easier to later anonymize the database when sharing it with researchers outside of the project. Example: ``Richard@n and Andrew@n were pretending to be Power+Rangers down the street at Walton+Park@n.``

.. _tg-6-12-1:

6.12.1 Anonymization nesting
============================

``@n`` should be considered a suffix and kept as close as possible to the word in question.  The only thing that trumps n is l, for letters :ref:`Section 6.4.3 <tg-6-4-3>`.  Therefore:

+-----------------------------+--------------------------------+
| For:                        | Transcribe it as:              |
+=============================+================================+
| Possessive                  | ``Hannah@n-'s``                |
+-----------------------------+--------------------------------+
| Contraction                 | ``Hannah@n's``                 |
+-----------------------------+--------------------------------+
| Letter                      | ``h@ln``                       |
+-----------------------------+--------------------------------+
| Letter and possessive       | ``h@ln-'s``                    |
+-----------------------------+--------------------------------+
