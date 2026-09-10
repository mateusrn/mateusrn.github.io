---
layout: home
title: THINK
---

## Posts

{% for post in site.posts %}
- <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span> [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
