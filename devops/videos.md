# Visit Videos

LDP visit videos can be accessed  ...

[ ... ]

I would recommend copying any new videos over to the RCC servers.  You can transfer them via SAMBA the same way you've been copying them to the ldpfs server.

Use the following address to connect:

    smb://midwaysmb.rcc.uchicago.edu/project/sgsg

This is SGM's project directory.

The only caveat is that when logging in you need to use "ADLOCAL\" before your username

So, you'd use "ADLOCAL\reihonna" as your username and then enter your regular cnet password.

As for the directory layout ...

Place "home" visit videos in `ldp/videos/visits/period-1`.

Place "literacy" visit videos in `ldp/videos/visits/period-2`.

Place the "later school" visit videos in `ldp/videos/visits/period-3`.

The new layout is described in the various README files you'll see once connected.
