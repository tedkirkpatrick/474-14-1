---
layout: course
title: Week 2, Day 2
sched-activation: class="active"
---

## A structure for Software as a Service (SaaS) 

Source: [{{ site.data.bibliography.helland2013.title }}]({{ site.data.bibliography.helland2013.url }}).

* Lowest level: Platform software providing basic services (local storage, processes, synchronization, networking)
* Separate out common features that are above the operating system but more general than one application

  * Cavage calls this infrastructure "plumbing" and "concierge" (two names for the same thing)
  * The term we prefer (from the Google Datacenter people) is _cluster-level infrastructure_
  * Neither term is precise---people may have different opinions about what lies at this level

* The cluster-level infrastructure can deal with new features of cloud technology:

  * Rapid scalability: provisioning new servers on demand.
  * Failure tolerance: Datacenters use hardware that is relatively unreliable; software also fails.
  * Rapid changes in datacenter networking: Processes can move to different machines, new servers can be added to an application, &hellip;
  * Transmission delays due to geography and network outages (the Consistency, Availability, and Partioning problem---CAP)

* Application-level software can provide commonly-required tools

  * Storage
  * Credit card payment processing
  * Sending emails
  * User ID management and login

## Breaking one service into multiple services

* A top-level user service, such as "Display the page for [_The 2009-2014 World Outlook for 60-Milligram Containers of Fromage Frais_](http://www.amazon.com/gp/product/0497929503/)", will be composed of many service calls within the application:

  * Add this book to the "recently-visited" session data for this user
  * Get sample pages, if any
  * Check session identifier remains valid
  * Get number of items in the shopping cart

* Each service, in turn, calls other services:

<!--<img src="HellandFig4.png"><br/>-->
<img src="http://deliveryimages.acm.org/10.1145/2400000/2398374/figs/f4.jpg" alt="Hierarchy of services in a service call graph"><br/>
Source: [{{ site.data.bibliography.helland2013.title }}]({{ site.data.bibliography.helland2013.url }}), Fig.&nbsp;4. Copyright&nbsp;2013, ACM.

* Each lower level has tighter SLA (response time) 

## Ensuring scalability

* How can we take advantage of elastic computing?
* If there's a sudden surge of requests, how do we scale up quickly?

  * Minimize communication between different user requests
  * Have multiple machines ready to serve a given user request

* _Sharding_ (Helland calls it "partitioning") breaks the database in sections with separate keys
* _Replication_ creates multiple copies of each shard

These methods are also listed in the table from Section&nbsp;2.2 of
[{{ site.data.bibliography.barroso2013.title }}]({{ site.data.bibliography.barroso2013.url }})
that you read for last Wednesday.

<!--<img src="HellandFig5.png"><br/>-->
<img src="http://deliveryimages.acm.org/10.1145/2400000/2398374/figs/f5.jpg" alt="Scaling by replication and sharding"><br/>
Source: [{{ site.data.bibliography.helland2013.title }}]({{ site.data.bibliography.helland2013.url }}), Fig.&nbsp;4. Copyright&nbsp;2013, ACM.

## No reading for Friday

{% comment %}
**[{{ site.data.bibliography.cavage2013.title }}]({{ site.data.bibliography.cavage2013.url }}) .**
{% endcomment %}