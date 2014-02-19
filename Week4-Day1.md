---
layout: course
title: Week 4, Day 1 (Monday Jan 27)
sched-activation: class="active"
---
## In-class exercise

List the biggest unknowns or risks you see for yourself or your team
in Assignment&nbsp;2. Items to think about:

In Part&nbsp;1:

* How will you format the messages from the server to the worker?

In Part&nbsp;2:

* How will you set up an EC2 instance so that it will start the worker process when CloudWatch starts a new instance?
* How will you force the load high enough to require that new instances be started?

## Reducing latency of service requests

* The SLA for our service might be legally binding or a market requirement.
* Variable latencies are inevitable.
* How to keep our latencies within our (binding or best-effort) SLA?
* Ways to reduce latency of a single request:

  * Hedge the request: Wait a bit, request a duplicate, cancel second on first reply
  * Tie the request: Issue two requests, cancel second once first begins

## Reading guide to next class

Read **[{{ site.data.bibliography.cavage2013.title }}]({{ site.data.bibliography.cavage2013.url }})**,
up to but not including "Messaging", p. 67.

Note that (as he says on p. 85), his use of "distributed system" is
synonymous with how we use "cloud". 

Key point:

<blockquote>While much of the discussion, literature, and presentations focus on the en vogue technologies such as Paxos, Dynamo, or MapReduce &hellip; the reality of building a large distributed system is that many “traditional” problems are left unsolved by off-the-shelf solutions, whether commercial or open source. (p.&nbsp;64)
</blockquote>

You don't need to pay close attention to:

* The opening pages (pp.&nbsp;63--64), giving two reasons for using a distributed system, are background.