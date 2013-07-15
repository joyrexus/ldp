.. _g2sect_6:


*************
Special Cases
*************

Multiple Gestures
=================

When more than one gesture is performed during an utterance, a semi-colon should be used to separate the codes for the gestures in each cell. There should be no spaces between codes.

 * In this example, the gesture is a point, represented by the ``[`` and ``]`` symbols.

+--------------------------------------------------------+------------+----------------------+----------+------------+------------------------+-----------+
| **Example**                                            | **G-Type** | **G-S Relationship** | **Time** | **Time-G** | **Semantic Correlate** | **Theme** |
+--------------------------------------------------------+------------+----------------------+----------+------------+------------------------+-----------+
| "He came [out of **there** and] got [**that one**]"    | DP:DP      | DA;DA                | 5;9,10   | M;E        | there;that one         | IS;PA     |
+--------------------------------------------------------+------------+----------------------+----------+------------+------------------------+-----------+

Multiple Meanings
=================

Sometimes gestures represent more than one value for a particular cell. This happens often in the "timing" column, but occasionally happens with other variables. When multiple values are represented by the gesture, the codes for the different values are separated by a comma (x,y). 

When the gesture could be interpreted as having one of several different meanings, the codes are separated by a slash (x/y). If a gesture takes more than one code separated by a / for one column, then all columns should be expanded to match the format of that column. 

 * i.e.  x,y: gesture has the value of x **AND** y
 * i.e. x/y: gesture has the value of x **OR** y


Deictic Show + Deictic Point
============================

When an object is held up and pointed to with the other hand, the first level gesture codes will be "hold + point." Since these two movements form a single, unified, act of showing (i.e. a **single gesture**), they are not coded as separate gestures, rather the four-letter code "DSDP" is used to distinguish these from other shows and points. Coding for all other categories remains the same as it would for either gesture on its own. Other gestures produced simultaneously (e.g. a point with a shake) are considered to be separate gestures and are separated with a semicolon in each column.

Sibling-directed talk
=====================

When the child or parent directs his or her speech to another adult or child, then the "NA" code should be used for the columns that rely on the CHAT transcription (timing, timing general, word, and word number). 

Example:

+---------+----------------+--------------+--------------+------------+----------------+------------+----------------+----------------+----------------+
| **Key** | **p_utts**     | **p_g_type** | **p_gs_rel** | **p_time** | **p_time_gen** | **p_word** | **p_word_num** | **p_sem_role** | **p_pres_ref** |
+---------+----------------+--------------+--------------+------------+----------------+------------+----------------+----------------+----------------+
| ``*``   | You stay here. | DP           | DA           | NA         | NA             | NA         | NA             | LO             | Y              |
+---------+----------------+--------------+--------------+------------+----------------+------------+----------------+----------------+----------------+

Adding or correcting first-level gesture codes
==============================================

Sometimes a second-level coder will notice a gesture that was overlooked by the first level coder. The transcribed speech is not to be altered by the second-level gesture coders, but it is possible to alter or add to the first-level gesture codes. The second-level coders are often the last people who watch the video and follow along with the transcripts, so it is their responsibility to make sure the first-level gesture codes are sufficient and correct. When minor changes to the codes need to be made, it is at the coder's digression to do so. When making a major change (such as adding a new gesture or deleting a previously-coded one), it is desirable that the coder check with one of the other second-level gesture coders to validate the change or addition.

Adding rows
-----------

If adding in a new gesture necessitates adding a line to the transcript (i.e. the gesture occurs without speech), then a line number must be added to the inserted row. The line number should be **n.1, n.2, n.3, etc.** for each line inserted after line n. If this intermediate code is not added to the line, then it is extremely difficult to integrate the gesture-coded transcript back into the dataset, as the line numbers no longer line up with other versions of the data. A note should be made in the edit and edit note columns to indicate a line has been inserted or that it should be omitted. When inserting a line, add the new line number in the correct column, and also write i in the edit column. In edit note, write the reason for inserting a new column. 

Omissions
---------

Do not omit lines. Instead, write o in the edit column and explain why the line should be omitted in the edit note column. 

Incorrect Speech or Gesture
---------------------------

Do not change speech in any transcript. If you believe the speech to have been transcribed incorrectly,  write *f* in the edit column and write what you believe was said in the edit note column. If you add or delete a gesture from the originally coded transcript, make a note of it by typing *f* in the edit column and a brief explanation of your changes in the edit note column. 


