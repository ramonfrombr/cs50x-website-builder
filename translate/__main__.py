import sys
from translate_functions.translate_notes import translate_notes
from translate_functions.translate_psets import translate_psets
from translate_functions.translate_specifications import translate_specifications
from translate_functions.translate_labs_code import translate_labs_code
from translate_functions.translate_labs_checks import translate_labs_checks
from translate_functions.translate_psets_checks import translate_psets_checks
from translate_functions.translate_lectures_code import translate_lectures_code
from translate_functions.translate_pages import translate_pages
from translate_functions.translate_lectures_scripts import translate_lectures_scripts
from translate_functions.translate_lectures_slides import translate_lectures_slides
from translate_functions.translate_manual import translate_manual
from translate_types import TypeCourse, TypeLanguage, TypeContent
from constants import COURSES, LANGUAGES, ContentTypes
from check_translation import check

# List content types
content_types = list(filter(lambda p: "__" not in p, dir(ContentTypes)))
content_types_lowercase = list(map(lambda s: s.lower(), content_types))
CONTENT_TYPES = content_types_lowercase

print("\n")
print("Translation tool for CS50x Website Builder")
print("##########################################\n")

if len(sys.argv)<4:
    print("To translate...")
    print("Usage: python translate COURSE CONTENT_TYPE LANGUAGE\n")
    print("or to check translations...")
    print("Usage: python translate check COURSE LANGUAGE\n")
    print(f"COURSE can be: {', '.join(COURSES)}\n")
    print(f"CONTENT_TYPE can be: {', '.join(CONTENT_TYPES)}\n")
    print(f"LANGUAGE can be: {', '.join(LANGUAGES)}\n")
    sys.exit()
elif sys.argv[1]=='check':
    check(sys.argv[2], sys.argv[3])
else:
    COURSE: TypeCourse = sys.argv[1]
    CONTENT_TYPE: TypeContent = sys.argv[2]
    LANGUAGE: TypeLanguage = sys.argv[3]
    
    if not COURSE in COURSES:
        raise Exception("Error: Invalid course")
    elif not CONTENT_TYPE in CONTENT_TYPES:
        raise Exception("Error: Invalid content type")
    elif not LANGUAGE in LANGUAGES:
        raise Exception("Error: Invalid language")
    else:
        print("Starting translation")
        match CONTENT_TYPE:
            case ContentTypes.PSETS:
                translate_psets(COURSE, LANGUAGE)
            case ContentTypes.PSETS_CHECKS:
                translate_psets_checks(COURSE, LANGUAGE)
            case ContentTypes.LABS_CODE:
                translate_labs_code(COURSE, LANGUAGE)
            case ContentTypes.LABS_CHECKS:
                translate_labs_checks(COURSE, LANGUAGE)
            case ContentTypes.NOTES:
                translate_notes(COURSE, LANGUAGE)
            case ContentTypes.SPECIFICATIONS:
                translate_specifications(COURSE, LANGUAGE)
            case ContentTypes.PAGES:
                translate_pages(COURSE, LANGUAGE)
            case ContentTypes.LECTURES_SCRIPTS:
                translate_lectures_scripts(COURSE, LANGUAGE)
            case ContentTypes.LECTURES_CODE:
                translate_lectures_code(COURSE, LANGUAGE)
            case ContentTypes.LECTURES_SLIDES:
                translate_lectures_slides(COURSE, LANGUAGE)
            case ContentTypes.MANUAL:
                translate_manual(COURSE, LANGUAGE)
            case _:
                print("Content type not found")
        print("Finished translation")