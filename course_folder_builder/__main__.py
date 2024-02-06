import sys
import os
from init_templates import root_init_template, blueprint_init_template
from notes_routes_template import notes_routes_template
from psets_routes_template import psets_routes_template
from weeks_routes_template import weeks_routes_template
from root_routes_template import root_routes_template
from language_template import language_template
from pathlib import Path
from templates_folder_templates import blank_template, index_template, layout_template, menu_template
from templates_folder_weeks_templates import weeks_layout_template, weeks_pset_item_macro_template, weeks_notes_item_macro_template
from string import Template

# Folder variations
languages = ["english", "french", "spanish", "portuguese", "japanese", "chinese", "german", "italian", "korean"]
content_folders = ["lectures_code", "notes", "psets", "psets_checks", "psets_code", "specifications"]

if len(sys.argv) != 2:
  print("Usage: python course_folder_builder COURSE_NAME")
  sys.exit(0)
else:
  COURSE = sys.argv[1]

  def create_root(path):
    os.mkdir(path)
    f = open(f"{path}/__init__.py", "w")
    f.write(root_init_template.substitute(course=COURSE))
    f.close()
    f = open(f"{path}/routes.py", "w")
    f.write(root_routes_template.substitute(course=COURSE))
    f.close()

  def create_blueprint(path, blueprint):
    os.mkdir(path)
    init_file = open(f"{path}/__init__.py", "a")
    init_file.write(blueprint_init_template.substitute(blueprint=blueprint))
    init_file.close()

    if blueprint=="notes":
      routes_file = open(f"{path}/routes.py", "a")
      routes_file.write(notes_routes_template.substitute(course=COURSE))
      routes_file.close()
      
    elif blueprint=="psets":
      routes_file = open(f"{path}/routes.py", "a")
      routes_file.write(psets_routes_template.substitute(course=COURSE))
      routes_file.close()

    elif blueprint=="weeks":
      routes_file = open(f"{path}/routes.py", "a")
      routes_file.write(weeks_routes_template.substitute(course=COURSE))
      routes_file.close()

  def create_templates_folder_weeks(path):
    Path(path).mkdir(parents=True, exist_ok=True)
    Path(f"{path}/weeks").mkdir(parents=True, exist_ok=True)

    weeks_layout = open(f"{path}/weeks/layout.html", "w")
    weeks_layout.write(weeks_layout_template.substitute(course=COURSE))
    weeks_layout.close()

    weeks_pset_item_macro = open(f"{path}/weeks/pset_item_macro.html", "w")
    weeks_pset_item_macro.write(weeks_pset_item_macro_template.substitute(course=COURSE))
    weeks_pset_item_macro.close()
    
    weeks_notes_item_macro = open(f"{path}/weeks/notes_item_macro.html", "w")
    weeks_notes_item_macro.write(weeks_notes_item_macro_template.substitute(course=COURSE))
    weeks_notes_item_macro.close()

  def create_templates_folder(path):
    create_templates_folder_weeks(path)

    # Components template folder
    Path(f"{path}/components").mkdir(parents=True, exist_ok=True)
    menu = open(f"{path}/components/menu.html", "w")
    menu.write(menu_template.substitute(course=COURSE, course_first_letter=COURSE[0]))
    menu.close()

    # Language template folders
    for language in languages:
      Path(f"{path}/{language}").mkdir(parents=True, exist_ok=True)
      Path(f"{path}/{language}/psets").mkdir(parents=True, exist_ok=True)

    # Creates blank.html
    blank = open(f"{path}/blank.html", "w")
    blank.write(blank_template.substitute(course=COURSE))
    blank.close()
    # Creates layout.html
    layout = open(f"{path}/layout.html", "w")
    layout.write(layout_template.substitute(course=COURSE))
    layout.close()
    # Creates index.html
    index = open(f"{path}/index.html", "w")
    index.write(index_template.substitute(course=COURSE))
    index.close()

  def create_content_folders(content_folders, language_path):
    for folder in content_folders:
      folder_path = f"{language_path}/{folder}"
      os.mkdir(folder_path)

  def create_language_py_file(language_path):
    language_file = open(f"{language_path}/language.py", "w")
    language_file.write(language_template)
    language_file.close()

  def create_language_folders(content_path):
    for language in languages:
      language_path = f"{content_path}/{language}"
      os.mkdir(language_path)
      create_language_py_file(language_path)
      create_content_folders(content_folders, language_path)

  def create_notes_files(content_path):
    for i in range(10):
      note_path = f"{content_path}/english/notes/{i}.md"
      note_file = open(note_path, "w")
      note_file.close()

  def create_psets_files(content_path):
    for i in range(10):
      psets_path = f"{content_path}/english/psets/{i}.html"
      psets_file = open(psets_path, "w")
      psets_file.close()

  def create_lectures_code_files(content_path):
    for i in range(10):
      lectures_code_path = f"{content_path}/english/lectures_code/src{i}"
      os.mkdir(lectures_code_path)

  def create_certificate_file(content_path):
    certificate_path = f"{content_path}/english/certificate.md"
    certificate_path = open(certificate_path, "w")
    certificate_path.close()

  def create_homepage_file(content_path):
    homepage_path = f"{content_path}/english/homepage.md"
    homepage_path = open(homepage_path, "w")
    homepage_path.close()

  def create_project_file(content_path):
    project_path = f"{content_path}/english/project.md"
    project_path = open(project_path, "w")
    project_path.close()

  def create_syllabus_file(content_path):
    syllabus_path = f"{content_path}/english/syllabus.md"
    syllabus_path = open(syllabus_path, "w")
    syllabus_path.close()

  def create_pages_file(content_path, page):
    page_path = f"{content_path}/english/{page}.md"
    page_file = open(page_path, "w")
    page_file.close()

  def import_menus():
    menu_import_template = Template("""from .${course}.content.${language}.language import menu as menu_${language}_${course}\n""")

    with open('app/__init__.py', 'r+') as f: #r+ does the work of rw
      lines = f.readlines()
      for i, line in enumerate(lines):
        if "# import menus" in line:
          for language in languages:
            lines[i] = lines[i].lstrip() + menu_import_template.substitute(course=COURSE, language=language)
      f.seek(0)
      for line in lines:
          f.write(line)

  def configure_menus():
    menu_config_template = Template("""        app.config["LANGUAGE_MENU_${course}"] = menu_${language}_${course}\n""")

    with open('app/__init__.py', 'r+') as f: #r+ does the work of rw
      lines = f.readlines()
      for i, line in enumerate(lines):
        for language in languages:
          if f'# {language} config' in line:
            lines[i] = "        " + lines[i].lstrip() + menu_config_template.substitute(course=COURSE, language=language) 
      f.seek(0)
      for line in lines:
          f.write(line)

  def register_blueprint():
    blueprint_register_template = Template("""        from .${course} import ${course} as ${course}_bp\n        app.register_blueprint(${course}_bp, url_prefix='/${course}')""")
    
    with open('app/__init__.py', 'r+') as f: #r+ does the work of rw
      lines = f.readlines()
      for i, line in enumerate(lines):
        if '# Blueprint register' in line:
          lines[i] = "        " + lines[i].lstrip() + "\n" + blueprint_register_template.substitute(course=COURSE)
      f.seek(0)
      for line in lines:
          f.write(line)

  # Folder paths
  course_path = f"./app/{COURSE}"
  notes_path = f"./app/{COURSE}/notes"
  psets_path = f"./app/{COURSE}/psets"
  weeks_path = f"./app/{COURSE}/weeks"
  content_path = f"./app/{COURSE}/content"
  templates_path = f"./app/{COURSE}/templates/{COURSE}"

  # Blueprints
  create_root(course_path)
  create_blueprint(notes_path, "notes")
  create_blueprint(psets_path, "psets")
  create_blueprint(weeks_path, "weeks")
  create_templates_folder(templates_path)

  os.mkdir(content_path)

  create_language_folders(content_path)
  create_notes_files(content_path)
  create_psets_files(content_path)
  create_lectures_code_files(content_path)

  pages = ["certificate", "homepage", "project", "syllabus"]
  for page in pages:
    create_pages_file(content_path, page)
  
  import_menus()
  configure_menus()
  register_blueprint()
