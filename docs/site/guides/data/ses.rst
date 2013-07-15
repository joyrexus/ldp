***********
Subject SES
***********


Overview
========

Kristi and Meredith have compiled a table of basic demographic/SES info for all
our Project 2 subjects.

.. warning::

    This information is based on information collected during a subject's 
    first home visit at 14 months of age. Note that some of the variables 
    are susceptible to change (PCG, income, education, etc.) at later 
    timepoints.

The :download:`Project 2 SES data file <ses.zip>` is in TSV (tab-separated value) format. Column descriptions are given below. 


To Do
=====

This summary table could be extended to include change status variables 
for each variable susceptible of changing. For example, paired with the 
*pcg* column would be a *pcg_change* column, simply indicating whether the 
PCG value indicated changed at a later timepoint.


Columns
=======


id
--

Subject ID.

:Type: Integer
:Values: Integer range (20 < x < 200)
:Static: Yes


firstborn
---------

Is the subject the firstborn/eldest sibling?

:Type: Boolean
:Values: 1 (yes), 0 (no)
:Static: Yes


edu
---

Education level of primary caregiver. For dual caregivers, only mother's 
education level is given.

:Type: Ordinal
:Values: 1 (some  high school),
         2 (high school),
         3 (some college or trade school),
         4 (bachelor's degree),
         5 (advanced degree)
:Static: No


sex
---

Subject's gender.

:Type: Categorical
:Values: M (male), 
         F (female)
:Static: Yes


ethn
----

Ethnicity is taken to be the combination of the subject's parent's ethnicities.

:Type: Categorical
:Values: H (hispanic), 
         N (non-hispanic)
:Static: Yes


race
----

Race is taken to be the combination of the subject's parent's races.

:Type: Categorical
:Values: B (black), 
         W (white), 
         A (asian), 
         I (american indian), 
         P (pacific islander), 
         M (multi-racial), 
         O (other)
:Static: Yes


pcg
---

Subject's primary caregiver.

:Type: Categorical
:Values: M (mother), F (father), B (both mother and father)
:Static: No


income
------

Income level of subject's primary caregiver.

:Type: Ordinal
:Values: 1 (< $15,000),
         2 ($15,000 - $34,999),
         3 ($35,000 - $49,999),
         4 ($50,000 - $74,999),
         5 ($75,000 - $99,999),
         6 (> $100,000)
:Static: No


single_parent
-------------

Is the subject living in a single parent home?

:Type: Boolean
:Values: 1 (yes), 0 (no)
:Static: No


siblings
--------

Number of siblings.

:Type: Integer
:Values: Integer range (0 to 20)
:Static: No
