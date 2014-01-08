---
layout: course
title: Week 1, Day 2
sched-activation: class="active"
commentary: commentary
---

## In-class exercise

Break into pairs. Take half of the following phrases and explain it to your
partner to the best of your understanding. Then switch roles, with your
partner explaining the other half to you. If you have no idea what a term
means, speculate.

* virtual machine
* virtualization
* provisioning
* overprovisioned
* oversubscribed
* elastic computing
* API

List the two or three words or phrases you found hardest to understand from
the readings (ignoring the legal terms in Amazon's SLA).

## Uptime and availability

Availability can be most simply defined as <code>uptime / (uptime +
downtime)</code>. But note that customers and providers (such as Amazon)
will define "downtime" differently. This is the source of the legalese in
Amazon's SLA (and every other cloud vendor's SLA).

<table class="table">
<caption>Availability and uptime</caption>
<thead>
<tr><th scope="col">Availability %</th><th scope="col">How much downtime is allowed per year?</th></tr>
</thead>
<tbody>	
<tr><td>90% ("one nine")</td><td>More than a month</td></tr>
<tr><td>99% ("two nines")</td><td>Less than 4 days</td></tr>
<tr><td>99.9% ("three nines")</td><td>Less than 9 hours</td></tr>
<tr><td>99.99% ("four nines")</td><td>Less than an hour</td></tr>
<tr><td>99.999% ("five nines")</td><td>~ 5 minutes</td></tr>
<tr><td>99.9999% ("six nines")</td><td>~ 31 seconds</td></tr>
</tbody>
</table>

Table from <a href="{{ site.data.bibliography.takada2013.url }}">
{{ site.data.bibliography.takada2013.title }}, Chap. 1</a>.  A good, more extensive, discussion
is at the Wikipedia page for [High Availability (HA)](http://en.wikipedia.org/wiki/High_availability).

## Reading guide for next class

Read the following before coming to the next class:

**[{{ site.data.bibliography.barroso2013.title }}]({{ site.data.bibliography.barroso2013.url }}),
Sections 1.0--1.3, 1.5--1.6.0 (stop before 1.6.1)**. 

Read these sections to get an idea of the overall structure of a
datacenter. Every time you do a search using Google, Bing, or Yahoo, every
time you tweet or update your Facebook account, the code is running on the
kind of warehouse-scale computer described here. This book was written by
three engineers who have designed data centers for Google.

After this reading, we will focus on software for the rest of the course.

Things to look for:

 * What is a warehouse-scale computer?
 * How does warehouse scale make it different from laptops or desktops?
 * Why does understanding this matter?

**[{{ site.data.bibliography.barroso2013.title }}]({{ site.data.bibliography.barroso2013.url }}),
Sections 2.0--2.1, skim 2.2**.

Read these sections to gain an overview of the software that forms the
cloud. We'll spend most of the course thinking about this topic.

Things to look for:

 * What distinguishes Platform-level, Cluster-level, and Application-level software?
 * What makes Internet-scale software different from the software on your desktop?

Familiarize yourself with the list of concepts in Section 2.2 but don't
expect to memorize it. We'll be covering many of these concepts in great
detail during the course.