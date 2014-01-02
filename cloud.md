---
layout: course
title: Sequence of assignments for cloud software
commentary: commentary
---

This page specifies the requirements for
{{site.serName}}. It is intended for the {{site.serName}} implementor,
not for the students in the class. The individual assignment pages
will describe the assignments for the students.

All assignments for {{site.serName}} will be in Python 3, so the APIs should all be in Python.

All assignments for {{site.serName}} will be done in groups of 3--4
and completed in one week. The workload should be commensurate with
that level of effort (18--24 programmer-hours per week).

To add to general specification:

 * CLIENT ROBOTS. 
 * OVERARCHING application narrative.

<h2 id="instance-sequence">Instance-level sequence</h2>

The first sequence of projects will run Week&nbsp;3--Week&nbsp;5,
inclusive, which runs Jan&nbsp;20--Feb&nbsp;9. The server must have
the functionality up to that necessary to support the
[latency](#latency) project by Jan&nbsp;20.

In the weeks before Jan.&nbsp;20, the TA should focus on getting the
{{site.serName}} software to run, downplaying interaction with the
students.

<h3 id="single">Single instance</h3>

The first assignment will require a simple, single instance. The
instance will not have any updatable store (that gets added in the
[key-value database step](#keyvalue)), although it might have a
read-only store, such as the music database.

I would prefer that students not need to know the details of REST
parsing and so forth. They should simply write functions that will be
called with fixed parameters when a service is requested.

This first sequence of assignments (up to and including [latency
control](#latency)) should require only simple computation, one
eligible for massive parallelism. The actual work of an individual
step is immaterial---we can fatten the latency as necessary in the
later steps.

Note that for some students, this will be their first assignment in
Python. I will be working with students in some class sessions, with
class members who are experienced Python programmers working with
students who are new or inexperienced with the language. The
assignment for [Week&nbsp;2](python-intro.html) will get the students
up to speed on the basics. Groups will be organized so that there is
at least one experienced Python programmer on each team.

<h3 id="cluster">Cluster instance</h3>

The students will next structure their application as a compute
cluster, spreading the computation from the previous week across
multiple instances in a master-minion organization. I suggest that the
synchronization be done by
[{{site.data.bibliography.hintjens2013.tooltitle}}]({{site.data.bibliography.hintjens2013.url}})
but am open to other suggestions. An [outstanding
issue](outstanding.html) of the course is that I have not yet written a
basic ZMQ application to do this kind of stuff.

<h3 id="latency">Latency control</h3>

In the final step of the sequence, students will implement
latency-control, using either the hedged request or tied request
techniques described on pp.&nbsp;77--78 of
[{{site.data.bibliography.dean2013.title}}]({{site.data.bibliography.dean2013.url}}).

This will require that {{site.serName}} provide a knob for the
instructor to define test cases where instances take extremely long
times or even outright fail. (Taking a long time is a required feature
for {{site.serName}}; failing outright is optional but would be nice
to have---it requires students to handle time outs rather than just
wait for a delayed response, however long it takes.)

<h2 id="cluster-sequence">Cluster-level infrastructure sequence</h2>

This sequence of assignments emphasizes using cluster-level
infrastructure (as defined in Sect.&nbsp;2.4 of
[{{site.data.bibliography.barroso2013.title}}]({{site.data.bibliography.barroso2013.url}})). It
will begin after the midterm and run Week&nbsp;7--Week&nbsp;13,
Feb.&nbsp;10--April&nbsp;9.

By this point in the semester, the teams should all be competent
Python programmers, although the expertise will vary across
individuals within a team.

To expand:

 * Correspondence of infrastructure here and AWS features (perhaps Google as well?)

<h3 id="keyvalue">Key-value database</h3>

Key-value database, perhaps [{{site.data.bibliography.basho2013home.tooltitle}}]({{site.data.bibliography.basho2013home.url}}).

<h3 id="infrastructure">Cluster-level infrastructure</h3>

Cluster-level infrastructure. Because!

<h3 id="cap">Trading off consistency, availability, and compensation</h3>

CAP.

<h3 id="perfanalysis">Performance analysis</h3>

Performance analysis.

<h3 id="logging">Logging</h3>

Logging.

<h3 id="robust">Robust system</h3>

Robust version.

<h3 id="final">Final report</h3>

Final report.