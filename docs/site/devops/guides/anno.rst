
*********************************
The Transcript Annotation Process
*********************************


Marking Edits
=============

Could we name the two new columns *edit* and *edit_note*?

My thought is that *edit* should only contain one of three possible values:

* ``o`` for "omit"
* ``i`` for "insert"
* ``f`` for "flag"

The other column, *edit_note*, will be an open-ended text field used to give
some indication of why the edit is needed. 

For example:

=====  ====================================================
edit   edit_note
=====  ====================================================
``o``  omit this line; not really a gesture
``f``  "slipperry" in child utterance should be "slippery"
``i``  insert this line; missed in original transcription
=====  ====================================================


As you can see, I changed my mind about deleting lines. We're not ever going to
delete anything from the transcript dataset. However, we will use the *edit*
column to mark lines that could optionally be omitted from future analyses
because a later editor judges them as problematic for some reason.

FWIW, I've also changed my mind about how annotators should incorporate new lines that were missed the first time around. Instead of inserting new lines within the existing/original transcript lines, for now I'm going to ask Galila (or anyone doing additional levels of annotation) to append lines to be inserted after the last line of the original transcript. This will make updating the transcript dataset much easier and allow us to establish permanent/canonical line IDs.
