---
layout: page
title: Verifying Binaries
permalink: /docs/verify
id: verify
---

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
