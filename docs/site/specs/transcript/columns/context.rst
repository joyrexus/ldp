.. _context-column:

3.33. Context - Transcriber Notes
=================================

.. _context-column-description:

3.33.1. Description
-------------------

Notes on the environment or condition of the communicative act made by
transcribers to further contextualize it


.. _context-column-format:

3.33.2. Format
--------------

.. productionlist::
   entry: `note` | `end_of_flag`
   note: <Any notes about the environment or condition of the communicative act>
   end_of_flag: "END OF" (`tape` | `transcript`)
   tape: "TAPE" ("1" | "2" | "3" | "4")
   transcript: "TRANSCRIPT"

.. _context-column-values:

3.33.3. Values
--------------

When the transcriber has access to inside knowledge about a gesture or speech
act or when the events are otherwise deemed difficult to interpret, notes can
be made in this column to ease interpretation without corresponding video data.
This could include notes about a child's current toy or television obsession 
(e.g. 
``C talking about Tuvok, a Star Trek guy who's lost in space, getting home``),
a child's speech or gesture peculiarities, or the environment
making it difficult to understand what is being said (e.g. 
``the television was turned up very loud and the dogs were barking``).

The Context column is also used to identify the points at which tape breaks
occur (e.g. ``END OF TAPE 1``) and the last line of the transcript 
for machine readers with ``END OF TRANSCRIPT``.


.. _context-column-vert-dep:

3.33.4. Vertical Dependencies
-----------------------------

None


.. _context-column-horz-dep:

3.33.5. Horizontal Dependencies
-------------------------------

None


.. _context-column-dep-by:

3.33.6. Depended Upon By
------------------------

:ref:`Time (Chronology) <time-c-column-horz-dep>`
