.. _lrb-column:

3.17. LRB - Place of Gesture Articulation
=========================================

.. _lrb-column-description:

3.17.1. Description
-------------------

Specifies the appendage(s) used to perform the gesture


.. _lrb-column-format:

3.17.2. Format
--------------

.. productionlist::
   entry: (`null` | `code`) [`op` (`null` | `code`)]*
   null: ""
   code: "L" | "R" | "B" | "H" | "LF" | "RF" | "W"
   op: "+" | "-" | "/" | "."


.. _lrb-column-values:

3.17.3. Values
--------------

Codes have the following interpretations:

======  ==========
 Code   Meaning   
======  ==========
``L``   Left hand
``R``   Right hand
``B``   Both hands
``H``   Head
``LF``  Left foot
``RF``  Right foot
``W``   Whole body
======  ==========

Ops have the following interpretations:

=====  ================================================================
Op     Meaning                                                           
=====  ================================================================
``+``  Simultaneous gestures
``-``  Sequential gestures without return to neutral position
``/``  Gestures morph into one another
``.``  Sequential gestures with return to neutral position - DEPRECATED
=====  ================================================================


.. _lrb-column-vert-dep:

3.17.4. Vertical Dependencies
-----------------------------

:ref:`See note on continued gestures below <lrb-column-horz-dep-continued-note>`


.. _lrb-column-horz-dep:

3.17.5. Horizontal Dependencies
-------------------------------

LRB is dependent on the :ref:`Form Column<form-column-dep-by>`.

LRB must have the same number of codes and the same number and type of
ops as the Form entry on which it depends.

The codes allowed in a given position in LRB are determined by the 
code in the corresponding position in Form:

===================  =  =  =  ==  ==  =  ==
Form code            L  R  B  LF  RF  H  WB 
===================  =  =  =  ==  ==  =  ==
``$``                                     

``cont palm``        X  X  X                
``cont point``       X  X  X  X   X         
``drag``             X  X  X  X   X         
``hold``             X  X  X  X   X         
``palm``             X  X  X                
``point``            X  X  X  X   X   X     
                                                    
``beat``             X  X  X  X   X   X     
``come``             X  X  X  X   X   X  X  
``dismiss``          X  X  X  X   X         
``flip``             X  X  X                
``got it``           X  X  X                
``listing``          X  X  X                
``naughties``        X  X  X  X   X         
``nod``              X  X             X     
``number``           X  X  X                
``oh my``            X  X  X                
``pick me``          X  X  X                
``pick up``          X  X  X  X   X         
``shh``              X  X  X  X   X         
``shrug``            X  X  X                
``shrug with flip``  X  X  X                
``shake``            X  X             X     
``sweep``            X  X  X                
``tada``             X  X  X                
``thinking``         X  X  X                
``wait``             X  X  X  X   X         
``wave``             X  X  X  X   X         
``x``                X  X  X  X   X   X  X  
``<aha>``            X  X  X                
``<back off>``       X  X  X                
``<darn it>``        X  X  X                
``<hero fist>``      X  X  X                
``<oh man>``         X  X  X                
``<pray you>``       X  X  X                
``<thumbs up>``      X  X  X                
``<whew>``           X  X  X                

``demo``             X  X  X  X   X   X  X  
``iconic``           X  X  X  X   X   X  X  
``metaphoric``       X  X  X  X   X   X  X  

``sign``             X  X  X                
===================  =  =  =  ==  ==  =  ==

.. _lrb-column-horz-dep-continued-note:

.. note::

   If the code in Form is :term:`continued` (ending with ``~``), the
   corresponding code in LRB must be the same as the LRB code associated with
   the Form code being continued on the immediately preceding line with a 
   communicative act on the part of the speaker.

   Example::

      Line 1: 
        Form: point + hold
        LRB: R + L
      Line 2:
        Form: point~
        LRB: R


.. _lrb-column-dep-by:

3.17.6. Depended Upon By
------------------------

    None
