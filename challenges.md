---
layout: course
title: Challenges of building distributed systems on warehouse-scale computers
challenges-activation: class="active"
---

Running a system on warehouse-scale computers, distributed
across multiple data centres (perhaps on multiple continents),
raises the following challenges:

* Single points of failure---hardware or software---can take the whole system down.
* Clocks from different machines or data centers will not agree.
* Data replicated at multiple locations may differ for each reader.
* Information takes substantial time to transmit long distances.
* Some governments require some data to be stored in specific geographic regions.
* Warehouse-scale computers have different performance bottlenecks than single servers.
* Demand can change suddenly and with little warning.