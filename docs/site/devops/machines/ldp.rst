******************
ldp (web services)
******************


Overview
========

This machine hosts the both the Project's `public-facing website`_ and our `internal portal site`_ (a Pylons-based web app). It's also running the Postgres_ database backing the portal.

.. _public-facing website: https://ldp.spc.uchicago.edu/

.. _internal portal site: https://ldp.spc.uchicago.edu/portal/ 


Specs
=====

:hardware: Mac Mini
:ram: 4 GB
:os: Snow Leopard (10.6.6)
:dns: ``ldp.spc.uchicago.edu``
:ip: 128.135.189.218 
:location: Green 512
:services: web app hosting, postgres database server


Config
======

The production environment is located in ``~/virtualenvs/production``.

Top-level contents::

    bin/                (binaries and scripts)
    build/
    data/
        images/
        sessions/
        templates/
    docs/               (doc site contents)
    include/            (link to Python lib)
    initial_data/       (csv data files for postgres db)
    lib/
    production.ini      (Pylons config file)
    server-scripts/     (scripts for syncing files, etc.)
    src/                (source files)
    wsgi-scripts/


Our ``launchd`` ``*.plist`` files can be found in ``\Library\LaunchDaemons``. (See `Cron Jobs`_ for overview.)

The log file for the doc site update script (``~/virtualenvs/production/server-scripts/sync-docs``) is in ``/var/log/ldpsite/docs.log``.


Server Scripts
==============



Cron Jobs
=========

Some of the scripts in ``~/virtualenvs/production/server-scripts/*`` are triggered by ``launchd`` at specified times. See the ``*.plist`` files 
in ``/Library/LaunchDaemons`` or try ``sudo launchctl list | grep ldp`` to see a list of LDP-related jobs.


Postgres
========

To access the postgres database use ``psql -U postgres ldp``.

Use ``\d`` to see the overall schema or ``\d TABLE`` where "TABLE" is
the name of one of the tables (e.g. ``\d samples``)

To see the list of user defined data types use ``\dT`` (or ``\dT+`` to see the
data type definitions).

To dump a set of rows from a table use the following sequence::

    \f ','          (set separator to comma)
    \a              (toggle alignment)
    \t              (toggle tuples/rows only) 
    \o out.csv      (dump to "out.csv")
    select ...      (your select statement)
    \o
    \q 


Log
===

A log of significant changes made to the system.

For example ...

01-31-2011 
----------

Added ``server-scripts`` dir to production environment. This currently contains
a script, ``sync-docs``, for updating the documentation site. (See comments in
source file for implementation details.)

Also added ``com.ldp.sync-docs.plist`` to ``/Libary/LaunchDaemons`` and loaded 
this job using ``launchctl``. This will run the ``sync-doc`` script at 3 AM
nightly.

