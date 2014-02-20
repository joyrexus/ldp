# SES - Group 1

Kristi and Meredith have compiled a table of basic demographic/SES info for all
our Group 1 (normally developing) subjects.

This information is based on information collected during a subject's first
home visit at 14 months of age. Note that some of the variables are susceptible
to change (PCG, income, education, etc.) at later timepoints.

The data file (`ses.tsv`) is in TSV (tab-separated value) format. Column descriptions are given below.  Notes on specific columns follows.


## To Do

This summary table could be extended to include change status variables for
each variable susceptible of changing. For example, paired with the pcg column
would be a pcg_change column, simply indicating whether the PCG value indicated
changed at a later timepoint.


## Columns

* `SUBJ` - subject ID
* `SEX` - subject gender
* `EDU` - education level
* `INC` - income level
* `RACE` - race
* `ETHN` - ethnicity

---

### `EDU` (education level)

Education level of primary caregiver. For dual caregivers, only mother's
education level is given.

1 (some high school), 2 (high school), 3 (some college or trade school), 4
(bachelor's degree), 5 (advanced degree)

### `INC` (income level)

Income level of subject's primary caregiver.

1 (< $15,000), 2 ($15,000 - $34,999), 3 ($35,000 - $49,999), 4 ($50,000 -
$74,999), 5 ($75,000 - $99,999), 6 (> $100,000)

### `RACE` (race)

B (black), W (white), A (asian), I (american indian), P (pacific islander), M
(multi-racial), O (other)

### `ETHN` (ethnicity)

H (hispanic), N (non-hispanic)
