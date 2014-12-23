---
layout: course-table
title: CMPT 474 readings and bibliography
readings-activation: class="active"
table: bibtable
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

## Bibliography

Readings will be taken from the following list (click on the column title to sort by that column):

<table id="{{ page.table }}" class="display">
<caption class="ignore-caption">Bibliography</caption>
<thead>
<tr><th scope="col">Title</th><th scope="col">Type</th><th scope="col">Topic</th></tr>
</thead>
<tbody>
{% for item in site.data.bibliography %}
<tr>
<td><a href="{{ item[1].url | escape }}">{{ item[1].title | escape}}</a></td>
<td>{{ item[1].type | escape }}</td>
<td>{{ item[1].topic | escape }}</td>
</tr>
{% endfor %}
</tbody>
</table>
