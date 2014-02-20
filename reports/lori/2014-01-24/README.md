# README

Lori Petersen is requesting a list of all parent utterances containing words of
interest within specificed transcript windows.

The "windows" are durations of time in which the subject was observed to engage
in a particular activity of interest, viz. playing with blocks.


## Files

* [words.txt](words.txt) - lists the word tokens to be matched
* [subjects.txt](subjects.txt) - lists the subject IDs to search
* [times.tsv](times.tsv) - specifies the windows of interest for each transript
* [report.tsv](report.tsv) - the requested report listing matched utterances
* [query.py](query.py) - the query script used to generate the requested report


## Report Format

The [requested report](report.tsv) contains the following columns:

* `SUBJECT` - subject ID 
* `SESSION` - session/visit ID
* `TIME` - time stamp of utterance (or last seen time stamp)
* `UTTERANCE` - matched parent utterance
* `MATCHES` - number of matched words
* `MATCHED` - matched words
* `CONTEXT` - context notes


## Notes

1. Most utterances do not contain timestamps.  If an utterance did not contain
   a timestamp, the last seen timestamp was used to determine if the utterance
   fell within one of the specified windows of interest.  

2. Only single-word token strings were used in order to simplifiy word
   matching.  For example, a multi-word string such as "a little" was 
   converted to a single-word string, "little".


## Request

    From: Lori P
    Subject: Spatial words
    Date: November 22, 2013

    I am looking into the spatial language that children use when they 
    are playing with blocks. Are you able to do word searches at this 
    fine-grained level (for example, from 0:01:24-0:25:13) by participant 
    by session, or are you only able to do word searches by participant 
    by session?

    I would like a list of all matching utterances if that is okay.


---


From: [Lori Petersen](mailto://lpetersen@uchicago.edu)
Subject: RE: Spatial words
Date: January 3, 2014 at 9:47:25 AM CST

I would like to look into the spatial language that parents use when their children are playing with blocks. Would you be able to send me the spatial language that parents use during block play by participant by session?

Here are the files for the session/time and the words. There are a couple of spatial terms that are multiple words. I highlighted them in the excel file. 
