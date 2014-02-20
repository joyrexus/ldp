README
******

Generate the following three tables for Steve Raudenbush to analyze feasability
of imputing missing data of the sort we find in our brain-injured (**BI**) subject sample.

He plans to use the typically-developing (**TD**) subject sample to assess
this, but will need the *pattern* of missing data from the **BI** sample to do
so.


TD Tables
=========

We're providing Steve with the following tables for the typically developing
sample.

(Note that he'd like to restrict the sample to the 40 subjects with the least amount of missing data.  Identify the most promising 40 candidates and filter out the others.)

Person-Period Format
--------------------

:SUBJ: subject ID
:SEX: subject gender
:EDU: parent education level
:INC: parent income level
:RACE: subject race
:ETHN: subject ethnicity
:SESS: session ID (i.e., timepoint, visit)
:AGE: subject age (in months)
:PWT: parent word types (at session)
:CWT: child word types (at session)

Person-Level Format
-------------------

:SUBJ: subject ID
:SEX: subject gender
:EDU: parent education level
:INC: parent income level
:RACE: subject race
:ETHN: subject ethnicity
:VOCB1: vocabulary measure (PPVT) at session 5
:VOCB2: vocabulary measure (PPVT) at session 8
:VOCB3: vocabulary measure (PPVT) at session 11
:VOCB4: vocabulary measure (PPVT) at session 27
:READ1: reading measure (WJ Word ID Score) at session 22
:READ2: reading measure (WJ Word ID Score) at session 25
:READ3: reading measure (GM Score) at session 22
:READ4: reading measure (GM Score) at session 25


BI Table
========

:SUBJ: subject ID
:SESS: session ID (i.e., timepoint, visit, 1 to 27)
:RECR: recruit status indicator (1 if recruited, 0 otherwise)
:STAT: visit indicator (1 if visit occurred, 0 otherwise)
:PROJ: projected visit indicator (1 if projected, 0 otherwise)

Regarding the **RECR** variable, Kristi informs us that there will be "10 kids who we will recruit to make up the *refreshed sample*.  These 10 subjects were given IDs of 200 through 209.

Regarding the **SESS** variable, this is an an ordinal variable indicating 
visit order.  Kristi indicated that subject ages are highly variable 
after visit 12 (i.e., the school visits). The table below indicates how
a visit like ``KG_2`` (the second kindergarten visit) corresponds to
the visit 14.

=====  ==  ==  ==
Grade   1   2   3
=====  ==  ==  ==
K3     13  14  15
1G     16  17  18
2G     19  20  21
3G     22  23  24
4G     25  26  27 
=====  ==  ==  ==

