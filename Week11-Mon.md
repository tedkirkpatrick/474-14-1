---
layout: course
title: Building reliable systems (Week 11, Monday, March 24)
sched-activation: class="active"
---
## Reliability for large-scale systems

Experiences of James Hamilton, then at Windows Live. <small>([{{site.data.bibliography.hamilton2007.title}}]({{site.data.bibliography.hamilton2007.url}}))</small>

Three main principles (Bill Hoffman):

* Expect failures
* Keep things simple
* Automate everything

### Application design

Keep development, test, and operations staff close to each other

* DevOps approach: "You built it, you support it"

Failure recovery must be

* Simple
* Tested frequently
* Perhaps hard-fail systems to shut them down

Redundancy

* Availability of four to five 9s require redundant systems
* True redundancy means you can hard-fail any system without work loss

Support and deploy only one version

Multi-tenant your services

* Share hardware cost across all services
* Give up some system efficiency for operations efficiency

Allow rare human intervention in an emergency

* Test the scripts with fire drills or Game Days

Admission control---block new work when system is overloaded

* Do this at interfaces within the system as well

  * For example, allow users to read but not write

Shard the data

* Arbitrarily adjustable (not just first letter of family name)
  * Use a hash or dictionary to map primary keys to shards
* Not bound to any real-world object (not "all employees of organization X")

Analyze throughput and latency

* With background tasks running (garbage collection, etc.)
* Predict and measure access patterns (especially to databases, but also network and other components)
* Every call to a subservice should have a timeout
  * Bound the number of restarts
  * Log restarts
* Dependent (lower-level) servics should commit to the same overall SLAs as their callers

### Automatic management

Make your secondary backups _synchronous_

* The write is considered complete when both copies are written
  * Cost in longer latency and lower throughput
* You can instantly route requests to the backup when the primary fails

Build in recovery at higher levels, not lower

* The service should have redundant messages
  * Don't conceal it lower, at the network protocol
  * TCP doesn't guarantee reliability across _sessions_
* Fail fast

Fail services regularly---see next day's class

### Operations

Never delete anything
* Just mark it deleted
* Make everything configurable ("Feature flags")

The "Big Red Switch"

* Turns off all non-essential services
* Use it when the system is melting down (or about to)
* Resetting the switch should restart stopped services _automatically_

Control admission into the service

Meter admission into the service when coming up after a failure

## Guide to reading for next class

**Read all of 
[{{site.data.bibliography.tseitlin2013.title}}]({{site.data.bibliography.tseitlin2013.url}}).**

This article describes Netflix's approach to automatically generating
failures of system components. They have created a powerful culture of
stress-testing their systems and learning from any failures.