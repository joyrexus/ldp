.. _mor-column:

3.7. Mor - Morphology
=====================


.. _mor-column-description:

3.7.1. Description
------------------

Speaker specific utterance transcription with morphological analysis


.. _mor-column-format:

3.7.2. Format
-------------

.. productionlist::
   entry: `value`+ `punct`
   value: `mor_unit` ["~" `mor_unit`]? 
   mor_unit: [`prefix` "#"]? (`basic_unit` | `compound_unit`) [("&" | "-") `suffix`]?
   basic_unit: `pos` "|" `word_type`
   compound_unit: `pos` "|+" `basic_unit` "+" `basic_unit`+
   word_type: `english_word` | `foreign_word` | `letter` | `idiosyncratic_word`
   english_word: <Any non-inflected English word>
   foreign_word: <Any non-English word>
   letter: <Any letter>
   idiosyncratic_word: <Any non-standard word used by the speaker in a regular linguistic context>
   pos: <See Part-of-Speech Code Table below>
   prefix: "anti" | "co" | "de" | "dis" | "mega" | "mini" | "mis" | "multi" | "non" | "out" | "over" | "pre" | "re" | "semi" | "super" | "un" | "under" | "up" 
   suffix: <See Suffix Code Table below>
   punct: "." | "!" | "?" | "+..."


Prefix codes are selected from the following:


.. _mor-column-values:

3.7.3. Values
-------------

A series of words with accompanying morphological information.

Parts of speech codes have the following interpretations:

================  =============================
POS Code          Meaning
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

Suffix codes have the following interpretations:

===========  =================================================
Suffix Code  Meaning
===========  =================================================
``13S``      first- and third-person singular
``1S``       first-person singular
``3S``       third-person singular
``ABLE``     "able" verb to adj derivational suffix
``AGT``      agentive suffix
``AL``       "al" noun to adj derivational suffix
``COND``     conditional verb suffix
``CP``       comparative adj and adverb suffix
``DIM``      diminutive suffix
``FULL``     "full/ful" nominal suffix (spoonful)
``GERUND``   gerund suffix
``ISH``      "ish" adjective or noun to adj suffix
``LESS``     "less" noun to adj suffix
``LIKE``     "like" noun to adj suffix (winglike)
``LOOKING``  "looking" adjective suffix (funnylooking)
``LY``       "ly" adj to adverb suffix
``NESS``     "ness" adj to noun suffix
``PAST``     past tense marker
``PERF``     perfect participle marker
``PL``       plural marker
``POSS``     possessive suffix
``PRES``     present tense marker
``PROG``     progressive participle marker
``SP``       superlative adj and adverb marker
``Y``        "y" verb or noun to adj suffix (burny)
``ZERO``     null suffix for verbs with no explicit past tense
===========  =================================================



.. _mor-column-vert-dep:

3.7.4. Vertical Dependencies
----------------------------

None


.. _mor-column-horz-dep:

3.7.5. Horizontal Dependencies
------------------------------

Mor is dependent on the :ref:`CHAT Column <chat-column-dep-by>` and the 
:ref:`Enum Column <enum-column-dep-by>`.

Similar to the format of the Enum column, with the following differences:

- each word token is replaced by its word type
- instead of a number, each word is preceded by a part-of-speech code, which
  consists of lower-case letters and colons
- suffixes may be added at the end of a word, marked by a dash (-) or an
  ampersand (&) and written using numbers and capital letters
- prefixes may be added before the part-of-speech code, separated from the main
  lexeme by a pound sign (#)
- compound words have normal part-of-speech codes and word types, joined
  together by plus signs (+), and preceded by the part-of-speech code of the
  compound as a whole (e.g., n|+adj|black+n|bird)
- cliticized words are written with a tilde (~) connecting it to the previous
  word.

Example::

   CHAT: let's see, I'm going to make Dad's dinner &xxx .``
   Enum: 1|let's 2|see 3|I 4|'m 5|going 6|to 7|make 8|Dad 9|'s 10|dinner 11|.``
   Mor: aux|let's v|see pro|I~aux|be&1S aux|go-PROG inf|to v|make n:prop|Dad-POSS n|dinner .


.. _mor-column-dep-by:

3.7.6. Depended Upon By
-----------------------

In :ref:`morpho-syntax-level`:
   :ref:`Syn <syn-column-horz-dep>`,
   :ref:`Clauses <clauses-column-horz-dep>`,
   :ref:`NP <np-column-horz-dep>`,
   :ref:`PP <pp-column-horz-dep>`,
   :ref:`DPP <dpp-column-horz-dep>`,
   :ref:`WPU <wpu-column-horz-dep>`,
   :ref:`Passives <passives-column-horz-dep>`,
   :ref:`SynType <syntype-column-horz-dep>`,

In :ref:`erica-level`:
   :ref:`Syn <syn-column-horz-dep>`,
   :ref:`Clauses <clauses-column-horz-dep>`,
   :ref:`NP <np-column-horz-dep>`,
   :ref:`PP <pp-column-horz-dep>`,
   :ref:`DPP <dpp-column-horz-dep>`,
   :ref:`WPU <wpu-column-horz-dep>`,
   :ref:`Passives <passives-column-horz-dep>`,
   :ref:`SynType <syntype-column-horz-dep>`,
