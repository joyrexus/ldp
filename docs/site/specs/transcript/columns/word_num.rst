.. _wordnum-column:

3.27. Word_Num - Enumeration of Speech Correlate
================================================


.. _wordnum-column-description:

3.27.1. Description
-------------------

Records the :ref:`Enum Column <enum-column>` index of the word that is 
reinforced or disambiguated by a gesture performed during the utterance.


.. _wordnum-column-format:

3.27.2. Format
--------------

.. productionlist::
   entry: `value_set` [`op` `value_set`]*
   value_set: `null` | [`non_consecutive`] `value_list` [`set_op` `value_list`]*
   null: "NA" | "UC" | "X"
   non_consecutive: "*"
   value_list: `value` [`list_op` `value`]*
   value: <integer no greater than the largest value in Enum>
   list_op: ","
   set_op: "/"
   op: ";"


.. _wordnum-column-values:

3.27.3. Values
--------------

Values are either a list of integers corresponding to the enumeration of an
utterance (optionally preceded by a ``*`` to indicate that they are tied to
non-consecutive words) or one of the three null codes described below:

======  ==============  =======================================================
Null    Meaning         Description
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


.. _wordnum-column-vert-dep:

3.27.4. Vertical Dependencies
-----------------------------

None


.. _wordnum-column-horz-dep:

3.27.5. Horizontal Dependencies
-------------------------------

Word_Num is dependent on the :ref:`Enum Column<enum-column-dep-by>` and the
:ref:`Word Column <word-column-dep-by>`.

``X`` is only allowed when the corresponding value in Word is also ``X``.

``UC`` is permitted whenever appropriate.

``NA`` is permitted only when the utterance is composed exclusively of 
meaningless speech resulting in an empty Enum entry.  Effectively, this means
that when Word is ``NA``, Word_Num should be as well.

Otherwise, the values in each value set of Word_Num should be the numbers 
appearing in Enum that are associated with the corresponding value set in Word.
Just like with Word, the ``*`` indicates non-consecutive values.

For Example::

    Enum = "1|How 2|are 3|you 4|and 5|where 6|are 7|you 8|going 9|?"
    Word = "ARE YOU"
    Word_Num could be either "2,3" or "6,7" but not "2,7"

    Enum = "1|The 2|pink 3|bunny 4|and 5|Tuvok 6|are 7|married 8|."
    Word = "*BUNNY TUVOK"
    Word_Num = "*3,5"


.. _wordnum-column-dep-by:

3.27.6. Depended Upon By
------------------------

None
