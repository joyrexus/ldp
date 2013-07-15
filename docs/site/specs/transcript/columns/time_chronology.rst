.. _time-c-column:

3.1. Time (Chronology)
======================


.. _time-c-column-description:

3.1.1. Description
------------------

Records the timestamp of the contents of the line


.. _time-c-column-format:

3.1.2. Format
-------------

.. productionlist::
   entry: `hour` ":" `minute` ":" `second`
   hour: "00".."23"
   minute: "00".."59"
   second: "00".."59"


.. _time-c-column-values:

3.1.3. Values
-------------

Any time stamp in the indicated form is allowed.  These typically range between
``00:00:00`` and ``01:30:00`` due to the size of the tape media used to record
visit data.


.. _time-c-column-vert-dep:

3.1.4. Vertical Dependencies
----------------------------

The value of a time entry must be chronologically later than the previously
recorded time (with the following :ref:`exception <time-c-column-horz-dep>`).


.. _time-c-column-horz-dep:

3.1.5. Horizontal Dependencies
------------------------------

Time is depdendent on the :ref:`Context Column <context-column-dep-by>`.

If Context contains an end of tape flag (e.g. ``END OF TAPE 1``), Time can be
less than the previously recorded Time.


.. _time-c-column-dep-by:

3.1.6. Depended Upon By
-----------------------

None
