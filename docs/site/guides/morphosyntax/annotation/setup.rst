.. _mg-setup:

*****
Setup
*****

Before you can start coding syntax, you must set up the necessary tools on your computer.  This section will explain how to download and install the CLAN software and how to set up an SVN repository for accessing and submitting new transcripts.

.. seealso::

	Before you begin, you may want to check out these guides to using the command line and the VI text editor.

	`UNIX/LINUX Tutorial for Beginners <http://www.ee.surrey.ac.uk/Teaching/Unix/index.html>`_
		A very good introduction to basic UNIX commands.  Tutorials One through Four are especially useful.
	`VI for Smarties <http://www.jerrywang.net/vi/>`_
		A short and simple tutorial on the basics of using the VI text editor.
	`Mastering the VI Editor <http://www.eng.hawaii.edu/Tutor/vi.html>`_
		A longer, more detailed tutorial on the VI text editor.


.. _mg-setup-1:

Xcode
=====

The first step in setting up a workspace is making sure that your computer is equipped with the tools to install all of the applications.  On computers running Mac OS X, that means having Xcode tools installed.  To test this, open the Terminal application and type::

	make --help

If a long message pops up showing a lot of different options, you have developer tools installed and are good to go.  You can skip ahead to :ref:`Installing CLAN software <mg-setup-2>`.

If instead you get a message saying::

	make: command not found

you will need to install Xcode Tools.

.. _mg-setup-1-1:

Installing Xcode Tools on Mac OS X
----------------------------------

Installing Xcode Tools is an easy process, though it may take a long time.

	#. Acquire a copy of the **Mac OS X Install Disc 2** and insert it into the computer.
		* Check the drawers of your desk for a copy.  If you can't find it there, ask Jason for a copy.
	#. Double-click the **Xcode Tools** folder and then the **Xcode Tools.mpkg** icon.
	#. Follow the instructions for installing Xcode tools.

Now just wait for it to finish installing.  It has a lot to install, so this could take a long, long time.


.. _mg-setup-5:

Subversion
==========

We're using Apache Subversion_ system for sharing code and files. This enables
everyone to be working from the same set of files.

How does this work? Well, we've put the essential code and files for doing
morphosyntactic analysis in a central **morphosyntax** repository (or "repo").
Anyone doing morphosyntactic analysis can then "check out" a copy of the repo
to work with on their machine. If they make any changes to the files or code,
they can then "commit" their local changes to the central repository so that
everyone else can then "update" their own local working copies to get the
changes. As a result, everyone is on the same page.

We also work with a **data** repo, which is used by many other groups in the
LDP, as well as its accompanying **code** repo.

The following steps outline how to check out a copy of the three repositories
for local use.

.. _Subversion: http://en.wikipedia.org/wiki/Apache_Subversion

.. _mg-setup-5-1:

Creating directory for repos
----------------------------

It is convenient to have all of the repositories you'll be using located in one
directory.  The one we'll use in this guide is *~/ldp* (where *~* is your user
directory).  To create this directory:

    #. Open the Terminal.  You should start in your user directory.
    #. Type ``ls ldp`` and hit Enter.
        * If the terminal says ``ls: cannot access ldp: No such file or directory``, proceed with the next step.
        * If you get a listing including *morphosyntax*, *data*, and *code*, the repositories are already installed in this location.  You may either skip the repository setup or set the repos up in a different directory.
        * If you get a listing that does not include those names, the directory *ldp* already exists, but the repos are not checked out.  You may skip to :ref:`checking out the morphosyntax repo <mg-setup-5-2>`, or create a new directory in which to set up the repos.
    #. To create a new *ldp* directory, type ``mkdir ldp``.
    #. Navigate to the newly created folder by typing ``cd ldp`` and proceed to :ref:`checking out the morphosyntax repo <mg-setup-5-2>`.

.. _mg-setup-5-2:

Checking out the morphosyntax repo
----------------------------------

	#. In the Terminal, navigate to the folder where you want to check out the repos (the default for this guide is *~/ldp*).
	#. Type ``find morphosyntax`` and hit Enter.
		* If the terminal says "No such file or directory", proceed with the next step.
		* If you get a long list of things, you already have the repository installed in this location.  You may either skip the repository setup, or install it in a different directory.
	#. Check out the morphosyntax repository by typing::

		svn checkout svn://joyrexus.spc.uchicago.edu/morphosyntax morphosyntax

	#. You now have the morphosyntax repository!  You'll notice a lot of file names popping up on your screen.  Those are all of the files that are under version control in the **morphosyntax** svn repository.  For more on the structure of this repository ADD STRUCTURE DOCUMENTATION

.. todo:

	Max, add some documentation for svn repository structure


.. note::

	If you are prompted for a username and password but you don't know if you have them or have forgotten what they are, contact Jason and he can set up an account for you.

.. _mg-setup-5-3:

Checking out the data repo
--------------------------

	#. In the Terminal, navigate to the folder where you want to check out the repos (the default for this guide is *~/ldp*).
	#. Type ``find data`` and hit Enter
		* If the terminal says "No such file or directory", proceed with the next step.
		* If you get a long list of things, you already have the repository installed in this location.  You may either skip the repository setup, or install it in a different directory.
	#. Check out the data repository by typing::

		svn checkout svn://joyrexus.spc.uchicago.edu/data/trunk data

	#. You now have the data repository!  You'll notice a lot of file names popping up on your screen.  Those are all of the files that are under version control in the **data** svn repository.  For more on the structure of this repository ADD STRUCTURE DOCUMENTATION

.. _mg-setup-5-4:

Checking out the code repo
--------------------------

	#. In the Terminal, navigate to the folder where you want to check out the repos (the default for this guide is *~/ldp*).
	#. Type ``find code`` and hit Enter
		* If the terminal says "No such file or directory", proceed with the next step.
		* If you get a long list of things, you already have the repository installed in this location.  You may either skip the repository setup, or install it in a different directory.
	#. Check out the code repository by typing::

		svn checkout svn://joyrexus.spc.uchicago.edu/code/trunk code

	#. You now have the code repository!  You'll notice a lot of file names popping up on your screen.  Those are all of the files that are under version control in the **code** svn repository.  For more on the structure of this repository ADD STRUCTURE DOCUMENTATION

.. _mg-setup-5-5:

Final steps for setting up repos
--------------------------------

You now have the repositories checked out, but there are still a few things you'll need to do to ensure that everything that relies on the repos is working properly.

    * When you :ref:`set up your .bash_profile <mg-setup-3>`, ensure that all environment variables are pointing to the right place.  If your repos have a different name than those in the above directions, or if you set them up in a directory other than *~/ldp*, you may have to reflect those differences in your .bash_profile.
	* In order to use the programs in the **code** repo, ensure that "$CODE/bin" is included in the PATH variable in your .bash_profile, where $CODE points to wherever you checked out the **code** repo.

.. _mg-setup-2:

CLAN
====

When you have developer tools installed and the svn repository checked out, you can then install the CLAN software, which uses the CHAT transcription format.  It will be helpful to install both the Graphical User Interface (GUI) and the command line tools.

.. _mg-setup-2-1:

.. _CLAN: http://childes.psy.cmu.edu/clan

Installing the GUI
------------------

The following steps outline how to download and install the CLAN GUI:

#. Go to the CLAN_ website.

#. Download CLAN for Mac.

#. If the installler does not open automatically, find the downloaded file and open it.

#. Follow the instructions on screen to complete the installation.

Once it is installed, you can use the application to open CHAT files.

.. _mg-setup-2-2:

Installing the command line tools
---------------------------------

Most of the work we do with CLAN software is done from the command line.  This setup process is a little more complicated, but you will only have to do it once.

#. Download the unix CLAN files from the CLAN_ website.

#. Move the zip file to your user directory (for example, ``/Users/maxmasich``).

#. Unpack the file by double-clicking it.  This should create a new 
   directory ``/Users/maxmasich/unix-clan``.

#. You now have to make some changes before installing.  Open the Terminal 
   and navigate to ``~/unix-clan/src`` (where ``~`` stands for your user directory).  
   Do this by typing::

    cd unix-clan/src

#. Open the *common.h* file by typing::

    vi common.h

#. Search for the following::

    #ifndef DEPDIR
        #if defined(CLAN_SRV)
            #define DEPDIR  "/web/childes/webclan/lib/"
        #else
            #define DEPDIR  "../lib/"
        #endif


#. Replace ``"/web/childes/webclan/lib/"``  and ``"../lib/"`` with 
   ``"/Users/USERNAME/ldp/morphosyntax/clan/lib/"``, 
   
   * *USERNAME* should reflect your user name on the computer.  

   * If you set up your morphosyntax repository somewhere else, 
     you'll have to reflect that change here.  It should look like::

		#ifndef DEPDIR
			#if defined(CLAN_SRV)
				#define DEPDIR  "/Users/maxmasich/ldp/morphosyntax/clan/lib/"
			#else
				#define DEPDIR  "/Users/maxmasich/ldp/morphosyntax/clan/lib/"
			#endif

#. Compile the command line tools by typing ``make``.

#. Move the tools to your morphosyntactic coding directory.

   * Move up one level in the directory hierarchy::

        $ cd ../unix				            
    
   * You should now be in ``~/unix-clan/unix``.

   * Copy the ``bin`` directory to your new morphosyntax directory::

        $ cp -r bin ~/ldp/morphosyntax/clan/		
    
   * Again, if you installed the repository somewhere else, reflect that change 
     here.  Otherwise, be sure you copy this command *exactly* as it is here.

#. To use these tools more easily, you will have to specify where they are in 
   your computer's ``$PATH`` variable, which is done by 
   :ref:`editing the .bash_profile file <mg-setup-3>`.


.. _mg-setup-3:

Edit your profile
=================

When you have all of the CLAN tools installed, you will have to create a ``.bash_profile`` file in your home directory.  If this file already exists, you may have to make some changes to it.

1. Download this :download:`.bash_profile template <_static/bash_profile_template>` to your home directory (for example, */Users/maxmasich*)

2. If you checked out the repos to a location other than what was specified in the :ref:`Subversion <mg-setup-5>` section, edit the downloaded file to reflect those differences (for example, if you checked out the repos in *~/coding* instead of *~/ldp*, change the line ``export LDP=$HOME/ldp`` to ``export LDP=$HOME/coding``.

3. Navigate to your home directory (you should be there automatically when you open the Terminal).
   
4. See if you already have a *.bash_profile* in your home directory by typing::

    find .bash_profile

You will see one of two things printed to the screen::

    .bash_profile		
						// This output means you already have a .bash_profile file

    find: .bash_profile: No such file or directory
						// This output means that there is no .bash_profile file

5. If you do not have a *.bash_profile* file, simply change the name of the downloaded *bash_profile_template.txt* to *.bash_profile* and finalize the changes by typing::

    mv bash_profile_template.txt .bash_profile
    source .bash_profile

You are now ready to set up the :ref:`morphosyntax repository <mg-setup-5>`.

6. If there is already a copy of *.bash_profile* in your home directory, make sure that each of the lines in the *bash_profile_template* is found in the current *.bash_profile*.  If any lines are missing, copy and paste them into your *.bash_profile*.  
   
7. Finalize the changes by typing on the command line::

    source .bash_profile


.. _mg-setup-4:

Edit ``vimrc``
==============

To make the process of correcting the syntax output faster, you will need to set up a file which contains shortcuts for the VI text editor.

#. Download the :download:`vimrc.txt file <_static/vimrc>` to your home directory.

#. Change the name of the file from *vimrc.txt* to *.vimrc* by typing::

    mv vimrc.txt .vimrc

You will now have many useful shortcuts when correcting syntax and part-of-speech information in VI.

.. seealso::

    The :ref:`VI Shortcuts <mg-shortcuts>` section for shortcuts you can use 
    when correcting syntax in VI.


After you have completed each of these steps, you're ready to start coding syntax!
