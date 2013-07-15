****************
Utterances Table
****************

The files in this directory are used to update the *utterances* table in 
the LDP's primary dataset. Each record/row in the *utterances* table 
contains info about one of the lines in a transcript.

.. note::

    Each line in a transcript corresponds to an observed utterance that 
    was transcribed and annotated.


Updates
=======

The ``updates`` directory contains update files, each of which consists of 
sql update statements for batch updating some pre-existing rows in the 
*utterances* table of a locally instantiated database.

Note the naming scheme for update files::

    [SUBJECT.SESSION].KIND[_SPEAKER].sql

*KIND* should indicate one of the following:

* an annotation tier (indicating a set of columns) being updated
* a particular column being updated
* a typical set of fixes/updates to be applied to the utterance columns

Consider the following examples:

==========================   ============================================= 
Filename                     Description          
==========================   ============================================= 
100.01.mor.sql               MOR tier updates for subject 100 at session 1
100.01.mor_p.sql             ditto but for parent only
100.01.mor_c.sql             ditto but for child only 
100.01.mor+syn.sql           MOR and SYN tier updates
100.01.mor+syn_c.sql         MOR and SYN tier updates for child only
100.01.mor+syn+max.sql       MOR and SYN and MAX tier updates (both speakers)
01-06.mor.sql                MOR tier updates for all subjects from sess 1-6
spell-1.sql                  spelling corrections made to utterance columns
spell-2.sql                  more spelling corrections
g_type.sql                   updates/corrections made to g_type columns
c_g_type.sql                 updates/corrections made to child g_type column


Problems
========

The ``problems`` directory contains lists of problematic values found within
particular columns in the utterance table. For example,
``problems/c_g_type.tsv`` contains a list of problematic values identified
within the child gesture type column (``c_g_type``).

Each line consists of an utterance ID and the problematic value found within
the column indicated by the filename. For example, here are the first two
lines of ``problems/c_g_type.tsv``::

    id	c_g_type
    10380700450	RF.a

The first line is just a column header line. The second line indicates that the
value for the child gesture type column (``c_g_type``) for utterance with ID
10380700450 is ``RF.a``, which is not a permissible value for that column.

.. note:: 

    See the `g_type column spec`_ for details on permissible values.

.. _g_type column spec: http://joyrexus.spc.uchicago.edu/ldp/docs/specs/transcript/columns/g_type.html

Each of these column values needs to be manually reviewed and corrected. Once
corrected, the resulting file can be converted into a TSV update file as
indicated above.
