.. index:: 
   single: column; gesture gloss
   single: gesture; gloss

.. _gloss-column:

3.19. Gloss - Meaning of Gesture
================================


.. _gloss-column-description:

3.19.1. Description
-------------------

The meaning of the gesture


.. _gloss-column-format:

3.19.2. Format
--------------

.. productionlist::
   entry: (`null` | `value`) [`op` (`null` | `value`)]*
   null: ""
   value: <Description of referent with no punctuation that is also an `op`>
   op: "+" | "-" | "/" | "."


.. _gloss-column-values:

3.19.3. Values
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


.. _gloss-column-vert-dep:

3.19.4. Vertical Dependencies
-----------------------------

:ref:`See note on continued gestures below <gloss-column-horz-dep-continued-note>`


.. _gloss-column-horz-dep:

3.19.5. Horizontal Dependencies
-------------------------------

Gloss is dependent on the :ref:`Form Column <form-column-dep-by>`.

Gloss must have the same number of values and the same number and type of ops as
the Form entry on which it depends.

If the corresponding Form code is a deictic, generally this will be the same as
the corresponding value in Gloss.  If the gesture can be interpreted as a 
giving or taking action and the value in Gloss is ``apple``, ``give apple`` or
``take apple`` will typically be used.

Many conventionals have commonly agreed-upon meanings.  When using one of these
codes in Form, the Gloss value should be pulled from the following:

+---------------------+--------------------------------------------------+
| Form Codes          | Canonical Gloss Values                           |
+=====================+==================================================+
| ``beat``            | ``emphasis``                                     |
+---------------------+--------------------------------------------------+
| ``come``            | ``come here``, ``go ahead``                      |
+---------------------+--------------------------------------------------+
| ``dismiss``         | ``no``, ``go away``, ``all done``                |
+---------------------+--------------------------------------------------+
| ``flip``            | ``all gone``, ``all done``, ``don't know``,      |
|                     | ``where?``, ``exclamation``, ``whatever``,       |
|                     | ``question``                                     |
+---------------------+--------------------------------------------------+
| ``naughties``       | ``warning``, ``gotcha``                          |
+---------------------+--------------------------------------------------+
| ``nod``             | ``yes``, ``emphasis``                            |
+---------------------+--------------------------------------------------+
| ``number``          | ``number one``, ``number two``, ...              |
|                     | ``counting number one``,                         |
|                     | ``counting number two``, ...                     |
+---------------------+--------------------------------------------------+
| ``got it``          | ``etc``, ``got it``, ``get it``, ``you know``,   |
|                     | ``ok``                                           |
+---------------------+--------------------------------------------------+
| ``oh my``           | ``surprise``, ``exclamation``                    |
+---------------------+--------------------------------------------------+
| ``pick up``         | ``lift c``                                       |
+---------------------+--------------------------------------------------+
| ``pick me``         | ``pick me``, ``I know``                          |
+---------------------+--------------------------------------------------+
| ``shake``           | ``no``, ``emphasis``                             |
+---------------------+--------------------------------------------------+
| ``shh``             | ``be quiet``                                     |
+---------------------+--------------------------------------------------+
| ``shrug``           | ``don't know``, ``doesn't matter``,              |
|                     | ``exclamation``                                  |
+---------------------+--------------------------------------------------+
| ``shrug with flip`` | ``all gone``, ``all done``, ``don't know``,      |
|                     | ``doesn't matter``, ``where?``, ``exclamation``, |
|                     | ``whatever``, ``question``                       |
+---------------------+--------------------------------------------------+
| ``sweep``           | ``all gone``, ``all done``                       |
+---------------------+--------------------------------------------------+
| ``tada``            | ``exclamation``                                  |
+---------------------+--------------------------------------------------+
| ``thinking``        | ``thinking``                                     |
+---------------------+--------------------------------------------------+
| ``x``               | ``ambiguous``                                    |
+---------------------+--------------------------------------------------+
| ``wait``            | ``wait``, ``slow down``, ``cool down``, ``stop`` |
+---------------------+--------------------------------------------------+
| ``wave``            | ``greeting``, ``attention``                      |
+---------------------+--------------------------------------------------+
| ``<back off>``      | ``back off``, ``don't move``                     |
+---------------------+--------------------------------------------------+
| ``<darn it>``       | ``darn it``                                      |
+---------------------+--------------------------------------------------+
| ``<hero fist>``     | ``victory``, ``jubilation``, ``encouragement``   |
+---------------------+--------------------------------------------------+
| ``<listening>``     |                                                  |
+---------------------+--------------------------------------------------+
| ``<oh man>``        | ``oh man``                                       |
+---------------------+--------------------------------------------------+
| ``<pray you>``      | ``please``                                       |
+---------------------+--------------------------------------------------+
| ``<score>``         |                                                  |
+---------------------+--------------------------------------------------+
| ``<so so>``         |                                                  |
+---------------------+--------------------------------------------------+
| ``<thumbs up>``     | ``good job``                                     |
+---------------------+--------------------------------------------------+
| ``<whew>``          |                                                  |
+---------------------+--------------------------------------------------+


.. _gloss-column-horz-dep-continued-note:

.. note::
   If the code in Form is :term:`continued` (ending with ``~``), the
   corresponding value in Gloss must be the same as the Gloss value associated
   with the Form code being continued on the immediately preceding line with a 
   communicative act on the part of the speaker.


.. _gloss-column-dep-by:

3.19.6. Depended Upon By
------------------------

None
