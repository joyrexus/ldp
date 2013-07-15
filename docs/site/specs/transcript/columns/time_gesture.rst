.. _time-g-column:

3.24. Time - Timing of Gesture
========================================


.. _time-g-column-description:

3.24.1. Description
-------------------

Records where a gesture occurs in the *word order* of a spoken utterance


.. _time-g-column-format:

3.24.2. Format
--------------

.. productionlist::
   entry: `value_set` [`op` `value_set`]*
   value_set: `value_list` [`set_op` `value_list`]*
   value_list: `value` [`list_op` `value`]*
   value: 0.5, 1..N, N.5 <See description below>
   list_op: ","
   set_op: "/"
   op: ";"

.. _time-g-column-values:

3.24.3. Values
--------------

Values have the following interpretations:

+-------------------+----------------+----------------------------------------+
| Value             | Meaning        | Description                            |
+===================+================+========================================+
| ``0.5``, ``1`` .. | Timing indices | Timing of gesture with respect to the  |
| ``N``, ``N.5``    |                | Enum column entry (``N`` is the        |
|                   |                | largest number associated with a word  |
|                   |                | in the :ref:`Enum column<enum-column>` |
|                   |                | entry)                                 |
+-------------------+----------------+----------------------------------------+
| ``X``             | Null           | No speech to available to relate       |
+-------------------+----------------+----------------------------------------+
| ``NA``            | Not applicable | Speech excluded by CHAT or to the      |
|                   |                | Enum column entry                      |
+-------------------+----------------+----------------------------------------+


Ops are drawn from the following set of operators:

=====  ==============================================================
Op     Meaning
=====  ==============================================================
``;``  Separates all codes
``/``  Used to combine representational codes into single units
``,``  Used to create a list of values
=====  ==============================================================


.. _time-g-column-vert-dep:

3.24.4. Vertical Dependencies
-----------------------------

    None


.. _time-g-column-horz-dep:

3.24.5. Horizontal Dependencies
-------------------------------

Time is dependent on the :ref:`Form Column<form-column-dep-by>`, the
:ref:`Utts Column<utts-column-dep-by>`, and the
:ref:`Enum Column<enum-column-dep-by>`.

+--------------------+--------------------------------------------------------+
| Time               | Conditions                                             |
+====================+========================================================+
| ``0.5``, ``1`` ..  | When the gesture is accompanied by normal speech, the  |
| ``N.5``, ``N``     | values can be 0.5, N.5, or an integral value between 1 |
|                    | and N, inclusive, where N is the number of words       |
|                    | in the Enum column.                                    |
+--------------------+--------------------------------------------------------+
| ``X``              | Used when a gesture is not accompanied by speech of    |
|                    | any kind, i.e. there is no value entered in either the |
|                    | Utts or the Enum column.                               |
+--------------------+--------------------------------------------------------+
| ``NA``             | Used when there is an entry in Form and Utts, but,     |
|                    | because of the CHAT handling of speech errors and      |
|                    | meaningless speech, the Enum column is empty.  As a    |
|                    | result, timing of gesture with respect to speech is,   |
|                    | for our purposes, not an applicable characteristic.    |
+--------------------+--------------------------------------------------------+


.. _time-g-column-dep-by:

3.24.6. Depended Upon By
------------------------

:ref:`Time_Gen <timegen-column-horz-dep>`
