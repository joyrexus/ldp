.. _syntype-column:

3.15. SynType - Coded Syntactic Type
====================================


.. _syntype-column-description:

3.15.1. Description
-------------------

Syntactic type of transcribed utterance


.. _syntype-column-format:

3.15.2. Format
--------------

.. productionlist::
   entry: `zero_clause_value` | `one_clause_value` | `two_clause_value`+
   zero_clause_value: "n" | "np" | "p" | "pp" | "adj" | "adjp" | "adv" | "advp" | "z" | "x"
   one_clause_value: "d | ";d" | "i" | ";i" | ";d/i" | "ni" | "q" | ";q" | "S2" | "ORC"
   two_clause_value: "CO | "S1" | "S2" | "SC" | "OC" | "SRC" | "ORC"


.. _syntype-column-values:

3.15.3. Values
--------------

Zero clause codes have the following interpretations:

========  =======================================
Code      Description
========  =======================================
``n``     Noun
``np``    Noun phrase
``p``     Preposition
``pp``    Prepositional phrase
``adj``   Adjective
``adjp``  Adjective phrase
``adv``   Adverb
``advp``  Adverb phrase
``z``     Proper noun
``x``     Other ("hi", "ouch", "bless+you", etc.)
========  =======================================


One clause codes have the following interpretations:

========  ============================================================================
Code      Description
========  ============================================================================
``d``     Declarative utterance with standard SV(O) word order
``;d``    Declarative utterance with non-standard word order
``i``     Imperative utterance with standard V(O) word order
``ni``    Imperative utterance with "do not" + VERB word order
``;i``    Imperative utterance with non-standard word order
``;d/i``  Ambiguous utterance with V(O) word order (only for child utterances)
``q``     Question with standard inverted word order ((wh-word)? aux SVO)
``;q``    Question with non-standard word order
``ORC``   Single NP with relative clause modifier ("the boy you saw")
``S2``    Non-verbal head of utterance with clausal argument ("thanks for helping me")
========  ============================================================================


Two clause codes have the following interpretations:

=======  ==============================================================
Code     Description
=======  ==============================================================
``CO``   Coordinated clauses
``S1``   Subordinate clause positioned before matrix clause
``S2``   Subordinate clause positioned after matrix clause
``SC``   Clause acting as subject of an utterance
``OC``   Clause acting as object of an utterance (complement clause)
``SRC``  Clause modifying a nominal that is the subject of an utterance 
``ORC``  Clause modifying a nominal that is the object of an utterance
=======  ==============================================================


.. _syntype-column-vert-dep:

3.15.4. Vertical Dependencies
-----------------------------

None


.. _syntype-column-horz-dep:

3.15.5. Horizontal Dependencies
-------------------------------

SynType is dependent on the :ref:`Mor Column <mor-column-dep-by>`, the
:ref:`Syn Column <syn-column-dep-by>`, and the 
:ref:`Clauses Column <clauses-column-dep-by>`.


.. _syntype-column-dep-by:

3.15.6. Depended Upon By
------------------------

None
