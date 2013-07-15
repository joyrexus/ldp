**************
Subjects Table
**************

The files in this directory are used to define, create, and populate the
*subjects* table in the LDP's primary dataset. Each record/row in the 
*subjects* table contains info about one of the subjects in our study.


Files
=====

The ``schema.sql`` file contains the schema definition for the *subjects* 
table.

The ``init.sql`` file can be used to initialize a sqlite database with 
subject info::

    sqlite3 subjects.db < init.sql

The ``data.tsv`` file contains subject info in TSV (tab-separated values) format.  
