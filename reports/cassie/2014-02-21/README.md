## 27-02-2014

Cassie requested a report indicating the number of verb types and tokens used by each group-1 child and parent at each period-1 visit.

We used [this script](query.py) to generate the [requested report](report.tsv).

The report contains the following columns:

* `SUBJ` - subject ID
* `SESS` - session ID
* `SPKR` - speaker (`C` for child and `P` for parent)
* `VTYP` - count of verb types
* `VTOK` - count of verb tokens

---

## Email to Cassie

> You requested a report indicating the number of verbs used by each
> child and each parent at each visit for the normally developing subjects.
> One caveat regarding identifying verb forms: there’s some ambiguity with 
> auxiliary forms and participles when making compound verb forms, e.g.: 
> “want to”, "is going”, “has been”.  The POS is often ambiguous even with 
> the syntactic annotation, which is only available on a subset of subjects 
> (12 total).  I’m just going to try to identify word tokens tagged with `v`
> and ignore any `aux` or `part` tags for now.  If this is a concern I’d be 
> happy to discuss.
