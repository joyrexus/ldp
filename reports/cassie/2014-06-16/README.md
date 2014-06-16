# 2014-06-16

Send Cassie and Rebecca utterances for a few additional transcripts:

* 109.07
* 77.09
* 88.09
* 22.12


# 2014-04-18

Cassie needs to align her coding on the original transcripts with the canonical dataset utterances and their unique IDs. We're providing the utterance and IDs for all of the transripts she's coded.

The visits.txt file contains a list of additional visits that Cassie needs.

The query.py file contains the script used to dump the needed utterances/IDs from the LDP dataset.

The resulting output files contain the following columns:

* _ID - unique utterance ID
* time - utterance timestamp
* row - utterance row number
* c_utts - child utterance
* p_utts - parent utterance
