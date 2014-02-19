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

<p><strong>Question 2:</strong> If your service were something like a Web search, where a "good-enough" answer
is sufficient, What approaches might you use for each table?
</p>

<h2>Sharding and replication</h2>

<p><strong>Question 1:</strong> Define <em>sharding</em>. Define <em>replication</em>. What is the difference?</p>

<p><strong>Question 2:</strong> Assume that you have a database storing data about 1000 products,
numbered 0&ndash;999. The products numbered 0&ndash;399 are accessed 1000
times/hr, the products numbered 400&ndash;799 are accessed 500 times/hr, and
the products numbered 800&ndash;999 are accessed 100 times/hr.</p>

<p>You want to maximize parallelism using some combination of sharding and
replication. You have up to 10000 servers. How might you divide your 1000
products into shards and replications to maximize the parallism? Note that
you'll want to assign the most servers to the products that have the most
requests. Your answer will probably not assign all 10000 servers.</p>

## Description

**Question:** What is the primary risk the network poses to a system?

**Question:** Define _authentication_ and _authorization_.

**Question:** List four categories of requirement that might be specified in an SLA.

**Question:** Why don't the percentile tables for response time include a row for 100%?

**Question:** What are the twin purposes of measuring the performance of your system?
