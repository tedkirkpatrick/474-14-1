---
layout: course
title: Week 3, Day 3 (Friday, Jan 24)
sched-activation: class="active"
---
## Distributing computation across instances

In the first part of Assignment&nbsp;2, you are going to build a service, comprising two subservices connected by an SQS queue:

<img src="images/a2-struct-part1.png" class="img-responsive" alt="Structure of Assignment 2: User, Server, Worker, S3">

In the second part, you are going to make the system scalable by partitioning the image resizing step across multiple workers:

<img src="images/a2-struct-part2-partial.png" class="img-responsive" alt="Structure of Assignment 2, Part 2: Multiple workers">

How many workers is enough? As the number of image resizes grows,
you'll need more workers. To make it _scalable_, you will need to
automatically _provision_ more workers (EC2 instances):

<img src="images/a2-struct-part2-complete.png" class="img-responsive" alt="Structure of Assignment 2, Part 2: Starting new workers">

## Reading guide for next class

**Complete [{{ site.data.bibliography.dean2013.title }}]({{ site.data.bibliography.dean2013.url }}), from "Cross-request long-term adaptations" to end.**

You might also consider rereading the sections on "Hedged requests" and "Tied requests".

Key points to look for:

* What is a good trade-off of partitions of the data?
* How do large information retrieval systems (such as search services) differ from other services?