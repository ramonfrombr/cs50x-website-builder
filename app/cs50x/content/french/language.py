from typing import TypedDict

class IMenu(TypedDict):
    title: str
    intro: str
    week: str
    week2: str
    week3: str
    week4: str
    week5: str
    cybersecurity: str
    seminars: str
    project: str
    honesty: str
    certificate: str
    faqs: str
    gradebook: str
    staff: str
    syllabus: str
    office_hours: str
    psets: str
    sections: str
    python_documentation: str
    adminer: str
    sqlite_browser: str
    manual: str
    style: str

class IWeekPage(TypedDict):
    week: str
    lecture: str
    audio: str
    notes: str
    slides: str
    source_code: str
    subtitles: str
    transcript: str
    video: str
    shorts: str
    section: str
    practice_problems: str
    lab: str
    problem_set: str

class IWeek(TypedDict):
    name: str
    number: int
    study_guide: str
    lecture_url: str
    lecture_embed_url: str
    google_slides_link: str
    pdf_slides_link: str

class IWeekAfter0(IWeek):
    zip_code_link: str
    pdf_code_link: str
    shorts: dict[str, dict[str, str]]

class IUrls(TypedDict):
    labs: str
    weeks: str
    notes: str
    psets: str
    cybersecurity: str
    seminars: str
    honesty: str
    certificate: str
    faqs: str
    staff: str
    syllabus: str
    project: str
    hello: str
    mario_less: str
    mario_more: str
    cash: str
    credit: str
    readability: str
    bulbs: str
    caesar: str
    substitution: str
    wordle50: str
    plurality: str
    runoff: str
    tideman: str
    filter: str
    recover: str
    reverse: str
    speller: str
    dna: str
    movies: str
    fiftyville: str
    homepage: str
    finance: str
    less: str
    more: str

menu: IMenu = {
    "title": "Ceci est CS50x",
    "intro": "Cours d'informatique de l'Université Harvard",
    "week": "Semaine",
    "week2": "Tableaux",
    "week3": "Algorithmes",
    "week4": "Mémoire",
    "week5": "Structures de données",
    "cybersecurity": "Cybersécurité",
    "seminars": "Séminaires",
    "project": "Projet final",
    "honesty": "Honnêteté académique",
    "certificate": "Certificat CS50",
    "faqs": "FAQs",
    "gradebook": "Carnet de notes",
    "staff": "Personnel",
    "syllabus": "Programme du cours",
    "office_hours": "Heures de bureau",
    "psets": "Liste de problèmes",
    "sections": "Révisions",
    "python_documentation": "Documentation Python",
    "adminer": "Navigateur PostgreSQL",
    "sqlite_browser": "Navigateur SQLite",
    "manual": "Manuel du programmeur",
    "style": "Guide de style"
}

week_page: IWeekPage = {
    "week": "Semaine",
    "lecture": "Cours",
    "audio": "Audio",
    "notes": "Notes",
    "slides": "Diapositives",
    "source_code": "Code source",
    "subtitles": "Sous-titres",
    "transcript": "Transcription",
    "video": "Vidéo",
    "shorts": "Sujets importants",
    "section": "Révision",
    "practice_problems": "Problèmes pratiques",
    "lab": "Laboratoire",
    "problem_set": "Liste de problèmes",
    "study_guide": "Guide d'Études"
}

week_0: IWeek = {
    "name": "Scratch",
    "number": 0,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "google_slides_link": "",
    "pdf_slides_link": ""
}

week_1: IWeekAfter0 = {
    "name": "C",
    "number": 1,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
    "shorts": {
        "data_types": {
            "name": "Types de données",
            "link": ""
        },
        "operators": {
            "name": "Opérateurs",
            "link": ""
        },
        "conditionals": {
            "name": "Instructions conditionnelles",
            "link": ""
        },
        "loops": {
            "name": "Boucles",
            "link": ""
        },
    }
}

week_2: IWeekAfter0 = {
    "name": "Tableaux",
    "number": 2,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
    "shorts": {
        "functions": {
            "name": "Fonctions",
            "link": ""
        },
        "variables_and_scope": {
            "name": "Variables et portée",
            "link": ""
        },
        "debugging_step_through": {
            "name": "Débogage (« Pas à pas »)",
            "link": ""
        },
        "debugging_step_into": {
            "name": "Débogage (« Pas à l'intérieur »)",
            "link": ""
        },
        "arrays": {
            "name": "Tableaux",
            "link": ""
        },
        "command_line_arguments": {
            "name": "Arguments de ligne de commande",
            "link": ""
        },
    }
}


week_3: IWeekAfter0 = {
    "name": "Algorithmes",
    "number": 3,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
    "shorts": {
        "linear_search": {
            "name": "Recherche linéaire",
            "link": ""
        },
        "binary_search": {
            "name": "Recherche binaire",
            "link": ""
        },
        "bubble_sort":  {
            "name": "Tri à bulles",
            "link": ""
        },
        "selection_sort":  {
            "name": "Tri par sélection",
            "link": ""
        },
        "insertion_sort": {
            "name": "Tri par insertion",
            "link": ""
        },
        "recursion":  {
            "name": "Récursivité",
            "link": ""
        },
        "merge_sort":  {
            "name": "Tri fusion", 
            "link": ""
        },
        "algorithms_summary": {
            "name": "Résumé des algorithmes",
            "link": "",
        }
    }
}

week_4: IWeekAfter0 = {
    "name": "Mémoire",
    "number": 4,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
    "shorts": {
        "hexadecimal": {
            "name": "Système hexadécimal",
            "link": ""
        },
        "pointers": {
            "name": "Pointeurs",
            "link": ""
        },
        "custom_types": {
            "name": "Définition de types personnalisés",
            "link": ""
        },
        "memory_allocation": {
            "name": "Allocation dynamique de mémoire",
            "link": ""
        },
        "call_stacks": {
            "name": "Piles d'appels",
            "link": ""
        },
        "file_pointers": {
            "name": "Pointeurs de fichier",
            "link": ""
        },
    }
}

week_5: IWeekAfter0 = {
    "name": "Structures de données",
    "number": 5,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
    "shorts": {
        "data_structures": {
            "name": "Structures de données",
            "link": ""
        },
        "structures": {
            "name": "Structures",
            "link": ""
        },
        "linked_lists": {
            "name": "Listes chaînées simples",
            "link": ""
        },
        "doubly_linked_lists": {
            "name": "Listes chaînées doubles",
            "link": ""
        },
        "hash_tables": {
            "name": "Tables de hachage",
            "link": ""
        },
        "tries": {
            "name": "Tries",
            "link": ""
        },
        "queues": {
            "name": "Files d'attente",
            "link": ""
        },
        "stacks": {
            "name": "Piles",
            "link": ""
        },
    }
}

week_6: IWeekAfter0 = {
    "name": "Python",
    "number": 6,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
    "shorts": {
        "python": {
            "name": "Python",
            "link": ""
        },
    }
}

week_7: IWeekAfter0 = {
    "name": "SQL",
    "number": 7,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
    "shorts": {
        "sql": {
            "name": "SQL",
            "link": ""
        },
    }
}

week_8: IWeekAfter0 = {
    "name": "HTML, CSS, JavaScript",
    "number": 8,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
    "shorts": {
        "internet_primer": {
            "name": "Introduction à Internet",
            "link": ""
        },
        "ip": {
            "name": "IP",
            "link": ""
        },
        "tcp": {
            "name": "TCP",
            "link": ""
        },
        "http": {
            "name": "HTTP",
            "link": ""
        },
        "html": {
            "name": "HTML",
            "link": ""
        },
        "css": {
            "name": "CSS",
            "link": ""
        },
        "javascript": {
            "name": "JavaScript",
            "link": ""
        },
        "dom": {
            "name": "DOM",
            "link": ""
        },
    }
}

week_9: IWeekAfter0 = {
    "name": "Flask",
    "number": 9,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
    "shorts": {
        "flask": {
            "name": "Flask",
            "link": ""
        },
        "ajax": {
            "name": "AJAX",
            "link": ""
        },
    }
}

week_10: IWeek = {
    "name": "Emoji",
    "google_slides_link": "",
    "pdf_slides_link": "",
    "number": 10,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
}

cybersecurity: IWeek = {
    "name": "Cybersécurité",
    "google_slides_link": "",
    "pdf_slides_link": "",
    "number": 11,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
}

urls: IUrls = {
    "labs": "labs",
    "weeks": "weeks",
    "notes": "notes",
    "psets": "problems",
    "cybersecurity": "cybersecurity",
    "seminars": "seminars",
    "honesty": "honesty",
    "certificate": "certificate",
    "faqs": "faqs",
    "staff": "staff",
    "syllabus": "syllabus",
    "project": "project",
    "hello": "hello",
    "mario_less": "mario/less",
    "mario_more": "mario/more",
    "cash": "cash",
    "credit": "credit",
    "readability": "readability",
    "bulbs": "bulbs",
    "caesar": "caesar",
    "substitution": "substitution",
    "wordle50": "wordle50",
    "plurality": "plurality",
    "runoff": "runoff",
    "tideman": "tideman",
    "filter": "filter",
    "recover": "recover",
    "reverse": "reverse",
    "speller": "speller",
    "dna": "dna",
    "movies": "movies",
    "fiftyville": "fiftyville",
    "homepage": "homepage",
    "finance": "finance",
    "less": "less",
    "more": "more",
}
