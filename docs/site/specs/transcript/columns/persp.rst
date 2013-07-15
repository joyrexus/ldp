.. _persp-column:

3.32. Persp - Perspective of Representational Gesture
=====================================================


.. _persp-column-description:

3.32.1. Description
-------------------

Determines when iconic gestures are produced from a character (1st person) 
versus an observer (3rd person) point of view


.. _persp-column-format:

3.32.2. Format
--------------

.. productionlist::
   entry: `code_set` [`op` `code_set`]*
   code_set: `null` | `code` [`set_op` `code`]*
   null: "X"
   code: "1" | "3" | "G" | "UC"
   set_op: "/"
   op: ";"


.. _persp-column-values:

3.32.3. Values
--------------

Codes must be drawn from the following:

+--------+--------------+-----------------------------------------------------+
| Code   | Meaning      | Description                                         |
+========+==============+=====================================================+
| ``1``  | First person | Gesture is produced as though the gesturer is       |
|        |              | performing the action or embodying the object       |
+--------+--------------+-----------------------------------------------------+
| ``3``  | Third person | Gesture is performed as though the gesturer is      |
|        |              | looking at the action or object from a distance     |
+--------+--------------+-----------------------------------------------------+
| ``G``  | Global       | Concept is one that cannot have a 1st person        |
|        |              | perspective                                         |
+--------+--------------+-----------------------------------------------------+
| ``UC`` | Unclear      | Perspective of gesture is unclear (could be either  |
|        |              | 1st or 3rd person)                                  |
+--------+--------------+-----------------------------------------------------+ 
| ``X``  | Null         | Gesture is non-iconic (i.e. deictic, conventional,  |
|        |              | or functional acts)                                 |
+--------+--------------+-----------------------------------------------------+

Ops are drawn from the following set of operators:

=====  ==============================================================
Op     Meaning
=====  ==============================================================
``;``  Separates all codes
``/``  Used to combine representational codes into single units
=====  ==============================================================


.. _persp-column-vert-dep:

3.32.4. Vertical Dependencies
-----------------------------

None


.. _persp-column-horz-dep:

3.32.5. Horizontal Dependencies
-------------------------------

Persp is dependent on the :ref:`G_Type Column <gtype-column-dep-by>`.

When a representational gesture is coded in the G_Type column, its
corresponding code in Persp should always be chosen from ``1``, ``3``, ``G``,
and ``UC``.  The null code ``X`` is reserved only for non-iconic gestures as
they lack iconic perspective by definition.


.. _persp-column-dep-by:

3.32.6. Depended Upon By
------------------------

None
