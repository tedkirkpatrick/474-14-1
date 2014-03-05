---
layout: course
title: Week 8, Wednesday (March 5, 2014)
sched-activation: class="active"
---
## CAP categories

The Consistency, Availability, and Partition Tolerance regions:

<img src="images/CAP-Venn.png" class="img-responsive" alt="CAP Venn diagram">
<small>After [Takada, Chapter 2]({{site.data.bibliography.takada2013.url}})</small>

Many traditional database systems favour Consistency and Availability over partition tolerance (CA):

<img src="images/CA-Venn.png" class="img-responsive" alt="CAP Venn diagram with C and A regions highlighted">

Any node in the system will always give the same answer, no matter what
sequence of reads and writes the system has seen. But it cannot run at all if any node is partitioned.
(This isn't really "available" at all.)

Some systems offer Consistency and Partition Tolerance but give up availability (CP):

<img src="images/CP-Venn.png" class="img-responsive" alt="CAP Venn diagram with C and P regions highlighted">

As with CA systems, any node that is _available_ will give you the same
answer, regardless of the sequence of reads and writes. If there is a
network partition, the main body will continue (provided it is large enough
to have a quorum), while the smaller part will not accept writes. The smaller
part might run in read-only mode but will get increasingly out of date.

Finally, systems might offer Availability and Partition Tolerance but give up consistency (AP):

<img src="images/AP-Venn.png" class="img-responsive" alt="CAP Venn diagram with A and P regions highlighted">

These systems will remain available, accepting reads and writes even in the case of network partitions. Their tradeoff
is that **different nodes might give different results to the same query**.

## Tradeoffs in the CAP space

<img class="aligncenter size-full wp-image-798" title="consistency-plot-3" alt="Tradeoffs between consistency, availability, and latency" src="http://highlyscalable.files.wordpress.com/2012/09/consistency-plot-3.png" class="img-responsive"/>

<small>Source: [Highly Scalable
blog](http://highlyscalable.wordpress.com/2012/09/18/distributed-algorithms-in-nosql-databases/). Rights
presumably held by Ilya Katsov.</small>

<img class="size-full wp-image-768" title="consistency-catalog" alt="" src="http://highlyscalable.files.wordpress.com/2012/09/consistency-catalog.png"  class="img-responsive"/>

<small>Source: [Highly Scalable
blog](http://highlyscalable.wordpress.com/2012/09/18/distributed-algorithms-in-nosql-databases/). Rights
presumably held by Ilya Katsov.</small>
