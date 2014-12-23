---
layout: course
title: Game Days (Week 11, Friday, March 28, 2014)
sched-activation: class="active"
---
## Game day intro
<small>From [{{site.data.bibliography.krishnan2012.title}}]({{site.data.bibliography.krishnan2012.url}}).</small>

{% comment %}
Exercise:  SOMETHING SOMETHING SOMETHING
{% endcomment %}

Annual, company-wide, event over several days

* DiRT: Disaster Recovery Training (or "Game Day")
* Expensive to run
* Has caused actual outages leading to revenue loss

Given that every team is ready and on-site, problems can be resolved quickly

Game Day complements continuous _component_ testing.

Example: A data centre is partitioned by failure of a switch

* Recovery requires both DNS and directory services to failover (switch to backups)
* The individual failovers should be tested regularly
* Game Day tests whether all the individual failovers work together

### Example: Simulated earthquake

Caused Failure of Bay Area Google data center

* Housed a number of internal services
* Some of those services could not recover (single home, single point of failure)
* Other services failed over to their local workstations
   * These didn't work either 
* Internal authentication services failed
   * Most Google staff now couldn't work
   * Everyone went to dinner
   * Local cafes Denial-of-Service'd
* System for redirecting pages and alerts to non-Bay Area offices also failed
   * Calls reporting errors were not received
* Accounting approvals-tracking _did_ failover
   * But the people who could approve the new topology were themselves cut off
   * So the automatically reconfigured system was useless

## What to test

Failures of multiple systems in parallel

* Loss of a data centre
* Backbone fiber cable cut
* Failure of core infrastructure on which other systems depend (Colossus file system, authentication, ...)

Identify weaknesses in less-tested interfaces between systems and groups

* Design by team with members from all affected groups
* Multiple teams collaborate to resolve problem
* Important to have them all there and ready

Be ready to turn off the test if serious problems arise

### Command centre

Technical team

* Design cross-service tests
* Evaluate tests by individual teams
* Cause large-scale outages
* Monitors test progress
* Manages recovery when things go "worng"

Coordinators

* Plan and schedule tests
* Ensure preparation done

### Example: Phone "bridge" emergency coordination

First test: Only one person figured out how to connect

Second test: 100 people connected ... but bridge only held 40 connections

Third test: A caller put the bridge on hold ... no one else could call in or out

### Example: Buying diesel fuel for long-term emergency generators

Simulated long-term power outage for a data center

Needed to buy extra diesel fuel for backup generator ($$$)

No authorization possible from central management (comm failure)

Expected employees to use (documented) emergency spending procedure

Instead: Charged > $100,000 on personal credit card

### Example: Zombies Attack!

One data centre goes down abruptly (Atlanta)

The zombies are fiction (... maybe?) but the shutdown is real

1. Other three centres take up slack
2. Performance SLA maintained
3. But resilience SLA requires running with only _two_ data centres
4. So they cleanly shut down another (Europe)
5. Now barely within performance SLA

## Growing the organization

Start off with a few volunteer teams

First tests can be quite safe

Don't expect a team's first tests to really test much

Increase complexity and breadth of tests with each run

Embrace failure as a means of learning

Track every problem

Solid champion amongst senior executives aids process (VP Operations at Google)

## Guide to reading for next class

**Read [{{site.data.bibliography.hoff2007.title}}]({{site.data.bibliography.hoff2007.url}}).**

Key points:

1. Why logging everything is necessary
2. Why you need to build logging in rather than bolt it on later
3. Why it needs to be fast

The post ends with a long list of bullet points for logging design. Each
entry is terse and there are many. Get a general gist of these guidelines
but don't expect to memorize every one.