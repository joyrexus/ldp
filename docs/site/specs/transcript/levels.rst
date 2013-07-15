.. _levels:

2. Annotation Levels
=====================

.. _levels-description:

While the original transcript format has been useful for general studies of the
interaction between speech and gesture, it has been necessary to augment them
with additional levels of annotation for more fine-grained studies of specific
aspects of child language use.  The original format, then, acts as a base upon 
which all other LDP annotation levels depend.

2.1. Overview of Levels
-----------------------

There are currently four annotation levels:

:ref:`base-level`
   The aforementioned, original transcript layout.  Records speech, roughly 
   categorizes gestures, and provides information about environmental
   conditions.

:ref:`seyda-level`
   Further classifies gestures according to type and meaning and provides 
   information regarding the relationship between speech and gestures.

:ref:`morpho-syntax-level`
   Provides CHAT formatted transcription of speech and counts and
   categorizations of morpho-syntactic structures used by the speaker.  It is
   referred to as a supplement as it is typically integrated with 
   :ref:`Erica Cartmill's Second Tier Gesture Annotation <erica-level>`

:ref:`erica-level`
   Builds upon 
   :ref:`Şeyda Özçalışkan's Second Tier Gesture Annotation <seyda-level>` and 
   the :ref:`Morpho-Syntactic Analysis Supplement <morpho-syntax-level>` to 
   permit detailed analysis of the relationship between gesture types and 
   concurrent speech.

.. _base-level:

2.2. Base Transcript
--------------------

2.2.1. Goals
^^^^^^^^^^^^

Explain general goals for this annotation level

2.2.2. Columns
^^^^^^^^^^^^^^

=====================  ========  =======
    Name               Position  Speaker  
=====================  ========  =======
:ref:`time-c-column`       1     N/A     
:ref:`line-column`         2     N/A     
:ref:`key-column`          3     N/A     
:ref:`utts-column`         4     Parent  
:ref:`form-column`         5     Parent  
:ref:`lrb-column`          6     Parent  
:ref:`obj-column`          7     Parent  
:ref:`gloss-column`        8     Parent  
:ref:`orient-column`       9     Parent  
:ref:`mspd-column`        10     Parent  
:ref:`utts-column`        11     Child   
:ref:`form-column`        12     Child   
:ref:`lrb-column`         13     Child   
:ref:`obj-column`         14     Child   
:ref:`gloss-column`       15     Child   
:ref:`orient-column`      16     Child   
:ref:`mspd-column`        17     Child   
:ref:`context-column`     18     N/A     
=====================  ========  =======


.. _seyda-level:

2.3. Şeyda Özçalışkan's Second Tier Gesture Annotation
------------------------------------------------------

2.3.1. Goals
^^^^^^^^^^^^

Description of goals of this annotation level

2.3.2. Columns
^^^^^^^^^^^^^^

=====================  ========  =======
    Name               Position  Speaker  
=====================  ========  =======
:ref:`time-c-column`       1     N/A     
:ref:`line-column`         2     N/A     
:ref:`key-column`          3     N/A     
:ref:`utts-column`         4     Parent  
:ref:`form-column`         5     Parent  
:ref:`lrb-column`          6     Parent  
:ref:`obj-column`          7     Parent  
:ref:`gloss-column`        8     Parent  
:ref:`orient-column`       9     Parent  
:ref:`mspd-column`        10     Parent  
:ref:`gtype-column`       11     Parent  
:ref:`gsrel-column`       12     Parent  
:ref:`utts-column`        13     Child   
:ref:`form-column`        14     Child   
:ref:`lrb-column`         15     Child   
:ref:`obj-column`         16     Child   
:ref:`gloss-column`       17     Child   
:ref:`orient-column`      18     Child   
:ref:`mspd-column`        19     Child   
:ref:`gtype-column`       20     Child   
:ref:`gsrel-column`       21     Child   
:ref:`context-column`     22     N/A     
=====================  ========  =======


.. _morpho-syntax-level:

2.4. Morpho-Syntactic Analysis Supplement
-----------------------------------------

2.4.1. Goals
^^^^^^^^^^^^

Provide morphological and syntactic analyses of utterances

2.4.2. Columns
^^^^^^^^^^^^^^

======================  ========  =======
         Name           Position  Speaker  
======================  ========  =======
:ref:`time-c-column`        1     N/A     
:ref:`line-column`          2     N/A     
:ref:`key-column`           3     N/A     
:ref:`utts-column`          4     Parent  
:ref:`chat-column`          5     Parent  
:ref:`enum-column`          6     Parent  
:ref:`mor-column`           7     Parent  
:ref:`syn-column`           8     Parent  
:ref:`clauses-column`       9     Parent  
:ref:`np-column`           10     Parent  
:ref:`pp-column`           11     Parent  
:ref:`dpp-column`          12     Parent  
:ref:`wpu-column`          13     Parent  
:ref:`passives-column`     14     Parent  
:ref:`syntype-column`      15     Parent  
:ref:`form-column`         16     Parent  
:ref:`lrb-column`          17     Parent  
:ref:`obj-column`          18     Parent  
:ref:`gloss-column`        19     Parent  
:ref:`orient-column`       20     Parent  
:ref:`mspd-column`         21     Parent  
:ref:`utts-column`         22     Child   
:ref:`chat-column`         23     Child   
:ref:`enum-column`         24     Child   
:ref:`mor-column`          25     Child   
:ref:`syn-column`          26     Child   
:ref:`clauses-column`      27     Child   
:ref:`np-column`           28     Child   
:ref:`pp-column`           29     Child   
:ref:`dpp-column`          30     Child   
:ref:`wpu-column`          31     Child   
:ref:`passives-column`     32     Child   
:ref:`syntype-column`      33     Child   
:ref:`form-column`         34     Child   
:ref:`lrb-column`          35     Child   
:ref:`obj-column`          36     Child   
:ref:`gloss-column`        37     Child   
:ref:`orient-column`       38     Child   
:ref:`mspd-column`         39     Child   
:ref:`context-column`      40     N/A     
======================  ========  =======


.. _erica-level:

2.5. Erica Cartmill's Second Tier Gesture Annotation
----------------------------------------------------

2.5.1. Goals
^^^^^^^^^^^^

What are the goals of this annotation level?

2.5.2. Columns
^^^^^^^^^^^^^^

======================  ========  =======
         Name           Position  Speaker  
======================  ========  =======
:ref:`time-c-column`        1     N/A     
:ref:`line-column`          2     N/A     
:ref:`key-column`           3     N/A     
:ref:`utts-column`          4     Parent  
:ref:`chat-column`          5     Parent  
:ref:`enum-column`          6     Parent  
:ref:`mor-column`           7     Parent  
:ref:`syn-column`           8     Parent  
:ref:`clauses-column`       9     Parent  
:ref:`np-column`           10     Parent  
:ref:`pp-column`           11     Parent  
:ref:`dpp-column`          12     Parent  
:ref:`wpu-column`          13     Parent  
:ref:`passives-column`     14     Parent  
:ref:`syntype-column`      15     Parent  
:ref:`form-column`         16     Parent  
:ref:`lrb-column`          17     Parent  
:ref:`obj-column`          18     Parent  
:ref:`gloss-column`        19     Parent  
:ref:`orient-column`       20     Parent  
:ref:`mspd-column`         21     Parent
:ref:`gtype-column`        22     Parent 
:ref:`gsrel-column`        23     Parent 
:ref:`time-g-column`       24     Parent 
:ref:`timegen-column`      25     Parent 
:ref:`word-column`         26     Parent 
:ref:`wordnum-column`      27     Parent 
:ref:`semrole-column`      28     Parent 
:ref:`presref-column`      29     Parent 
:ref:`reinf-column`        30     Parent 
:ref:`added-column`        31     Parent 
:ref:`persp-column`        32     Parent 
:ref:`utts-column`         33     Child   
:ref:`chat-column`         34     Child   
:ref:`enum-column`         35     Child   
:ref:`mor-column`          36     Child   
:ref:`syn-column`          37     Child   
:ref:`clauses-column`      38     Child   
:ref:`np-column`           39     Child   
:ref:`pp-column`           40     Child   
:ref:`dpp-column`          41     Child   
:ref:`wpu-column`          42     Child   
:ref:`passives-column`     43     Child   
:ref:`syntype-column`      44     Child   
:ref:`form-column`         45     Child   
:ref:`lrb-column`          46     Child   
:ref:`obj-column`          47     Child   
:ref:`gloss-column`        48     Child   
:ref:`orient-column`       49     Child   
:ref:`mspd-column`         50     Child   
:ref:`gtype-column`        51     Child   
:ref:`gsrel-column`        52     Child   
:ref:`time-g-column`       53     Child 
:ref:`timegen-column`      54     Child 
:ref:`word-column`         55     Child 
:ref:`wordnum-column`      56     Child 
:ref:`semrole-column`      57     Child 
:ref:`presref-column`      58     Child 
:ref:`reinf-column`        59     Child 
:ref:`added-column`        60     Child 
:ref:`persp-column`        61     Child 
:ref:`context-column`      62     N/A     
======================  ========  =======


Description of what's going on here
