---
layout: course
title: Week 5, Day 3 (Friday, February 7)
sched-activation: class="active"
---

## In class---sharding and replication

Suppose our image processing application (Assignment&nbsp;2) included
its own image storage function rather than using Amazon&nbsp;S3. Some
of the images on our site might become very popular (say, a striking
photograph of a celebrity). When an image is popular, we want to
retrieve it with low latency. We also want to ensure our images are
retained even if there are disk crashes. (Recall that many data centers
intentionally use disks with relatively low reliabilities.)



## Implementation <small>(from [You Are Building a Distributed System]({{ site.data.bibliography.cavage2013.url }}))</small>

Build versus buy is not a simple choice

Testing is difficult

* Transient bugs are common
* Total network outage is rare---degraded performance is common
* Drive the system at expected load
* **Induce failures** (more on this in Week&nbsp;8)

Operating the system requires careful monitoring (Week&nbsp;9)

* If it moves, measure it
* Need both real-time and analytic data
* You will produce lots of data---which might require its own highly scalable, reliable system to manage

## Anonymous poll

On an **unsigned** sheet of paper, briefly complete:

1. I most want to see the class start doing &hellip;
2. I most want to see the class continue doing &hellip;
3. I most want to see the class stop doing &hellip;

## No readings over Reading Break

Work on [Assignment&nbsp;3](sla.md) and review the previous readings.