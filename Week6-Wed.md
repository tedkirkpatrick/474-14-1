---
layout: course
title: Review of Weeks 3&ndash;5 (Week 6, Wednesday)
sched-activation: class="active"
---
## Latency: Consider the following three percentile tables:

<table class='table'>
<caption class='big-caption'>Table 1</caption>
<thead>
<tr><th class='rttd' scope='col'>Percentile of completed subrequests</th><th class='rttd' scope='col'>Time (ms)</th></tr>
</thead>
<tbody>
<tr><td class='rttd'>50</td><td class='rttd'>300</td></tr>
<tr><td class='rttd'>75</td><td class='rttd'>350</td></tr>
<tr><td class='rttd'>99</td><td class='rttd'>375</td></tr>
</tbody>
</table>

<table class='table'>
<caption class='big-caption'>Table 2</caption>
<thead>
<tr><th class='rttd' scope='col'>Percentile of completed subrequests</th><th class='rttd' scope='col'>Time (ms)</th></tr>
</thead>
<tbody>
<tr><td class='rttd'>50</td><td class='rttd'>1000</td></tr>
<tr><td class='rttd'>75</td><td class='rttd'>1100</td></tr>
<tr><td class='rttd'>99</td><td class='rttd'>1200</td></tr>
</tbody>
</table>

<table class='table'>
<caption class='big-caption'>Table 3</caption>
<thead>
<tr><th class='rttd' scope='col'>Percentile of completed subrequests</th><th class='rttd' scope='col'>Time (ms)</th></tr>
</thead>
<tbody>
<tr><td class='rttd'>50</td><td class='rttd'>500</td></tr>
<tr><td class='rttd'>75</td><td class='rttd'>1000</td></tr>
<tr><td class='rttd'>99</td><td class='rttd'>1750</td></tr>
</tbody>
</table>

<p><strong>Question 1:</strong> Assume your SLA for latency is a 99% of
900&nbsp;ms. For the response times for each table, what approach would you
use to achieve your SLA?</p>

<p><strong>Answer:</strong></p>

<ol>
<li>For these response times, even the slowest responses are well under our SLA. The simplest algorithm, distributing the work across the
workers, will be more than enough.</li>
<li>For these response times, even the 50th percentile is too low. The system must be rearchitected to speed up the basic operations. No amount of hedging or tying will make the system fast enough.
</li>
<li>These response times are a case where hedged or tied requests will help. Half the results are returned in 500 ms and three-quarters in 1000 ms but the last 25% form a long, slow tail. Hedged or tied requests will shrink that tail. We might not get down to our 900 ms goal but we could get close.
</li>
</ol>


<p><strong>Question 2:</strong> If your service were something like a Web search, where a "good-enough" answer
is sufficient, What approaches might you use for each table?
</p>

<p><strong>Answer:</strong></p>

<ol>
<li>As in the first case, these response times are so fast that we don't need any special handling to meet our target.
</li>
<li>Again, these times remain too slow. We don't even get half the results within our 900 ms target. That's not close to "good enough".
</li>
<li>Given these response times, we could elect to return a result to the user when we only have 50-70% of the data. That would keep our latencies within the 900 ms target.
</li>
</ol>

<h2>Sharding and replication</h2>

<p><strong>Question 1:</strong> Define <em>sharding</em>. Define <em>replication</em>. What is the difference?</p>

<p><strong>Answer:</strong></p>

<dl class="dl-horizontal">

<dt>sharding</dt><dd>Breaking the primary key range of a dataset into sub-ranges
('shards') so that requests to different shards can be handled
independently.</dd>

<dt>replication</dt><dd>Creating identical copies of a dataset or shard of a dataset so that requests to different replicas
can be handled independently.</dd>

</dl>

<p>Both methods increase the number of requests that can be handled
independently. Sharding splits different data across multiple
instances, while replication spreads identical copies of some data
across multiple instances.  </p>

<p><strong>Question 2:</strong> Assume that you have a database storing data about 1000 products,
numbered 0&ndash;999. The products numbered 0&ndash;399 are accessed 1000
times/hr, the products numbered 400&ndash;799 are accessed 500 times/hr, and
the products numbered 800&ndash;999 are accessed 100 times/hr.</p>

<p>You want to maximize parallelism using some combination of sharding and
replication. You have up to 10000 servers. How might you divide your 1000
products into shards and replications to maximize the parallism? Note that
you'll want to assign the most servers to the products that have the most
requests. Your answer will probably not assign all 10000 servers.</p>

**Answer:** The problem rewuests that you shard and replicate the
  data. There are many ways of organizing this. Here is one. Start by
  setting up shards that will require the same number of accesses: 

<table class="table">
<caption class="big-caption">Sharding of the 1000 products</caption>
<thead>
<tr><th scope="col" class="rttd">Accesses/hr/product</th><th scope="col" class="rttd">Products/shard</th>
<th scope="col" class="rttd">Accesses/hr/shard</th><th scope="col" class="rttd">Products</th><th scope="col" class="rttd">Shards</th>
</tr>
</thead>
<tbody>
<tr><td class="rttd">1000</td><td class="rttd">1</td><td class="rttd">1000</td><td class="rttd">400</td><td class="rttd">400</td></tr>
<tr><td class="rttd">500</td><td class="rttd">2</td><td class="rttd">1000</td><td class="rttd">400</td><td class="rttd">200</td></tr>
<tr><td class="rttd">100</td><td class="rttd">10</td><td class="rttd">1000</td><td class="rttd">200</td><td class="rttd">20</td></tr>
</tbody>
</table>

Total shards is 620, all accessed 1000&nbsp;times/hr. Replicating 620
shards as many times as possible across 10000 servers, we get 16
replications each, with 80 servers left over.

## Descriptive questions

**Question:** What is the primary risk the network poses to a system?

**Answer:** The network will rarely fail completely but it is extremely likely that it will degrade
  in quality and capacity at times. Your application must be ready to
  handle such degradation. ([{{ site.data.bibliography.cavage2013.shorter }}]({{ site.data.bibliography.cavage2013.url }}), p.&nbsp;69) 

**Question:** Define _authentication_ and _authorization_.

**Answer:** _Authentication_ is the process of determining that a user
  is who they claim to be. _Authorization_ is the process of
  determining whether an authenticated user can do an operation they have requested.

**Question:** List four categories of requirement that might be specified in an SLA.

**Answer:** [{{ site.data.bibliography.cavage2013.shorter }}]({{ site.data.bibliography.cavage2013.url }}) lists five: availability, latency, throughput, consistency, and durability. Not all of these will be specified for every service but you do need to consider them all.

**Question:** Why don't the percentile tables for response time include a row for 100%?

**Answer:** There is no upper bound on the very longest time a response might take. The worker may have crashed, resulting in infinite response time (you will never get an answer) or it may just take a very long time.

**Question:** What are the twin purposes of measuring the performance of your system?

**Answer:** 1. Monitoring the system in real time to detect failures and overloads, and 2. Analytics to determine usage trends.
 ([{{ site.data.bibliography.cavage2013.shorter }}]({{ site.data.bibliography.cavage2013.url }}), p.&nbsp;70)