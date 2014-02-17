---
layout: course
title: Review of Weeks 1&ndash;2+
sched-activation: class="active"
---

## Who wrote these articles?

* [{{ site.data.bibliography.barroso2013.title }}]({{ site.data.bibliography.barroso2013.url }}):
Three architects of the hardware and software for Google's data centers.

* [{{ site.data.bibliography.armbrust2010.title }}]({{ site.data.bibliography.armbrust2010.url }}):
Professor and students at UC Berkeley Reliable Adaptive Systems Lab (RAD Lab).

* [{{ site.data.bibliography.helland2013.title }}]({{ site.data.bibliography.helland2013.url }}):
Architect for distributed systems at Tandem, Microsoft, and Salesforce (a company offering a cloud-based service and a platform for building cloud-based systems).

* [{{ site.data.bibliography.dean2013.title }}]({{ site.data.bibliography.dean2013.url }}):
Fellows (a senior technical position) in the Google Systems Infrastructure Group.

* [{{ site.data.bibliography.cavage2013.title }}]({{ site.data.bibliography.cavage2013.url }}):
Software engineer at Joyent (a cloud provider) and Amazon Web Services.

## Review questions

* What are some of the advantages of large, centralized data structures?
* What are some of the layers of cloud software?
* What does SLA stand for? What is in one?
* What does the layered structure of a service do to its SLAs?
* What is a hedged request?

## What did the readings say?

* Large, centralized datacentres change the economics of computing
  * Elastic provisioning---pay only for as much as you need, when you need it
  * Much cheaper to manage very large centers, located close to power source, with only a few hardware types
  * Store large, shared data
  * Infrastructure can be shared across multiple applications and services

* A cloud service provides several layers of software 
  * Platform-level: Supporting the basic container in which applications run. Often a virtual machine (VM)
    * Amazon EC2 virtual machines, Heroku dynos
  * Cluster-level: Basic operations underlying __distributed__ services
    * Message-sending (Amazon SQS)
    * Monitoring performance and responding (Amazon CloudWatch)
    * Distributed storage (Amazon S3)
    * Deployment and maintenance (after midterm)
    * Frameworks (Google AppEngine)

* Service Level Agreements (SLAs) define the requirements for your service
  * Many categories: latency, throughput, availability, durability, consistency
  * May be hard requirements (legal) or soft requirements (objectives)

* A user-facing service in turn calls many subservices
  * SLAs for lower-level services have tight latencies
  * Common subservices ("plumbing") might be made reusable
    * Business logic will be specific to the application
    * But assumptions underlying the common services have to match your requirements

* Latency, latency, latency, latency
  * Users want their answers quickly
  * Reduce latency by spreading work over multiple workers
  * Cannot predict which workers will be slow or fail outright
    * **But some will!**
    * Can accelerate by duplicating requests---but that doubles resource consumption
    * Hedged request: Wait till most (99% or more) of requests have completed, then issue second requests for remaining 1%

{% comment %}
* Service-oriented architecture (SOA)
{% endcomment %}

