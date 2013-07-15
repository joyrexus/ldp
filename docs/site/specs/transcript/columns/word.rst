.. _word-column:

3.26. Word - Speech Correlate of Gesture
========================================


.. _word-column-description:

3.26.1. Description
-------------------

Records the word that is reinforced or disambiguated by a gesture performed
during the utterance.


.. _word-column-format:

3.26.2. Format
--------------

.. productionlist::
   entry: `value_set` [`op` `value_set`]*
   value_set: `null` | [`non_consecutive`] `value_list` [`set_op` `value_list`]*
   null: "X" | "NA" | "UC"
   non_consecutive: "*"
   value_list: `value` [`list_op` `value`]*
   value: <Any word from the utterance as represented in Enum>
   list_op: ","
   set_op: "/"
   op: ";"


.. _word-column-values:

3.26.3. Values
--------------

Values are either a list of words (optionally preceded by a ``*`` to indicate
that they are non-consecutive words from an utterance) or one of the three
null codes described below:

======  ==============  =======================================================
Nulls   Meaning         Description
======  ==============  =======================================================
``NA``  Not applicable  The gesture is only accompanied by meaningless speech
``UC``  Unclear         The words being reinforced or disambiguated are unclear
``X``   Null            The gesture neither reinforces nor disambiguates
======  ==============  =======================================================


Ops are drawn from the following set of operators:

=====  ========================================================
 Op     Meaning
=====  ========================================================
``;``  Separates all codes
``/``  Used to combine representational codes into single units
``,``  Used to create a list of values
=====  ========================================================


.. _word-column-vert-dep:

3.26.4. Vertical Dependencies
-----------------------------

None


.. _word-column-horz-dep:

3.26.5. Horizontal Dependencies
-------------------------------

Word is dependent on the :ref:`Utts Column<utts-column-dep-by>`,
the :ref:`Enum Column<enum-column-dep-by>`,
the :ref:`Form Column<form-column-dep-by>`,
the :ref:`G_Type Column<gtype-column-dep-by>`,
and the :ref:`GS_Rel Column<gsrel-column-dep-by>`.

``X`` is only permitted if the corresponding G_Type is ``C``, ``FA``, or ``G`` 
or the the corresponding GS_Rel code is ``E``, ``X``, or an ``ADD``-type.

``NA`` is only permitted if there is a gesture in Form with an Utts entry
composed entirely of meaningless speech such that Enum is empty.

``UC`` is permitted whenever appropriate.

Word value sets must otherwise overlap with values found in the Enum column in
one of two ways: 1) The entire value set must appear, in order, in Enum or 2)
If the value set begins with ``*``, the words in the value set must appear, in 
order, in Enum.

For Example::

    Enum = "1|How 2|are 3|you 4|?"
    Word can be "HOW ARE" but not "HOW YOU" or "YOU ARE"

    Enum = "1|The 2|pink 3|bunny 4|and 5|Tuvok 6|are 7|married 8|."
    Word can be "*BUNNY TUVOK" but not "*TUVOK BUNNY"


.. _word-column-dep-by:

3.26.6. Depended Upon By
------------------------

In :ref:`erica-level`:
   :ref:`Word_Num <wordnum-column>`
