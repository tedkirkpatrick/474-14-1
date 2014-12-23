---
layout: course
title: Week 5, Day 2 (Wednesday, February 5)
sched-activation: class="active"
---

## In class: Criteria for authentication and authorization

Assume that you are implementing the following two services:

**Service 1: Authentication.** Given an id, password, and MFA token, verify that
they correctly identify a user. Return a cookie that indicates the
holder has been authenticated as this user.

**Service 2: Authorization.** Given a cookie indicating an
authenticated user, and an operation requested by that user, determine
if that user can perform that operation. For example, the user may be
able to read and write files they created, only list the names of files
created by their coworkers, and not be able to learn anything about
files created by anyone outside their company.

For each service, answer the following:

1. Should it be global or regional?

2. If a typical user will do ten requests each time they are assigned
a cookie, and each request will take 500&nbsp;ms, what is a reasonable
latency for each service?
3. What do you think the typical ratio of reads to writes will be for
the underlying database that each service is based upon?



## Guide to readings for next class

**Complete [{{ site.data.bibliography.cavage2013.title }}]({{ site.data.bibliography.cavage2013.url }})**, Implementation (p.&nbsp;69)--Conclusion (p.&nbsp;70).

Points to look for:

Up to this point, the article has described choices in system
_architecture_. These last sections describe the choices you have to
make when _implementing_ your chosen architecture:

* When is it OK to use a component that is already built? What are the risks?
* What is the great threat that the network poses to meeting your reliability SLA?
* What information do you need to run the system effectively?
* What are the risks of using a "platform as a service" rather than writing your own?

By the way, if you're intrigued by the notion of the Netflix
_Chaos&nbsp;Monkey_, see [{{ site.data.bibliography.tseitlin2013.title }}]({{ site.data.bibliography.tseitlin2013.url }}),
which describes that system and others like it.  We'll read that article
around the middle of the course.