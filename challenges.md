---
layout: course
title: Challenges of building distributed systems on networks of warehouse-scale computers
challenges-activation: class="active"
---

Running a system on warehouse-scale computers, distributed
across multiple data centres (perhaps on multiple continents),
raises the following challenges:

* Every component---processors, storage, network, software---can and will fail.
* Centralized services---hardware or software---can take all their dependencies down if they fail.
* Clocks from different machines or data centers can give different results.
* Users will notice and dislike even small (100&nbsp;ms = 0.1&nbsp;s) delays.
* When the network fails, you have to choose between consistent storage or available storage.
* Information takes substantial time to transmit long distances.
* Messages can be slow, lost, or duplicated (even when using TCP).
* Demand can change on short notice
{% comment %}
* Some governments require some data to be stored in specific geographic regions.
* Warehouse-scale computers have different performance bottlenecks than single servers.
{% endcomment %}
