.. _reinf-column:

3.30. Reinf - Reinforcing Information
=====================================


.. _reinf-column-description:

3.30.1. Description
-------------------

Specifies what type of information is being reinforced by the gesture.


.. _reinf-column-format:

3.30.2. Format
--------------

.. productionlist::
   entry: `code_set` [";" `code_set`]*
   code_set: (`null` | `code_list`) ["/" ( `null` | `code_list` )]*
   code_list: `code` ["," `code`]*
   code: "AB" | "AO" | "L" | "M" | "P" | "SH" | "SI"
   null: "X"


.. _reinf-column-values:

3.31.3. Values
--------------

Codes have the following interpretations:

+--------+-----------+----------------------------+---------------------------+
| Code   | Meaning   | Description                | Example                   |
+========+===========+============================+===========================+
| ``AB`` | Action by | An object referenced by an | Hands form claws, raised  |
|        |           | action it typically        | up and swept out and down |
|        |           | performs                   | to signifiy "bear"        |
+--------+-----------+----------------------------+---------------------------+
| ``AO`` | Action on | An object referenced by an | Flat hands with palms     |
|        |           | action typically performed | together, hands open out  |
|        |           | on it                      | to signifiy "book"        |
+--------+-----------+----------------------------+---------------------------+
| ``L``  | Location  | The (relative) location of | Flat hands held palms     |
|        |           | an act or object           | down side by side to      |
|        |           |                            | indicate that one object  |
|        |           |                            | is close to another       |
+--------+-----------+----------------------------+---------------------------+
| ``M``  | Manner    | The type of action         | Hand is bounced up and    |
|        |           | performed or the way in    | down to indicate jumping  |
|        |           | which it is executed       |                           |
+--------+-----------+----------------------------+---------------------------+
| ``P``  | Path      | The path through which an  | Hand sweeps out and to    |
|        |           | act moves as it is         | the side to signify the   |
|        |           | performed                  | path something has taken  |
|        |           |                            | around another object     |
+--------+-----------+----------------------------+---------------------------+
| ``SH`` | Shape     | The shape of an object     | Finger traces "v" in air  |
|        |           |                            | to signify the type of    |
|        |           |                            | shirt desired             |
+--------+-----------+----------------------------+---------------------------+
| ``SI`` | Size      | The size of an object      | Hand extends over head to |
|        |           |                            | signify "tall"            |
+--------+-----------+----------------------------+---------------------------+
| ``X``  | Null      | The gesture does not       |                           |
|        |           | reinforce the speech       |                           |
+--------+-----------+----------------------------+---------------------------+

Ops have the following interpretations:

=====  ==============================================================
Op     Meaning
=====  ==============================================================
``;``  Separates all codes
``/``  Used to combine representational codes into single units
``,``  Used to create lists of codes
=====  ==============================================================


.. _reinf-column-vert-dep:

3.31.4. Vertical Dependencies
-----------------------------

None


.. _reinf-column-horz-dep:

3.31.5. Horizontal Dependencies
-------------------------------

Reinf is dependent upon the :ref:`Utts Column <utts-column-dep-by>`, the
:ref:`G_Type Column <gtype-column-dep-by>`, and the
:ref:`Added Column <added-column-dep-by>`

+--------+--------------------------------------------------------------------+
| Reinf  | Conditions                                                         |
+========+====================================================================+
| ``AB`` | An utterance is transcribed in Utts and the corresponding G_Type   |
|        | code is ``R.a``, ``R.d``, ``R.m``, or ``R.met``                    |
+--------+--------------------------------------------------------------------+
| ``AO`` | An utterance is transcribed in Utts and the corresponding G_Type   |
|        | code is ``R.a``, ``R.d``, ``R.m``, or ``R.met``                    |
+--------+--------------------------------------------------------------------+
| ``L``  | An utterance is transcribed in Utts and the corresponding G_Type   |
|        | code is ``R.a``, ``R.d``, ``R.m``, or ``R.met``                    |
+--------+--------------------------------------------------------------------+
| ``M``  | An utterance is transcribed in Utts and the corresponding G_Type   |
|        | code is ``R.a``, ``R.d``, ``R.m``, or ``R.met``                    |
+--------+--------------------------------------------------------------------+
| ``P``  | An utterance is transcribed in Utts and the corresponding G_Type   |
|        | code is ``R.a``, ``R.d``, ``R.m``, or ``R.met``                    |
+--------+--------------------------------------------------------------------+
| ``SH`` | An utterance is transcribed in Utts and the corresponding G_Type   |
|        | code is ``R.a``, ``R.d``, ``R.m``, or ``R.met``                    |
+--------+--------------------------------------------------------------------+
| ``SI`` | An utterance is transcribed in Utts and the corresponding G_Type   |
|        | code is ``R.a``, ``R.d``, ``R.m``, or ``R.met``                    |
+--------+--------------------------------------------------------------------+
| ``X``  | Either:                                                            |
|        |                                                                    |
|        | An utterance is transcribed in Utts, the corresponding             |
|        | G_Type code is ``R.a``, ``R.d``, ``R.met``, or ``C``, and the      |
|        | corresponding Added code is not ``X``                              |
|        |                                                                    |
|        | An utterance is not transcribed in Utts                            |
+--------+--------------------------------------------------------------------+


.. _reinf-column-dep-by:

3.31.6. Depended Upon By
------------------------

:ref:`Added <added-column-horz-dep>`
