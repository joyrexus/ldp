.. _presref-column:

3.29. Pres_Ref - Presence of Referent
=====================================


.. _presref-column-description:

3.29.1. Description
-------------------

Records whether an object or action is physically present when it is referenced
in gesture


.. _presref-column-format:

3.29.2. Format
--------------

.. productionlist::
   entry: `code_set` [`op` `code_set`]*
   code_set: (`null` | `code`) [`set_op` (`null` | `code`)]*
   null: "X"
   code: "Y" | "N" | "UC"
   set_op: "/"
   op: ";"


.. _presref-column-values:

3.29.3. Values
--------------

Codes have the following interpretations:

+--------+---------+----------------------------------------------------------+
| Code   | Meaning | Description                                              |
+========+=========+==========================================================+
| ``Y``  | Yes     | Gesturer can see the object or action (or its location)  |
|        |         | that is referred to in gesture                           |
+--------+---------+----------------------------------------------------------+
| ``N``  | No      | Gesturer cannot see the object or action (or its         |
|        |         | location) that is referred to in gesture                 |
+--------+---------+----------------------------------------------------------+
| ``UC`` | Unclear | Gesture refers to an object or action that is not        |
|        |         | visible to the camera but which might be present (e.g.   |
|        |         | something on a computer screen or in a book)             |
+--------+---------+----------------------------------------------------------+
| ``X``  | Null    | Gesture refers to something that cannot have a physical  |
|        |         | referent                                                 |
+--------+---------+----------------------------------------------------------+

Ops have the following interpretations:

=====  ==============================================================
Op     Meaning
=====  ==============================================================
``;``  Separates all ``code``\ s
``/``  Used to combine representational ``code``\ s into single units
=====  ==============================================================


.. _presref-column-vert-dep:

3.29.4. Vertical Dependencies
-----------------------------

    None


.. _presref-column-horz-dep:

3.29.5. Horizontal Dependencies
-------------------------------

Pres_Ref is dependent on the :ref:`G_Type Column <gtype-column-dep-by>`.

``X`` is only allowed when the corresponding G_Type code is ``C``, ``E``,
``FA``, or ``G``, and is required when G_Type is ``E``.  Otherwise, a non-``X``
code is required.


.. _presref-column-dep-by:

3.29.6. Depended Upon By
------------------------

None
