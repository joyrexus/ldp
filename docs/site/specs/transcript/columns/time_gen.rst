.. _timegen-column:

3.25. Time_Gen - General Timing
===============================

.. _timegen-column-description:

3.25.1. Description
-------------------

Records, in general terms, where gestures fall in relation to the 
*whole utterance*


.. _timegen-column-format:

3.25.2. Format
--------------

.. productionlist::
   entry: `value_set` [`op` `value_set`]*
   value_set: `null` | `value` [`set_op` `value`]*
   value: "B" | "M" | "E" | "W"
   null: "X"
   set_op: "/"
   op: ";"


.. _timegen-column-values:

3.25.3. Values
--------------

+--------+----------------+---------------------------------------------------+
| Code   | Meaning        | Description                                       |
+========+================+===================================================+
| ``B``  | Beginning      | Gesture overlaps with the beginning of the        |
|        |                | utterance but does not last until the end         |
+--------+----------------+---------------------------------------------------+
| ``M``  | Middle         | Gesture is performed entirely within the utterance|
+--------+----------------+---------------------------------------------------+
| ``E``  | End            | Gesture overlaps with the end of the utterance    |
|        |                | but not the beginning                             |
+--------+----------------+---------------------------------------------------+
| ``W``  | Whole          | Gesture overlaps with the whole utterance         |
+--------+----------------+---------------------------------------------------+
| ``X``  | Null           | Null for some reason                              |
+--------+----------------+---------------------------------------------------+
| ``NA`` | Not applicable | Not applicable for some other reason              |
+--------+----------------+---------------------------------------------------+


Ops are drawn from the following set of operators:

=====  ========================================================
 Op    Meaning
=====  ========================================================
``;``  Separates all codes
``/``  Used to combine representational codes into single units
``,``  Used to create a list of values
=====  ========================================================


.. _timegen-column-vert-dep:

3.25.4. Vertical Dependencies
-----------------------------

    None


.. _timegen-column-horz-dep:

3.25.5. Horizontal Dependencies
-------------------------------

Time_Gen is dependent upon the :ref:`Time (Gesture) Column <time-g-column>` and
the :ref:`Enum Column <enum-column-dep-by>`.

General timing translates the values found in Time (Gesture) to a simplified
code that indicates the extent and position of overlap between gesture and
speech.  The conversion works as follows:

  -Determine the highest number associated with a word in the Enum column, N

  -If an entry in Time (Gesture) begins with 0.5 or 1 and ends with a value
   that is less than N, the matching Time_Gen entry is ``B``.

  -If an entry in Time (Gesture) begins with a value greater than 1 and ends
   with a value less than N, the matching Time_Gen entry is ``M``.

  -If an entry in Time (Gesture) begins with a value greater than 1 and ends 
   with a value that is either equal to N or N.5, the matching Time_Gen entry
   is ``E``.

  -If an entry in Time (Gesture) begins with 0.5 or 1 and ends with a value
   that is equal to either N or N.5, the matching Time_Gen entry is ``W``.

  -If the value in Time (Gesture) is ``X`` or ``NA``, it is the same in 
   Time_Gen.


.. _timegen-column-dep-by:

3.25.6. Depended Upon By
------------------------

None
