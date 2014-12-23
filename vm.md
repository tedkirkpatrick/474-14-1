---
layout: course
title: Ubuntu Virtual Machine for testing assignments
---
## Why you might want to use this

### The simple but slow method

If you wish, you can run your entire project by submitting it to the
test server. This has the appeal of simplicity: All you need on your
own computer is your preferred editor and
[git](http://git-scm.com/downloads).

But this approach has the disadvantage of being slow. Every submisison
takes time, and you will wind up going through the process many times,
only to find out you have a syntax error because you mis-typed a
variable name or forgot a closing colon. Or you get a runtime error because
you mispelled the method for one of the library classes.

### Install everything: The faster method that requires lots of setup

It will be a lot faster to run short, initial tests on your own
machine, clean out the dumb errors, and only then submit to the test
server to see how well your code performs.

To run tests, on your own machine, you'll need to install on your
machine the full software stack that runs on the test server.  That
can take a lot of time, is specific to your operating system, and is
generally annoying. But if you already have all or most of the tools
installed, it could be a good approach.

### This VM: The almost-as-fast method that requires much less setup

The final approach is to download and use this virtual machine, containing
Ubuntu 13.10 Server and all the necessary packages. **This approach will
require at least 1GB free space on your disk.** You still have to do a bit
of installation (to install VirtualBox), followed by some configuration, but
it's generally less work than building the entire stack yourself.  Once you
have the VM installed, you development cycle becomes:

1. Edit your program using your standard editor on your regular operating system.
2. Test it by running it under our stack on the virtual machine.
3. Once it works, `git push submit master` from your regular operating system, to run your code on the test server.

## Setting up the virtual machine

If you decide to use the virtual machine, here's how to set it up.

### Installing the system (do once)

1. Download and install [Oracle VirtualBox](https://www.virtualbox.org/wiki/Downloads). There are versions
for the popular operating systems.

2. Download the [virtual machine](http://innovate.cs.surrey.sfu.ca/ovas/ubuntu-13.10-3GB-disk.ova)  Note that the `ubuntu-13.10-3GB-disk.ova` file is 430
MB long---you might schedule the download at a time when the network is less congested, such as the morning.

3. Import the virtual machine file `ubuntu-13.10-3GB-disk.ova` into Virtual
Box. Use the `File/Import Appliance...` menu entry. Accept all the default settings.

4. Start the virtual machine (green arrow button) and sign on. Your userid and password are both 'ubuntu'.

5. <p>Set your git id and email:</p>
<pre><code>git config --global user.name YOURNAME
git config --global user.email YOUREMAIL
</code></pre>

replacing `YOURNAME` and `YOUREMAIL` with your name and email as single-quoted strings (i.e., `'Hao Ramayanan'`, and `'hr543@sfu.ca'`).

6. Shutdown the machine (menu entry `Machine/ACPI Shutdown`---you will probably want to learn the hotkey for this action).

### Sharing a directory between your host OS and the guest OS in the virtual machine (repeat for every assignment)

For each assignment, you will want to share the directory containing your
code on the host machine with a directory in the guest Ubuntu OS in the
virtual machine.

Assume that you have cloned the boilerplate repository for your current assignment into directory `assign` and are editing code there.

1. Select the virtual machine from the list in VirtualBox.
2. Press the "Settings" button (orange gear).
3. Select the "Shared Folders" tab on the far right top.
4. Press the "Add" button (folder with '+' sign on right).
5. Navigate the "Folder Path" to the directory containing your assignment (`assign` in our example) and select that directory.
6. Check the "Auto-mount" box.  The directory should appear in the "Machine Folders" list, with "Auto-mount" as "Yes" and "Access" as "Full".
7. Press "OK".
8. Start the machine and sign in.

Your assignment directory will be `/media/sf_NAME`, where `NAME` is your
assignment (`/media/sf_assign` in our example). You can edit files in your
host operating system using your favourite editor, save them, and those updated files will
be visible to the guest Ubuntu system, where you can run your tests.

{% comment %}
## Appendix---how the machine was created

The base install was [Ubuntu 13.10](http://www.ubuntu.com/download/server).

And this:

`sudo su -c "echo 'ubuntu ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers"`

Also:

`sudo sh -c "echo 'manual' > /etc/init/ssh.override"`

{% endcomment %}