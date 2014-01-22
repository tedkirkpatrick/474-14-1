---
layout: course
title: Week 3, Day 2 (Wednesday, Jan 22)
sched-activation: class="active"
commentary: commentary
---
## In-class activity

### Access key

1. Check: Everyone has an AWS access key ID and secret access key
2. Everyone knows the path to the file containing their access key
3. Test: Access function works

  * Sign on to your EC2 instance.
  * Check if you have git installed (probably not): if the command `which git` displays a path, you **have git**.
  * If you need git, install it: `sudo apt-get install git`.
  * Get the test code: `git clone https://gist.github.com/8553680.git`
  * Run the test:
<pre><code>    cd 8553680
    python
    import testcreds
    testcreds.test('YOUR CREDENTIALS PATH') 
</code></pre>

replacing YOUR CREDENTIALS PATH with the absolute path to your credentials file. The path will begin with `/home/ubuntu/`.

Congratulations! You won't have to do these steps again for this EC2
instance. These changes will be retained even if you stop and then restart
the instance.

### Introduction to Assignment 2

1. Groups of 1 or 2.
2. Form a group using CourSys group facilities. (Form own group, invite another to join yours, accept/decline invitations.)
3. Groups formed by midnight Thursday (tomorrow).



## Reading guide for next class

Read the following before coming to the next class:

**[{{ site.data.bibliography.dean2013.title }}]({{ site.data.bibliography.dean2013.url }})**,
from beginning up to but not including "Cross-request long-term adaptations".

The key points:

* _latency_ is the length of time for a request to complete
* The sources of variability in system response
* The algorithm for hedged requests (p.&nbsp;77)

Less important:

* The middle section on "reducing component variability". This is good
  advice on how to improve response time for individual requests

