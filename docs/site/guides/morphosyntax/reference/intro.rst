*****
Intro
*****


Overview
========

A subset of the LDP transcripts have received morphosyntactic coding --
an additional level of annotation that describes the morphosyntactic properties
and relations among the word tokens in an utterance.

These transcripts have a **mor** column (for both parent and child) 
containing morphological coding and a **syn** column containing syntactic 
coding for each utterace.  

The tables below provide a key to the part-of-speech tags and
grammatical-relation labels used in these two columns. 


A Simple Example
----------------

Here's an example of an annotated utterance::

    I         spilled       it       .              # utt
    pro|I     v|spill-PAST  pro|it   .              # mor
    1|2|SUBJ  2|0|ROOT      3|2|OBJ  4|2|PUNCT      # syn

The first line shows the utterance as it would be transcribed
in the **utt** column, the second line shows the morphology annotation that
would be contained in the corresponding **mor** column, and the third line
shows the syntactic annotation that would be contained in the correspoding
**syn** column.

We can represent the above example in a slightly different format, combining
the annotation of the two columns, with one word token per line::

    #  WORD     LEMMA   SUFFIX  POS  DEP  REL
    1  I        I               pro  2    SUBJ
    2  spilled  spill   PAST    v    0    ROOT
    3  it       it              pro  2    OBJ
    4  .        .               .    2    PUNCT

The morphology annotation indicates that the first word ("I") is tagged as 
a pronoun (``pro``) and the second word ("spilled") is tagged as a verb (``v``)
and contains a past-tense suffix (``PAST``).

The syntactic annotation indicates that the first word ("I") is dependent on
the second word ("spilled"), the verb of the utterance, and is playing the
role of grammatical subject in relation to the verb.

Note how it represents the grammatical dependency relations::

                 ┌── PUNCT ──┐
    I      spilled     it    .
    └─ SUBJ ─┘ └─ OBJ ──┘      


.. note::

    For more information about the various steps involved in adding 
    morphosyntactic coding see our `Morphosyntax Annotation Guide`_.

.. _Morphosyntax Annotation Guide: http://joyrexus.spc.uchicago.edu/ldp/docs/guides/morphosyntax/index.html
