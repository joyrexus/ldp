Measures Table
==============

The files in this directory are used to define, create, and populate the *measures* table in the LDP's primary dataset. Each record/row in the *measures* table contains summary measures for a unique triple of `(subject, session, speaker)` based on one of the visits made during the course of our study.

The measures table currently contains standard speech counts for both parent and child speakers for all home visits (sessions 1 to 12).

The standard speech counts consist of counts for utterances, word tokens and types, as well as the MLU (mean length of utterance) measure.


## Columns

The data table (`data.tsv`) contains the following columns:

* `subject` - subject id
* `session` - session id (1 = 14m; 12 = 58m) 
* `speaker` - speaker (P = parent, C = child)
* `utterances` - utterance count
* `word_tokens` - word token count
* `word_types` - word type count
* `mlu` - mean length of utterance


## Notes

Summary measures are derived from project transcripts and task assessments.

Information about a particular transcript can be found in the
`transcripts` table.  Visit specific information (such as **SES** variables)
can be found in the `visits` table.


## Files

The `schema.sql` file contains the schema definition for the *measures*
table.

The `init.sql` file can be used to initialize a sqlite database with visit info:

    sqlite3 visits.db < init.sql

The `data.tsv` file contains transcript info in TSV (tab-separated values) format.  
