.. _key-column:

3.3. Key - Coded Environmental Context
======================================


.. _key-column-description:

3.3.1. Description
------------------

List a concise set of environmental conditions


.. _key-column-format:

3.3.2. Format
-------------

.. productionlist::
   entry: [`code`]*
   code: <Keys can be productively generated.  See table below for details>

.. _key-column-values:

3.3.3. Values
-------------

As a result of collective experience gained from several years of transcribing,
the values of the :ref:`Key <key-column>` vary slightly depending on the type
of the visit being transcribed and the transcription guidelines being used.
The most current set of key values are as follows:

+-------------+-------------------------------+-------------------------------+
| Value       | Meaning                       | Example                       |
+=============+===============================+===============================+
| ``*[1-9]*`` | Sibling directed speech       | Mother or child speaks to the |
|             |                               | child's one other sibling:    |
|             |                               | ``M*`` or ``*``               |
|             |                               |                               |
|             |                               | Mother or child speaks to the |
|             |                               | sibling identified as SIB1 in |
|             |                               | the cast: ``M*1`` or ``*1``   |
|             |                               |                               |
|             |                               | Mother or child speaks to     |
|             |                               | siblings SIB1 and SIB2 as     |
|             |                               | identified in the cast:       |
|             |                               | ``M*12`` or ``*12``           |
+-------------+-------------------------------+-------------------------------+
| ``a``       | Child responds to normally    | Mother is talking on the phone|
|             | untranscribed speech          | and child responds directly to|
|             |                               | something mother says to the  |
|             |                               | person on the phone           |
+-------------+-------------------------------+-------------------------------+
| ``d``       | Child talking to pet          | Child says "Tuvok, come!"     |
|             |                               | where Tuvok is the family dog |
+-------------+-------------------------------+-------------------------------+
| ``e``       | Child talking to experimenter | Child says "Tuvok, run!" where|
|             |                               | Tuvok is the experimenter     |
+-------------+-------------------------------+-------------------------------+
| ``F``       | Father speech if father is    | Father says anything and is a |
|             | also a PCG                    | PCG.  This can also be used as|
|             |                               | a suffix for all other keys   |
|             |                               | unless otherwise stated.      |
+-------------+-------------------------------+-------------------------------+
| ``f``       | Child or mother talking to    | Child or mother says "Dad,    |
|             | father                        | run!".  Cannot be prefixed    |
|             |                               | with ``F``.                   |
+-------------+-------------------------------+-------------------------------+
| ``i``       | PCG talking to self           | Mother says "Note to self..." |
+-------------+-------------------------------+-------------------------------+
| ``l``       | Non-English words used in     | Child says "I was watching    |
|             | an otherwise English sentence | Tuvok when el encantador did  |
|             |                               | some magic."                  |
+-------------+-------------------------------+-------------------------------+
| ``M``       | Mother speech                 | Mother says anything and is a |
|             |                               | PCG.  This can also be used as|
|             |                               | a suffix for all other keys   |
|             |                               | unless otherwise stated.      |
|             |                               |                               |
|             |                               | Literacy transcripts only     |
+-------------+-------------------------------+-------------------------------+
| ``m``       | Child speaking to mother      | Child says "Mom, run!". Cannot|
|             |                               | be prefixed with ``M``.       |
+-------------+-------------------------------+-------------------------------+
| ``o``       | PCG talking to other adult    | Mother is talking to aunt     |
+-------------+-------------------------------+-------------------------------+
| ``p``       | Spontaneous praying           | Child or PCG starts saying a  |
|             |                               | non-canonical prayer ("Bless  |
|             |                               | Mom and Dad and help Tuvok get|
|             |                               | home", not "Our Father, who   |
|             |                               | art in heaven...")            |
+-------------+-------------------------------+-------------------------------+
| ``r``       | Reading                       | Child or PCG is reading "Hop  |
|             |                               | on Pop"                       |
+-------------+-------------------------------+-------------------------------+
| ``t``       | Child talking on phone        | Child is talking on real or   |
|             |                               | toy phone                     |
+-------------+-------------------------------+-------------------------------+
| ``v``       | Spontaneous singing           | Child or PCG starts singing   |
|             |                               | non-canonical song ("Work, you|
|             |                               | old goat" over and over, not  |
|             |                               | "Row, row, row your boat")    |
+-------------+-------------------------------+-------------------------------+
| ``x``       | Non-transcribed speech        | Aunt says something to mother |
|             | overheard in the preceding    | at some point in the preceding|
|             | five minutes                  | five minutes                  |
+-------------+-------------------------------+-------------------------------+
| ``xc``      | Non-PCG speech directed       | Aunt says something to child  |
|             | toward child in the preceding | at some point in the preceding|
|             | five minutes                  | five minutes                  |
+-------------+-------------------------------+-------------------------------+

.. note::

   You will likely see two other key values that have since been deprecated.
   The first is ``@``, which was the original code for ``F``.  Both have
   identical interpretations and usage.

   The other is ``b``, which was meant to indicate when both parent and child
   speech began simultaneously.  To simplify programmatic analysis and
   validation of transcripts and because of the highly subjective nature of the
   conditions in which the key was appropriate, ``b`` was removed as of 
   revision 1.4 of the transcription guidelines.  With ``b`` gone, utterances
   that could be construed as simultaneous are given in the following canonical
   order: child, mother, father, experimenter.  Each speaker involved is then
   afforded one line of the transcript.


.. _key-column-vert-dep:

3.3.4. Vertical Dependencies
----------------------------

None


.. _key-column-horz-dep:

3.3.5. Horizontal Dependencies
------------------------------

None


.. _key-column-dep-by:

3.3.6. Depended Upon By
-----------------------

In :ref:`base-level`:
   :ref:`Utts <utts-column-horz-dep>`

In :ref:`seyda-level`:
   :ref:`Utts <utts-column-horz-dep>`

In :ref:`erica-level`:
   :ref:`Utts <utts-column-horz-dep>`
