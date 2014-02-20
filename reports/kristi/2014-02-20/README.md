Kristi provided an excel file that contains open ended descriptions of the
people present at a given visit for the first six sessions.

I extracted the "people at visit" column for each session resulting in the
`cast-info.tsv` file.

Some of this information might be of value if normalized.  For example,
boolean-valued (T/F) columns indicating whether ...

* the mother was present
* the father was present
* siblings were present
* other family members were present
* other non-family members were present

The first three items could probably be inferred without too much trouble by
searching for the presence of "M" for mother, "F" for father, and a small
number of patterns to identify the presence of siblings ("S1", "S2", ...,
"sib1", "sib2", "sis", "bro").  Patterns to identify whether other family
members are present may be possible too, but the annotation seems to be highly
variable.
