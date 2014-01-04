---
layout: course
title: Design principles for cloud-based systems
design-activation: class="active"
---
Key design principles for systems intended to run on one or more warehouse-scale computers:

 * Design to run at massive scale (see [{{site.data.bibliography.hull2013.title}}]({{site.data.bibliography.hull2013.url}}))
 * Design with the expectation of subcomponent failure (see Chapter&nbsp;7 of [{{site.data.bibliography.barroso2013.title}}]({{site.barroso2013.data.bibliography.url}}))
 * Control latency caused by the high-percentile instances (see [{{site.data.bibliography.dean2013.title}}]({{site.data.bibliography.dean2013.url}}))
 * Test failure resistance by inducing failures in production systems (see [{{site.data.bibliography.tseitlin2013.title}}]({{site.data.bibliography.tseitlin2013.url}}))
 * For each service, trade off consistency, availability, and mitigation (see [{{site.data.bibliography.brewer2012.title}}]({{site.data.bibliography.brewer2012.url}}))
