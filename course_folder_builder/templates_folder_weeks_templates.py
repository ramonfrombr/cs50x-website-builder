from string import Template

weeks_layout_template = Template("""{% extends '${course}/layout.html' %}
{% block content %}
{% from "${course}/weeks/pset_item_macro.html" import pset_item with context %}
{% from "${course}/weeks/notes_item_macro.html" import notes_item with context %}

<h1>
  {{week_page.week}} {{week.number}}
  <small class="text-muted strong">{{week.name}}</small>
</h1>

<!--
<iframe width="560" height="315" src="{{week.lecture_embed_url}}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
-->

<ul>
  <li data-marker="-">
    {{week_page.lecture}}
    <ul>
      <li data-marker="*">
        <a href="{{week.study_guide}}">{{week_page.study_guide}}</a>
      </li>
      <li data-marker="*">
        <a href="{{week.lecture_url}}">{{week_page.video}}</a>
      </li>
      {{ notes_item(title=week_page.notes, number=week.number) }}

      <li data-marker="-">
        {{week_page.source_code}}
        <ul>
          <li data-marker="*">
            <a target="_blank" href="{{week.pdf_code_link}}">PDF</a>
          </li>
          <li data-marker="*">
            <a target="_blank" href="{{week.zip_code_link}}">Zip</a>
          </li>
        </ul>
      </li>
      <li data-marker="-">
        {{week_page.slides}}
        <ul>
          <li data-marker="*">
            <a target="_blank" href="{{week.google_slides_link}}"
              >Google Slides</a
            >
          </li>
          <li data-marker="*">
            <a target="_blank" href="{{week.pdf_slides_link}}">PDF</a>
          </li>
        </ul>
      </li>
    </ul>
  </li>

  {% if week.shorts %}
  <li data-marker="-">
    {{week_page.shorts}}
    <ol>
      {% for short in week.shorts %} {% if week.shorts[short].link %}
      <li>
        <a target="_blank" href="{{week.shorts[short].link}}"
          >{{week.shorts[short].name}}</a
        >
      </li>
      {% endif %} {% endfor %}
    </ol>
  </li>
  {% endif %} {{ pset_item(title=week_page.problem_set, number=week.number) }}
</ul>
{% endblock %}
""")

weeks_pset_item_macro_template = Template("""{% macro pset_item(number, title) %} {% if number == 0 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.psets.pset0') }}">{{title}} {{number}} </a>
</li>
{% elif number == 1 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.psets.pset1') }}">{{title}} {{number}} </a>
</li>
{% elif number == 2 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.psets.pset2') }}">{{title}} {{number}} </a>
</li>
{% elif number == 3 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.psets.pset3') }}">{{title}} {{number}} </a>
</li>
{% elif number == 4 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.psets.pset4') }}">{{title}} {{number}} </a>
</li>
{% elif number == 5 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.psets.pset5') }}">{{title}} {{number}} </a>
</li>
{% elif number == 6 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.psets.pset6') }}">{{title}} {{number}} </a>
</li>
{% elif number == 7 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.psets.pset7') }}">{{title}} {{number}} </a>
</li>
{% elif number == 8 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.psets.pset8') }}">{{title}} {{number}} </a>
</li>
{% elif number == 9 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.psets.pset9') }}">{{title}} {{number}} </a>
</li>
{% endif %} {% endmacro %}
""")

weeks_notes_item_macro_template = Template("""{% macro notes_item(number, title) %} {% if number == 0 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.notes.notes0') }}">{{title}} </a>
</li>
{% elif week.number == 1 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.notes.notes1') }}">{{title}} </a>
</li>
{% elif week.number == 2 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.notes.notes2') }}">{{title}} </a>
</li>
{% elif week.number == 3 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.notes.notes3') }}">{{title}} </a>
</li>
{% elif week.number == 4 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.notes.notes4') }}">{{title}} </a>
</li>
{% elif week.number == 5 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.notes.notes5') }}">{{title}} </a>
</li>
{% elif week.number == 6 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.notes.notes6') }}">{{title}} </a>
</li>
{% elif week.number == 7 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.notes.notes7') }}">{{title}} </a>
</li>
{% elif week.number == 8 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.notes.notes8') }}">{{title}} </a>
</li>
{% elif week.number == 9 %}
<li data-marker="*">
  <a href="{{ url_for('${course}.notes.notes9') }}">{{title}} </a>
</li>

{% endif %} {% endmacro %}
""")