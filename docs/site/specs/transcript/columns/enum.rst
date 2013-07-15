.. _enum-column:

3.6. Enum - Enumerated Utterances
=================================


.. _enum-column-description:

3.6.1. Description
------------------

Speaker specific utterance transcription with each word and final punctuation
enumerated to aid in second-layer gesture coding


.. _enum-column-format:

3.6.2. Format
-------------

.. productionlist::
   entry: `enum`+ `enum_punct`
   enum: `number` "|" `value`
   number: <Positive integer>
   value: english_word | foreign_word | letter | idiosyncratic_word | clitic
   english_word: <Any English word>
   foreign_word: "word@f" <where word is any foreign word>
   letter: "x@l" <where x is any letter>
   idiosyncratic_word: "word@" <where word is any word unique to child>
   clitic: "'s" | "'ll" | "'m" | "'d" | "'ve"
   enum_punct: `number` "|" `punct`
   punct: "." | "?" | "!" | "+..."


.. _enum-column-values:

3.6.3. Values
-------------

Enum entries are composed of enumerated words and orthographic elements.  They
are created by:

1. Expanding a CHAT formatted utterance into a list of all canonically
   spelled words, proper nouns, clitics (``'s``, ``'ll``, ``'m``,
   ``'d``, and ``'ve``), standard sentence-final punctuation, and ``+...``\ s

2. Going through the list and prepending each list item with its numbered
   position (positions start with 1), and a pipe symbol (``|``)


.. _enum-column-vert-dep:

3.6.4. Vertical Dependencies
----------------------------

None


.. _enum-column-horz-dep:

3.6.5. Horizontal Dependencies
------------------------------

Enum is dependent upon the :ref:`CHAT Column <chat-column-dep-by>`.

Enum is derived directly from the content of the CHAT column with the following
modifications:

- Each word that has the ``&`` prefix is removed, as are all non-sentence-final
  punctuation and the ``#`` symbol

- Words that are contractions with the word "not" are expanded (e.g. don't => 
  do not)

- Other words that are written with an apostrophe (I'm, he'll, Mom's, etc.)
  are split before the apostrophe (with the exception of let's)

- All remaining words and punctuation are prefixed by their word number and
  the ``|`` symbol.

Example::

   CHAT: let's see, I'm going to make Dad's dinner &xxx .
   Enum: 1|let's 2|see 3|I 4|'m 5|going 6|to 7|make 8|Dad 9|'s 10|dinner 11|.


.. _enum-column-dep-by:

3.6.6. Depended Upon By
-----------------------

None
