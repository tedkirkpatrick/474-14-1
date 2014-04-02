---
layout: course
title: F1 (Week 12, Wednesday, April 2)
sched-activation: class="active"
---
## F1 is as mission-critical as it gets

<small>Source: [{{site.data.bibliography.shute2013.title}}]({{site.data.bibliography.shute2013.url}})</small>

Stores Google AdWords data

* Google's core revenue source
* High amount of data stored (100 TB)
* High velocity of incoming data
* High query rate (100 kilo-requests/s)
* High processing rate (10 Tera-rows scanned/day)
* Availability "reaches" five 9s (~5 min/year)
* Five-way replication across datacentres in multiple US regions

## F1 does way more than your grandparents' NoSQL services

Strongly consistent

<div class="well">
"Designing applications to cope with concurrency anomalies in their data [eventual consistency] is very error-prone,
time-consuming, and ultimately not worth the performance gains." (p.&nbsp;1068)
</div>

Supports database transactions (ACID)

Full SQL query support and indexing

### Built on Spanner
<small>(Optional) [{{site.data.bibliography.corbett2012.title}}]({{site.data.bibliography.corbett2012.url}})</small>

Spanner is a service that provides

* Extremely scalable storage
* Synchronous replication across datacentres
  * Quorum algorithm (Paxos)
  * Higher latency
  
Global timestamps provide a total order

* But only up to a slightly-old _global safe timestamp_
* The safe timestamp is typically 5--10&nbsp;s ago
* Can read from any replica, anywhere in the world as of the safe timestamp

The system has an uncertainty measure that indicates fuzziness of times

* Uncertainty computed using a mixture of GPS and atomic clocks
* Uncertainty typicall around 10&nbsp;ms

## Latency and throughput for F1

Read latencies of 5--10&nbsp;ms

Write (commit) latencies of 50--150&nbsp;ms

User-perceived latencies of 200&nbsp;ms

* Comparable to older MySQL database
* Better tail latency

Queries more highly paralellizable

* Linear speedup (claimed) with more instances

### Some limitations

Higher CPU costs than MySQL

Clients have to change access patterns and schema to achieve above latency

## Upcoming activities

### Final assignment

The final assignment, which builds on and integrates the last two
assignments into an eventually-consistent service, will be made available
tonight or early tomorrow.

### Course review 

The answer key to the midterm will be made available on-line.

Exercises for the final exam will be made available on-line.