************
Visits Table
************

The files in this directory are used to define, create, and populate the
*visits* table in the LDP's primary dataset. Each record/row in the 
*visits* table contains info for one of the visits made during the
course of our study.

.. note:: 

    Info about a transcript resulting from a visit can be found in the
    transcripts table.

    The ID for a visit will correspond to the ID for the transcript 
    resulting from the visit.


Files
=====

The ``schema.sql`` file contains the schema definition for the *visits*
table.

The ``init.sql`` file can be used to initialize a sqlite database with
visit info::

    sqlite3 visits.db < init.sql

The ``data.tsv`` file contains transcript info in TSV (tab-separated values) format.  
