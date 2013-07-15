.. _mg-repo:

**********
Repository
**********

The following section outlines the hierarchy of the morphosyntax repository 
that all syntax coders check out.  The repository is split up into four main 
directories: ``bin``, ``lib``, ``clan``, and ``chat``.  The first three should 
require minimal attention after the initial setup.  The final one, ``chat``, 
is where you will do most of your work.


.. _mg-repo-bin:

``bin``
=======

This directory contains all of the scripts and programs developed by people in the LDP.  These include *dis* and *caps*, used for :ref:`prepping transcripts <mg-clean>`, *dic*, *add*, and *fixlines*, used during the :ref:`annotation process <mg-steps>`, and *graspParse.py*, *synflagger*, and *syntax_extract*, used for correcting syntax transcripts and generating higher-level syntax codes.

In order to use these programs, you must have the **bin** directory specified as part of the PATH variable in your :ref:`.bash_profile <mg-setup-3>`.  After you do this, you won't need to directly access this directory, unless you are developing a new program or need to modify one of the exisiting programs.


.. _mg-repo-lib:

``lib``
=======

This directory contains all of the required modules written by people in the LDP.  These are required for many of the scripts and programs found in :ref:`the bin directory <mg-repo-bin>`.  These modules are split into two directories, **perl** and **python**, depending on the language in which they were written.  Again, unless you are writing a new program or need to modify the modules used in one of the programs, you will not need to directly access this directory.


.. _mg-repo-clan:

``clan``
========

This directory contains all of the information used by the CLAN tools that we use to automatically code the syntax of our transcripts.  When you first check out the morphosyntax repository, **clan** will contain only the directory **lib**.  However, once you :ref:`set up the CLAN tools <mg-setup-2-2>`, it will also contain another directory, **bin**, which is not under version control.


.. _mg-repo-clan-lib:

``clan/lib``
------------

This directory contains the lexical entries and rules used by the various CLAN programs we run.  You won't have to worry about most of the files in here, except in **clan/lib/english/lex**.  That directory contains the lexical entries used by *mor* and *post*, and you will frequently have to edit these files when :ref:`adding words to the lexicon <mg-steps-4-5>`.

While you will be changing files in the **clan/lib** directory, if you use the *add* and *commitlex* commands, you will not have to access the lexicon files directly by navigating to this folder.


.. _mg-repo-clan-bin:

``clan/bin``
------------

This directory contains the compiled CLAN tools developed at Carnegie Mellon University.  However, this folder is not included when you check out the morphosyntax repository, since the tools must be compiled on each machine that it is run on.

Once you :ref:`install the CLAN command line tools <mg-setup-2-2>` and :ref:`include this folder in your PATH variable <mg-setup-3>`, you will not have to directly access the files in this folder again.


.. _mg-repo-chat:

``chat``
========

This directory contains all of the transcript files that syntax coders process and code, as well as the final insert files that are passed along to the gesture coders.  These files are split into two directories, **proj_2** and **proj_3**.  Within each of these subdirectories is four more directories: **incoming**, **coders**, **final**, and **inserts**.


.. _mg-repo-chat-incoming:

``chat/incoming``
-----------------


.. _mg-repo-chat-coders:

``chat/coders``
---------------


.. _mg-repo-chat-final:

``chat/final``
--------------


.. _mg-repo-chat-inserts:

``chat/inserts``
----------------
