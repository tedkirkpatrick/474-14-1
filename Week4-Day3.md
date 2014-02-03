---
layout: course
title: Week 4, Day 3 (Friday, January 31)
sched-activation: class="active"
---
## In-class exercise---individual, signed and turned in

Assume the following table describes two highly parallel systems, one with no hedges and one that issues tied requests after 1&nbsp;ms:

<img src="http://deliveryimages.acm.org/10.1145/2410000/2408794/figs/t2.jpg" class="img-responsive" alt="Read Latencies observed in a BigTable service benchmark">

Source: Table 2 of [{{ site.data.bibliography.dean2013.title }}]({{ site.data.bibliography.dean2013.url }}), Copyright ACM&nbsp;2013.

### Instructions

1. First, do this exercise without consulting anyone else.

2. WHEN INSTRUCTED, consult with one or two people around you, revising your answers if you wish.

### Questions

Assuming you sent a request during a lightly-loaded period,

1. If you only cared about half of the response, how long would you expect to wait for the unhedged system versus the tied system?
2. For requests that require the entire response before they can complete, how much latency do you save using a tied system?

Assuming you sent a request during a heavily-loaded period,

1. For requests that require the entire response before they can complete, how much latency do you save using a tied system?
2. If you had a heavily-loaded system that used unhedged requests and you wanted to reduce your latency, would it be better to increase your provisioning or implement tied requests? (Assume both solutions have the same cost.)

## Demo of testing software

By Izaak.

## Discussion of distributed systems

**Moved to Monday.**

