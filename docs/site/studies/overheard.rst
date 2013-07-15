.. index:: 
   single: directed/overhead speech; study of
   single: research; directed/overheard speech

.. _overheard-study:

*************************
Directed/Overheard Speech
*************************

*Properties of Directed and Overheard Speech at 14 months*


Investigators
=============

* Laura Shneidman (`email <mailto:lshneidman@gmail.com>`__)


Overview
========

This study investigated characteristics of speech overheard by children at
14 months and explored variability in the attentional behaviors of children
that might relate to their ability to learn from overheard speech.  Results
demonstrated that speech overheard by children differed from speech
directed to them in ways that may potentially make overheard speech a
difficult source of input to learn lexical items from.  Overheard speech
contained less reference to visually present objects, and was less likely
to follow in on children’s attentional focus than child-directed speech.
Results of this study also demonstrated that there exists variability in
children’s ability to attend to objects referenced in overheard speech, and
that this variability may be related to children’s experiences as
overhearers.  Children who received a higher percentage of their total
input in overheard speech were more able than their peers to independently
shift attention and attend to objects referenced in overheard speech.  This
manuscript is in prep.


Dataset
=======

A subset of 18 families from the program project 01 visit were used in this
study.   9 of these families were households that contained multiple adult
caregivers or siblings.  The children living in these households were
regularly exposed to overheard speech input.   The other 9 families lived
in households where the children spent most of their waking hours with a
single caregiver.  The target child living in these households was less
likely to receive overheard input.   The two groups of families were
matched with one another (as best possible) based on target child sex,
ethnicity, maternal education level and family income.

================   ================
Multi-speaker      Single Speaker
================   ================
108.01.LS.TXT      103.01.LS.TXT
28.01.LS.TXT	   106.01.LS.TXT
40.01.LS.TXT	   119.01.LS.TXT
61.01.LS.TXT	   33.01.LS.TXT
62.01.LS.TXT	   44.01.LS.TXT
68.01.LS.TXT	   45.01.LS.TXT
82.01.LS.TXT	   50.01.LS.TXT
87.01.LS.TXT	   51.01.LS.TXT
91.01.LS.TXT	   72.01.LS.TXT
================   ================


Dataset Enhancement
===================

We made a number of additions to the base transcripts that comprised our 
dataset.

First, all audible, intelligible utterances were added to the
transcript (these additions include speech directed to the child from
household members other than the primary caregiver as well as speech
overheard by the child).

Second, we added codes for the following five items.


1. Speaker/target
-----------------

All utterances were coded for who is speaking and whether the speech
is directed to the child or overheard by the child.  This information can
be found in the *key_2* column (column ``G``) of the transcript.  

*key_2* codes
+++++++++++++

**Overheard Speech**

:1: Primary caregiver is speaking to other
:2: Other child (under 13yrs) is speaking to other
:3: Other adult is speaking to other

**Directed Speech**

:4: Primary caregiver is speaking to child
:5: Other child is speaking to child
:6: Other adult is speaking to child


2. Objects
----------

All objects referenced in speech are coded for whether the object is present 
or absent.  This information is found in the *p_obj_pres* column.  If
two (or more) objects were referenced in a single utterance, that utterance
received two (or more) codes (e.g. PP)

*p_obj_pres* codes
++++++++++++++++++

:P: if object is present (from the speakers point of view )
:A: if object is absent (from the speakers point of view)
:U: if it is unclear if object is absent or present


3. Focus
--------

All utterances that contained a visually present object labeled
were coded for whether or not the speaker followed in on the child’s focus.

If two (or more) present objects were referenced in a single utterance,
that utterance received two (or more) codes separated by a period (e.g.
``y.n``) This information can be found in the *p_follow* column.  

*p_follow* codes
++++++++++++++++

:y: if parental utterance (AT ONSET) follows child’s attentional focus 
    (focus can be gaze, skilled touch, mouthing, or gesture).
    Example: Child is looking at bird, Parent says "that’s a bird"  
    (if child is looking at bird when parent starts to say "that’s ...")
:n: if parental utterance (at onset) does not follow child’s attentional 
    focus.  Example: Child is looking at bird, Parents says "Here's a truck"
:u: if unclear


4. Non-verbal cues
------------------

All utterances that contained a visually present object label were
coded for the kind of nonverbal cue the speaker gave to object name in
utterance.  This information can be found in the *nvc* column.  

*nvc* codes
+++++++++++

:e: eye-gaze only
:g: gesture (gestures include hold up gestures, pointing gestures and 
    give gestures)
:eg: eye gaze and gesture
:t: touch
:et: eye gaze and touch
:u: unclear


5. Attention
------------

Sixth, children’s attention to objects referenced in speech was coded for.
Attention was inferred by gaze, skilled touch, mouthing, or gesture.  This 
information is in the *c_attention* column.  

*c_attention* codes
+++++++++++++++++++

:y: if the child attends to referent before the start of the next speaker 
    utterance
:n: if the child fails to attend to referent before the start of speaker’s 
    next utterance or before 5 seconds
:u: if this in unclear
