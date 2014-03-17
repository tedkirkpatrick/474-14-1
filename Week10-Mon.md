---
layout: course
title: Amazon DynamoDB (Week 10, Monday, March 17, 2014)
sched-activation: class="active"
---
## Replicated data accepting independent writes
Source: [{{site.data.bibliography.takada2013.title}}, Chapter 5]({{site.data.bibliography.takada2013.url}}eventual.html).

Suppose instead of a single database, we have several replicas storing values for the same key.

Two problems:

* When the system is completely connected (no network partitions), we have to propagate changes to all the replicas

* If we continue accepting updates to all replicas even when they are
  separated by network partitions, we have to reconcile conflicting values
  for the same key

If we're willing to give up strong consistency, we can be

* Highly available, even in the presence of partitions

* Low latency

* Almost always "consistent enough"

Amazon's DynamoDB is an example of such a system

## Partial quorums

DynamoDB (and systems inspired by it) replace the notion of strict quorum with a partial quorum

* Assume we have N replicas of the data

* We _synchronously_ write to W replicas on a write (1 <= W <= N)

  * If W < N, we gossip to make the remaining N-W replicas consistent

* We _synchronously_ read from R replicas on a read (1 <= R <= N)

Describe these using the first two diagrams of [{{site.data.bibliography.katsov2012.title}}]({{site.data.bibliography.katsov2012.url}})

## Demonstration

See the Berkeley [{{site.data.bibliography.bailis-nd.title}}]({{site.data.bibliography.bailis-nd.url}}).

{% comment %}
## Guide to reading for next class

{% endcomment %}