---
layout: course
title: Week 2, Day 1
sched-activation: class="active"
---
## What am I supposed to get from a reading, in-class activity, or assignment?

Levels of skill (<a href="{{ site.data.bibliography.anderson2000.url }}">{{ site.data.bibliography.anderson2000.title }}</a>, right hand column of table, "2000"):

* Remember (Level 1, Simplest)
* Understand (Level 2)
* Apply (Level 3)
* Analyze (Level 4)
* Evaluate (Level 5)
* Create (Level 6, most complete)

Every [course outcome](outcomes.html) has a specified level of understanding
and every [week](schedule.html) has one or two outcomes. The reading guides
for each day highlight the parts of each reading that are most important for
that week's outcome.

<div class="well">The readings form the basis of what we do in class and tests and assignments. Read them before class, using the reading guide to locate the important points.
</div>

## Architecture of typical Software as a Service (SaaS)

<p><img src="http://deliveryimages.acm.org/10.1145/2400000/2398374/figs/f3.jpg" alt="Typical front-end application pattern"/><br/>
Source:&nbsp;<a href="{{ site.data.bibliography.helland2013.url }}">{{ site.data.bibliography.helland2013.title }}</a>, Fig.&nbsp;3. Copyright ACM, 2013.</p>

### Example---Purchase at Amazon

For the following use case:

1. Purchaser searches a book title using Google/Bing/Yahoo, gets list of 20 links.
2. Clicks on link to book in Amazon, gets page for that book.
3. Clicks to see the book's cover.
4. Adds book to shopping cart.
5. Signs in to Amazon account.
6. Buys book by clicking on "1-Click" button, which automatically sends book to purchaser's home address.

Assume the above figure describes the Amazon book site. For each of the
above steps, which boxes (if any) in the figure take part? When a box
participates, what does it do?

Which of these services has the smallest response time in its SLA (Service Level Agreement)?

_Example:_ Assume the fifth step said, "Buys book and sends to friend's address from address book".  The boxes might participate this way:

1. Session State (within Service) records user's id.
2. Service requests address book from from application data cache, selects friend's address.
3. Service sends book stock ID and shipping address to shipping service (in "Other service" box). Shipping service works asynchronously---the user does not wait, the service proceeds in the background, emailing the user once it's complete.
4. Other &hellip;

## Anonymous poll

On an **unsigned** sheet of paper, briefly complete:

1. I most want to see the class start doing &hellip;
2. I most want to see the class continue doing &hellip;
3. I most want to see the class stop doing &hellip;

## Reading guide for next class

Read the following before coming to the next class:

**[{{ site.data.bibliography.helland2013.title }}]({{ site.data.bibliography.helland2013.url }}), from "A quick refresher on simple queuing theory" (p.&nbsp;55) up to but not including "The drive toward commonality in computing" (p.&nbsp;58).**

The short queuing theory part that begins the reading is optional. 

{% if site.courseId != '474-14-1' %}
**Plumbing and concierge == cluster-level infrastructure.<br/>
'partitioning' in his sense we call 'sharding'.**
{% endif %}

Key points to look for:

* Why the lower-level services have such tight service requirements.
* What is the purpose of the session state?
* What does the back-end do?
* For "Styles of back-end processing" (pp.&nbsp;57--58), the key point for now is that there are a range of styles. In the second half of the course (after the midterm) we will go into these in much more detail.