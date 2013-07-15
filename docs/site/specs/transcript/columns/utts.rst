.. _utts-column:

3.4. Utts - Transcribed Utterances
==================================


.. _utts-column-description:

3.4.1. Description
------------------

Speaker specific utterance transcription


.. _utts-column-format:

3.4.2. Format
-------------

.. productionlist::
    entry: `value` [" " `value`]*
    value: <Any English word> | `foreign_word` | `untranscribed` 
    foreign_word: "x@f"
    untranscribed: "###"

Normal English sentence structure with all words but proper nouns in lower
case.  Special classes of words are marked with the following characters:

Characters     Meaning           Example
  @l         alphabet letter   a@l

etc.


.. _utts-column-values:

3.4.3. Values
-------------

Any canonically spelled series of words or proper nouns, ``---``, or ``###``\ .


.. _utts-column-vert-dep:

3.4.4. Vertical Dependencies
----------------------------

None


.. _utts-column-horz-dep:

3.4.5. Horizontal Dependencies
------------------------------

Utts is dependent on the :ref:`Key Column <key-column-dep-by>`.


.. _utts-column-dep-by:

3.4.6. Depended Upon By
-----------------------

In :ref:`morpho-syntax-level`:
   :ref:`Chat <chat-column-horz-dep>`

In :ref:`erica-level`:
   :ref:`Time (Gesture) <time-g-column-horz-dep>`,
   :ref:`Word <word-column-horz-dep>`,
   :ref:`Word_Num <wordnum-column-horz-dep>`,
   :ref:`Added <added-column-horz-dep>`,
   :ref:`Reinf <reinf-column-horz-dep>`
