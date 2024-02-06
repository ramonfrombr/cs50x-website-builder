from string import Template

blank_template = Template("""{% extends '${course}/layout.html' %} {% block content %} {{markdown_text | safe}}
{%endblock%}
""")

index_template = Template("""{% extends '${course}/layout.html' %} {% block content %} {{markdown_text | safe}}

<img
  style="margin-top: 100px"
  id="logo"
  alt="CS50"
  src="{{ url_for('static', filename='images/'+config['LANGUAGE']+'.png') }}"
/>
{% endblock %}
""")

layout_template = Template("""<!DOCTYPE html>

<html lang="en-us">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <meta
      property="og:description"
      content=""
    />

    <meta property="og:image" content="" />
    <meta property="og:title" content="CS50" />
    <link
      href="https://cs50.harvard.edu/summer/2020/favicon.ico?1593528821"
      rel="icon"
    />

    <script
      src="https://kit.fontawesome.com/df44463090.js"
      crossorigin="anonymous"
    ></script>

    <link
      href="{{ url_for('static', filename='css/all.min.css') }}"
      rel="stylesheet"
    />

    <link
      href="{{ url_for('static', filename='css/page.css') }}"
      rel="stylesheet"
    />

    <link
      rel="stylesheet"
      type="text/css"
      href="{{ url_for('static', filename='css/personalizado.css') }}"
    />

    <!-- http://getbootstrap.com/docs/4.5/getting-started/introduction/ -->
    <script src="{{ url_for('static', filename='js/jquery.min.js') }}"></script>
    <script src="{{ url_for('static', filename='js/popper.min.js') }}"></script>
    <script src="{{ url_for('static', filename='js/bootstrap.min.js') }}"></script>

    <!-- https://momentjs.com/, https://momentjs.com/timezone/ -->
    <script src="{{ url_for('static', filename='js/moment.min.js') }}"></script>
    <script src="{{ url_for('static', filename='js/moment-timezone-with-data.min.js') }}"></script>
    <script src="{{ url_for('static', filename='js/luxon.min.js') }}"></script>

    <!-- https://www.algolia.com/doc/guides/building-search-ui/installation/js/ -->
    <script src="{{ url_for('static', filename='js/algoliasearchLite.min.js') }}"></script>
    <script src="{{ url_for('static', filename='js/instantsearch.production.min.js') }}"></script>
    <script src="{{ url_for('static', filename='js/jekyll-theme-cs50.js') }}"></script>

    <script src="{{url_for('static', filename="highlight/highlight.min.js")}}"></script>
    <link
      rel="stylesheet"
      type="text/css"
      href="{{ url_for('static', filename='highlight/styles/vs.min.css') }}"
    />
    <script>hljs.initHighlightingOnLoad();</script>

    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.8.0/dist/mermaid.min.js"></script>

    <style>

      code {
        border: 1px solid #dee2e6;
      }

      pre {
        padding: 0 !important;
      }

      /* Don't shrink these */
      code,
      pre {
        font-size: inherit;
      }

      .mermaid {
        background-color: white !important;
        border: none !important;
      }
    </style>
    <title>{{config['LANGUAGE_MENU_${course}'].title}}</title>
  </head>

  <body>
    <!-- Markdown Flux Diagrams -->
    <script type="module">
      mermaid.initialize({ startOnLoad: true });
    </script>
    <div class="container-fluid">
      <div class="row">
        {% include '${course}/components/menu.html' %}
        <main class="col-md markdown-body" style="margin-bottom: 286px">
          {% block content %} {% endblock %}
        </main>
      </div>
    </div>
  </body>
</html>
""")

menu_template = Template("""<aside class="col-md" style="background-color: {{config['ASIDE_BG_COLOR']}}">
  <header>
    <h2 data-id="this-is-cs50">
      <a href="{{ url_for('${course}.index') }}"
        >{{config['LANGUAGE_MENU_${course}'].title}}</a
      >
    </h2>
  </header>

  <button
    aria-controls="nav"
    aria-expanded="false"
    class="btn btn-sm collapsed d-md-none"
    data-target="aside &gt; nav"
    data-toggle="collapse"
  >
    Menu
  </button>

  <nav class="collapse d-md-block" id="nav">
    <hr />
    <ul class="fa-ul">
      <li data-marker="*">
        <span class="fa-li"><i class="fas fa-circle"></i></span>
        <a href="{{ url_for('${course}.weeks.week0') }}"
          >{{config['LANGUAGE_MENU'].week}} 0
          <span class="week-title"
            >{{config['LANGUAGE_MENU_${course}'].week0}}</span
          ></a
        >
      </li>
      <li data-marker="*">
        <span class="fa-li"><i class="fas fa-circle"></i></span>
        <a href="{{ url_for('${course}.weeks.week1') }}"
          >{{config['LANGUAGE_MENU'].week}} 1
          <span class="week-title"
            >{{config['LANGUAGE_MENU_${course}'].week1}}</span
          ></a
        >
      </li>

      <li data-marker="*">
        <span class="fa-li"><i class="fas fa-circle"></i></span>
        <a href="{{ url_for('${course}.weeks.week2') }}"
          >{{config['LANGUAGE_MENU'].week}} 2
          <span class="week-title"
            >{{config['LANGUAGE_MENU_${course}'].week2}}</span
          ></a
        >
      </li>

      <li data-marker="*">
        <span class="fa-li"><i class="fas fa-circle"></i></span>
        <a href="{{ url_for('${course}.weeks.week3') }}"
          >{{config['LANGUAGE_MENU'].week}} 3
          <span class="week-title"
            >{{config['LANGUAGE_MENU_${course}'].week3}}</span
          ></a
        >
      </li>

      <li data-marker="*">
        <span class="fa-li"><i class="fas fa-circle"></i></span>
        <a href="{{ url_for('${course}.weeks.week4') }}"
          >{{config['LANGUAGE_MENU'].week}} 4
          <span class="week-title"
            >{{config['LANGUAGE_MENU_${course}'].week4}}</span
          ></a
        >
      </li>

      <li data-marker="*">
        <span class="fa-li"><i class="fas fa-circle"></i></span>
        <a href="{{ url_for('${course}.weeks.week5') }}"
          >{{config['LANGUAGE_MENU'].week}} 5
          <span class="week-title"
            >{{config['LANGUAGE_MENU_${course}'].week5}}</span
          ></a
        >
      </li>

      <li data-marker="*">
        <span class="fa-li"><i class="fas fa-circle"></i></span>
        <a href="{{ url_for('${course}.weeks.week6') }}"
          >{{config['LANGUAGE_MENU'].week}} 6
          <span class="week-title"
            >{{config['LANGUAGE_MENU_${course}'].week6}}</span
          ></a
        >
      </li>

      <li data-marker="*">
        <span class="fa-li"><i class="fas fa-circle"></i></span>
        <a href="{{ url_for('${course}.weeks.week7') }}"
          >{{config['LANGUAGE_MENU'].week}} 7
          <span class="week-title"
            >{{config['LANGUAGE_MENU_${course}'].week7}}</span
          ></a
        >
      </li>

      <li data-marker="*">
        <span class="fa-li"><i class="fas fa-circle"></i></span>
        <a href="{{ url_for('${course}.weeks.week8') }}"
          >{{config['LANGUAGE_MENU'].week}} 8
          <span class="week-title"
            >{{config['LANGUAGE_MENU_${course}'].week8}}</span
          ></a
        >
      </li>

      <li data-marker="*">
        <span class="fa-li"><i class="fas fa-circle"></i></span>
        <a href="{{ url_for('${course}.weeks.week9') }}"
          >{{config['LANGUAGE_MENU'].week}} 9
          <span class="week-title"
            >{{config['LANGUAGE_MENU_${course}'].week9}}</span
          ></a
        >
      </li>
    </ul>
    
    <hr />

    <ul class="fa-ul">
      <li data-marker="*">
        <span class="fa-li"><i class="fas fa-circle"></i></span>
        <a href="{{ url_for('${course}.honesty') }}"
          >{{config['LANGUAGE_MENU'].honesty}}</a
        >
      </li>
      <li data-marker="*">
        <span class="fa-li"><i class="fas fa-circle"></i></span>
        <a href="{{ url_for('${course}.certificate') }}"
          >{{config['LANGUAGE_MENU'].certificate}}</a
        >
      </li>
      <li data-marker="*">
        <span class="fa-li"><i class="fas fa-circle"></i></span>
        <a href="{{ url_for('${course}.faqs') }}"
          >{{config['LANGUAGE_MENU'].faqs}}</a
        >
      </li>
      <li data-marker="*">
        <span class="fa-li"><i class="fas fa-circle"></i></span>
        <a href="https://cs50.me/cs50${course_first_letter}">{{config['LANGUAGE_MENU'].gradebook}}</a>
      </li>
      <li data-marker="*">
        <span class="fa-li"><i class="fas fa-circle"></i></span>
        <a href="{{ url_for('${course}.staff') }}"
          >{{config['LANGUAGE_MENU'].staff}}</a
        >
      </li>
      <li data-marker="*">
        <span class="fa-li"><i class="fas fa-circle"></i></span>
        <a href="{{ url_for('${course}.syllabus') }}"
          >{{config['LANGUAGE_MENU'].syllabus}}</a
        >
      </li>
    </ul>
              
    <hr />
    {% include 'components/courses.html' %}
    <hr />
  </nav>
  <footer></footer>
</aside>
""")