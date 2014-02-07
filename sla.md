---
layout: course
title: Developing a Service-Level Agreement (SLA)
sched-activation: class="active"
commentary: commentary
---
## Submission details

**Due:** February&nbsp;??????, 2014<br/>
**Turn in:** A pdf file with your answers. Show your work.<br/>
**Percentage of course grade:** ???

## Latency, long tails, and hedged requests

This assignment asks you to work through the issues discussed in
[{{ site.data.bibliography.dean2013.title }}]({{ site.data.bibliography.dean2013.url }}). We will use
the structure of Assignment&nbsp;2 as an example application.

The latency of a request in Assignment&nbsp;2 is due to the latencies
of each of its component parts: The server (which saves the original
image in S3 and queues up resizes on the workers), the SQS queue, and
the workers (which do one or more resizes and save them in S3). Assume
the following characteristics for each component:

* the latency of the server is a constant 200&nbsp;ms,
* the latency of the queue in ms is a linear function of the number of workers, `ql = 50 + w * 25`, where `w` is the number of workers, and
* the latencies of the workers vary according to the following tables:

### Latency for 2 workers

<table class="table">
<caption class="ignore-caption">Worker latency percentiles for `w=1000 workers`</caption>
<thead><tr><th scope="col" class="rttd">Percentile</th><th scope="col">Time (ms)</th>
</tr></thead>
<tbody>
<tr><td class="rttd">50</td><td>125</td></tr>
<!--
<tr><td class="rttd">75</td><td>175</td></tr>
<tr><td class="rttd">90</td><td>250</td></tr>
<tr><td class="rttd">99</td><td>300</td></tr>
-->
<tr><td class="rttd">99.9</td><td>175</td></tr>
</tbody>
</table>

### Latency for 1000 workers

<table class="table">
<caption class="ignore-caption">Worker latency percentiles for `w=1000 workers`</caption>
<thead><tr><th scope="col" class="rttd">Percentile</th><th scope="col">Time (ms)</th>
</tr></thead>
<tbody>
<tr><td class="rttd">50</td><td>150</td></tr>
<!--<tr><td class="rttd">75</td><td>175</td></tr>-->
<tr><td class="rttd">90</td><td>325</td></tr>
<tr><td class="rttd">99</td><td>650</td></tr>
<tr><td class="rttd">99.9</td><td>1050</td></tr>
</tbody>
</table>

### Part 1

Assume the latency for a complete request is the sum of the server,
queue, and worker latencies. This is the time between the receipt of a
request from a user task and all the thumbnails being stored in S3 and
available to be read.

Using the above formulas, calculate the 99.9th percentile latency for 2 workers.

### Part 2

Using the same assumptions as above, but now asssuming 1000 workers
and that every request will have 1000 resizes, one for each worker,
calculate the 99.9th percentile latency.

### Part 3

Now assume that you have revised your project to use a hedged request
algorithm. At the 99th percentile time, for every worker that has
still not replied, you start a second worker with the same
request. Assume you have a pool of idle workers from which to assign
the duplicate request. Assume that a duplicated request has the latency
distribution of 2 workers. (This is unrealistically simple but it makes the
computation easier.)

What is the 99.9th percentile of this latency distribution?

