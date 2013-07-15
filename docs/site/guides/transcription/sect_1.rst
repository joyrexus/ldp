.. _tg-1:

*********
1. Basics 
*********

The starting point for each new transcript is the Transcript Template.  This section will explain the various worksheets on the template as well as the fields on each worksheet.  It will also go over a few steps you may need to complete before you start transcribing.

.. _tg-1-1:

.. index::
   single: transcript; template
   single: excel; transcript template
   single: excel; autocorrect file
   single: excel; applescripts
   single: excel; shortcuts
   single: applescript; transcription shortcuts
   single: transcription; environment

1.1 Setup your transcription environment
========================================

Before you start transcribing it's necessary to setup a working transcription environment. Transcription is done in Microsoft Excel, which provides a nice grid format for transcribing utterances (one per line) and annotating utterances in separate columns. There are three pieces you'll need in additional to the Excel application itself: (1) the official transcript template (for generating properly formatted transcripts); (2) the project's modified Autocorrect file (to avoid having Excel from automatically replacing certain characters); and (3) a set of AppleScript shortcuts (which provide certain key commands). The third item is not required but highly recommended and will make your transcription work both more efficient and less tedious.

1.1.1 Use a transcript template
-------------------------------

Always use a transcript template to generate new transcript documents. A
template creates a skeletal document with the appropriate worksheets and
formatting, which you will then fill out when doing your transcription and
coding. You can download the transcript template :download:`here <downloads/transcript.xlt>`. If you prefer, you can download an .xls version of the template :download:`here <downloads/transcript.xls>`.

1.1.2 Install the Autocorrect file
----------------------------------

To help with the automated analysis of transcripts, it may be necessary to modify the Autocorrect file for Excel. When a transcriber writes something like "dont," Excel automatically adds an apostrophe. The default file has a slightly different apostrophe (don’t) than the standard keyboard apostrophe (don't). It's a subtle difference, but enough to throw off the analysis software. If the Autocorrect file on your computer has not been modified (i.e. you are working on a new computer) please modify it to assist in the automated analysis process. You can download the Autocorrect file for Microsoft Office 2008 :download:`here <downloads/autocorrect/office_2008.zip>`. (If you're using the older version of Excel you can download the Autocorrect file for Microsoft Office v.X :download:`here <downloads/autocorrect/office_vX.zip>`.) The download consists of a zip file. After downloading, double-click the zip file to expand it. You'll then have a folder containing the Autocorrect file ("Microsoft Office ACL [English]") and a "Read Me" file with instructions on how to install it.

1.1.3 Install the AppleScript shortcuts
---------------------------------------

The AppleScript shortcuts provide key-commands that help streamline the
transcription process. There are seven shortcuts total: three for jumping 
between columns, three for adjusting playback speed, and one for inserting a 
timestamp.

To install the shortcuts, first download the zip archive containing them 
:download:`here <downloads/applescripts.zip>`. After downloading you'll have a
file named `applescripts.zip`. Unzip this archive and put the seven scripts in
`<YourHomeFolder>/Documents/Microsoft User Data/Excel Script Menu Items`.

With the scripts now in place, restart Excel if you have it open. After restarting you should be able to use them.

* To jump to the parent utts column hit `Control-P`.

* To jump to the child utts column hit `Control-C`.

* To jump to the context column hit `Control-X`.

* To set the movie playback speed to half speed hit `Control-1`.

* To set the movie playback speed to normal speed hit `Control-2`.

* To set the movie playback speed to 1.5x speed hit `Control-3`.

* To insert a timestamp you need to have a movie open in the Quicktime Player.
  Within Excel hit `Control-T` to insert the current playback time in the 
  first column of whatever row is currently active/selected.

.. note::

    The `Control` key is usually in the far lower lefthand corner of the keyboard.  Note that it's distinct from the `Command` (a.k.a., puppy-paw) key.

.. note::

    These shortcuts are set up for base level transcripts but can be easily be modified for transcripts with additional columns. (See Jason or Ben for assistance with this.) 


.. _tg-1-2:

1.2 Fill out the info worksheet
===============================

When you generate a new transcript from a template you'll first see the
Info worksheet. This is where you'll note general information about the
transcription, such as the name of the transcriber, date of transcription, cast
of characters present (and any nicknames used in the video), etc. It is
critical that you fill out the *Transcription Version No.* field with the
latest version number of the transcription guide you are now reading. This
should be indicated at the top of the :ref:`Revision History <tg-revisions>`. For example, if the top line of the Revision History reads "Version
1.5", you would fill out the *Transcription Version No.* field with
``1.5``.

.. _tg-1-2-1:

1.2.1 Transcript notes
----------------------

Use the *Notes* field to record any idiosyncratic child speech and any unusual circumstances of the visit and/or video (e.g. father is PCG for this visit only, visit was cut short, etc).  All notes should be contained in one cell, separating information with commas and semicolons where necessary.

.. _tg-1-2-2:

1.2.2 Cute moments
------------------

Make a note in the *Cute Moments* field if you come across something cute that the subject's family might like to have on a DVD. Include a timestamp and a very brief description of the moment. This field is optional, but if somebody eventually makes a *Cute Moments* DVD for the families, it would make their job easier. All cute moments should be contained in one cell, separating information with commas or semicolons where necessary. Maintaining the number of cells on the Info page is necessary to run programs to analyze transcripts.

.. _tg-1-2-3:

1.2.3 Spontaneous speech time
-----------------------------

Calculate and note the length in minutes of the transcribed spontaneous speech in the *Total Time of Spontaneous Speech* field. Due to unforeseen circumstances, visits are sometimes shorter than ninety minutes, which could have bearing on studies that use this data. Making a note of the actual length allows researchers to adjust their research accordingly. Simply type the two-digit length without any accompanying text (e.g. ``90`` or ``54``, NOT ``90 min``).

.. _tg-1-2-4:

1.2.4 New words
---------------

Place words that are not yet recognized by the spell-checker/validator in the *New Words* field.  After completing a transcript, you must run spell-check.  If there are words that are not recognized, but that you feel are real words, first check the `Oxford English Dictionary <http://www.oed.com/>`_ or the LDP's :ref:`list of recognized words and standardized spellings <tg-spelling>` to see whether you are simply misspelling them.  If you cannot find a word in either place, discuss with other RAs and come to a consensus as to whether it is a (somewhat) widely recognized word that just happens to be missing from these repositories, or whether it is idiosyncratic to the child.  In the former case, you may add this word to *New Words* field so that the validator recognizes it.  In the latter case, transcribe the word with an ``@`` symbol at the end of the word (see :ref:`Section 6.1.1 <tg-6-1-1>` for more on the ``@`` symbol). 

.. _tg-1-3:

1.3 Transcribe and annotate
===========================

You should transcribe and annotate visit videos on the Transcript worksheet. This sheet is where you will transcribe parent and child utterances and do the first layer gesture coding, adding key codes, timestamps, and context where necessary.

.. _tg-1-3-1:

1.3.1 Timestamps
----------------

Place timestamps for all gestures and for some key codes in the *time* column. Include the hour, minutes, and seconds of the gesture or key code (e.g. ``0:12:34``). You may also make a timestamp every few minutes, even if it is not required, to help you and other transcribers and coders later. See :ref:`Section 2.10 <tg-2-10>` for more on which key codes receive a timestamp. 

.. _tg-1-3-2:

1.3.2 Line numbers
------------------

Number each line sequentially in the *line* column. In Excel, simply enter a ``1`` in the first cell and a ``2`` in the second. Then highlight those two cells, move the cursor to the bottom right corner of the selection, click and drag down. Excel will fill in the remaining numbers. Make sure that each row has a unique line number and that no numbers have been skipped. 

.. _tg-1-3-3:

1.3.3 Key codes
---------------

Place key codes for certain transcribing scenarios in the *key* column. For example, type ``*`` when the PCG is speaking to a sibling, ``v`` when the subject child is singing, or ``F`` when the father speaks and is PCG or co-PCG.  Key codes are also used at five-minute intervals when there is any non-transcribed speech.  See Sections :ref:`2.1 <tg-2-1>` to :ref:`2.5 <tg-2-5>`, :ref:`2.8 <tg-2-8>` to :ref:`2.10 <tg-2-10>`, :ref:`3.3 <tg-3-3>`, and :ref:`6.10 <tg-6-10>` for more on key codes. 

.. _tg-1-3-4:

1.3.4 Utterances
----------------

All appropriate PCG speech goes in the *p_utts* column, while all child speech goes in the *c_utts* column. For more on what to transcribe, see :ref:`Section 2 <tg-2>`; the rest of this document outlines how to transcribe parent and child speech. 

.. _tg-1-3-5:

1.3.5 Gesture form
------------------

When coding gesture, mark the type of gesture in the *p_form* or *c_form* column.  There is `a comprehensive list of gesture forms <https://spreadsheets.google.com/a/uchicago.edu/ccc?key=p7XpiQv1lXwg3fNbst_lHIg&hl=en>`_ on the LDP website. [Note: let's replace the link to the google doc with a link to the transcript spec once we have the transcript spec deployed.]

.. _tg-1-3-6:

1.3.6 Body parts used in gesture
--------------------------------

Note the body part used to make the gesture in the *p_lrb* or *c_lrb* column. Mark whether the gesture was made with the left hand (``L``), right hand (``R``), both hands (``B``), left foot (``LF``), right foot (``RF``), head (``H``), or whole body (``WB``).

.. _tg-1-3-7:

1.3.7 Object used in gesture
----------------------------

Note the object, if any, that was used or referred to in a gesture in the *p_obj* or *c_obj* column. A wide variety of things can be entered in this cell, as this is where you note the referent of deictic gestures (gestures referring to a person or object) or, occasionally, an object used in an iconic gesture. 

.. _tg-1-3-8:

.. index:: 
   single: gesture; gloss

1.3.8 Gesture gloss
-------------------

Write the meaning of the gesture in the *p_gloss* or *c_gloss* column. For deictic gestures, this will usually be exactly the same as the *obj* column, with the exception of ``give/take object`` and non-literal points.  For conventional gestures, there are agreed-upon glosses which you can find on the list of gesture forms [Note: Link to glosses for conventional gestures]. For iconic gestures, simply type in whatever you think the gesture is trying to convey. 

.. _tg-1-3-9:

.. index:: 
   single: gesture; orientation

1.3.9 Gesture orientation
-------------------------

Put information regarding the motion and orientation of certain gestures in the *p_orient* or *c_orient* column. Gestures with the form ``(cont) point``, ``(cont) palm``, and ``drag`` that are accompanied by touching or tapping receive ``touch`` or ``tap`` in this column. A ``palm`` gesture requires a description of the orientation of the palm (``palm up``, ``palm down``, ``palm side``, or ``palm out``). A ``hold`` gesture can be accompanied by ``shake`` in the *orient* column. Finally, iconic and metaphoric gestures can be marked ``tracepath`` or ``traceshape``. 

.. _tg-1-3-10:

.. index:: 
   single: gesture; motion and space description
   single: gesture; mspd

1.3.10 Motion and space description
-----------------------------------

When necessary, describe the appearance of gestures in the *p_mspd* or *c_mspd* column. This is required for iconic and metaphoric gestures.  Since they are generally unique (i.e. not conventional), it helps to know what exactly the gesture looked like. After noting the gloss, give a concise description of the motion of the gesture. 

.. _tg-1-3-11:

.. index:: 
   single: column; context

1.3.11 Context
--------------

If the meaning of an utterance is unclear, use the *context* column to describe circumstances relevant to it that are not readily inferable from the speech. This could be interactions that are not transcribed (e.g. from a sibling) that the child or parent responds to, situations which make an utterance unintelligible or which could help clarify an unintelligible utterance, or the name of a song that is sung but not transcribed. This column is also used in conjunction with the ``x`` and ``xc`` key codes every five minutes to describe overheard but non-transcribed speech. See Sections :ref:`2.3.3 <tg-2-3-3>`, :ref:`2.6.1 <tg-2-6-1>`, :ref:`2.8.1 <tg-2-8-1>`, :ref:`2.10 <tg-2-10>`, :ref:`3.4 <tg-3-4>`, and :ref:`7.6 <tg-7-6>` for more on the *context* column. 

.. _tg-1-4:

1.4 Checklist
=============

A checklist of requirements for submitting a transcript can be found on the Checklist and Reminders worksheet. Make sure all of the items on the checklist are marked ``done`` before submitting each transcript. Simply click on a cell containing ``---``, click on the drop-down list, and select ``done``. 

.. _tg-1-5:

