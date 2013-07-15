.. _g2sect_9:

*************************************************
Logistic Issues (Prepare and Submit a Transcript)
*************************************************

Overview
========

This guide is designed to provide a detailed outline of the steps necessary to prepare a speech reliable transcript for second level gesture annotation. It will also explain how to deal with several problems that might occur while coding, and how to submit your fully coded transcript.

Preparing the Transcript
========================

#. Pull the speech reliable transcript off analord. You can find these transcripts in Analord > Datashare > Project (2/3) > Home Visits > Transcripts > Base > Reliable.

#. Save the transcript to your computer in the format *subject#.visit#.project#_GX.xls* (e.g. 48.10H.P2_GX.xls).

#. Retrieve the Part of Speech/Syntax inserts from analord. Find them in Datashare > Project (2/3) > Home Visits > Transcripts > Supplemented > Gesture Coded (Erica) > Inserts > pos_syn++.

#. Copy columns B through L of the insert spreadsheet (*p_chat* through *p_syntype*), and paste in the speech reliable transcript between the columns for *p_utts* and *p_form*. Copy columns M through W of the insert spreadsheet (*c_chat* through *c_syntype*), and paste in the speech reliable transcript between the columns for *c_utts* and *c_form*.

#. To make things a little easier to work with, it may be best to hide all inserted columns except *p_enum* and *c_enum*, though it may be helpful to keep the chat columns visible as well.

#. Download the Gesture Coding Template :download:`here <downloads/gx_template.xls>`. Copy columns G through AF (*p_g_type* through *p_persp*) and paste in the speech reliable transcript between *p_mspd* and *c_utts*. Copy columns AY through BI (*c_g_type* through *c_persp*) and paste in the speech reliable transcript between *c_mspd* and *context*.

#. Copy columns BK and BL (*edit* and *edit_note*) from the Gesture Coding Transcript and paste after the *context* column in the SR transcript. You’re finally done with copy and paste!

#. Check the info page of the SR transcript and add the necessary information (Gesture Annotator, Gesture Annotation Date, and Gesture Version No.).

#. Save the video from the video server onto your computer and begin gesture coding.

Adding, Omitting, and Flagging
==============================

Occasionally, you may encounter one of three situations that require you to use the last two columns on the template, *edit* and *edit_note*.  Be aware that a) and b) apply only to gestures which do or should occur on their own line and which are not accompanied by speech.

* *Missing gesture.* The original transcriber missed notating a gesture where you are confident a gesture exists. Here, insert a line and code the gesture as usual, including adding the timestamp. In the Line Number column, put ``.1`` after the number of the line before it. For instance, if inserting a line after line ``200``, label it ``200.1``. If it is necessary to add more than one line for gesture in the same space between two existing lines, label them sequentially (``200.1``, ``200.2``, ``200.3`` ... ``200.13``, ``200.14`` ...). In the *edit* column, type ``i`` for "insert." In the *edit_note* column, provide a brief explanation for the suggested addition, such as ``insert line; missed in original transcript``.

* *Incorrectly attributed gesture.* The original transcriber notated a gesture where you are confident a gesture does not exist. Do not delete the line! In the *edit* column, insert ``o`` for "omit." In the *edit_note* column, provide a brief explanation for the suggested omission, such as ``omit line; not really a gesture``.

* *Utterance flag.* The original transcriber has made an error in the utterance column. This may be a misspelling, speech placed in the wrong utterance column, or a missed or misheard word. In the *edit* column, insert ``f`` for "flag." In the *edit_note* column, provide a brief explanation for the flag, such as ``slipppery in c_utts should be slippery``.

As mentioned above, the *edit* and *edit_note* fields are for gestures on their own line (or flagging utterances). When a gesture needs to be added, deleted, or modified without the proposed insertion or omission of a full line, feel free to make the necessary changes. There is no need to mark these lines as modified. If you add a gesture to a line with an utterance, be sure to add a timestamp.

Submitting Completed Transcript
===============================

When you are finished working, save the transcript to your computer and submit it to the validator. Find the validator by logging in `here <https://ldp.uchicago.edu/portal>`_ then navigating to "Data" and choosing "Validate a Transcript." Make the necessary changes to have your transcript approved by the validator and submit!
