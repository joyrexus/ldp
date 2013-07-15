**********
Morphology
**********

The values in the **mor** column contain a morphological analysis of the word 
tokens in a given utterance: viz., each word's ...

* lemma
* part-of-speech
* prefix
* suffix

For example, consider the utterance transcribed:: 

    let's see, I'm going to make Dad's dinner &xxx .

This would be coded in the mor column as follows::

    aux|let's v|see pro|I~aux|be&1S aux|go-PROG inf|to v|make n:prop|Dad-POSS n|dinner .

Note the following:

- each word token is replaced by its lemma (dictionary form)

- each word is preceded by a part-of-speech code, which consists of 
  lower-case letters and colons

- suffixes may be added at the end of a word, marked by a dash (``-``) or an
  ampersand (``&``) and written using numbers and capital letters

- prefixes may be added before the part-of-speech code, separated from the main
  lexeme by a pound sign (``#``)

- compound words have normal part-of-speech codes and word types, joined
  together by plus signs (``+``), and preceded by the part-of-speech code of the
  compound as a whole (e.g., ``n|+adj|black+n|bird``)

- cliticized words are written with a tilde (``~``) connecting it to the 
  previous word.


POS Tags
--------

The **mor** column indicates the part-of-speech of each word token in an
utterance.  The following table provides short descriptions of the meaning
of each part-of-speech tag.


================  =============================
Tag               Part of Speech
================  =============================
``adj``           adjective
``adj:n``         adjective derived from noun
``adj:v``         adjective derived from verb
``adv``           adverb
``adv:adj``       adverb derived from adjective
``adv:int``       intensifying adverb
``adv:loc``       locational adverb
``adv:tem``       temporal adverb
``adv:wh``        WH adverb
``aux``           auxiliary verb
``co``            communicator
``co:voc``        vocative communicator
``conj:coo``      coordinating conjunction
``conj:subor``    subordinating conjunction
``det``           determiner
``det:num``       numeric determiner
``det:wh``        WH determiner
``fil``           filler
``inf``           infinitive
``int``           interjection
``n``             noun
``n:adj``         noun derived from adjective
``n:gerund``      nominal gerund
``n:pt``          plurale tantum noun
``n:v``           noun derived from verb
``neg``           negation
``on``            onomatopoeia
``part``          participle
``post``          postposition
``prep``          preposition
``pro``           pronoun
``pro:dem``       demonstrative pronoun
``pro:exist``     existential pronoun
``pro:indef``     indefinite pronoun
``pro:poss``      possessive pronoun
``pro:poss:det``  determiner possessive pronoun
``pro:refl``      reflexive pronoun
``pro:wh``        WH pronoun
``ptl``           particle
``qn``            quantifier
``rel``           relativizer
``v``             verb
``v:n``           verb derived from noun
================  =============================


POS Notes
+++++++++

Below is a quick overview of the main part-of-speech classes.

**Adjectives** modify nouns, either prenominally, or predicatively. Unitary compound modifiers such as *good-looking* should be labeled as adjectives.

**Adverbs** cover a heterogenous class of words including: manner adverbs, which generally end in *-ly*; locative adverbs, which include expressions of time and place; intensifiers that modify adjectives; and post-head modifiers, such as *indeed* and *enough*.

**Communicators** are used for interactive and communicative forms which fulfill a variety of functions in speech and conversation. Many of these are formulaic expressions such as *hello, good-morning, good-bye, please, thank-you*. Also included in this category are words used to express emotion, as well as imitative and onomatopeic forms, such as *ah, aw, boom, boom-boom, icky, wow, yuck, yummy*.

**Conjunctions** conjoin two or more words, phrases, or sentences. Coordinating conjunc- tions include: *and, but, or, yet*. Subordinating conjunctions include: *although, because, if, unless, until*.

**Determiners** include articles, and definite and indefinite determiners. Possessive determiners such as *my* and *your* are tagged ``det:poss``.

The **infinitive** marker is the word *to* which is tagged ``inf|to``. 

**Nouns** are tagged with ``n`` for common nouns, and ``n:prop`` for proper nouns 
(names of people, places, fictional characters, brand-name products).

The word *not* serves as a **negation** marker and is tagged ``neg|not``.

**Numbers** are tagged ``num`` for cardinal numbers. The ordinal numbers are adjectives. 

**Particles** are words that are often also prepositions, but serve as verbal particles.

**Prepositions** are tagged as ``prep``. Only words that are part of a prepositional phrase should be coded as prepositions.  

**Quantifiers** include *each, every, all, some*, and similar items.


Prefix Codes
------------

==========  ===========================
Prefix      Function
==========  ===========================
``CO``      verb prefix (*co-*)
``DE``      verb prefix (*de-*)
``MEGA``    verb prefix (*mega-*)
``MINI``    verb prefix (*mini-*)
``MULTI``   verb prefix (*multi-*)
``NON``     verb prefix (*non-*)
``SEMI``    verb prefix (*semi-*)
``SUPER``   verb prefix (*super-*)
``UNDER``   verb prefix (*under-*)
``UP``      verb prefix (*up-*)
``ANTI``    verb prefix (*anti-*)
``DIS``     verb prefix (*dis-*)
``MIS``     verb prefix (*mis-*)
``OUT``     verb prefix (*out-*)
``OVER``    verb prefix (*over-*)
``PRE``     verb prefix (*pre-*) 
``PRO``     verb prefix (*pro-*)
``RE``      verb prefix (*re-*)
``UN``      verb prefix (*un-*)
==========  ===========================


Suffix Codes
------------

===========  =================================================
Suffix       Meaning
===========  =================================================
``13S``      first- and third-person singular
``1S``       first-person singular
``3S``       third-person singular
``ABLE``     *-able* verb to adj derivational suffix
``AGT``      agentive suffix
``AL``       *-al* noun to adj derivational suffix
``COND``     conditional verb suffix
``CP``       comparative adj and adverb suffix
``DIM``      diminutive suffix
``ER``       *-er* nominalizer
``FULL``     *-full/ful* nominal suffix (*spoonful*)
``GERUND``   gerund suffix
``ISH``      *-ish* adjective or noun to adj suffix
``LESS``     *-less* noun to adj suffix
``LIKE``     *-like* noun to adj suffix (*fishlike*)
``LOOKING``  *-looking* adjective suffix (*funnylooking*)
``LY``       *-ly* adj to adverb suffix
``NESS``     *-ness* adj to noun suffix
``PAST``     past tense marker
``PERF``     perfect participle marker
``PL``       plural marker
``POSS``     possessive suffix
``PRES``     present tense marker
``PROG``     progressive participle marker
``SP``       superlative adj and adverb marker
``Y``        *-y* verb or noun to adj suffix (*burny*)
``ZERO``     null suffix for verbs with no explicit past tense
===========  =================================================

