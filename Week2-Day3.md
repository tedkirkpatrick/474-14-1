---
layout: course
title: Week 2, Day 3
sched-activation: class="active"
---
## In-class activity

Session spent bringing everyone to point where they could sign on
to an EC2 instance. This included:

* Installing an SSH client (Windows users only)
* Generating an SSH key (if user didn't have one)
* Signing on to AWS
* Uploading public part of key pair to Amazon
* Adding frequently-used services to AWS menu (optional, but useful)
* Understanding EC2 console page
* Specifying and launching an EC2 instance
* Connecting to the EC2 instance using SSH and the key generated earlier
* Using tmux to manage SSH session (optional, for better usability)

## Post-class optional session

For those who wished to stay after 3:20&nsp;PM, Izaak continued:

* Running Python on the EC2 instance
* Connecting to AWS S3 storage
* Uploading images to AWS S3 storage using Python boto library

## (Optional) Reading guide for next class

**Optional but useful preparation for Monday's class.**

Review the [Tutorial on using SQS from boto](http://boto.s3.amazonaws.com/sqs_tut.html). Skim the [Reference for the boto SQS module](http://boto.s3.amazonaws.com/ref/sqs.html).

Key points to look for:

* Creating a queue
* Writing a message
* Reading a message
* Deleting a message. Note that reading doesn't delete a message.

Cautions:

* The boto reference manual is confusingly organized and a bit out of date. For now, just skim it.

If you want to play with SQS, try connecting, creating a queue,
writing a message, reading a message, and deleting it. Note that if
you simply create a queue using <code>SQSConnection</code>, it will be
created in the us-east-1 region, not the us-west-2 (Oregon) region we
used on Friday. To create a queue in us-west-2, do
<code>boto.sqs.connect_to_region('us-west-2').create_queue('queuename')</code>.