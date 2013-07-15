******
DevOps
******


Docs for the Development & Operations team.


.. toctree::

   issues.rst
   requests.rst


Specs
=====

Basic info for all mission-critical LDP servers and systems.


Machines
--------

.. toctree::
   :maxdepth: 1
   :glob:

   machines/*


Systems
-------

* Portal (https://ldp.spc.uchicago.edu/portal/)

* Docs (https://ldp.spc.uchicago.edu/portal/docs/)

* Database (``fmnet:/ldpdb.spc.uchicago.edu``)

* File Server (``afp://analord.spc.uchicago.edu``)

* Video Server (``smb://ldpfs.spc.uchicago.edu/``)

* Subversion Repository (``svn://joyrexus.spc.uchicago.edu/ldp``)


Guides
======

How to ...

* setup a ``launchd`` job on Snow Leopard

* setup an ``rsync`` mirror


.. toctree::
   :hidden:
   :glob:

   guides/*
