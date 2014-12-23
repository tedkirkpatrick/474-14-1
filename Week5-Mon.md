---
layout: course
title: Week 5, Day 1 (Monday, February 3)
sched-activation: class="active"
---
## Discussion of answers to Friday's in-class exercise

Walking through the table we used on Friday.

<img src="http://deliveryimages.acm.org/10.1145/2410000/2408794/figs/t2.jpg" class="img-responsive" alt="Read Latencies observed in a BigTable service benchmark">

Source: Table 2, p.&nbsp;78 of [{{ site.data.bibliography.dean2013.title }}]({{ site.data.bibliography.dean2013.url }}), Copyright ACM&nbsp;2013.



## Design options for distributed systems <small>(From [{{ site.data.bibliography.cavage2013.title }}]({{ site.data.bibliography.cavage2013.url }}))</small>

The categories of analysis:

* Geographies (one global system versus regional "silos")
* Data segregation (single- versus multi-tenancy)
* SLA guarantees

  * availability
  * latency
  * throughput
  * consistency 
  * durability

* IAAA (Identity, Authentication, Authorization, and Audit)
* Usage tracking
* Deployment

The standard design questions for _any_ system also apply (versioning, upgrades, ...).

## Automating failover <small>(From [{{ site.data.bibliography.cavage2013.title }}]({{ site.data.bibliography.cavage2013.url }}))</small>

Many systems have a "leader" instance that assigns work to the other instances.

* In our design for Assignment&nbsp;2, there can only be on `server.py`, assigning tasks to the `worker.py` instances.

What happens when the "leader" fails? Do you bring up a new leader
automatically or have the operations staff do it?

## Guide to readings for next class

_Carried over from Friday._

**Read [{{ site.data.bibliography.cavage2013.title }}]({{ site.data.bibliography.cavage2013.url }})**, from Platform Components (p.&nbsp;68) up to and including Platform Usage Collection (p.&nbsp;69).

Two key points from these sections:

1. There are many components of these systems that are not glamorous nor "complicated" but that are necessary for the system.
2. How do these components have to be designed to make them _scalable_?
