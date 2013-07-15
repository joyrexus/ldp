.. _mg-shortcuts:

************
VI Shortcuts
************

Coding syntax can be quite a strain on your hands when you are constantly entering and exiting insert mode and typing out long parts-of-speech and GRs.  The following shortcuts in VI will save you a lot of time and effort.

.. _mg-shortcuts-general:

General use shortcuts
=====================

There are various shortcuts that will help you navigate a transcript, find and count flags, and complete other common tasks:

+-----------------+----------------------------------+
| Key Combination | What it is used for              |
+=================+==================================+
| e               | Move the page down               |
+-----------------+----------------------------------+
| E               | Move the page up                 |
+-----------------+----------------------------------+
| w               | Move to the beginning of         |
|                 | the next word                    |
+-----------------+----------------------------------+
| b               | Move to the beginning of         |
|                 | the previous word                |
+-----------------+----------------------------------+
| 0               | Move to the beginning            |
|                 | of a line                        |
+-----------------+----------------------------------+
| \-              | Move to the end of a line        |
+-----------------+----------------------------------+
| mct             | Count the number of              |
|                 | utterances with flags (press     |
|                 | **n** for next flagged           |
|                 | utterance)                       |
+-----------------+----------------------------------+
| ==              | Find the next flag               |
+-----------------+----------------------------------+
| \`c             | Affix *&* to the beginning       |
|                 | of all instances of *oh*,        |
|                 | *uh*, *um*, *ooh*, and *ah*      |
+-----------------+----------------------------------+
| \`m             | Finds non-capitalized instances  |
|                 | of common familial proper nouns  |
|                 | and capitalizes them if they're  |
|                 | not preceded by a determiner     |
+-----------------+----------------------------------+
| \`d             | Finds capitalized instances of   |
|                 | common familial proper nouns and |
|                 | lower-cases them if they are     |
|                 | preceded by a determiner         |
+-----------------+----------------------------------+
| \`v             | Finds common formatting errors   |
|                 | that require closer inspection   |
+-----------------+----------------------------------+
| mw              | Save the file you are            |
|                 | working on                       |
+-----------------+----------------------------------+

.. _mg-shortcuts-gr:

Changing GR information
=======================

While in command mode in vi, move the cursor to any part of the GR that needs to be changed and use the following shortcuts to change the GR:

+-----------------+------------------------+
| Key Combination | Change GR to           |
+=================+========================+
| ma              | AUX                    |
+-----------------+------------------------+
| mf              | COORD                  |
+-----------------+------------------------+
| mz              | CPZR                   |
+-----------------+------------------------+
| md              | DET                    |
+-----------------+------------------------+
| mu              | ENUM                   |
+-----------------+------------------------+
| mi              | INF                    |
+-----------------+------------------------+
| mj              | JCT                    |
+-----------------+------------------------+
| ml              | LOC                    |
+-----------------+------------------------+
| mm              | MOD                    |
+-----------------+------------------------+
| mo              | OBJ                    |
+-----------------+------------------------+
| m2              | OBJ2                   |
+-----------------+------------------------+
| mb              | POBJ                   |
+-----------------+------------------------+
| me              | PRED                   |
+-----------------+------------------------+
| mp              | PTL                    |
+-----------------+------------------------+
| mq              | QUANT                  |
+-----------------+------------------------+
| mt              | SRL                    |
+-----------------+------------------------+
| ms              | SUBJ                   |
+-----------------+------------------------+
| mg              | TAG                    |
+-----------------+------------------------+
| mv              | VOC                    |
+-----------------+------------------------+


+-----------------+------------------------+
| Key Combination | Change GR to           |
+=================+========================+
| mcj             | CJCT                   |
+-----------------+------------------------+
| mcm             | CMOD                   |
+-----------------+------------------------+
| mcc             | COM                    |
+-----------------+------------------------+
| mco             | COMP                   |
+-----------------+------------------------+
| mce             | CPRED                  |
+-----------------+------------------------+
| mcs             | CSUBJ                  |
+-----------------+------------------------+
| mcn             | NEG                    |
+-----------------+------------------------+


+-----------------+------------------------+
| Key Combination | Change GR to           |
+=================+========================+
| mxo             | XCOMP                  |
+-----------------+------------------------+
| mxj             | XJCT                   |
+-----------------+------------------------+
| mxm             | XMOD                   |
+-----------------+------------------------+
| mxe             | XPRED                  |
+-----------------+------------------------+
| mxs             | XSUBJ                  |
+-----------------+------------------------+


+-----------------+------------------------+
| Key Combination | Change GR to           |
+=================+========================+
| mkaj            | AUX-CJCT               |
+-----------------+------------------------+
| mkam            | AUX-CMOD               |
+-----------------+------------------------+
| mkac            | AUX-COMP               |
+-----------------+------------------------+
| mkdo            | DET-OBJ                |
+-----------------+------------------------+
| mkdb            | DET-POBJ               |
+-----------------+------------------------+
| mkde            | DET-PRED               |
+-----------------+------------------------+
| mkds            | DET-SUBJ               |
+-----------------+------------------------+
| mkij            | INF-CJCT               |
+-----------------+------------------------+
| mkic            | INF-COMP               |
+-----------------+------------------------+
| mkix            | INF-XCOMP              |
+-----------------+------------------------+


The following shortcuts will change the GR and the headword number will become 0:

+-----------------+-------------------+--------------------+
| Key Combination | Change GR to      | Change headword to |
+=================+===================+====================+
| mr              | ROOT              | 0                  |
+-----------------+-------------------+--------------------+
| mkar            | AUX-ROOT          | 0                  |
+-----------------+-------------------+--------------------+
| mkir            | INF-ROOT          | 0                  |
+-----------------+-------------------+--------------------+

The following shortcuts will change the headword number:

+-----------------+--------------------+
| Key Combination | Change headword to |
+=================+====================+
| m,              | Word number of the |
|                 | ROOT               |
+-----------------+--------------------+
| m;              | 6                  |
+-----------------+--------------------+
| m.              | Decreases by 1     |
+-----------------+--------------------+
| m/              | Increases by 1     |
+-----------------+--------------------+

.. _mg-shortcuts-pos:

Changing part-of-speech information
===================================

While in command mode in vi, move the cursor to any part of the word you would like to change the part-of-speech of and use the following shortcuts to change the part-of-speech (alternative part-of-speech for select words in parentheses):

+-----------------+--------------------------+
| Key Combination | Change part-of-speech to |
+=================+==========================+
| caj             | adj                      |
+-----------------+--------------------------+
| cav             | adv                      |
+-----------------+--------------------------+
| ci              | adv:int (**to**: inf)    |
+-----------------+--------------------------+
| cv              | adv:loc (**\*day**,      |
|                 | **\*night**, **\*time**, |
|                 | **\*ever**, **after**,   |
|                 | **tomorrow**, **then**:  |
|                 | adv:tem)                 |
+-----------------+--------------------------+
| cx              | aux                      |
+-----------------+--------------------------+
| cco             | co                       |
+-----------------+--------------------------+
| c;              | co:voc                   |
+-----------------+--------------------------+
| cs              | conj:subor               |
+-----------------+--------------------------+
| cd              | det:num (**what**,       |
|                 | **which**: det:wh;       |
|                 | **that**, **these**,     |
|                 | **those**, **another**,  |
|                 | **the**, **this**: det)  |
+-----------------+--------------------------+
| ccn             | neg                      |
+-----------------+--------------------------+
| cp              | prep (**too**: post;     |
|                 | **own**, **her**: pro)   |
+-----------------+--------------------------+
| cm              | pro:dem                  |
+-----------------+--------------------------+
| ct              | pro:exist                |
+-----------------+--------------------------+
| cr              | pro:indef (**that**,     |
|                 | **who**, **which**: rel) |
+-----------------+--------------------------+
| co              | pro:poss:det             |
+-----------------+--------------------------+
| ch              | pro:wh                   |
+-----------------+--------------------------+
| cl              | ptl                      |
+-----------------+--------------------------+
| cq              | qn                       |
+-----------------+--------------------------+

The following shortcuts will change the part-of-speech and the morphology of the word:

+-----------------+--------------------------+--------------------+
| Key Combination | Change part-of-speech to | Change suffix to   |
+=================+==========================+====================+
| cn              | n                        | PL                 |
+-----------------+--------------------------+--------------------+
| cg              | n:gerund                 | GERUND             |
+-----------------+--------------------------+--------------------+
| cf              | part                     | PERF               |
+-----------------+--------------------------+--------------------+
| cu              | part                     | PROG               |
+-----------------+--------------------------+--------------------+
| c,              | v                        | 3S                 |
+-----------------+--------------------------+--------------------+

And finally, the following miscellaneous shortcuts:

+-----------------+--------------------------+
| Key Combination | What it does             |
+=================+==========================+
| cz              | Removes ``&ZERO`` suffix |
+-----------------+--------------------------+
| ce              | Changes POS to ``quote`` |
|                 | and adds ``@q`` suffix   |
|                 | to word on speech tier   |
+-----------------+--------------------------+
