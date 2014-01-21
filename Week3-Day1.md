---
layout: course
title: Week 3, Day 1 (Monday, Jan 20)
sched-activation: class="active"
---
## In-class activity

{% comment %}
### Part 0: Forming groups for [Assignment 2](simple-sqs.html)

Form groups of two. At least one member of the group should be an
intermediate Python programmer.

### Part 1: SQS and its boto interface

The key calls to the [boto interface to SQS](http://boto.s3.amazonaws.com/sqs_tut.html):

* Writing a message: <code>set_body</code> and <code>write</code>.
* Reading a message: <code>get_messages</code>.
* Deleting a message: <code>delete_message</code>

Setting up:

* Create a connection: <code>connect_to_region</code>.
* Creating a queue <code>create_queue</code>.

{% endcomment %}

Introduction to the SQS Console.

## For next class

Using the [Tutorial for creating access keys](access-keys-tut.html), create
a new access key for your AWS account.

{% comment %}
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

{% endcomment %}