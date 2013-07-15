.. _semrole-column:

3.28. Sem_Role - Semantic Role
==============================


.. _semrole-column-description:

3.28.1. Description
-------------------

Detemines what types of semantic roles are supported by gesture or conveyed
solely in gesture


.. _semrole-column-format:

3.28.2. Format
--------------

.. productionlist::
   entry: `code_set` [`op` `code_set`]*
   code_set: `code_list` [`set_op` `code_list`]*
   code_list: `null` | `code` | `entity_code` [`entity_op` `entity_code`]*
   null: "X"
   code: "TA" | "IA" | "PO" | "EX" | "PA" | "TH" | "EN" | "AE" | "IE" | "AS" | "IS" | "PT" | "SC" | "AC" | "IN" | "AA" | "BE" | "TI" | "LO" | "UC"
   entity_code: "EO" | "EP" | "ED" | "EL" 
   entity_op: ","
   set_op: "/"
   op: ";"


.. _semrole-column-values:

3.28.3. Values
--------------

CODE must be drawn from the following:

+--------+--------------------+----------------------------------------------+
| Code   | Meaning            | Description                                  |
+========+====================+==============================================+
| ``TA`` | Transitive Agent   | The actor purposefully performs an action    |
|        |                    | to or on another entity.                     |
+--------+--------------------+----------------------------------------------+
| ``IA`` | Inransitive Agent  | The actor purposefully performs an action    |
|        |                    | that does not have a patient or theme.       |
+--------+--------------------+----------------------------------------------+
| ``PO`` | Possessor          | An entity characterized in a sentence by     |
|        |                    | having, owning, or holding an object.        |
+--------+--------------------+----------------------------------------------+
| ``EX`` | Experiencer        | The person or entity that experiences a      |
|        |                    | state or event but does not initiate or      |
|        |                    | affect it.                                   |
+--------+--------------------+----------------------------------------------+
| ``PA`` | Patient            | The recipient of a transformative action     |
|        |                    | performed by the AGENT.  The action leaves   |
|        |                    | the patient changed in form or kind.         |
+--------+--------------------+----------------------------------------------+
| ``TH`` | Theme              | The entity moving in a locative action.      |
|        |                    | The action leaves the theme changed in       |
|        |                    | space or time.                               |
+--------+--------------------+----------------------------------------------+
| ``EL`` | Locative Entity    | An object or entity that is described as     |
|        |                    | being in a particular place                  |
+--------+--------------------+----------------------------------------------+
| ``EO`` | Owned Entity       | An object or entity that is described as     |
|        |                    | belonging to or being in the possession of   |
|        |                    | a person, animal, or character.  Entities    |
|        |                    | described as belonging to non-animate        |
|        |                    | objects are described entities.              |
+--------+--------------------+----------------------------------------------+
| ``EP`` | Perceived Entity   | An object or entity that is described as     |
|        |                    | being perceived through a sense or emotion   |
|        |                    | (usually paired with an experiencer)         |
+--------+--------------------+----------------------------------------------+
| ``ED`` | Described Entity   | An object or entity that is described as     |
|        |                    | having a particular characteristic or use    |
+--------+--------------------+----------------------------------------------+
| ``EN`` | Named Entity       | An object or entity that is labeled with     |
|        |                    | no futher description                        |
+--------+--------------------+----------------------------------------------+
| ``AE`` | Animate Endpoint   | The person/animal at which a translocational |
|        |                    | action ends                                  |
+--------+--------------------+----------------------------------------------+
| ``IE`` | Inanimate Endpoint | The place at which a translocational action  |
|        |                    | ends                                         |
+--------+--------------------+----------------------------------------------+
| ``AS`` | Animate Source     | The persona/animal from whence a             |
|        |                    | translocational action originates or the     |
|        |                    | origin of an entity                          |
+--------+--------------------+----------------------------------------------+
| ``IS`` | Inanimate Source   | The place from when a translocational action |
|        |                    | originates or the origin of an entity        |
+--------+--------------------+----------------------------------------------+
| ``PT`` | Path               | The relative location where an action takes  |
|        |                    | place or through which an object moves       |
+--------+--------------------+----------------------------------------------+
| ``SC`` | Static Comparative | The second argument in comparisons of static |
|        |                    | traits between entities                      |
+--------+--------------------+----------------------------------------------+
| ``AC`` | Active Comparative | The second argument in comparisons of action |
|        |                    | traits between entities                      |
+--------+--------------------+----------------------------------------------+
| ``IN`` | Instrument         | A tool used to perform an action.  It can    |
|        |                    | take the place of an agent, but is still     |
|        |                    | referred to as an instrument if it is        |
|        |                    | incapable of performing the action without   |
|        |                    | an agent.                                    |
+--------+--------------------+----------------------------------------------+
| ``AA`` | Accompanying Actor | A person or entity that performs the action  |
|        |                    | along with the agent                         |
+--------+--------------------+----------------------------------------------+
| ``BE`` | Beneficiary        | A person or animate character who benefits   |
|        |                    | as the restul of the action.  Purposes (e.g. |
|        |                    | this is for dinner) are not coded.           |
+--------+--------------------+----------------------------------------------+
| ``TI`` | Time               | The time at which an action/event occurs     |
+--------+--------------------+----------------------------------------------+
| ``LO`` | Location           | The location where an action/event occurs    |
+--------+--------------------+----------------------------------------------+
| ``UC`` | Unclear            | The role of the gesture is unclear           |
+--------+--------------------+----------------------------------------------+
| ``X``  | Doesn't Exist/Null | The gestures refers to a part of speech that |
|        |                    | cannot take a semantic role (e.g. a verb).   |
+--------+--------------------+----------------------------------------------+


Ops are drawn from the following set of operators:

======  ==============================================================
``op``  Meaning
======  ==============================================================
``;``   Separates all ``code``\ s
``/``   Used to combine representational ``code``\ s into single units
``,``   Used to create a list of ``value``\ s
======  ==============================================================


.. _semrole-column-vert-dep:

3.28.4. Vertical Dependencies
-----------------------------

None


.. _semrole-column-horz-dep:

3.28.5. Horizontal Dependencies
-------------------------------

Sem_Role is dependent on the :ref:`G_Type Column <gtype-column-dep-by>`.

If the corresponding G_Type code is ``C``, ``FA``, or ``G``, the Sem_Role code
must be ``X``.  Otherwise, anything that is appropriate for the current 
utterance is allowed.


.. _semrole-column-dep-by:

3.28.6. Depended Upon By
------------------------

None
