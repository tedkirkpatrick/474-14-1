---
layout: course
title: Schedule
sched-activation: class="active"
---
The working schedule for the course. Future weeks and classes are tentative and subject to change. Past weeks and classes (indicated by a dark background) can only be modified by [Internet time travelers](http://arxiv.org/abs/1312.7128).

<table class="table">
<caption class="ignore-caption">Planned topics, readings, in-class activities, and out-of-class assignments</caption>
<thead><tr>
<th scope="col">Week</th><th scope="col">Classes</th><th scope="col">Outcomes (level)</th><th scope="col">Readings</th><th scope="col">Activities</th><th scope="col">Assignments</th>
</tr></thead>
<tbody>
{% for item in site.data.schedule %}
	<tr class="{{item.completed}}">
		<td>{{ item.week }}</td>
                <td>
                        {% for day in item.days %}
                           <a href="Week{{ item.week }}-{{ day.prefix }}.html" class="{{day.completed}}">{{ day.prefix }}</a><br/>
                        {% endfor %}
                </td>
		<td>{{ item.outcomes | xml_escape }}</td>
		<td>
			{% for entry in item.readings %}
				<a href="{{ site.data.bibliography[entry.tag].url | escape }}">
					{{ site.data.bibliography[entry.tag].title | xml_escape }}
					{% for sect in entry.sect %}
					   , {{ sect }}
					{% endfor %}
				</a><br/>
			{% endfor %}
		</td>
		<td>
			{% for activity in item.activities %}
			   {{ activity.name }}
			{% comment %}
			   <a href="{{ activity.url | escape }}">{{ activity.name | xml_escape }}</a>
			{% endcomment %}
			{% endfor %}
		</td>
		<td>
			{% for assignment in item.assignments %}
			   <a href="{{ assignment.url | escape }}">{{ assignment.name | xml_escape }}</a>
			{% endfor %}
		</td>
	</tr>
{% endfor %}
</tbody>
</table>

{% comment %}
Week 1

* [Day 2](Week1-Day2.html "Week 1, Day 2")
* [Day 1](Week1-Day1.html "Week 1, Day 1")
{% endcomment %}