---
layout: course
title: Developing a Service-Level Agreement (SLA)
sched-activation: class="active"
---
## Submission details

**Due:** Wednesday, February&nbsp;19, 2014<br/>
**Submit to [CourSys](https://courses.cs.sfu.ca/2014sp-cmpt-474-d1/+a3-sla):** A PDF file giving your answers to each question. Show how they were derived.<br/>
**Percentage of course grade:** 4%

## Part 1: SLA for Latency

This assignment asks you to work through the issues discussed in
[{{ site.data.bibliography.dean2013.title }}]({{ site.data.bibliography.dean2013.url }}). We will use
the structure of Assignment&nbsp;2 as an example application.

The latency of a request in Assignment&nbsp;2 is due to the latencies
of each of its component parts: The server (which saves the original
image in S3 and queues up resizes on the workers), the time it takes
the SQS queue to deliver messages from the server to the workers, and
the workers (which do one or more resizes and save them in S3). Assume
the following characteristics for each component:

* the latency of the server is a constant 200&nbsp;ms,
* the latency of the queue (the time it takes for a message to travel from the server to a worker) in ms is a logarithmic function of the number of workers, `ql = 50 + 25 * log10 w`, where `w` is the number of workers, and
* the latencies of the workers according to the following tables:

### Latency for 2 workers

<table class="table">
<caption class="ignore-caption">Latency percentiles for <code>w = 2</code> workers</caption>
<thead><tr><th scope="col" class="rttd">Percentile</th><th scope="col" class="rttd">Time (ms)</th>
</tr></thead>
<tbody>
<tr><td class="rttd">50.0</td><td class="rttd">125</td></tr>
<!--
<tr><td class="rttd">75</td><td class="rttd">175</td></tr>
<tr><td class="rttd">90</td><td class="rttd">250</td></tr>
<tr><td class="rttd">99</td><td class="rttd">300</td></tr>
-->
<tr><td class="rttd">99.9</td><td class="rttd">175</td></tr>
</tbody>
</table>

Example: If two workers are creating thumbnails and every request
requires each worker to make a thumbnail, 50% of the time all
thumbnails for one request will be completed within 125&nbsp;ms after
the _workers_ have received them and virtually all requests will have
all their thumbnails ready 175&nbsp;ms after the _workers_ have
received them.

### Latency for 1000 workers

<table class="table">
<caption class="ignore-caption">Latency percentiles for <code>w = 1000</code> workers</caption>
<thead><tr><th scope="col" class="rttd">Percentile</th><th scope="col" class="rttd">Time (ms)</th>
</tr></thead>
<tbody>
<tr><td class="rttd">50.0</td><td class="rttd">150</td></tr>
<!--<tr><td class="rttd">75</td><td class="rttd">175</td></tr>-->
<tr><td class="rttd">90.0</td><td class="rttd">325</td></tr>
<tr><td class="rttd">99.0</td><td class="rttd">650</td></tr>
<tr><td class="rttd">99.9</td><td class="rttd">1050</td></tr>
</tbody>
</table>

### Question 1

Assume the latency for a complete request is the sum of the server,
queue, and worker latencies. This is the time between the receipt of a
request from a user task and all the thumbnails being stored in S3 and
available to be read.

Using the above formulas, calculate the 99.9th percentile latency for requests when there are two workers.

### Question 2

Using the same assumptions as above, but now asssuming 1000 workers
and that every request will require creation of 1000 thumbnails, one for each worker,
calculate the 99.9th percentile latency.

### Question 3

Now assume that you have revised your project to use a hedged request
algorithm. At the 99th percentile time, for every worker that has
still not replied, you start a second worker with the same
request. Assume you have a pool of idle workers from which to assign
the duplicate request. Assume that a duplicated request has the latency
distribution of 2 workers. (This is unrealistically simple but it makes the
computation easier.)

What is the 99.9th percentile of this latency distribution?

## Part 2: SLA for Throughput

Assume that your latency computations make you comfortable setting an
SLA of 99% at 1400&nbsp;ms for all your requests. You have reserved
four EC2 instances that will be used exclusively for this service (in other words, _single-tenant_). These
instances are identical to the one used for the latency
computation.

**What is your SLA for throughput?**

## part 3: SLA for Availability

Assume that Amazon offers an availability of "four nines" (99.99%). In addition, your
operations staff tell you that they will likely need to have the
system down for one working day (eight hours) per year. 

**How many "nines" is your SLA for annual availability?**
