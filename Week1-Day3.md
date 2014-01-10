---
layout: course
title: Week 1, Day 3
sched-activation: class="active"
---
## In-class exercise

Break up into groups of __three__.  

1. Using Barroso, Clidaras, and H&ouml;lzle's categories of platform-level software, cluster-level infrastructure, and application-level software, which level would the following most likely fit:

  * Software that logs an error from a specific disk drive.
  * Software that collects error logs from every disk drive in the cluster.
  * A MySQL database server running on a single machine.
  * A package management tool (such as <code>yum</code>, <code>npm</code>, or <code>apt-get</code>) that installs software on a machine.
  * A database that supports 10,000 queries per second.
  * A messaging utility that distributes 100,000 messages per second.

2. Describe one attack that would be prevented by multi-factor authentication on a userid. Describe another attack that would work even with multi-factor authentication.

## Discussion of AWS services

See screen listing all AWS services.

## Reading guide for next class

Read the following before coming to the next class:

**[{{ site.data.bibliography.helland2013.title }}]({{ site.data.bibliography.helland2013.url }}), pp. 53--55 (from "SaaS: Front end, back end, and decision support" and stop before "A Quick Refresher on Simple Queing Theory").**

This section begins with the structure of a typical application for
the cloud. Online stores such as Amazon or Indigo might have a
structure such as this. Then the article focuses on the front-end
portion of the application, which interacts directly with the user and
therefore has strong response time requirements.

The key points for this week:

* the general-purpose logic _outside_ the grey box in Figure&nbsp;3. 
* the way a single user request is broken into many simpler services.
* the very tight response times required of the lower level services.

**[{{ site.data.bibliography.barroso2013.title }}]({{ site.data.bibliography.barroso2013.url }}), Sections 2.3--2.4.**

These two pages describe the lower two of the three layers of software
(see p.&nbsp;15 for the definitions of the levels), platform-level ad
custer-level. We'll be going into the concrete details of these layers
as the course proceeds, using their counterparts on AWS and {{ site.serName }}.

The platform level (2.3) and the resource, hardware, and eployment
infrastructures (2.4.1--2.4.3) are mostly the concern of the
datacenter operators. We won't consider them in this course. We will
consider the programming framework infrastructure (2.4.4). That is the
general-purpose logic from Figure&nbsp; of today's first article.