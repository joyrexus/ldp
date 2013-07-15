.. _mspd-column:

3.21. MSPD - Motion-Space Descriptor
====================================


.. _mspd-column-description:

3.21.1. Description
-------------------

A detailed description of what the gesture looked like; can also be used if 
someone points at something with another object in the same hand


.. _mspd-column-format:

3.21.2. Format
--------------

.. productionlist::
   entry: (`null` | `value`) [`op` (`null` | `value`)]*
   null: ""
   value: <Description of gesture with no punctuation that is also an `op`>
   op: "+" | "-" | "/" | "."


.. _mspd-column-values:

3.21.3. Values
--------------

Values are whatever constitute a thorough description of the gesture without 
punctuation that double as ops.

Ops have the following interpretation:

=====  ================================================================
 Op    Meaning
=====  ================================================================
``+``  Simultaneous gestures
``-``  Sequential gestures without return to neutral position
``/``  Gestures morph into one another
``.``  Sequential gestures with return to neutral position - DEPRECATED
=====  ================================================================


.. _mspd-column-vert-dep:

3.21.4. Vertical Dependencies
-----------------------------

:ref:`See note on continued gestures below <mspd-column-horz-dep-continued-note>`


.. _mspd-column-horz-dep:

3.21.5. Horizontal Dependencies
-------------------------------

MSPD is dependent on the :ref:`Form Column <form-column-dep-by>`.

MSPD must have the same number of values and the same number and type of ops as
the Form entry on which it depends.


.. _mspd-column-horz-dep-continued-note:

.. note::
   If the code in Form is :term:`continued` (ending with ``~``), the
   corresponding value in MSPD must be the same as the MSPD value associated
   with the Form code being continued on the immediately preceding line with a 
   communicative act on the part of the speaker.


.. _mspd-column-dep-by:

3.21.6. Depended Upon By
------------------------

None
