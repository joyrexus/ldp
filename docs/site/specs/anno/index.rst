****************
Annotation Tiers
****************


Overview
========

Language Development Project transcripts consist of transcribed speech
supplemented with various tiers of annotation. These annotations capture a
range of phenomena associated with a given utterence (both within the utterance
and the context in which it occurred).

Annotation tiers do not necessarily get created simulataneously with the
speech transcription. A transcript may be supplemented with an additional 
"tier" of annotation at some later time.  

For this reason, we needed to create a simple mechanism for noting what annotations are present or absent in a particular transcript. The 
annotation tracking mechanism we've devised is indeed quite simple: it
consists of (1) this document, which names the various tiers of 
annotation currently recognized, and (2) an annotation worksheet associated 
with each transcript, indicating what annotation tiers are present or absent 
on that particular transcript (and for which speakers).

The table below indicates the annotation tiers currently recognized:

==========  ===================================================
Tier        Phenomena annotated
==========  ===================================================
Base_       Basic structural/contextual info
SR_         Gesture
GS_         Gesture-speech relationship
GX_         Additional gesture-speech relations 
MOR_        Morphology/part-of-speech
SYN_        Syntax
MAX_        Syntactic/semantic categories
==========  ===================================================

Each tier is described in more detail below. In particular, we note what
transcript columns are included in each tier. 

.. note:: 

    If the annotation worksheet in a transcript file indicates that 
    a particular tier is present, that implies that every column included 
    in the tier's definition is present -- i.e., has been coded -- in 
    that transcript.

See the :ref:`transcript column specification <ts>` for details on 
particular columns.


Base
====

The *Base* tier annotates the sequential/temporal order of utterances in a transcript as well as speaker/contextual information. The columns comprising this tier are speaker-independent and present on every transcript.  This annotation tier is created by the original transcriber in the course of transcription.

:Columns: time, line, key, context

.. note::

    Unlike the *Base* tier, all of the remaining annotation tiers are
    comprised of speaker-dependent columns. That means there are actually two
    columns indicated by each column name, one for the
    child speaker (indicated by a ``c_`` prefix) and one for the 
    parent speaker (indicated by a ``p_`` prefix). 
    
    For example, when we say the *GS* tier includes the *g_type* column, one
    should note that this refers to both a column annotating parent
    utterances (``p_g_type``) and a column annotating child utterances
    (``c_g_type``). 

    The annotation worksheet included with each transcript file allows one to
    specify which speakers (parent and/or child) have a particular annotation
    tier. (Yes, there are occassions when a child speaker may get annotated but
    not a parent.)
    

SR
==

The *SR* annotation tier captures basic gesture information.

:Columns: 
    form, lrb, obj, gloss, orient, mspd


GS
==

:Columns: 
    gs_rel, g_type


GX
==

:Columns: 
    time, time_gen, word, word_num, sem_role, pres_ref, reinf, added, persp


MOR
===

:Columns:
    chat, enum, mor


SYN
===

:Columns: syn


MAX
===

:Columns:
    clauses, np, pp, dpp, wpu, passives, syntype
