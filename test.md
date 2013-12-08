---
layout: course
test: Test
test-activation: class="active"
---

{% assign foo = 'hue' %}

{% if foo != 'hue' %}
It was not equal to hue.
{% else %}
It was equal to hue.
{% endif %}

And here we are, at *St. Alphonzo's Pancake Breakfast*. Does we haz "smart quotes"---even em-dashes?

Testing .{{ page.test }}. .{{ foo }}. and we're done.