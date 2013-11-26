# README

Lori Petersen is requesting a list of all utterances containing words of
interest within specificed transcript windows.

The "windows" are durations of time in which the subject was observed to engage
in a particular activity of interest, viz. playing with blocks.


## Files

* `times.tsv` - specifies the windows of interest for each transript
* `words.txt` - lists the word tokens to be matched
* `report.tsv` - the requested report listing matched utterances
* `query.py` - the query script used to generate the requested report


## Report Format

The report requested contains the following columns:

* SUBJECT - subject ID 
* SESSION - session/visit ID
* TIME - time stamp of utterance (or last seen time stamp)
* CONTEXT - context notes
* UTT - matched utterance
* MATCHES - number of matched words
* MATCHED - matched words


## Request

    From: Lori Petersen <lpetersen@uchicago.edu>
    Subject: Spatial words
    Date: November 22, 2013 at 3:49:15 PM CST

    I am looking into the spatial language that children use when they 
    are playing with blocks. Are you able to do word searches at this 
    fine-grained level (for example, from 0:01:24-0:25:13) by participant 
    by session, or are you only able to do word searches by participant 
    by session?

    I would like a list of all matching utterances if that is okay.
