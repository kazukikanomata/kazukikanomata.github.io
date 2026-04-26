---
layout: page
title: Learning
---

技術的な学びを記録するページです。

{% assign sorted = site.learning | sort: 'date' | reverse %}
{% for entry in sorted %}

<div style="margin-bottom: 1.5rem; padding-bottom: 1.5rem; border-bottom: 1px solid #eee;">
  <time style="font-size: 0.85em; color: #999;">{{ entry.date | date: "%Y-%m-%d" }}</time>
  <h2 style="margin: 0.25rem 0; font-size: 1.1rem;"><a href="{{ site.baseurl }}{{ entry.url }}">{{ entry.title }}</a></h2>
</div>
{% endfor %}

{% if site.learning.size == 0 %}
まだエントリがありません。
{% endif %}
