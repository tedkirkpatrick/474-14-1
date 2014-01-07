---
layout: course
title: Course readings
readings-activation: class="active"
---
All the readings for this course will be articles for professional
programmers and system designers. Most of them have been published in
magazines written for a general computing audience, such as
[Communications of the ACM](http://www.acm.org/cacm/ "CACM") and [IEEE
Computer](http://www.computer.org/portal/web/computingnow "IEEE
Computer"). A few will come from conferences and blog posts.

## To read a linked article or book

* Click on the link
* If you are not on the SFU network, you may be asked to enter your SFU email id and password.
* If the link is to a blog, you can just read the post
* If the link is to an article or book, you will see a page giving one or more options:

  * Some articles (including all the ones from ACM) will be readable directly as HTML or downloaded as PDF
  * Other articles are only available as PDF

## Caution

Please do not repost the copyrighted entries somewhere else. Downloading the articles from the original sites allows the author and publisher to track the downlaod count. This rewards the author and encourages the publisher to accept more articles on that topic.

{% comment %}

<!-- The following does not work, for reasons I have not been able to determine. -->

## Bibliography

Readings will be taken from the following list (which unfortunately is not sorted in any useful order yet):

{% for item in site.data.bibliography %}

[Title {{ item.title }}]({{ item.url }})<br/>

{% endfor %}

{% endcomment %}