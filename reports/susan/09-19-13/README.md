# README

Kristi (on behalf of Susan Levine) is requesting a summary report of child gesture counts based on the [LRB](http://joyrexus.spc.uchicago.edu/ldp/docs/specs/transcript/columns/lrb.html) column from sessions 1 to 5 and 8 of the home visits.


## Reports

The first report (`summary-1.xls`) provides summary counts of each of the [LRB codes](http://joyrexus.spc.uchicago.edu/ldp/docs/specs/transcript/columns/lrb.html) found as values in the **LRB** column.

The second report (`summary-2.xls`) provides summary counts of each of the [LRB codes](http://joyrexus.spc.uchicago.edu/ldp/docs/specs/transcript/columns/lrb.html) and their co-occurence with the [gesture type codes](http://joyrexus.spc.uchicago.edu/ldp/docs/specs/transcript/columns/g_type.html) found in the **G_TYPE** column.

The third report (`summary-3.xls`) provides summary counts of each of the [LRB codes](http://joyrexus.spc.uchicago.edu/ldp/docs/specs/transcript/columns/lrb.html) and their co-occurence with the [gesture-speech relation codes](http://joyrexus.spc.uchicago.edu/ldp/docs/specs/transcript/columns/gs_rel.html) found in the **GS_REL** column.


## LRB Codes

The valid **LRB** codes are listed below. See the [transcript column
specification](http://joyrexus.spc.uchicago.edu/ldp/docs/specs/transcript/) for
an overview of the valid codes for the other gesture columns.

    CODE  MEANING
    L     Left hand (or foot)
    R     Right hand (or foot)
    B     Both hands
    H     Head
    W     Whole body


## Notes

* As requested, repeated gesture codes (or gesture code combinations for the
latter two reports) were eliminated from the counts.  For example, if the
**LRB** codes for a given utterance consisted of `L+L+R+R+R`, both the `L` code
and `R` code totals were only incremented by one (instead of by 2 for the `L`
code total and 3 for the `R` code total).

* `WB` codes were counted as `W` codes. (`WB` is not a valid code.  
  We're assuming transcribers intended to code these as `W`, the code 
  for "whole body".)

* `LF` codes were counted as `L` and `RF` as `R` codes.  That is, instead of
  having separate coding categories for "left hand" and "left foot", there's
  simple a "left" category.


---

    From: Kristi Schonwald <kschonwa@uchicago.edu>
    Subject: data request
    Date: September 9, 2013 2:17:28 PM CDT
    To: Jason Voigt <jvoigt@uchicago.edu>
    Cc: Susan Levine <s-levine@uchicago.edu>

    Hi Jason, Susan Levine wanted to check something stated in a recent 
    paper that was submitted by Susan G-M and others on the BI kids.  
    She wanted to check to see how often each BI kid uses which hand when 
    they gesture, and how that compares to the TD kids at two timepoints, 
    05H and 08H.  Furthermore, she is interested in if the handedness of 
    the gesture differs based on the type of gesture (deictic, 
    representational, conventional, etc.).  

    Subjects/sessions:  all P2 and P3 kids who have both 05H and 08H visits

    Utterances:  from the above sessions, utterances that include an "L", "R", 
    or "B" in the c_lrb column (this includes when two gestures are coded in 
    the same cell, e.g., "L + L").  
