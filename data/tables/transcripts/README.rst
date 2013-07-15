*****************
Transcripts Table
*****************

The files in this directory are used to define, create, and populate the
*transcripts* table in the LDP's primary dataset. Each record/row in the 
*transcripts* table contains info about one of the transcripts in our study.

.. note:: 

    The ID for a visit will correspond to the ID for the transcript 
    resulting from the visit.

    Info about the visit from which a given transcript originated 
    can be found in the visits table.

    The *transcripts* table only contains meta-data about transcripts. 

    The *utterances* table contains the actual transcript line data from the
    original transcripts (utterances and gesture codes, etc.)


Files
=====

The ``schema.sql`` file contains the schema definition for the *transcripts*
table.

The ``init.sql`` file can be used to initialize a sqlite database with
transcript info::

    sqlite3 transcripts.db < init.sql

The ``data.tsv`` file contains transcript info in TSV (tab-separated values) format.  
