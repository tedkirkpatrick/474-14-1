---
layout: course
title: Solution to "Developing an SLA"
sched-activation: class="active"
requires-math: yes
---
## The latency formula

The formula for computing all the latencies in this design is:

<p>\[
    s + q(n) + w(n)
\]</p>

<p> where \(s\) is the server latency, \(q\) is the queue latency,
\(w\) is the worker latency, and \(n\) is the number of workers. The
values for queue latency and worker latency are functions of the
number of workers, as defined in the original assignment by the <code>ql</code>
equation and the percentile tables.</p>

## Part 1

<p><b>Question 1:</b> Assuming 2 workers, the latency formula becomes
\(200 + (50+25 \times .30) + 175 = 407.5~\mathrm{ms}\), where
\(\log_{10}(2)=.30\).</p>

<p><b>Question 2:</b> Assuming 1000 workers, the formula becomes \(200 + (50+25 \times 3) + 1050 = 1375~\mathrm{ms}\).</p>

**Question 3:** Assuming 1000 workers and a requests that are hedged
at the 99th percentile, the worker latency now has two parts: The time
it takes for the first 990 workers to complete (650&nbsp;ms) plus the time
it takes for the remaining 10 hedged requests to complete (which each
complete in the time for 2 requests, 175&nbsp;ms).

Using those results, the formula becomes

<p>\[
    200 + (50 \times 25 \times 3) + (650+175) = 1150~\mathrm{ms}
\]</p>

For estimating an actual system, you'd
likely use a more sophisticated statistical model for hedged
requests. But this computation gives you a back-of-the-envelope estimate
of the savings from a hedged request.

This result is a special case of [Amdah's
Law](http://en.wikipedia.org/wiki/Amdahl's_law): Parallelization
reduces the time required for that part of an algorithm that
can be made parallel but has no effect on the sequential part. This
makes the sequential portion the limiting case of the algorithm. In
our case, hedging the requests reduced the latency for the 1000 workers from 1050&nbsp;ms
to 825&nbsp;ms, a \\((1050-825)/1050=21\%\\) saving, but the sequential part of
325&nbsp;ms was unchanged, so the savings on the total latency was only \\((1375-1150)/1375 = 16\%\\).

## Part 2

Throughput is the number of requests possible per unit time. If each request completes in at most 1400&nbsp;ms and you have four instances reserved to exclusively perform this operation, throughput becomes

<p>\[
    4 \times (1/1400) = 2.857 \times 10^{-3}~\mathrm{resizes/ms} = 2.857~\mathrm{resizes/s} = 171.42~\mathrm{resizes/min} = 10286~\mathrm{resizes/hr}.
\]</p>

These answers are equivalent; any one will do, as would
approximations. For provisioning estimates, the most useful estimate
would likely be \\(10300~\mathrm{resizes/hr}\\).

## Part 3

Assuming the worst case, Amazon's downtime will occur outside your own
maintenance downtime, so the worst-case total downtime of your system
will be their sum. Referring to the [availability table](Week1-Day2.html)
from the first week of the course, the "four
nines" downtime we are assuming for Amazon translates to one hour per
year.  Adding the eight hours per year your operations staff want for
their work gives a total of nine hours per year. Referring again to
the table, nine hours per year is an annual rate of 99.9%, **"three
nines"**.