.. _gsrel-column:

3.23. GS_Rel - Gesture-Speech Relation
======================================

.. _gsrel-columni-description:

3.23.1. Description
-------------------

Specify the relationship between transcribed speech and gestures


.. _gsrel-column-format:

3.23.2. Format
--------------

.. productionlist::
   entry: `code-set` [`op` `code-set`]*
   code-set: `code` [`set-op` `code`]*
   code: `add` | `emphasize` | `reinforcing` | "DA" | "MS" | "UC" | "X"
   add: "ADD" [".err" [".s"] | ".f" | ".met" | ".nr" | ".ns" | ".q" | ".s"]
   emphasize: "E" [".b"]
   reinforcing: "RF" [".a" | ".p"]
   set-op: "/"
   op: ";"


.. _gsrel-column-values:

3.23.3. Values
--------------

GS_Rel codes have the following interpretations:

+---------------+-----------------+---------------------+---------------------+
| Code          | Meaning         | Description         | Example             |
+===============+=================+=====================+=====================+
| ``ADD``       | Adding          | Gesture adds info to| "Cookie" + [give    |
|               | information     | speech such that G+S| gesture]            |
|               |                 | = one proposition   |                     |
+---------------+-----------------+---------------------+---------------------+
| ``ADD.a``     |                 |                     |                     |
+---------------+-----------------+---------------------+---------------------+
| ``ADD.d``     |                 |                     |                     |
+---------------+-----------------+---------------------+---------------------+
| ``ADD.err``   | Matching error  | Gesture and speech  | "Cat" +[point to    |
|               |                 | refer to same object| dog]                |
|               |                 | but one incorrectly |                     |
|               |                 | labels it (occurs   |                     |
|               |                 | mainly in infants)  |                     |
+---------------+-----------------+---------------------+---------------------+
| ``ADD.err.s`` | Matching error  | Gesture and non-word| "Meow" + [point to  |
|               | at sound level  | sound refer to same | dog]                |
|               |                 | object but one      |                     |
|               |                 | incorrectly labels  |                     |
|               |                 | it (occurs in       |                     |
|               |                 | infants)            |                     |
+---------------+-----------------+---------------------+---------------------+
| ``ADD.f``     | Adding info to  | Adding info to a    | "OK" + [give        |
|               | a filler        | filler expression   | gesture]            |
|               | expression      |                     |                     |
+---------------+-----------------+---------------------+---------------------+
| ``ADD.met``   | Adding          | Speech adds meaning |                     |
|               | metaphoric      | to ``metaphoric``   |                     |
|               |                 | gesture             |                     |
+---------------+-----------------+---------------------+---------------------+
| ``ADD.nr``    | Adding info to  | Gestures adds a new | "Put the book on the|
|               | unrelated       | proposition or      | table" + [hold up   |
|               | utterance       | speech and gesture  | shoe]               |
|               |                 | convey unrelated    |                     |
|               |                 | information such    |                     |
|               |                 | that G+S = two      |                     |
|               |                 | propositions        |                     |
+---------------+-----------------+---------------------+---------------------+
| ``ADD.ns``    | Adding info to  | Speech adds         | "Uh-oh" + [point to |
|               | unrelated sound | unrelated meaningful| cat]                |
|               |                 | sound               |                     |
+---------------+-----------------+---------------------+---------------------+
| ``ADD.q``     | Adds info       | Gesture provides    | "Where is the bird?"|
|               | answering a     | information (such as| + [point to tree]   |
|               | spoken question | location or yes/no  |                     |
|               |                 | info) that answers  | "Is this the one?"  |
|               |                 | the question posed  | + [head shake]      |
|               |                 | in speech           |                     |
+---------------+-----------------+---------------------+---------------------+
| ``ADD.s``     | Adding info to  | Speech adds related | "Meow" + [point to  |
|               | a related sound | meaningful sound    | cat]                |
+---------------+-----------------+---------------------+---------------------+
| ``DA``        | Disambiguation  | Gesture             | "Put it there" +    |
|               |                 | disambiguates speech| [point to table]    |
+---------------+-----------------+---------------------+---------------------+
| ``E``         | Emphasizes w/o  | Gestures that act   | "Hard to decide" +  |
|               | ``beat``        | like discourse      | [head shake]        |
|               |                 | markers by          |                     |
|               |                 | emphasizing what is |                     |
|               |                 | said                |                     |
+---------------+-----------------+---------------------+---------------------+
| ``E.b``       | Emphasizes      | Hand, arm, or head  | "What I'm SAYING is"|
|               | with ``beat``   | movements where the | + [hand beat on     |
|               |                 | gesture stroke      | "saying"]           |
|               |                 | syncronizes with    |                     |
|               |                 | emphasis in speech  |                     |
+---------------+-----------------+---------------------+---------------------+
| ``ELAB.a`` *  |                 |                     |                     |
+---------------+-----------------+---------------------+---------------------+
| ``ELAB.b`` *  |                 |                     |                     |
+---------------+-----------------+---------------------+---------------------+
| ``FA``        |                 |                     |                     |
+---------------+-----------------+---------------------+---------------------+
| ``MS`` *      | Adds to a       | Gesture is          | "Da!" + [hold up toy|
|               | meaningless     | accompanied by a    | truck]              |
|               | sound           | meaningless sound   |                     |
|               |                 | (almost only occurs |                     |
|               |                 | in infants)         |                     |
+---------------+-----------------+---------------------+---------------------+
| ``RF``        | Reinforcing     | Gesture reinforces  | "Cat" + [point to   |
|               |                 | the info provided   | cat]                |
|               |                 | in speech           |                     |
+---------------+-----------------+---------------------+---------------------+
| ``RF.a``      | Reinforcing     | Gesture reinfoces   | "Here is a blue one"|
|               | attribute       | an adjective in     | + [point to blue    |
|               |                 | speech describing   | block]              |
|               |                 | perceptual features |                     |
+---------------+-----------------+---------------------+---------------------+
| ``RF.d``      |                 |                     |                     |
+---------------+-----------------+---------------------+---------------------+
| ``RF.met``    |                 |                     |                     |
+---------------+-----------------+---------------------+---------------------+
| ``RF.p``      | Reinforcing     | Gesture reinforces  | "Crying" + [point to|
|               | predicate       | the spoken predicate| crying baby in book]|
|               |                 | describing an action|                     |
|               |                 | the referenced      |                     |
|               |                 | object performs     |                     |
+---------------+-----------------+---------------------+---------------------+
| ``UC``        | Unclear         | The gloss for the   | "I want ###" +      |
|               | relationship    | gesture does not    | [point to toy]      |
|               |                 | provide enough info |                     |
|               |                 | or the speech is    |                     |
|               |                 | indecipherable      |                     |
+---------------+-----------------+---------------------+---------------------+
| ``X``         | No speech       | Gesture is produced | [point to desired   |
|               |                 | on its own          | object]             |
+---------------+-----------------+---------------------+---------------------+

.. warning::
   Codes marked with \* are considered deprecated in Erica's Second Tier
   Gesture Annotation


Ops have the following interpretations:

=====  ==============================================================
 Op    Meaning
=====  ==============================================================
``;``  Separates all ``code``\ s
``/``  Used to combine representational ``code``\ s into single units
=====  ==============================================================


.. _gsrel-column-vert-dep:

3.23.4. Vertical Dependencies
-----------------------------

None


.. _gsrel-column-horz-dep:

3.23.5. Horizontal Dependencies
-------------------------------

GS_Rel is dependent on the :ref:`G_Type Column <gtype-column-dep-by>`, the
:ref:`Form Column <form-column-dep-by>`, and the 
:ref:`Enum Column <enum-column-dep-by>`.

+---------------+-------------------------------------------------------------+
| GS_Rel        | G_Type, Form, and Enum Conditions                           |
+===============+=============================================================+
| ``ADD``       | ``C``, ``DP``, ``DP.nl``, ``DS``, ``DSDP``, ``G``, or ``S`` |
|               | in G_Type                                                   |
+---------------+-------------------------------------------------------------+
| ``ADD.a``     | ``R.a``, ``R.a.e``, or ``R.a.pp`` in G_Type                 |
+---------------+-------------------------------------------------------------+
| ``ADD.d``     | ``R.d``, ``R.d.e``, or ``R.d.pp`` in G_Type                 |
+---------------+-------------------------------------------------------------+
| ``ADD.err``   | ``DP``, ``DP.nl``, ``DS``, ``DSDP``, or ``G`` in G_Type     |
+---------------+-------------------------------------------------------------+
| ``ADD.err.s`` | ``DP``, ``DP.nl``, ``DS``, or ``DSDP`` in G_Type            |
+---------------+-------------------------------------------------------------+
| ``ADD.f``     | ``C``, ``DP``, ``DP.nl``, ``DS``, ``DSDP``, or ``G`` in     |
|               | G_Type                                                      |
+---------------+-------------------------------------------------------------+
| ``ADD.met``   | ``R.met`` in G_Type                                         |
+---------------+-------------------------------------------------------------+
| ``ADD.nr``    | ``C``, ``DP``, ``DP.nl``, ``DS``, ``DSDP``, or ``G`` in     |
|               | G_Type                                                      |
+---------------+-------------------------------------------------------------+
| ``ADD.ns``    | ``DP``, ``DP.nl``, ``DS``, or ``DSDP`` in G_Type            |
+---------------+-------------------------------------------------------------+
| ``ADD.q``     | ``R.m``, ``R.m.e``, or ``R.m.pp`` in G_Type                 |
+---------------+-------------------------------------------------------------+
| ``ADD.s``     | ``DP``, ``DP.nl``, ``DS``, or ``DSDP`` in G_Type            |
+---------------+-------------------------------------------------------------+
| ``DA``        | ``DP``, ``DP.nl``, ``DS``, or ``DSDP`` in G_Type            |
+---------------+-------------------------------------------------------------+
| ``E``         | ``C`` in G_Type and ``shake`` or ``nod`` in Form            |
+---------------+-------------------------------------------------------------+
| ``E.b``       | ``E`` in G_Type                                             |
+---------------+-------------------------------------------------------------+
| ``ELAB.a``    | ``R.a``, ``R.a.e``, or ``R.a.pp`` in G_Type                 |
+---------------+-------------------------------------------------------------+
| ``ELAB.b``    | ``R.m``, ``R.m.e``, or ``R.m.pp`` in G_Type                 |
+---------------+-------------------------------------------------------------+
| ``FA``        | ``FA`` in G_Type                                            |
+---------------+-------------------------------------------------------------+
| ``MS``        | ``DP``, ``DP.nl``, ``DS``, ``DSDP``, ``G``, ``FA``, or      |
|               | ``S`` in G_Type                                             |
+---------------+-------------------------------------------------------------+
| ``RF``        | ``C``, ``DP``, ``DP.nl``, ``DS``, ``DSDP``, ``G``, or ``S`` |
|               | in G_Type                                                   |
+---------------+-------------------------------------------------------------+
| ``RF.a``      | ``DP``, ``DP.nl``, ``DS``, ``DSDP``, ``R.a``, ``R.a.e``,    |
|               | or ``R.a.pp`` in G_Type                                     |
+---------------+-------------------------------------------------------------+
| ``RF.d``      | ``R.d``, ``R.d.e``, or ``R.d.pp`` in G_Type                 |
+---------------+-------------------------------------------------------------+
| ``RF.met``    | ``R.met`` in G_Type                                         |
+---------------+-------------------------------------------------------------+
| ``RF.p``      | ``DP``, ``DP.nl``, ``DS``, ``DSDP``, ``R.m``, ``R.m.e``,    |
|               | or ``R.m.pp`` in G_Type                                     |
+---------------+-------------------------------------------------------------+
| ``UC``        | Can be used with any Form code if appropriate               |
+---------------+-------------------------------------------------------------+
| ``X``         | Can be used with any Form code if there is no utterance     |
|               | enumeration in Enum                                         |
+---------------+-------------------------------------------------------------+


.. _gsrel-column-dep-by:

3.23.6. Depended Upon By
------------------------

In :ref:`seyda-level`:
   None

In :ref:`erica-level`:
   :ref:`Word <word-column-horz-dep>`
