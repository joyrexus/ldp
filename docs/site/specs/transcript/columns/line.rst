.. _line-column:

3.2. Line - Line Number
=======================


.. _line-column-description:

3.2.1. Description
------------------

Indicates the line number in the transcript


.. _line-column-format:

3.2.2. Format
-------------

.. productionlist::
   entry: `base_number` | `annotation_number`
   base_number: <An integer value between 1 and N, where N is the number of lines>
   annotation_number: <A decimal value between 0 and N+1, where N is the number of lines>


.. _line-column-values:

3.2.3. Values
-------------

Any non-zero integer or decimal with at most one digit to the right of the
decimal


.. _line-column-vert-dep:

3.2.4. Vertical Dependencies
----------------------------

Must be greater than the previously recorded :ref:`Line <line-column>` value by
no more than 1.


.. _line-column-horz-dep:

3.2.5. Horizontal Dependencies
------------------------------

None


.. _line-column-dep-by:

3.2.6. Depended Upon By
-----------------------

None
