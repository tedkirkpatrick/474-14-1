---
layout: course
title: Week 8, Friday (March 7, 2014)&mdash;Two eventually consistent algorithms
sched-activation: class="active"
---
## Some basic issues <small>From [Distributed Databases]({{site.data.bibliography.katsov2012.url}})</small>

**Eventually consistent:** Vague commitment that system will _eventually_
  converge to a consensus, if you wait long enough after the "last update". 

* No Guarantee _what_ value system will converge to
* Simply means "not strongly consistent"
* Different degrees and kinds

### Handling conflicting writes

**Conflict detection:** Detect that a conflict has occurred and either

  * Pick a tie-breaker by algorithm
  * Return both values to the application to resolve (Used in [Riak]({{site.data.bibliography.basho2013overview.url}}))

**Conflict prevention:** Don't allow conflicting writes

  * Slows system down due to communication costs
  * Necessarily intolerant of network partitions

## Anti-entropy via gossip

Algorithm that is:

* Scalable
* Partition-tolerante
* Weakly consistent
   * Not even guaranteed to converge to _latest_ value

## Read Quorum/ Write Quorum

Given N replications

* Write W versions synchronously
* Read R replicats

If R + W > N

* Ensures read-after-write consistency for a given client
* But different readers can get different values (during update)
* If W > N/2, can detect conflicts
* Not tolerant of network partitions
   * Can be modified to achieve that

{% comment %}

## Guide to reading for next class

{% endcomment %}