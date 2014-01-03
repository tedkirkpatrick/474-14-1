---
layout: course
title: Amazon Web Services (AWS) technical details
aws-activation: class="active"
---
Semi-structured list of technical details of working with Amazon Web Services (AWS).

## Userids

* Distinguish the account id, any IAM ids, your public/private key pair for SSH to any EC2 instances, and your access key/private key pair.

## EC2 instances

* Connecting to an instance: `ssh -i <keyfile> ec2-user@<public IP for your machine>`, where `<keyfile>` is the path to your public/private key pair and `public IP for your machine>` is taken from the instance description, available on the EC2 console.

* Installing ZMQ, on an EC2 instance running Amazon linux:

  * `sudo yum group-install "Development Tools"`
  * `curl -O http://download.zeromq.org/zeromq-4.0.3.tar.gz`
  * `tar -xvf zeromq-4.0.3.tar.gz`
  * `cd zeromq-4.0.3`
  * `./configure`
  * `sudo make install`
  * `sudo make check` Succeeds but all tests will fail if no sudo
  * `sudo ldonfig /usr/local/lib`
  * System can now compile and run basic C calls to 0mq __but__ `sudo easy_install pyzmq` still fails
  * `PKG_CONFIG_PATH=/usr/local/lib/pkgconfig/`
  * `export PKG_CONFIG_PATH`
  * Now `python setup.py install` finds zmq but still fails to compile `timer_create` or `init_threads`. Perhaps because Amazon comes with Python 2.6 and it's probably not the full development version?

* Installing Python distribution with all necessary libraries and packages:

  * Download Anaconda 1.8.0 `curl -O http://09c8d0b2229f813c1b93-c95ac804525aac4b6dba79b00b39d1d3.r79.cf1.rackcdn.com/Anaconda-1.8.0-Linux-x86_64.sh`
  * Check MD5: `md5sum Anaconda[TAB]`
  * Install Anaconda: `bash Anaconda[TAB]`
  * Result includes boto, zmq, redis, ipython. Runs Python 2.7, with option to insall 3.3 using `conda` package manager.

* ssh sessions into EC2 instances will simply drop with broken pipe at times. [To fix, set](http://ocaoimh.ie/2008/12/10/how-to-fix-ssh-timeout-problems/) `ServerAliveInterval 60` in `/etc/ssh_config` or `/etc/ssh/ssh_config`. Might also set `ClientAliveInterval 60` in `/etc/ssh/sshd_config` on EC2 instance.
