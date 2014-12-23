---
layout: course
title: Design principles for cloud systems
design-activation: class="active"
---
Key design principles, addressing the [challenges of systems built on networked data centres](challenges.html):

 * Design from the outset to run at massive scale (see [{{site.data.bibliography.hull2013.title}}]({{site.data.bibliography.hull2013.url}})).
 * Design with the expectation of subcomponent failure (see Chapter&nbsp;7 of [{{site.data.bibliography.barroso2013.title}}]({{site.barroso2013.data.bibliography.url}})).
 * Design to ignore duplicate copies of a message (see [{{site.data.bibliography.helland2012.title}}]({{site.data.bibliography.helland2012.url}})).
 * Control latency caused by the high-percentile instances (see [{{site.data.bibliography.dean2013.title}}]({{site.data.bibliography.dean2013.url}})).
 * Test failure resistance by inducing failures in production systems (see [{{site.data.bibliography.tseitlin2013.title}}]({{site.data.bibliography.tseitlin2013.url}})).
 * Use existing, widely-used implementations of distributed algorithms rather than building one-off solutions (see ???).
 * For each service, trade off consistency, availability, and mitigation (see [{{site.data.bibliography.brewer2012.title}}]({{site.data.bibliography.brewer2012.url}})).
 * Design for monitoring, tuning, and limiting system load (see [{{site.data.bibliography.hamilton2007.title}}]({{site.data.bibliography.hamilton2007.url}})).
