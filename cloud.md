---
layout: course
title: Sequence of assignments for cloud software
commentary: commentary
---

This page specifies the requirements for
{{site.serName}}. It is intended for the {{site.serName}} implementor,
not for the students in the class. The individual assignment pages
will describe the assignments for the students.

All assignments for {{site.serName}} will be in Python, so the APIs should all be in Python.

All assignments for {{site.serName}} will be done in groups of 3--4
and completed in one week. The workload should be commensurate with
that level of effort (18--24 programmer-hours per week).

To add to general specification:

 * CLIENT ROBOTS. 
 * OVERARCHING application narrative.


<section>
	<h1>Izaak's Overview</h1>

	<section>
		<h2>Nomenclature</h2>
		<dl>
			<dt>Instance</dt>
			<dd>
				A single container with assigned virtual network,
				a set of services and an owner.
			</dd>
			
			<dt>Container</dt>
			<dd>
				An LXC container. 
			</dd>
			
			<dt>Service</dt>
			<dd>
				A single program with distinct configuration and setup
				requirements. This program may or may not spawn other
				processes, listen on sockets, manipulate files, etc.
			</dd>

			<dt>Application</dt>
			<dd>
				A collection of services on a non-empty set of instances
				providing some developer-defined functionality to users.
			</dd>
			
			<dt>User</dt>
			<dd>
				An entity which uses an application by accessing its
				services on one or more instances. 
			</dd>

			<dt>Redis</dt>
			<dd>
				A key-value store available as one of the services.
			</dd>
		</dl>
	</section>

	<section>
		<h2>Architecture</h2>
		<p>
			Platform makes use of a variety of Linux tools
			to simulate a large scale cloud platform on
			smaller scale hardware. 
		</p>
	</section>

	<section>
		<h2>Timeline</h2>
		<section>
			<h3>Week 3 - Availability</h3>
			<p>
				Students are given two instances, one with a Redis service, 
				the other with the load-balancer service. Students are to
				explore using the existing code given for the load-balancer.
				The Redis service instance is setup to fail periodically and 
				thus students need to create an appropriate number of new 
				Redis instances that mirror the data such that the global
				failure rate for requests approaches 0.
			</p>
			<p>
				Evaluated by calculating request failures.
			</p>
			<p>
				Learning outcomes / stuff here.
			</p>
		</section>
		<section>
			<h3>Week 4 - Latency</h3>
			<p>
				Student's existing setup, while now containing some redundency,
				does not yet address the problem whereby some requests take 
				longer than others (when a request is made and the instance its
				being made to times out, for example). Students are to address
				this using hedged requests which is a relatively simple extension
				of their work in week 3.
			</p>
		</section>
		<section>
			<h3>Week 5 - Data Partitioning</h3>
			<p>
				Students are required to add more data than can fit in any single
				instance. They must add another two Redis instances and distribute
				their existing and new data amongst all the Redis instances using
				consistent hashing. 
			</p>
		</section>
		<section>
			<h3>Week 6 - Midterm</h3>
			<p>
				No activity.
			</p>
		</section>
		<section>
			<h3>Week 7 - Network Partitioning</h3>
			<p>
				Students add writes.
			</p>
		</section>
		<section>
			<h3>Week 8 - Consistency</h3>
			<p>
				Student's are required to make consistency garantees for their writes.
			</p>
		</section>
		<section>
			<h3>Week 9 - </h3>
			<p>
				
			</p>
		</section>
		<section>
			<h3>Week 10 - </h3>
			<p>
				
			</p>
		</section>
		<section>
			<h3>Week 11 - </h3>
			<p>
				
			</p>
		</section>
		<section>
			<h3>Week 12 - </h3>
			<p>
				
			</p>
		</section>
	</section>

</section>

## Ted's Overview

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

Key-value database, probably [{{site.data.bibliography.citrusbyte2014.tooltitle}}]({{site.data.bibliography.citrusbyte2014.url}}).

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