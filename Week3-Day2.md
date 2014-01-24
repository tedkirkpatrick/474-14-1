---
layout: course
title: Week 3, Day 2 (Wednesday, Jan 22)
sched-activation: class="active"
gist-name: 8553680
---
## In-class activity

### Access key

1. Check: Everyone has an AWS access key ID and secret access key
2. Everyone knows the path to the file containing their access key
3. Test: Access function works

  * Sign on to your EC2 instance.
  * Copy your credentials file from your machine to your instance:
    * On Mac OS and Linux: `scp CREDENTIALS-FILE ubuntu@IP-ADDRESS`, where `CREDENTIALS-FILE` is the path to your access key credentials, downloaded from Amazon, and `IP-ADDRESS` is the public IP address of the instance (the address you connected to via ssh).
    * On Windows: Download [WinSCP](http://winscp.net/eng/index.php) and use that to send `CREDENTIALS-FILE` to the EC2 instance.
  * Check if you have git installed (probably not): if the command `which git` displays a path, you **have git**.
  * If you need git, install it: `sudo apt-get install git`.
  * Get the test code: `git clone https://gist.github.com/8553680.git`
  * Run the test:
<pre><code>    $ cd {{ page.gist-name }}
    $ python
    &gt;&gt;&gt; import testcreds
    &gt;&gt;&gt; testcreds.test('YOUR-CREDENTIALS-PATH') 
</code></pre>

replacing `YOUR-CREDENTIALS-PATH` with the absolute path to your credentials file. The path will begin with `/home/ubuntu/`.

#### To download the latest version of the test software

The test software has been revised. To download it _to your EC2 instance_, sign on to your EC2 instance and

<pre><code>$ cd {{ page.gist-name }}
$ git pull
</code></pre>

You will see some messages from `git`.

Now run the test using the instructions above.

#### Analyzing your test results

**If the test succeeds**, you will see `Test SUCCEEDED`. Congratulations! You won't have to do these steps again for this EC2
instance. These changes will be retained even if you stop and then restart
the instance.

**If you get a Python file IO error**, it is most likely that the path to the credentials file is incorrect.

**If you get a 403 Permissions error**, and your access key is for an IAM id, it is likely that your IAM id does not have a full range of permissions. In the IAM console, select your ID and go to the Permissions tab. View the policies for your id. They should include one like the following:

<pre><code>{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
</code></pre>

#### Another way to use your access keys

Redditor `sickan90` suggests an alternative approach: Placing your
access keys into the boto configuration file. See their
[post on Reddit](http://www.reddit.com/r/sfu_innovation/comments/1vwkbb/an_easy_way_to_setup_your_credentials_to_sqs/).

Thanks, `sickan90`!

### Groups for Assignment 2

1. Groups of 1 or 2.
2. Form a group using CourSys group facilities. (Form own group, invite another to join yours, accept/decline invitations.)
3. Groups formed by midnight Thursday (tomorrow).

### Structure of the assignment

See [My Little Image Sharer](a2.html).

* Creating a service that distributes images.
* Service has two subservices.
* Customer-facing service called `server`.
* Server stores images into S3 (we provide code).
* Server sends message to `worker` subservice behind the scenes.
* You write the connection between worker and server using SQS.
* Worker creates thumbnails of images and stores thumbnails
* We provide thumbnail code
* You provide communications code between worker and server

## Reading guide for next class

Read the following before coming to the next class:

**[{{ site.data.bibliography.dean2013.title }}]({{ site.data.bibliography.dean2013.url }})**,
from beginning up to but not including "Cross-request long-term adaptations".

The key points:

* _latency_ is the length of time for a request to complete
* The sources of variability in system response
* The algorithm for hedged requests (p.&nbsp;77)

Less important:

* The middle section on "reducing component variability". This is good
  advice on how to improve response time for individual requests

