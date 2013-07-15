**************
Sessions Table
**************

The files in this directory are used to define, create, and populate the
*sessions* table in the LDP's primary dataset. Each record/row in the 
*sessions* table contains info about one of the sessions in our study.


Files
=====

The ``schema.sql`` file contains the schema definition for the *sessions* 
table.

The ``init.sql`` file can be used to initialize a sqlite database with 
session info::

    sqlite3 sessions.db < init.sql

The ``data.tsv`` file contains session info in TSV (tab-separated values) format.  
