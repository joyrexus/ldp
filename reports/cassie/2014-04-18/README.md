# 2014-05-21 

Send Casse the requested session 7 utterances.  For some reason these were not
included in the first request.


# 2014-04-18 

Cassie needs to align her coding on the original transcripts with the canonical
dataset utterances and their unique IDs.  We're providing the utterance and IDs
for all of the transripts she's coded.

The [`visits.txt`](visits.txt) file contains a list of all visits that Cassie
has coded.

The [`query.py`](query.py) file contains the script used to dump the needed
utterances/IDs from the LDP dataset.

The resulting output files contain the following columns:

* `_ID` - unique utterance ID
* `time` - utterance timestamp
* `row` - utterance row number
* `c_utts` - child utterance
* `p_utts` - parent utterance
