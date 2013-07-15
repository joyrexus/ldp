LDP Resources
=============

*A list of LDP-related resources.*


## Overview

The Language Development Project provides two public facing web sites:

* [Main Site](https://ldp.uchicago.edu/)

* [Doc Site](http://joyrexus.spc.uchicago.edu/ldp/docs/)

The [Psych Dept website](http://psychology.uchicago.edu/people/faculty/levine/language.shtml) also provides an overview of the project and a list of personnel.

In addition to these sites, the [LDP web portal](https://ldp.uchicago.edu/portal/) is a password protected site used for internal admistration and workflow tracking.

For an overview of the LDP's main resources for research and how to access them, see [this gist](https://gist.github.com/joyrexus/97371bcb93ab7b7a5958).


## Servers

* `joyrexus.spc.uchicago.edu` - svn server with LDP doc site mirror
* `analord.spc.uchicago.edu` - shared file server with all LDP transcripts

* `ldp.uchicago.edu` - LDP web server
* `ldpdb.spc.uchicago.edu` - filemaker database server
* `ldpfs.spc.uchicago.edu` - LDP file/video server
* `ldp-backup.spc.uchicago.edu` - LDP file/video server's offsite backup

* `sgmlab.spc.uchicago.edu` - SGM file/video server
* `sgmlab-offsite.spc.uchicago.edu` - SGM file/video server offsite backup

The Language Development Project has a number of servers with project-related resources accessible via one or more of the following network protocols: Secure Shell (`ssh`), Samba (`smb`), Screen Sharing (`vnc`), or Apple File Protocol (`afp`).


#### Samba Shares

* [ccp / cronus](smb://ccp.uchicago.edu/ldp) - [SSCS-supported box](http://sscs.uchicago.edu/page/who-we-support#server) on which we have space.
* [ldpdb](smb://ldpdb.spc.uchicago.edu) - filemaker database server
* [ldpfs](smb://ldpfs.spc.uchicago.edu) - video server


#### Screen Sharing

* [ldpdb](vnc://ldpdb.spc.uchicago.edu) - filemaker database server
* [analord](vnc://analord.spc.uchicago.edu) - shared file server


#### Apple File Protocol

* [joy](afp://joy.uchicago.edu) - sandbox system
* [analord](afp://analord.spc.uchicago.edu) - shared file server
