---
layout: page
title: Documentation
---

## Building Armory From Source

The latest stable version of Armory is available in precompiled, GPG-signed binaries for Windows, Ubuntu/Debian, and Mac. You can download them from the [Releases](/releases) page. Non-Debian-based Linux users will have to compile from source.

Compiling in Linux has proven to be quite easy. There are only a couple dependencies, and they’re all versionless, so there are no games you have to play with system library versions in order to get it to work.

If you want to compile in Windows, the build process is far from simple, but extremely well-documented. Do it at your own risk! It involves downloading and manually installing about 7 packages, then using Microsoft Visual Studio to compile the C++ code and create a python-module. But it does work!

### Verifying Source Code Authenticity

The latest stable version or Armory is always be tagged in the git repository by its version number, and signed with the [Armory signing key (4922589A)](http://keyserver.ubuntu.com/pks/lookup?search=goatpig). For releases 0.93.3 and earlier, the [old Armory signing key (98832223)](http://keyserver.ubuntu.com/pks/lookup?search=Alan+Reiner) was used.

Here’s how you download the Armory signing key directly into your keyring from the Ubuntu keyserver, and then verify the signature using `git tag -v`:

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
 

The above example is specifically for checking the tag for version "v0.93.3", which may not be the latest version by the time you are reading these instructions.  You can replace it with the latest version number posted on our website. All releases can be viewed on the [github releases page](https://github.com/goatpig/BitcoinArmory/releases). All major releases are accompanied by a signed tag.

To checkout and build a specific version, simply use `git checkout [tag]` before the `make` command in the Ubuntu build instructions below.  For instance, to build version 0.93.3, you would simply use:

~~~ bash
$ git checkout v0.93.3
Note: checking out 'v0.93.3'
...
HEAD is now at e59e10d... Add comment explaining why the padding was removed
~~~

### Ubuntu Build Instructions

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

### Mac OS X Build Instructions

To build Armory on Mac OS X, you can follow the directions found in the "osxbuild" directory in the Armory github project.  Specifically:

<https://github.com/goatpig/BitcoinArmory/blob/master/osxbuild/OSX_build_notes.md>

The instructions are plain-text and can be viewed directly from the Github webpage.

### Windows Build Instructions

Please note that it is a very involved process to build from source on Windows!  We have done our best to make this as straightforward as possible, but it may still require some patience and possibly some experience with MS Visual Studio.

<https://github.com/goatpig/BitcoinArmory/blob/master/windowsbuild/Windows_build_notes.md>

These instructions are also in plaintext and can be viewed directly from the Github webpage.

## Verifying the downloaded binaries

The latest binaries and signed hash files can be found on the [releases](/releases) page or on the [github releases page](https://github.com/goatpig/BitcoinArmory/releases).

To check the files, first import the [Armory signing key (4922589A)](http://keyserver.ubuntu.com/pks/lookup?search=goatpig). Then download the files. For each file, take its sha256 hash and then check that the hash matches the one in the signed hash file. Then verify the signed hash file.

For example, in Ubuntu, to verify the .dev file for 0.94.1, do the following.

~~~bash
$ gpg --recv-keys --keyserver keyserver.ubuntu.com 4922589A
gpg: requesting key 4922589A from hkp server keyserver.ubuntu.com
gpg: key 4922589A: public key "goatpig (Offline signing key for Armory releases) <moothecowlord@gmail.com>" imported
gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
gpg: depth: 0  valid:   2  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 2u
gpg: Total number processed: 1
gpg:               imported: 1  (RSA: 1)
$ sha256sum -c sha256sum.asc.txt armory_0.94.1_amd64.deb 2>&1 | grep OK
armory_0.94.1_amd64.deb: OK
$ gpg --verify sha256sum.asc.txt 
gpg: Signature made Sun 22 Nov 2015 01:34:46 AM EST using RSA key ID 4922589A
gpg: Good signature from "goatpig (Offline signing key for Armory releases) <moothecowlord@gmail.com>"
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 745D 707F BA53 968B DF63  AA8D 8C52 1176 4922 589A
~~~
