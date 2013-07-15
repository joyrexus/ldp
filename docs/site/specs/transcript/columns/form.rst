.. _form-column:

3.16. Form - Gesture Name
=========================

.. _form-column-description:

3.16.1. Description
-------------------

Indicates the category and name of the gesture being coded

.. _form-column-format:

3.16.2. Format
--------------

.. productionlist::
   entry: `offcamera` | `code` [`op` `code`]*
   offcamera: "$"
   code: <Any `code` from the table below other than `offcamera`>[`continued`]
   continued: "~"
   op: "+" | "-" | "/" | "."


.. _form-column-values:

3.16.3. Values
--------------

Codes have the following interpretation:

+-----------------------+--------------------------+-----------------------+
| Form Code             | Description              | Example               |
+=======================+==========================+=======================+
| **Off Camera**                                                           |
+-----------------------+--------------------------+-----------------------+
| ``$``                 | Gesture occurred off     |                       |
|                       | camera and is            |                       |
|                       | indeterminate            |                       |
+-----------------------+--------------------------+-----------------------+
| **Deictics**                                                             |
+-----------------------+--------------------------+-----------------------+
| ``point``             | One or more fingers      |                       |
|                       | are extended to          |                       |
|                       | indicate an object or    |                       |
|                       | set of objects           |                       |
+-----------------------+--------------------------+-----------------------+
| ``cont point``        | One or more fingers      |                       |
|                       | are used to indicate     |                       |
|                       | multiple members of a    |                       |
|                       | set or group of objects  |                       |
+-----------------------+--------------------------+-----------------------+
| ``drag``              | A point with a trace     | Deprecated            |
|                       | along a present object   |                       |
+-----------------------+--------------------------+-----------------------+
| ``palm``              | Entire palm used to      |                       |
|                       | identify or indicate     |                       |
|                       | an entity or set of      |                       |
|                       | objects                  |                       |
+-----------------------+--------------------------+-----------------------+
| ``cont palm``         | Entire palm used to      |                       |
|                       | indicate multiple        |                       |
|                       | members of a set or      |                       |
|                       | group of objects         |                       |
+-----------------------+--------------------------+-----------------------+
| ``hold``              | Holding an object in     |                       | 
|                       | to explicitly indicate   |                       | 
|                       | or draw attention to     |                       | 
|                       | it, can also hold a      |                       | 
|                       | body part by raising it  |                       |
+-----------------------+--------------------------+-----------------------+
| **Conventionals**                                                        |
+-----------------------+--------------------------+-----------------------+
| ``beat``              | Any sharp motion         |                       |
|                       | corresponding with the   |                       |
|                       | prosody of speech        |                       |
+-----------------------+--------------------------+-----------------------+
| ``come``              | Beckoning to another     | Holding out palms of  |
|                       | entity                   | hands toward the      |
|                       |                          | entity being beckoned |
|                       |                          |                       |
|                       |                          | Extending one or more |
|                       |                          | fingers and bending   |
|                       |                          | fingers back toward   |
|                       |                          | palm with palm up     |
+-----------------------+--------------------------+-----------------------+
| ``dismiss``           | Brushed hand(s) away     |                       |
|                       | from body (can look      |                       |
|                       | very similar to a flip   |                       |
|                       | but accompanies a        |                       |
|                       | different context        |                       |
|                       | established by speech    |                       |
+-----------------------+--------------------------+-----------------------+
| ``flip``              | Turning up palm(s) of    |                       |
|                       | hand(s) by rotating      |                       |
|                       | wrist or arm             |                       |
+-----------------------+--------------------------+-----------------------+
| ``got it``            | Both hands spread in     |                       |
|                       | front of body with       |                       |
|                       | palms facing down or     |                       |
|                       | inwards and pressing     |                       |
|                       | down once or repeatedly  |                       |
+-----------------------+--------------------------+-----------------------+
| ``listing``           | Fingers move through a   |                       |
|                       | sequence of numbers      |                       |
|                       | while verbally listing   |                       |
|                       | items                    |                       |
+-----------------------+--------------------------+-----------------------+
| ``naughties``         | Shaking or waving the    |                       |
|                       | index finger             |                       |
+-----------------------+--------------------------+-----------------------+
| ``nod``               | Moving the head up and   |                       |
|                       | down by bending the      |                       |
|                       | neck                     |                       |
+-----------------------+--------------------------+-----------------------+
| ``number``            | Indicates a number       |                       |
|                       | being referenced by      |                       |
|                       | holding up the           |                       |
|                       | corresponding number     |                       |
|                       | of fingers               |                       |
+-----------------------+--------------------------+-----------------------+
| ``oh my``             | Raising one or both      |                       |
|                       | hands to the mouth       |                       |
+-----------------------+--------------------------+-----------------------+
| ``pick me``           | Hand raised above head,  |                       |
|                       | optionally waving        |                       |
+-----------------------+--------------------------+-----------------------+
| ``pick up``           | Holding limb(s),         |                       |
|                       | usually the arm(s),      |                       |
|                       | outstretched toward an   |                       |
|                       | adult to indicate the    |                       |
|                       | desire to be picked up   |                       |
+-----------------------+--------------------------+-----------------------+
| ``shake``             | Turning head left and    |                       |
|                       | right                    |                       |
+-----------------------+--------------------------+-----------------------+
| ``shh``               | Hold index finger        |                       |
|                       | vertically against lips  |                       |
+-----------------------+--------------------------+-----------------------+
| ``shrug``             | Raising one or both      |                       |
|                       | shoulders up towards     |                       |
|                       | the head                 |                       |
+-----------------------+--------------------------+-----------------------+
| ``shrug with flip``   | Simultaneous flip and    |                       |
|                       | shrug                    |                       |
+-----------------------+--------------------------+-----------------------+
| ``sweep``             | Holding arm(s) and       |                       |
|                       | hand(s) parallel to the  |                       |
|                       | ground with palms down   |                       |
|                       | and moving from center   |                       |
|                       | of body to respective    |                       |
|                       | side(s) of body          |                       |
+-----------------------+--------------------------+-----------------------+
| ``tada``              | Opening of arms and      |                       |
|                       | hands up and/or out      |                       |
+-----------------------+--------------------------+-----------------------+
| ``thinking``          | Putting a finger to the  |                       |
|                       | head or face and         |                       |
|                       | holding it there or      |                       |
|                       | tapping it in place      |                       |
+-----------------------+--------------------------+-----------------------+
| ``wait``              | Index finger pointing    | Traditional "one      |
|                       | up, other fingertips     | moment" gesture       |
|                       | curled under, palm out   |                       |
+-----------------------+--------------------------+-----------------------+
| ``wave``              | Moves hand side to side  | A traditional greeting|
|                       | with palm out or moves   | wave                  |
|                       | hand up and down         |                       |
+-----------------------+--------------------------+-----------------------+
| ``<aha>``             | Raising hand with index  |                       |
|                       | finger pointed up        |                       |
+-----------------------+--------------------------+-----------------------+
| ``<back off>``        | Holds hand(s) out with   | The quintisential     |
|                       | palm out                 | "STOP!" gesture       |
+-----------------------+--------------------------+-----------------------+
| ``<darn it>``         | Holds hand in fist with  |                       |
|                       | are bent at elbow and    |                       |
|                       | pulls arm toward center  |                       |
|                       | of body                  |                       |
+-----------------------+--------------------------+-----------------------+
| ``<hero fist>``       | Raising arm(s) up with   |                       |
|                       | hand(s) in fist(s)       |                       |
+-----------------------+--------------------------+-----------------------+
| ``<listening>``       | Cupping hand(s) to       |                       |
|                       | ear(s)                   |                       |
+-----------------------+--------------------------+-----------------------+
| ``<oh man>``          | Holding hand(s) to head  |                       |
+-----------------------+--------------------------+-----------------------+
| ``<pray you>``        | Holding palms together   |                       |
|                       | in a prayer position     |                       |
+-----------------------+--------------------------+-----------------------+
| ``<thumbs up>``       | Raising one or both      |                       |
|                       | thumbs up from the rest  |                       |
|                       | of the fingers in a      |                       |
|                       | fist                     |                       |
+-----------------------+--------------------------+-----------------------+
| ``<score>``           | Holding hand in fist     |                       |
|                       | with arm bent at elbow   |                       |
|                       | and pulling it toward    |                       |
|                       | body                     |                       |
+-----------------------+--------------------------+-----------------------+
| ``<so so>``           | Holding hand out with    |                       |
|                       | palm down and            |                       |
|                       | alternately tilting      |                       |
|                       | hand from side to side   |                       |
+-----------------------+--------------------------+-----------------------+
| ``<whew>``            | Wiping brow with the     |                       |
|                       | palm or back of hand(s)  |                       |
+-----------------------+--------------------------+-----------------------+
| ``x``                 | Ambigous gestures that   |                       |
|                       | do not fall into these   |                       |
|                       | categories or for which  |                       |
|                       | an accurate meaning      |                       |
|                       | cannot be described      |                       |
+-----------------------+--------------------------+-----------------------+
| **Representationals**                                                    |
+-----------------------+--------------------------+-----------------------+
| ``iconic``            | A gesture which          | Action: flapping arms | 
|                       | represents a thing or    | in the air to convey  |
|                       | idea                     | 'flying'              |
|                       |                          |                       |
|                       |                          | Direction: moving the |
|                       |                          | index finger downward |
|                       |                          | to indicate 'downward |
|                       |                          | path'                 |
|                       |                          |                       |
|                       |                          | Attribute: holding    |
|                       |                          | cupped hands in the   |
|                       |                          | air to convey the size|
|                       |                          | or shape of a ball    |
|                       |                          |                       |
|                       |                          | Shape: tracing the    |
|                       |                          | shape of a square with|
|                       |                          | fingers on a drawing  |
|                       |                          | or in the air         |
+-----------------------+--------------------------+-----------------------+
| ``metaphoric``        | A gesture which          | Cupping hands in air  |
|                       | represents a conceptual  | as if holding an idea |
|                       | relationship without     | for the purpose of    |
|                       | directly mapping to a    | referencing an idea or|
|                       | tangible property of     | concept of an idea    |
|                       | the relationship or      |                       |
|                       | entity befing            |                       |
|                       | referenced               |                       |
+-----------------------+--------------------------+-----------------------+
| ``demo``              | A gesture which          | Holding a spoon and   |
|                       | represents a procedure   | moving in a stirring  |
|                       | using at least one       | motion in the air     |
|                       | object involved in that  | without actually      |
|                       | procedure without        | stirring anything to  |
|                       | actually completing or   | show how to stir      |
|                       | carrying out the action  |                       |
+-----------------------+--------------------------+-----------------------+
| **Sign**                                                                 |
+-----------------------+--------------------------+-----------------------+
| ``sign``              | Baby sign or ASL sign    |                       |
+-----------------------+--------------------------+-----------------------+

.. note::
   Any code except ``$`` may be suffixed with a tilde (``~``) to indicate
   continuation from the speaker's immediately preceding communicative act in
   the transcript.


Ops have the following interpretations:

=====  ================================================================
Op     Meaning
=====  ================================================================
``+``  Simultaneous gestures
``-``  Sequential gestures without return to neutral position
``/``  Gestures morph into one another
``.``  Sequential gestures with return to neutral position - DEPRECATED
=====  ================================================================


.. _form-column-vert-dep:

3.16.4. Vertical Dependencies
-----------------------------

If a Form code is suffixed with the continuation operator (``~``), it must have
an antecedent that is either the base form or the continued form of the code in
the immediately preceding transcribed communicative act for the given speaker.
I.e., if the child says something and uses a point, the parent talks for 30
lines in the transcript, and then the child, still holding the point, says
something else, the second point could be continued from the first because
there is no intervening utterance or gesture on the part of the child.


.. _form-column-horz-dep:

3.16.5. Horizontal Dependencies
-------------------------------

    None


.. _form-column-dep-by:

3.16.6. Depended Upon By
------------------------

In :ref:`base-level`:
   :ref:`LRB <lrb-column-horz-dep>`,
   :ref:`Obj <obj-column-horz-dep>`,
   :ref:`Gloss <gloss-column-horz-dep>`,
   :ref:`Orient <orient-column-horz-dep>`,
   :ref:`MSPD <mspd-column-horz-dep>`

In :ref:`seyda-level`:
   :ref:`G_Type <gtype-column-horz-dep>`,
   :ref:`GS_Rel <gsrel-column-horz-dep>`

In :ref:`erica-level`:
   :ref:`G_Type <gtype-column-horz-dep>`,
   :ref:`GS_Rel <gsrel-column-horz-dep>`,
   :ref:`Time (Gesture) <time-g-column-horz-dep>`
