.. _syn-column:

3.8. Syn - Syntax
=================


.. _syn-column-description:

3.8.1. Description
------------------

Grammatical relationship information for transcribed utterances


.. _syn-column-format:

3.8.2. Format
-------------

.. productionlist::
   entry: `value`+
   value: `word_number` "|" `dependency` "|" `gr`
   word_number: <Positive integers>
   dependency: <Non-negative integers>
   gr: <See Grammatical Relationship Code table below>


.. _syn-column-values:

3.8.3. Values
-------------

A series of grammatical relationships with corresponding word and head word 
numbers, following the format above.  The grammatical relationship codes have 
the following interpretations:

===========  ======================================= 
Code         Meaning
===========  ======================================= 
``AUX``      Auxiliary
``CJCT``     Finite clausal adjunct
``CMOD``     Finite clausal modifier
``COM``      Communicator
``COMP``     Finite complement
``COORD``    Coordinated word
``CPRED``    Finite clausal predicate
``CPZR``     Complementizer
``CSUBJ``    Finite clausal subject
``DET``      Determiner
``ENUM``     Enumerated word
``ESUBJ``    Existential subject
``INF``      Infinitive
``IOBJ``     Preposition introducing indirect object 
``JCT``      Non-clausal adjunct
``LOC``      Obligatory locative identifier
``MOD``      Non-clausal modifier of a nominal
``NEG``      Negation
``OBJ``      Object
``OBJ2``     Indirect object without preposition
``POBJ``     Prepositional object
``PRED``     Predicate
``PTL``      Particle
``PUNCT``    Punctuation
``QUANT``    Quantifier
``ROOT``     Head of sentence (verbal)
``ROOT-NV``  Head of sentence (non-verbal)
``SRL``      Serial verb
``SUBJ``     Subject
``TAG``      Verb used as tag
``TOP``      Topicalizer
``VOC``      Vocative
``XCOMP``    Non-finite complement
``XJCT``     Non-finite clausal adjunct
``XMOD``     Non-finite clausal modifier
``XPRED``    Non-finite clausal predicate
``XSUBJ``    Non-finite clausal subject
===========  ======================================= 

.. note:
   Additionally, ``DET`` may be combined with ``-SUBJ``, ``-OBJ``, ``-POBJ``,
   or ``-PRED`` (e.g. ``DET-PRED``).  ``AUX`` and ``INF`` may be combined with
   ``-COMP``, ``-XCOMP``, ``-CJCT``, ``-XJCT``, ``-CSUBJ``, ``-XSUBJ``,
   ``-CMOD``, ``-XMOD``, ``-CPRED``, ``-XPRED``, or ``ROOT`` (e.g. 
   ``INF-ROOT``, ``AUX-COMP``).  ``COORD`` may be combined with any GR type 
   that is being coordinated (e.g. ``COORD-ROOT``, ``COORD-POBJ``).


.. _syn-column-vert-dep:

3.8.4. Vertical Dependencies
----------------------------

None


.. _syn-column-horz-dep:

3.8.5. Horizontal Dependencies
------------------------------

Syn is dependent on the :ref:`Mor Column <mor-column-dep-by>`.

Each unit from the Mor column (including the punctuation) is replaced with a 
unit that encodes the word's order in the utterance, the number of the word on 
which it is dependent, and the relationship of that dependency.

Example::

   Mor: pro|you v|get&PAST pro|me !
   Syn: 1|2|SUBJ 2|0|ROOT 3|2|OBJ 4|2|PUNCT


.. _syn-column-dep-by:

3.8.6. Depended Upon By
-----------------------

In :ref:`morpho-syntax-level`:
   :ref:`Clauses <clauses-column-horz-dep>`,
   :ref:`NP <np-column-horz-dep>`,
   :ref:`PP <pp-column-horz-dep>`,
   :ref:`DPP <dpp-column-horz-dep>`,
   :ref:`WPU <wpu-column-horz-dep>`,
   :ref:`Passives <passives-column-horz-dep>`,
   :ref:`SynType <syntype-column-horz-dep>`

In :ref:`erica-level`:
   :ref:`Clauses <clauses-column-horz-dep>`,
   :ref:`NP <np-column-horz-dep>`,
   :ref:`PP <pp-column-horz-dep>`,
   :ref:`DPP <dpp-column-horz-dep>`,
   :ref:`WPU <wpu-column-horz-dep>`,
   :ref:`Passives <passives-column-horz-dep>`,
   :ref:`SynType <syntype-column-horz-dep>`
