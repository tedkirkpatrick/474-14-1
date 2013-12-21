---
layout: course
title: Design principles for Cloud-based systems
design-activation: class="active"
---
Key design principles for systems intended to run on one or more warehouse-scale computers:

 * Design to run at massive scale (see [20 Obstacles to Scalability](http://dl.acm.org.proxy.lib.sfu.ca/citation.cfm?id=2500468.2500475&coll=DL&dl=ACM&CFID=390847521&CFTOKEN=93977062))
 * Design with the expectation of subcomponent failure (see Chapter&nbsp;7 of [The Datacenter as a Computer, 2d. Ed.](http://www.morganclaypool.com/doi/abs/10.2200/S00516ED2V01Y201306CAC024))
 * Control latency caused by the high-percentile instances (see [The Tail at Scale](http://dl.acm.org.proxy.lib.sfu.ca/citation.cfm?id=2408776.2408794&coll=DL&dl=ACM&CFID=390847521&CFTOKEN=93977062))
 * Test failure resistance by inducing failures in production systems (see [The Antifragile Organization](http://dl.acm.org.proxy.lib.sfu.ca/citation.cfm?id=2492007.2492022&coll=DL&dl=ACM&CFID=390847521&CFTOKEN=93977062))
 * For each service, trade off consistency, availability, and mitigation (see [CAP Twelve Years Later](http://ieeexplore.ieee.org.proxy.lib.sfu.ca/xpl/articleDetails.jsp?tp=&arnumber=6133253&queryText%3Dcap+twelve+years+later))


