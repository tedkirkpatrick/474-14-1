---
layout: course
title: Oustanding issues
outstanding-activation: class="active"
commentary: commentary
---
Issues to be resolved before start of course:

* Team selection. Spread the Python expertise around.
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
  * Download Anaconda 1.8.0 `curl -O http://09c8d0b2229f813c1b93-c95ac804525aac4b6dba79b00b39d1d3.r79.cf1.rackcdn.com/Anaconda-1.8.0-Linux-x86_64.sh`
  * Check MD5: `md5sum Anaconda[TAB]`
  * Install Anaconda: `bash Anaconda[TAB]`
  * Result includes boto, zmq, redis, ipython. Runs Python 2.7, with option to insall 3.3 using `conda`.

* Run cluster via [{{site.data.bibliography.hintjens2013.tooltitle}}]({{site.data.bibliography.hintjens2013.url}}), both on {{site.serName}} and EC2.
* On Mac OS (at least and perhaps other OSes), ssh sessions into EC2 instances will simply drop with borken pipe at times. Try setting `ServerAliveInterval 60` in `/etc/ssh_config` or `/etc/ssh/ssh_config`. Might also set `ClientAliveInterval 60` in `/etc/ssh/sshd_config` on EC2 server.
* [Logging](log.html) in {{site.serName}}.
* Support for adding {{site.serName}} projects to student porfolios.
* Rolling over AWS access key and secret key
* Is there any circumstance when I would only use the first AWS access key?
* Levels 1, 2, and 3 networking (perhaps see [VL2]({{site.data.bibliography.greenberg2011.url}})).
* SFU formatting of this site.
* Ted consistenly misspells "outstanding". He also seems to have problems with "consistently".