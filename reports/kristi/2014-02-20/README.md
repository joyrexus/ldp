Kristi provided an excel file that contained descriptions of the people present at a given visit for the first six sessions of visits to the homes of normally developing subjects.

I extracted the "people at visit" column for each session resulting in the
`cast-info.tsv` file.  Columns: ID (subject ID), 1 (visit 1), 2, 3, 4, 5, 6.

This may be of use to researchers interested in knowing whether (and perhaps how many) siblings or other family members were present at a given visit.  "Cast" information is typically available on the "info" worksheet of a standard LDP transcript, but such worksheets are not available on the earlier (< session 5) visit transcripts.

Some of this cast annotation might be of value if normalized.  For example,
boolean-valued (`T`/`F`) columns indicating whether ...

* the mother was present
* the father was present
* siblings were present
* other family members were present
* other non-family members were present

The first three items could be inferred without too much trouble by searching for the presence of `M` for mother, `F` for father, and a small number of patterns to identify the presence of siblings (`S1`, `S2`, ..., `sib1`, `sib2`, `sis`, `bro`).  Patterns to identify whether other family members are present may be possible too, but the annotation seems to be highly variable.

It doesn't look like it'd be possible to infer the total number of individuals
present at a given session for all cases.  The annotation is often ambiguous (e.g., "kids at park" or "neighbors").

It's also not clear how valuable any of this information would be without
knowing how long each individual was present at a vist and, for non-primary
caregivers, how many utterances were exchanged with the child subject.  (Note
that all subject utterances were transcribed, but only primary caregiver speech directed at the subject was transcribed.)
