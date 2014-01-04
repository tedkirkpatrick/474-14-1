---
layout: course
title: Course readings
readings-activation: class="active"
---
All the readings for this course will be articles for professional programmers and system designers. Most of them have been published in magazines
written for a general computing audience, such as [Communications of the ACM](http://www.acm.org/cacm/ "CACM") and [IEEE Computer](http://www.computer.org/portal/web/computingnow "IEEE Computer"). A few will come from conferences and blog posts.

When a reading is copyrighted, the link will download the article through the SFU Library proxy service. If you are not downloading from an SFU network address, you will be asked to enter your SFU email and password before downloading.

**On the article page, locate the PDF icon and download the article.**

Please do not repost the copyrighted entries somewhere else. Downloading the articles from the original sites allows the author and publisher to track the downlaod count. This rewards the author and encourages the publisher to accept more articles on that topic.

{% comment %}

The following does not work, for reasons I have not beeb able to determine.

## Bibliography

Readings will be taken from the following list (which unfortunately is not sorted in any useful order yet):

{% for item in site.data.bibliography %}

[{{ itemt.title }}]({{ item.url }})<br/>

{% endfor %}

{% endcomment %}