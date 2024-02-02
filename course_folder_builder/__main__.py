import sys
import os
from init_templates import root_init_template, blueprint_init_template
from notes_routes_template import notes_routes_template
from psets_routes_template import psets_routes_template
from weeks_routes_template import weeks_routes_template
from root_routes_template import root_routes_template
from language_template import language_template

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
      routes_file.write(weeks_routes_template)
      routes_file.close()

  # Folder variations
  languages = ["english", "french", "spanish", "portuguese"]
  content_folders = ["lectures_code", "notes", "psets", "psets_checks", "psets_code", "specifications"]

  # Folder paths
  course_path = f"./app/{COURSE}"
  notes_path = f"./app/{COURSE}/notes"
  psets_path = f"./app/{COURSE}/psets"
  weeks_path = f"./app/{COURSE}/weeks"
  content_path = f"./app/{COURSE}/content"

  # Blueprints
  create_root(course_path)
  create_blueprint(notes_path, "notes")
  create_blueprint(psets_path, "psets")
  create_blueprint(weeks_path, "weeks")

  # Content folder
  os.mkdir(content_path)
  for language in languages:
    language_path = f"{content_path}/{language}"
    os.mkdir(language_path)

    language_file = open(f"{language_path}/language.py", "w")
    language_file.write(language_template)
    language_file.close()
    
    for folder in content_folders:
      folder_path = f"{language_path}/{folder}"
      os.mkdir(folder_path)

  # Created notes empty files
  for i in range(10):
    note_path = f"{content_path}/english/notes/{i}.md"
    note_file = open(note_path, "w")
    note_file.close()

  # Creates lectures code empty folders
  for i in range(10):
    lectures_code_path = f"{content_path}/english/lectures_code/src{i}"
    os.mkdir(lectures_code_path)

  homepage_path = f"{content_path}/english/homepage.md"
  homepage_path = open(homepage_path, "w")
  homepage_path.close()

  honesty_path = f"{content_path}/english/honesty.md"
  honesty_path = open(honesty_path, "w")
  honesty_path.close()

  faqs_path = f"{content_path}/english/faqs.md"
  faqs_path = open(faqs_path, "w")
  faqs_path.close()

  syllabus_path = f"{content_path}/english/syllabus.md"
  syllabus_path = open(syllabus_path, "w")
  syllabus_path.close()

  staff_path = f"{content_path}/english/staff.md"
  staff_path = open(staff_path, "w")
  staff_path.close()

  project_path = f"{content_path}/english/project.md"
  project_path = open(project_path, "w")
  project_path.close()
