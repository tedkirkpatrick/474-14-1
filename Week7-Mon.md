---
layout: course
title: Week 7, Monday (February 24, 2014)
sched-activation: class="active"
---
## S&hellip;tuff gets real
So far, we've assumed data are read-only

  * Sharding and replication are easy---every copy is the same!
  * If it takes too long to transmit a value, make a copy and place it closer to the user

Life gets more complicated when the data can change

### Example 1: Geographic time lag

Takes 30&nbsp;ms for light to make round trip Canada/Europe

  * Actual transmission time longer (routers, congestion, protocols, &hellip;)

A user in Vancouver adds a comment to an article while another user in Budapest comments on the same article

  * In what order should those comments be displayed?
  * What if instead they are both trying to buy the last available seat on the same flight?

### Example 2: Network link degradation

We have users accessing a database from Halifax and Surrey. What happens if the cross-country backbone temporarily degrades?

  * Turn off access completely for one city? (Which one?)
  * Only let one city update it and give the other read-only access?
  * Let both cities update it without coordinating, then share updates afterwards?

### Example 3: Machine failure

Once again, we have users in Halifax and Surrey. Suppose we store Surrey user's data in Surrey and Halifax user's data in Halifax.

  * Ensures rapid local access, at expense of slower remote access
  * Robust against cross-country link degradation or failure
  * But what happens to the Surrey data if the Surrey storage fails?

Durability alone might require us to distribute our data, even when it is only used locally.

## Availability

[Takada]({{ site.data.bibliography.takada2013.url }}intro.html):
Availability is the proportion of time a system is in a functioning
condition. If a user cannot access the system, it is said to be unavailable.

* Distributed systems allow us to use redundancy to build a system that is more reliable than any one of its components
* But our designs have to tolerate failures
* Assume [message unreliability]({{ site.data.bibliography.helland2012.url }}):

   * A message may never get through
   * A message may be delivered *after* one that was sent *later*
   * A message may be delivered multiple times
   * Can't assume TCP will solve the problem

## Partitioning

What happens when messages are delayed or lost between two nodes?

* Perhaps due to unreliable transmission
* Perhaps due to failure of the sender
* Distinguishing these cases is impossible until after the problem is resolved

## Consistency

How do you coordinate updates when you have multiple copies of a database?

* Especially hard when copies are geographically separated
* Different grades of consistency

  * If I read after I write, will I get what I wrote?
  * If you read after I write, will you get what I wrote?
  * If we both write, what will the final value be?

{% comment %}

**Strong consistency:** There is a single order for all writes and every user everywhere sees the same order

  * Easier to program with but lower performance

**

{% endcomment %}

## Guide to reading for next class

**Read [{{ site.data.bibliography.takada2013.title }}]({{ site.data.bibliography.takada2013.url }}intro.html),
  Chapter 1**, from "What we want to achieve: Scalability and other good things", up to and including,
  "What prevents us from achieving good things?".
