---
layout: course
title: Schedule
sched-activation: class="active"
---

<table class="commentary table">
<caption>Planned topics, readings, in-class activities, and out-of-class assignments</caption>
<thead><tr>
<th scope="col">Week</th><th scope="col">Outcomes (Bloom 2001 level)</th><th scope="col">Readings</th><th scope="col">Activities</th><th scope="col">Assignments</th>
</tr></thead>
<tbody>
{% for item in site.data.schedule %}
	<tr>
		<td>{{ item.week }}</td>
		<td>{{ item.outcomes | xml_escape }}</td>
		<td>
			{% for entry in item.readings %}
				<a href="{{ site.data.bibliography[entry].url | escape }}">
					{{ site.data.bibliography[entry].title | xml_escape }}
				</a>
			{% endfor %}
		</td>
		<td>
			{% for activity in item.activities %}
			   <a href="{{ activity.url | escape }}">{{ activity.name | escape }}</a>
			{% endfor %}
		</td>
		<td>
			{% for assignment in item.assignments %}
			   <a href="{{ assignment.url | escape }}">{{ assignment.name | escape }}</a>
			{% endfor %}
		</td>
	</tr>
{% endfor %}
</tbody>
</table>

Week 1

* [Day 2](Week1-Day2.html "Week 1, Day 2")
* [Day 1](Week1-Day1.html "Week 1, Day 1")
