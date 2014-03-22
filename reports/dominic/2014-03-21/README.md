Dominic requested a list of parent and child utterances from sessions 1 to 7 that contain any of the following quantifiers:

* all
* another
* any
* both
* few
* many
* more
* most
* much
* only
* several
* some


## Files

* [report.xls](report.xls) - the requested report
* [summary.tsv](summary.tsv) - summary counts
* [query.py](query.py) - query script used to generate the report and summary
  counts
* [words.txt](words.txt) - list of words to match


## Report Column Key

* `SUBJ`  - subject ID
* `SESS`  - session/visit ID
* `SPKR`  - speaker (`P` for parent or `C` for child)
* `ROW`   - transcript row number
* `UTT`   - matched utterance
* `MATCH` - matched word token(s)
