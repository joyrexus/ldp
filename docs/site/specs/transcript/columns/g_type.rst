.. _gtype-column:

3.22. G_Type - Gesture Type
===========================


.. _gtype-column-description:

3.22.1. Description
-------------------

A broad categorization of gestures


.. _gtype-column-format:

3.22.2. Format
--------------

.. productionlist::
   entry: `code_set` [`op` `code_set`]*
   code_set: `code` [`set_op` `code`]*
   code: "C" | `deictic` | "E" | "FA" | "G" | "S" | `representational`
   deictic: "DP" | "DP.nl" | "DS" | "DSDP"
   representational: ("R.a" | "R.d" | "R.m") [".pp" | ".e" ] | "R.met"
   set_op: "/"
   op: ";"


.. _gtype-column-values:

3.22.3. Values
--------------

Codes have the following interpretation:

+-----------+-------------------+---------------------------------------------+
| Code      | Gesture Type      |  Description                                |
+===========+===================+=============================================+
|           |                   | Culturally-determined or ritualized         |
| ``C``     | Conventional      | gestures that serve as symbolic             |
|           |                   | replacements for ideas that are produced in |
|           |                   | similar form every time.                    |
+-----------+-------------------+---------------------------------------------+
|           |                   | Indication of a distal object through       |
| ``DP``    | Deictic point     | directional extension of the finger, hand,  |
|           |                   | limb, or head.                              |
+-----------+-------------------+---------------------------------------------+
| ``.nl``   | Non-literal       | Gesture uses a point to one object or       |
|           | suffix for ``DP`` | location to reference a different object or |
|           |                   | location.                                   |
+-----------+-------------------+---------------------------------------------+
| ``DS``    | Deictic show      | Drawing attention to an object or body part |
|           |                   | by holding it up towards the interlocutor.  |
+-----------+-------------------+---------------------------------------------+
| ``DSDP``  | Deictic show and  | Combination of a deictic show and a deictic |
|           | deictic point     | point                                       |
+-----------+-------------------+---------------------------------------------+
| ``G``     | Give              | Requesting an object by reaching towards    |
|           |                   | the interlocutor with the hand palm-up      |
+-----------+-------------------+---------------------------------------------+
|           |                   | Simple manual gestures or nods marking the  |
| ``E``     | Emphatic          | prosody of speech through temporal          |
|           |                   | correlation with particular words or        |
|           |                   | syllables                                   |
+-----------+-------------------+---------------------------------------------+
|           |                   | Gesture-like movements that re-enact desired|
| ``FA``    | Functional act    | actions (demonstrators) or start object     |
|           |                   | transfers (hold out).                       |
+-----------+-------------------+---------------------------------------------+
| ``S``     | Sign              | Gesture is a sign from either baby sign or  |
|           |                   | ASL.                                        |
+-----------+-------------------+---------------------------------------------+
| ``R.a``   | Representing      | Iconic gesture characterizing an entity by  |
|           | attribute         | means of specifying an attribute or a part  | 
|           |                   | associated with the entity, or the entity   |
|           |                   | itself                                      |
+-----------+-------------------+---------------------------------------------+
| ``R.d``   | Representing      | Iconic gesture characterizing the direction |
|           | direction         | of the motion                               |
+-----------+-------------------+---------------------------------------------+
| ``R.m``   | Representing      | Iconic gesture characterizing an entity by  |
|           | motion            | means of an action associated with the      |
|           |                   | entity                                      |
+-----------+-------------------+---------------------------------------------+
| ``R.met`` | Representing      | Representational gesture indicating a       |
|           | metaphoric        | metaphorical object or movement             |
+-----------+-------------------+---------------------------------------------+
| ``.pp``   | Pretend play      | Gesture is used to mime specific actions    |
|           | suffix for        | from an imagined scene.                     |
|           | ``R.(a|d|m|met)`` | not shared with most other children in the  |
+-----------+-------------------+---------------------------------------------+
| ``.e``    | Emblem suffix for | Gesture appears to be conventional but is   |
|           | ``R.a``, ``R.d``, | not shared with most other children in the  |
|           | ``R.m``, and      | sample.                                     |
|           | ``R.met``         |                                             |
+-----------+-------------------+---------------------------------------------+


Ops have the following interpretation:

=====  ==============================================================
 Op    Meaning
=====  ==============================================================
``;``  Separates all codes
``/``  Used to combine representational codes into single units
=====  ==============================================================


.. _gtype-column-vert-dep:

3.22.4. Vertical Dependencies
-----------------------------

    None


.. _gtype-column-horz-dep:

3.22.5. Horizontal Dependencies
-------------------------------

G_Type is dependent on the :ref:`Form Column <form-column-dep-by>` and the 
:ref:`Gloss Column <gloss-column-dep-by>`.

Generally, G_Type must have the same number of codes and ops as the Form entry
on which it depends.  However, this guideline is made inaccurate by two factors:
  
1. The coalescence of morphing gestures with respect to the second
   tier gesture annotation, i.e. the Form entry ``hold + point / palm`` is 
   interpreted as two units in second tier coding, not three.  Moreover, the 
   final gesture of a set of morphing gestures is considered the sole reference
   point for the subsequent second tier coding.  This is not a common occurrence
   due to the ambiguities of identifying a set of morphing gestures. 

2. A ``hold`` combined with a ``cont palm``, ``cont point``, ``palm``,
   or ``point`` using the ``+`` operator in the Form entry is interpreted as a
   combination of deictic show and deictic point, or ``DSDP``.   This is fairly
   common.

As a result, the number of codes and ops in the G_Type column is related to the
codes in Form, but the relation is not 1:1.

G_Type codes must be drawn from the following table based on the corresponding
Form code or Gloss value:

+-----------------------------+-----------------------------------------------+
| G_Type                      | Form Code (or Gloss Value)                    |
+=============================+===============================================+
| ``C``                       | Form is any conventional gesture              |
+-----------------------------+-----------------------------------------------+
| ``DP``                      | ``cont palm``, ``cont point``, ``palm``,      |
|                             | ``point``                                     |
+-----------------------------+-----------------------------------------------+
| ``DP.nl``                   | ``cont palm``, ``cont point``, ``palm``,      |
|                             | ``point``                                     |
+-----------------------------+-----------------------------------------------+
| ``DS``                      | ``hold``                                      |
+-----------------------------+-----------------------------------------------+
| ``DSDP``                    | The sequence ``hold + P`` or ``P + hold``,    |
|                             | where ``P`` is ``cont palm``, ``cont point``, |
|                             | ``palm``, or ``point``.                       |
+-----------------------------+-----------------------------------------------+
| ``E``                       | ``beat``                                      |
+-----------------------------+-----------------------------------------------+
| ``FA``                      | ``demo`` in Form or ``take`` in Gloss         |
+-----------------------------+-----------------------------------------------+
| ``G``                       | ``give`` in Gloss                             |
+-----------------------------+-----------------------------------------------+
| ``R.((a|d|m)[.e|.pp]|met)`` | ``iconic`` or ``metaphoric``                  |
+-----------------------------+-----------------------------------------------+
| ``S``                       | ``sign``                                      |
+-----------------------------+-----------------------------------------------+


.. _gtype-column-dep-by:

3.22.6. Depended Upon By
------------------------

In :ref:`seyda-level`:
   :ref:`GS_Rel <gsrel-column-horz-dep>`

In :ref:`erica-level`:
   :ref:`GS_Rel <gsrel-column-horz-dep>`,
   :ref:`Time (Gesture) <time-g-column-horz-dep>`,
   :ref:`Time_Gen<timegen-column-horz-dep>`,
   :ref:`Word <word-column-horz-dep>`,
   :ref:`Word_Num <wordnum-column-horz-dep>`,
   :ref:`Sem_Role <semrole-column-horz-dep>`,
   :ref:`Pres_Ref <presref-column-horz-dep>`,
   :ref:`Reinf <reinf-column-horz-dep>`,
   :ref:`Added <added-column-horz-dep>`,
   :ref:`Persp <persp-column-horz-dep>`
