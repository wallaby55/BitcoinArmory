---
layout: page
title: Documentation
---

Building Armory From Source
===========================

The latest stable version of Armory is available in precompiled, GPG-signed binaries for Windows, Ubuntu/Debian, and Mac. You can download them from the [Releases](/releases) page. Non-Debian-based Linux users will have to compile from source.

Compiling in Linux has proven to be quite easy. There are only a couple dependencies, and they’re all versionless, so there are no games you have to play with system library versions in order to get it to work.

If you want to compile in Windows, the build process is far from simple, but extremely well-documented. Do it at your own risk! It involves downloading and manually installing about 7 packages, then using Microsoft Visual Studio to compile the C++ code and create a python-module. But it does work!

Verifying Source Code Authenticity
----------------------------------

The latest stable version or Armory is always be tagged in the git repository by its version number, and signed with the [Armory signing key (98832223)](http://keyserver.ubuntu.com:11371/pks/lookup?search=Alan+Reiner).

Here’s how you download the Armory signing key directly into your keyring from the Ubuntu keyserver, and then verify the signature using git tag -v:

~~~ bash
$ gpg --recv-keys --keyserver keyserver.ubuntu.com 98832223
gpg: requesting key 98832223 from hkp server keyserver.ubuntu.com
gpg: key 98832223: public key "Alan C. Reiner (Armory Signing Key) <alan.reiner@gmail.com>"
$ git tag -v v0.93.3
tag v0.93.3
tagger Armory Technologies, Inc <contact@bitcoinarmory.com> 1424537423 -0500
gpg: Signature made Sat 21 Feb 2015 11:50:23 AM EST using RSA key ID 98832223
gpg: Good signature from "Alan C. Reiner (Offline Signing Key) <alan@bitcoinarmory.com>"
~~~
 

The above example is specifically for checking the tag for version "v0.93.3", which may not be the latest version by the time you are reading these instructions.  You can replace it with the latest version number posted on our website.  You can view all tags from the Armory's Github page, click on the button that says "branch: master" and then select the "tags" tab.  All major releases are accompanied by a signed tag.

To checkout and build a specific version, simply use "git checkout [tag]" before the "make" command in the Ubuntu build instructions below.  For instance, to build version 0.93.3, you would simply use:

~~~ bash
$ git checkout v0.93.3
Note: checking out 'v0.93.3'
...
HEAD is now at e59e10d... Add comment explaining why the padding was removed
~~~

Ubuntu Build Instructions
-------------------------

In Ubuntu, open a terminal (Applications → Accessories → Terminal) and copy in each of the following lines one at a time (omit the dollar sign at the beginning of each line):

~~~ bash
$ sudo apt-get install git-core build-essential pyqt4-dev-tools swig libqtcore4 libqt4-dev python-qt4 python-dev python-twisted python-psutil
$ git clone git://github.com/etotheipi/BitcoinArmory.git
$ cd BitcoinArmory
$ make
$ python ArmoryQt.py
~~~

Alternatively you can run "sudo make install" after building and it and it will install Armory onto your Ubuntu system, including but shortcuts in your the Applications --> Internet menu.

NOTE:  The above instructions do not check Armory's signatures the as shown in the previous section.  If you know the latest version (0.93.1 as of this writing), then you can add the verification checks before the "make" command, as seen below:

~~~ bash
$ sudo apt-get install git-core build-essential pyqt4-dev-tools swig libqtcore4 libqt4-dev python-qt4 python-dev python-twisted python-psutil
$ git clone git://github.com/etotheipi/BitcoinArmory.git
$ cd BitcoinArmory
$ git checkout v0.93.1  # put latest version number here
$ git tag -v v0.93.1    # confirm signatures before continuing
$ make
$ python ArmoryQt.py
~~~

Mac OS X Build Instructions
---------------------------

To build Armory on Mac OS X, you can follow the directions found in the "osxbuild" directory in the Armory github project.  Specifically:

<https://github.com/goatpig/BitcoinArmory/blob/master/osxbuild/osx_build_notes.txt>

The instructions are plain-text and can be viewed directly from the Github webpage (unlike the Windows instructions below).

Windows Build Instructions
--------------------------

Please note that it is a very involved process to build from source on Windows!  We have done our best to make this as straightforward as possible, but it may still require some patience and possibly some experience with MS Visual Studio.

We have committed the Windows build instructions to an RTF file in the master branch of the repository.  However, because of the way github webpage works and the fact that it is an RTF file, it's not easy to view the instructions just by opening the link.  You either need to manually download the file from Github, or install git, clone the Armory and then open the RTF file from the cloned project directory.  To manually download the RTF, click on the link below, then right-click on the "Raw" button on the right side of the page and select "Save link as...".  This will allow you to save it to the directory of your choice.

<https://github.com/goatpig/BitcoinArmory/blob/master/Windows_Build_Instructions.rtf>

Once you have the RTF file on disk you should be able to double-click it in a file browser to open with a word-processing application such as OpenOffice/LibreOffice or MS Word.
