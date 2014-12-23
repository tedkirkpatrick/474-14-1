---
layout: course
title: Learning Outcomes
outcomes-activation: class="active"
---
By the end of this course, you will be able to:

<ul class="list">
{% for outcome in site.data.outcomes %}
  <li>{{ outcome[1].full }}<br/>Level: {{ outcome[1].level }}</li>
{% endfor %}
</ul>
   
The outcomes levels are taken from the revised Bloom
taxonomy. 'Remember' is the simplest level, while 'Create' is
the most sophisticated.