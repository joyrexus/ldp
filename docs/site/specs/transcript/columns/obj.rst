.. _obj-column:

3.18. Obj - Referent of Gesture
===============================


.. _obj-column-description:

3.18.1. Description
-------------------

Used for deictic gestures (and, optionally, demos) to indicate the referent of 
the gesture


.. _obj-column-format:

3.18.2. Format
--------------

.. productionlist::
   entry: (`null` | `value`) [`op` (`null` | `value`)]*
   null: ""
   value: <Description of referent with no punctuation that is also an `op`>
   op: "+" | "-" | "/" | "."


.. _obj-column-values:

3.18.3. Values
--------------

Because it would be impossible to account for all potential referents, 
values can be anything so long as they do not include punctuation that double
as ops.

Ops have the following interpretation:

=====  ================================================================
 Op    Meaning
=====  ================================================================
``+``  Simultaneous gestures
``-``  Sequential gestures without return to neutral position
``/``  Gestures morph into one another
``.``  Sequential gestures with return to neutral position - DEPRECATED
=====  ================================================================


.. _obj-column-vert-dep:

3.18.4. Vertical Dependencies
-----------------------------

:ref:`See note on continued gestures below <obj-column-horz-dep-continued-note>`


.. _obj-column-horz-dep:

3.18.5. Horizontal Dependencies
-------------------------------

Obj is dependent on the :ref:`Form Column <form-column-dep-by>`.

Obj must have the same number of values and the same number and type of ops
as the Form entry on which it depends.

Only deictic and demo gestures can take values in the Obj column.
Specifically, ``cont palm``, ``cont point``, ``drag``, ``palm``, ``point``, and
``hold`` require a corresponding value in Obj; demo can optionally take one.

.. _obj-column-horz-dep-continued-note:

.. note::
   If the code in Form is :term:`continued` (ending with ``~``), the
   corresponding value in Obj must be the same as the Obj value associated with
   the Form code being continued on the immediately preceding line with a 
   communicative act on the part of the speaker.

   Example::

      Line 1:
         Form: hold + point
         Obj: eraser + pencil
      Line 2:
         Form: point~
         Obj: pencil


.. _obj-column-dep-by:

3.18.6. Depended Upon By
------------------------

None
