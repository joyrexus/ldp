.. _orient-column:

3.20. Orient - Manner of Gesture
================================


.. _orient-column-description:

3.20.1. Description
-------------------

Orient contains any extra information about how a gesture was performed.


.. _orient-column-format:

3.20.2. Format
--------------

.. productionlist::
   entry: (`null` | `value`) [`op` (`null` | `value`)]*
   null: ""
   value: <Description of referent with no punctuation that is also an `op`>
   op: "+" | "-" | "/" | "."


.. _orient-column-values:

3.20.3. Values
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


.. _orient-column-vert-dep:

3.20.4. Vertical Dependencies
-----------------------------

:ref:`See note on continued gestures below <orient-column-horz-dep-continued-note>`


.. _orient-column-horz-dep:

3.20.5. Horizontal Dependencies
-------------------------------

Orient is dependent on the :ref:`Form Column <form-column-dep-by>`.

Orient must have the same number of values and the same number and type of ops
as the Form entry on which it depends.

Some Form codes have canonical orientations:

+---------------+----------------------------+---------------------------------+
| Form Code     | Canonical Orient Values    | Explanation                     |
+===============+============================+=================================+
| ``palm``      | ``palm up``, ``palm down``,| ``palm DIRECTION`` indicates    |
|               | ``palm side``,             |  the direction the palm is      |
|               | ``palm out``; These four   |  facing                         |
|               | values can optionally be   |                                 |
|               | followed by either ``tap`` | ``tap`` indicates multiple,     |
|               | or ``touch``               |  rapid contacts with the object |
|               |                            |  being referenced               |
|               |                            |                                 |
|               |                            | ``touch`` indicates a single    |
|               |                            |  contact with the object being  |
|               |                            |  referenced                     |
+---------------+----------------------------+---------------------------------+
| ``hold``      | ``shake``; An empty string | Used when the object being held |
|               | is also acceptable         | is shaken to, for example, draw |
|               |                            | attention to it                 |
+---------------+----------------------------+---------------------------------+
| ``iconic``    | ``trace path``,            | ``trace shape`` would be used   |
|               | ``trace shape``; An empty  | if the speaker is talking about |
|               | string is also acceptable  | a STOP sign and draws an        |
|               |                            | octagon in the air              |
|               |                            |                                 |
|               |                            | ``trace path`` would be used if |
|               |                            | the speaker is talking about a  |
|               |                            | boy running home while drawing  |
|               |                            | a representation of the path,   |
|               |                            | be it concrete or abstract, he  |
|               |                            | followed to get there           |
+---------------+----------------------------+---------------------------------+
| metaphoric    | ``trace path``,            | Same as ``trace shape`` and     |
|               | ``trace shape``; An empty  | ``trace path`` for ``iconic``\ s|
|               | string is also acceptable  |                                 |
+---------------+----------------------------+---------------------------------+


.. _orient-column-horz-dep-continued-note:

.. note::
   If the code in Form is :term:`continued` (ending with ``~``), the
   corresponding value in Gloss must be the same as the Gloss value associated
   with the Form code being continued on the immediately preceding line with a 
   communicative act on the part of the speaker.


.. _orient-column-dep-by:

3.20.6. Depended Upon By
------------------------

None
