---
layout: course
title: Week 4, Day 2 (Wednesday, Jan 29)
sched-activation: class="active"
---
## In-class exercise

 * How are these terms relevant or related to your app:
   * data center
   * virtual machine
   * virtualization
   * provisioning
   * overprovisioned
   * underprovisioned
   * elastic computing
   * utilization
   * throughput
   * latency
   * API
 * If you were to define an overall SLA for your service, what kinds of targets would you have to set?
 * How does or doesn't your ID generation algorithm prevent conflicts?
 * What platform-level, cluster-level, and application-level software is being used in your app?
 * How does your app scale?
{% comment %}
 * How might it fail? (Hint: server.py)
{% endcomment %}
 * How could you change it to scale better?
 * What other existing apps might use a similar platform? Why? (Hint: Video.)
 * What metric did you chose for your AutoScaler/CloudWatch alarm? Why?
 * If a worker fails while encoding an image, what happens? Can your system recover?

## Distributed/Cloud systems structure 

From [{{ site.data.bibliography.cavage2013.title }}]({{ site.data.bibliography.cavage2013.url }}).

Cloud applications are distributed systems---designing for the cloud is designing a distributed system

Every application is different

* Many off-the-shelf components won't perform well enough

Note how much other stuff is necessary to build an application:

<img src="http://deliveryimages.acm.org/10.1145/2470000/2461274/figs/uf1.jpg" class="img-responsive" alt="The distributed services of an image resize service"><br/>
Source: p.&nbsp;66 of [{{ site.data.bibliography.cavage2013.title }}]({{ site.data.bibliography.cavage2013.url }}), Copyright ACM, 2013.

The many questions to ask about a distributed service:

* Will the system have regions or be global?
* Single- or multiple-tenant?
* SLAs (for availability, latency, throughput, consistency, durability, &hellip;)
* Security
* Usage tracking
* Deployment and configuration management

## Reading guide for next class

**Read [{{ site.data.bibliography.cavage2013.title }}]({{ site.data.bibliography.cavage2013.url }})**, from Messaging (p.&nbsp;67) up to but not including Platform Components (p.&nbsp;68).

These two sections are short but dense. For the "Messaging" section,
consider how your use of SQS in Assignment&nbsp;2 fits his
description. Also note how he considers each of the factors (geographies, etc.) for this subservice.

For the "Automating Failover" section, focus on the basic need: We need
to design how the system recovers when a subcomponent fails.