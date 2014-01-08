---
layout: course
title: Week 1, Day 1
sched-activation: class="active"
---
## Who we are

 * Ted Kirkpatrick---instructor
 * Izaak Schroeder---Teaching Assistant, programmer extraordinaire

Contact information is on the course home page (URL below).

## Things you need to know about this course:

 * There will be group projects.
 * There will be writing.
 * There will be reading.
 * Python (either 2.7 or 3.x) will be the language for all assignments.
 * A credit card is highly recommended for the Amazon assignments.

   * There will be alternate assignments that don't require an Amazon Web Services (AWS) ID, but you will learn the most (and gain the most valuable experience for your portfolio) from using an actual AWS ID (which requires a credit card).
   * All AWS usage will remain within the Free Tier—you will be able to complete your assignments without having your card charged.

 * Material given in class will not necessarily be available in other forms (lecture notes and class exercises may not be posted on line). But all the key points will be repeated in several classes.
 * Much class time will be spent working with material, often in ad-hoc groups, using laptops.

***

## Grading Proportions

 * 50% assignments---though they will comprise more than 50% of your effort
 * 15% Midterm
 * 35% final

***

## Office hours

Poll of candidate office hours.

***

## Web sites

<table class="table">
<thead><tr><th scope="col">Site</th><th scope="col">URL</th><th scope="col">Purpose</th><th scope="col">Blame</th></tr></thead>
<tbody>
<tr><td>Course pages</td><td>http://sfu-innovation.github.io/474-14-1/</td><td>Description of activities, assignments, policies, &hellip;</td><td>Ted</td></tr>
<tr><td>Course cloud</td><td>To be announced</td><td>Programming assignments</td><td>Izaak</td></tr>
<tr><td>Grades</td><td>https://courses.cs.sfu.ca/2014sp-cmpt-474-d1/</td><td>Standard CourSys site for CMPT grades</td><td>Greg Baker</td></tr>
</tbody>
</table>

***

## What we'll focus on

 * How cloud architectures differ from your laptop, desktop, and phone
 * Designing software that works well with cloud architecture
 * The unique requirements of services delivered across the Internet
 * The services offered by Amazon Web Services (AWS)

## What we won't focus on

 * Customer-facing features such as Apple iCloud, Microsoft Office365, or Google Gmail
 * Details of building a data centre

***

## An Introduction to Warehouse-Scale Computers

* [{{ site.data.bibliography.google2014.title }}]({{ site.data.bibliography.google2014.url }})

  * Photo tour of Google Data Centres around the world
  * [Video of Google data centre]({{ site.data.bibliography.google2014a.url }})
  * [Video of Google's container-based data centre]({{ site.data.bibliography.google2014b.url }}) (Section at 2:47--5:00 shows containers)

* [{{ site.data.bibliography.gauthier2013a.title }}]({{ site.data.bibliography.gauthier2013a.url }}) (see photo of outdoor containers at Boydon, Virginia, USA).

***

## In-class exercise

_This exercise was moved to Wednesday due to lack of time._

Break into pairs. Take half of the following phrases and explain it to your partner to the best of your understanding. Then switch roles, with your partner explaining the other half to you. If you have no idea what a term means, speculate.

* data center
* virtual machine
* virtualization
* provisioning
* overprovisioned
* oversubscribed
* elastic computing
* utilization
* throughput
* latency
* API

## Reading guide for next class

Read the following before coming to the next class:

**1. [{{ site.data.bibliography.armbrust2010.title }}]({{ site.data.bibliography.armbrust2010.url }}), pp. 50--53** (up to but not including "Top 10 Obstacles").

Things to look for in this article:

  * Key enabler of cloud computing.
  * Advantages of clouds.
  * The difference between Amazon Web Services and Google App Engine. But note that these services have become more similar since 2010.
  * How customer usage changes provisioning requirements.

Things of less importance:

  * public versus private clouds.

**2. [{{ site.data.bibliography.helland2013.title }}]({{ site.data.bibliography.helland2013.url }}) pp. 50--53** (up to but not including "Patterns in SAAS Apps")

Things to look for in this article:

  * What are the factors that make cloud computing attractive?

As with the first article, we won't pay much attention in this course to the distinction between public and private clouds. 

**3. Skim [Amazon EC2 Service Level Agreement (SLA)](http://aws.amazon.com/ec2-sla/).**

Things to look for:

  * What is Amazon promising, in general terms?
  * How would the customer know Amazon has broken its promise?
  * What compensation does Amazon offer if the customer accuses them of breaking their promise?

Things to **ignore**:

  * The complex, legal escape clauses and definitions.
