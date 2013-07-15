.. _repo:

**********************************
Repository/Environment Setup Guide
**********************************

*The purpose of this guide is to show you how to quickly and easily 
get your computing environment up and running by acquiring the LDP 
repositories and making a few configurations to your system.*

A version control system (VCS) is used to store and manage resource 
collections called "repositories" (or "repos" for short).

The DevOps team currently uses Subversion as our version control system. Our
Subversion server is currently serving up three repos corresponding to our 
primary resource collections: data, code, and docs.

The first part of this guide describes how to access and use these repos.

The second part of the guide discusses system configurations (e.g., setting 
shell environment variables, etc.) that may be necessary in order to ensure 
proper functioning of all components in the code and data repositories critical 
to LDP worker workflow.

.. admonition:: Code samples

    This guide makes use of a number of code samples involving shell commands being run in a terminal emulator (e.g., Apple's Terminal, etc.). These samples will generally be of the form::

        $ <command> <argument(s)>
        <output>

    In such samples, the ``$`` (dollar sign) represents a generic command prompt, which is followed by the name of some command, like ``cd``, ``mkdir``, ``ls``, etc., which is in turn followed by any arguments required by the command just entered.

    After typing the command along with any necessary arguments, and hitting return, you should see whatever output the command produces (represented here by <output>) printed to your screen.


Preliminaries
=============


Check dependencies
------------------

This guide assumes you've got a few basic tools installed on your system:

* GNU Make (``make``)
* Subversion (``svn``)
* Sqlite (``sqlite3``)
* Python (``python``)

You can check whether or not you already have these tools installed by using 
the ``which`` command from a terminal emulator (e.g., Apple's Terminal, 
usually found in ``/Applications/Utilities/`` on your hard drive)::

    $ which make
    /usr/bin/make
    $ which svn
    /usr/bin/svn
    $ which sqlite3
    /usr/bin/sqlite3
    $ which python
    /Library/Frameworks/Python.framework/Versions/2.7/bin/python

If you have all of these tools installed on your system, you should get a 
non-empty output each time you execute ``make <command>``, and each output 
should look somewhat similar to the ones shown above.

If you're running Mac OS X, these items are all included in Apple's
developer toolset, Xcode_. 

.. _Xcode: http://developer.apple.com/technologies/xcode.html


Create an LDP project directory
-------------------------------

It's handy to have all of the Project's repos stored in one place. We recommend that you 
create an ``LDP`` directory in your home directory::

    $ mkdir ~/LDP

and then enter the ``~/LDP`` directory in order to be able to checkout repositories into it::

    $ cd ~/LDP

This is where you'll be putting the code, data, and docs repositories shortly.


Repositories
============

The data repo is our central repository for project data, the code repo 
is our central repository for code used to manipulate project data, and the 
docs repo is our central repository for several types of project documentation. 

In the steps below, we'll guide you through the process of doing an initial checkout 
and show you how to build a local copy of the project's primary dataset.


Checkout
--------

If you aren't already there, navigate to your ``LDP`` directory::

    $ cd ~/LDP

Within your ``LDP`` directory, check out a copy of the transcript data from 
the data repo, a copy of the code repo, and a copy of the docs repo::

    $ svn checkout svn://joyrexus.spc.uchicago.edu/data/trunk data
    $ svn checkout svn://joyrexus.spc.uchicago.edu/code/trunk code
    $ svn checkout svn://joyrexus.spc.uchicago.edu/ldp/site/docs docs

You should see quite a bit of output after each of these ``svn checkout`` commands. 
Below is a snippet of the output that I see on my machine when freshly checking out the code 
repo, so that you might know what to expect (please note that I am checking the repo out into 
a directory called ``temp`` for the purposes of this demonstration)::

    $ svn checkout svn ://joyrexus.spc.uchicago.edu/code/trunk temp
    A    temp/lib
    A    temp/lib/python
    A    temp/lib/python/ldp
    A    temp/lib/python/ldp/data.py
    A    temp/lib/python/ldp/tests
    A    temp/lib/python/ldp/tests/data_test.py
    A    temp/lib/python/ldp/__init__.py
    
    ...

    A    temp/lib/python/datastore/__init__.py
    A    temp/lib/python/datastore/sqlite.py
    A    temp/lib/python/datastore/table.py
     Checked out revision 146.

.. admonition:: Repo access

    Upon attempting to checkout the repos, you may be denied access to some of them if your user credentials haven't been authorized for access. If this is the case, please email `Jason Voigt <mailto:jvoigt@uchicago.edu>`_ to resolve the issue.

Environment Setup
=================

Now that you have the code, data, and docs repositories checked out, and 
before you start making use of them, a few configurations need to be made.

Environment Variables
---------------------

In order for vital parts of the code and data repositories to function properly, 
your shell must have a number of *shell environment variables* defined. Shell environment 
variables are often used to simply point to certain files or directories on your machine.

Defining a shell variable is simple::

    $ FOO="/Users/stefanbehr/foo"
    $ export FOO

Let's break down that code snippet.

* ``$`` is simply the command line/shell prompt.
* ``FOO`` is the name that we've chosen for our environment variable.

  * Convention dictates that we use all uppercase letters (and numbers and underscores if needed).

* The equal sign, ``=``, tells the shell that you're setting ``FOO`` to some value. Spaces are not permitted on either side of ``=``.
* ``"/Users/stefanbehr/foo"`` is the path to a directory called ``foo`` in my home directory. Doubles quotes optional, but recommended.
* Finally, ``export FOO``, tells the shell that you want the variable to be globally available.

An equivalent, and more compact, way of writing the code snippet above is::

    $ export FOO="/Users/stefanbehr/foo"

After defining shell variables, you can *reference* them when you want to use them. For example::

    $ echo $FOO
    /Users/stefanbehr/foo

``echo`` prints its arguments to terminal output. Referencing the ``FOO`` variable is done using the ``$<variable name>`` syntax 
(not to be confused with the generic shell prompt).

~/.bash_profile (Mac OS X)
--------------------------

Now that you know how to create and use environment variables, you'll have to set up the ones you need for LDP work. 
If you're on a Mac, this can be done in your Bash profile. After opening a Terminal, execute the following::

    $ vim ~/.bash_profile

This opens the document ``.bash_profile`` in your Vim text editor. The document may already exist in your home directory, but, if it doesn't, a new one will be created.

Now that your Bash profile is open in Vim, you'll need to add some things to the end of it. First, type ``G`` to move your cursor to the end of the document. Next, type ``i`` to enter Vim's insert mode, which will allow you to enter text.

Enter the block of code below into your ``.bash_profile``. Cutting and pasting works, or you can type it in manually. Please note that any text following a ``#`` symbol in the code below is a comment, which you may modify without disrupting the effect of the code)::

    # variables pointing to LDP directory and subdirectories

    export LDP="$HOME/LDP"
    export LDP_DAT="$LDP/data"                  # data repo
    export LDP_COD="$LDP/code"                  # code repo
    export LDP_DOC="$LDP/docs"                  # docs repo
    export LDP_DB="$LDP_DAT/ldp.db"             # LDP database file
    export LDP_LIB="$LDP_COD/lib/python"        # holds vital Python modules
    export LDP_BIN="$LDP_COD/bin"               # holds important executables

    # PYTHONPATH and PATH variables for import and executable search

    export PYTHONPATH="$LDP_LIB:$PYTHONPATH"    # tells Python where importable Python code lives
    export PATH="$LDP_BIN:$PATH"                # tells the shell where to look for executables

    # useful aliases

    alias update="echo 'Update DATA repo'; svn up $LDP_DAT; echo 'Update CODE repo'; svn up $LDP_COD; echo 'Update DOCS repo'; svn up $LDP_DOC" 

After pasting this block of code into your ``.bash_profile``, hit the escape key to exit Vim's insert mode, and type ``:wq`` to write the file and quit Vim.

You can now reference any of the variables you just put into your ``.bash_profile`` by typing ``$``, followed directly by the name of the desired variable. You can also use the ``update`` alias that was created, by simply invoking it at the command line::

    $ update
    Update DATA repo
    ...
    Update CODE repo
    ...
    Update DOCS repo
    ...

LDP Database
------------

With your ``.bash_profile`` set up, you should now be able to build the LDP database in your data repository, after which your environment will be completely set up.

Simply execute the following commands at the command line, and you'll be done::

    $ cd $LDP_DAT
    $ make

Upon executing the ``make`` command, the LDP database will be built. This will probably involve a download, which might last up to several minutes (there will be a download timer shown). Once the shell prints a new prompt, you'll know that the build process is complete, and you'll be ready to go!
