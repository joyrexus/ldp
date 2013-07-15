.. _mg-prog:

********
Programs
********

The following list outlines the various scripts and programs developed by members of the LDP.


.. _mg-prog-all:

all
===

A simple script that updates all svn repositories that are being used.  This 
was a lot more useful before the repositories were consolidated, but this 
can still be run from anywhere.


.. _mg-prog-add:

add
===

A simple script that opens the specified ``.cut`` file from the 
``$CLAN/lib/english/lex`` in a vi editor.


.. _mg-prog-caps:

caps
====

Identifies all capitalized words and all ampersanded words in a CHAT file.
Also identifies those capitalized words that also appear in lower case and
those ampersanded words that also appear without an ampersand.

Usage::

    caps xx.xx.cha

Sample output::

	Capitalized words:

	Alls
	Bam             -->     check lower case
	Caribou
	Dad
	Daddy
	Flipper
	Fuh
	Ick             -->     check lower case
	Kuh             -->     check lower case
	La
	Lilia
	Mama            -->     check lower case
	Mexican
	Mom
	Mommy
	Museum_Of_Science_And_Industry
	Pete
	Seesee
	Uhuh
	Vroom           -->     check lower case
	Vuh             -->     check lower case
	Wah             -->     check lower case
	Zs

	Ampersanded words:

	&fa             -->     check for unampersanded instances
	&fuh
	&la


.. _mg-prog-commitlex:

commitlex
=========

A simple script that changes directory to the ``$CLAN/lib/english/lex`` 
directory, commits any changes to the svn repository, and returns to the 
previous working directory.


.. _mg-prog-compare:

compare.py
==========

Compares the tags of specified tiers in chat files.

The script compares a *test* tier against a *gold* standard tier. 
The tiers to be compared can be in the same file or separate files.

Usage 
-----

To compare two syntax tiers in the same file ('test.cha')::

    compare.py --test TIER --gold TIER test.cha

If comparing seperate files ('test.cha' against 'gold.cha')::

    compare.py --test TIER --gold TIER test.cha gold.cha

Note that both --test and --gold default to 'syn'::

    compare.py test.cha gold.cha

Options
-------

::

  -h, --help                show this help message and exit
  -g <TIER>, --gold=<TIER>  tier to use as gold standard
  -t <TIER>, --test=<TIER>  tier to test against gold standard
  --mismatch=<TEST> <GOLD>  print lines with specified tag mismatches
  --mismatches              print all mismatches
  --matrix                  print confusion matrix
  --labeled                 evaluate syntax tiers with dependency labels
  --unlabeled               evaluate syntax tiers without dependency labels
  --omit_single_words       exclude single word utts from evaluation


.. _mg-prog-dic:

dic
===

``dic`` is a bash script for looking up words in the CLAN lexicon.  It will 
search for the term with word boundaries on either side.  Thus searching for 
"how" will find "how", "how_come", or "know+how", but not "howl", "howitzer", 
or "shower".

The default output is in the same format as it would be in a transcript , i.e. 
*pos|word(+comp|word...)*.  Adding the ``-f`` switch shows output in the format 
of grep, i.e. *filename:word {[scat pos]([comp comp+comp])}*.

You can add the ``-p`` switch to search for parts of words.  
Thus ``dic -p how`` will find "how", "how_come", "know+how" AND "howl", 
"howitzer", and "shower".

Usage
-----

:dic how: 
    Searches lexicon for "how" with word boundaries.  Output is same as 
    in CHAT transcripts.

:dic -f how:
    Searches lexicon for "how" with word boundaries.  Output is same as 
    if grep had been used.

:dic -p how:
    Searches lexicon for any word containing the pattern "how".  
    Output is same as in CHAT transcripts.

:dic -p -f how: Alternatively, ``dic -f -p how``.
    Searches lexicon for any word containing the pattern "how".  
    Output is same as if grep had been used.


.. _mg-prog-dis:

dis
===


.. _mg-prog-fixlines:

fixlines
========


.. _mg-prog-grasper:

grasper
=======


.. _mg-prog-postal:

postal
======


.. _mg-prog-root_nv:

root_nv
=======


.. _mg-prog-synflagger:

synflagger
==========


.. _mg-prog-syntax_extract:

syntax_extract
==============


Helper programs
===============

dict
----

fixpost.pl
----------
