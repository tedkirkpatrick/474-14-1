---
layout: course
title: Logging (Week 12, Monday, March 31)
sched-activation: class="active"
---
## Logging defined

### Basic idea

From [Python 3 logging tutorial](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial):

```python
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
```

```python
2010-12-12 11:41:42,612 DEBUG:root:This message should go to the log file
2010-12-12 11:41:43,015 INFO:root:So should this
2010-12-12 11:42:35,756 WARNING:root:And this, too
```

0. When you record it?
1. What information do you record?
2. Do you have levels (DEBUG, INFO, WARNING)?
3. When do you turn levels on and off?
4. How do you analyze the logs?

### When do you use it?

<small>[From Python 3 tutorial](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)</small>

<table class='table'>
<caption>When to use logging</caption>
<thead><tr><th scope="col">Task you want to perform</th><th scope="col">The best tool</th></tr>
</thead>
<tbody>
<tr><td>Display output for ordinary use of a command-line program</td><td><code>print()</code></td></tr>
<tr><td>Report events from normal operation</td><td><code>logging.info()</code> or <code>logging.debug()</code></td></tr>
<tr><td>Issue a warning regarding an event</td><td><code>logging.warning()</code> if there is nothing the application can do</td></tr>
<tr><td>Report an error from a specific event</td><td>Raise an exception</td></tr>
<tr><td>Report suppression of an error in a long-running process</td><td><code>logging.error()</code>, <code>logging.exception()</code>, or <code>logging.critical()</code>, as appropriate</td></tr>
</tbody>
</table>

### Importance of logging

From [{{site.data.bibliography.hull2013.title}}]({{site.data.bibliography.hull2013.url}}), p.&nbsp;58:

Number 7: Insufficient monitoring and metrics

 * "it should be so basic you cannot imagine working without it"

Number 10: Insufficient logging

* "You may enable a lot more of it when you are troubleshooting and debugging, but on an ongoing basis you will need it for key essential services"

From [{{site.data.bibliography.hamilton2007.title}}](site.data.bibliography.hamilton2007.url}}), pp.&nbsp;231--232:

## Log everything all the time
<small>From [{{site.data.bibliography.hoff2007.title}}]({{site.data.bibliography.hoff2007.url}}).</small>

For highly-available applications

* Log **everything**
* Log **all the time**
* Only have two levels, NORMAL and DEBUG
* Turn on debugging per-module
* Every event should include the id of the customer request that started it:

  * Customer S. Lee requested a resize of image 'my-vacation-july-24-444.jpg' => Request `QX3567187`

```
2014-02-12 11:41:42,612 root:QX3567187:Resize from S. Lee of 'my-vacation-july-24-444.jpg' started
2014-02-12 11:41:43,015 root:QX3567187:Resize saved in S3 entry 'lee-mvj24-3617846.jpg'
2014-02-12 11:41:43,212 root:QX3567187:Resize sent to instance EC2-Q347HN for 100 by 100 resize
2014-02-12 11:42:35,756 root:QX3567187:Resize completed by EC2-Q347HN
```

### Keeping it efficient

Set up fast queue between high-priority worker process and low-priority logging process

* Logging process does slower formatting operations
* Allocating/deallocating queue buffers must be fast
* Logger pushes to permanent storage in the background

Any object should be easily dumped to the log

* `logging.dump(myobj)`

## Analyzing the logs

Products such as
[{{site.data.bibliography.loggly-nd.title}}]({{site.data.bibliography.loggly-nd.url}})
integrate logs from multiple sources and analyze them.

## Guide to reading for next class

**Read the following two short sections from [{{site.data.bibliography.shute2013.title}}]({{site.data.bibliography.shute2013.url}}):**

1. Section 1: Introduction (pp.&nbsp;1068--1069, not including "2. Basic Architecture").

2. Section 10: Latency and Throughput (p.&nbsp;1078, not including "11. Related Work").

Key points: Most of the paper is concerned with database topics that are outside the scope of this course. However, the two sections I selected respond to two themes of the course:

* The relation between scalability, availability, and latency. The F1 team claims to have found a unique design point in that space.
* Latency, replication, and distribution across data centres. The Paxos algorithm they mention is a quorum algorithm that requires a quorum of instances to be available in order to run. 