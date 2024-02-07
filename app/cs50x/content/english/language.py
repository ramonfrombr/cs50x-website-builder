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
    courses: str

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
    study_guide: str

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
    "title": "This is CS50x",
    "intro": "Harvard University's computer science course",
    "week": "Week",
    "week2": "Arrays",
    "week3": "Algorithms",
    "week4": "Memory",
    "week5": "Data Structures",
    "cybersecurity": "Cybersecurity",
    "seminars": "Seminars",
    "project": "Final Project",
    "honesty": "Academic Honesty",
    "certificate": "CS50 Certificate",
    "faqs": "FAQs",
    "gradebook": "Gradebook",
    "staff": "Staff",
    "syllabus": "Course Syllabus",
    "office_hours": "Office Hours",
    "psets": "Problem Listss",
    "sections": "Reviews",
    "python_documentation": "Python Documentation",
    "adminer": "PostgreSQL Browser",
    "sqlite_browser": "SQLite Browser",
    "manual": "Programmer's Manual",
    "style": "Style Guide",
    "courses": "Courses"
}

week_page: IWeekPage = {
    "week": "Week",
    "lecture": "Lecture",
    "audio": "Audio",
    "notes": "Notes",
    "slides": "Slides",
    "source_code": "Source Code",
    "subtitles": "SubtitlesLegendas",
    "transcript": "Transcript",
    "video": "Video",
    "shorts": "Important Topics",
    "section": "Review",
    "practice_problems": "Practice Problems",
    "lab": "Lab",
    "problem_set": "Problem List",
    "study_guide": "Study Guide"
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
            "name": "Data Types",
            "link": ""
        },
        "operators":{
            "name": "Operators",
            "link": ""
        },
        "conditionals": {
            "name": "Conditional Statements",
            "link": ""
        },
        "loops": {
            "name": "Loops",
            "link": ""
        },
    }
}

week_2: IWeekAfter0 = {
    "name": "Arrays",
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
            "name": "Functions",
            "link": ""
        },
        "variables_and_scope": {
            "name": "Variables and Scope e Escopo",
            "link": ""
        },
        "debugging_step_through": {
            "name": "Debugging (“Step through”)",
            "link": ""
        },
        "debugging_step_into": {
            "name": "Debugging (“Step into”)",
            "link": ""
        },
        "arrays": {
            "name": "Arrays",
            "link": ""
        },
        "command_line_arguments": {
            "name": "Command Line Arguments",
            "link": ""
        },
    }
}

week_3: IWeekAfter0 = {
    "name": "Algorithms",
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
            "name": "Linear Search",
            "link": ""
        },
        "binary_search": {
            "name": "Binary Search",
            "link": ""
        },
        "bubble_sort":  {
            "name": "Bubble Sort",
            "link": ""
        },
        "selection_sort":  {
            "name": "Selection Sort",
            "link": ""
        },
        "insertion_sort": {
            "name": "Insertion Sort",
            "link": ""
        },
        "recursion":  {
            "name": "Recursion",
            "link": ""
        },
        "merge_sort":  {
            "name": "Merge Sort", 
            "link": ""
        },
        "algorithms_summary": {
            "name": "Algorithms Summary",
            "link": "",
        }
    }
}

week_4: IWeekAfter0 = {
    "name": "Memory",
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
            "name": "Hexadecimal System",
            "link": ""
        },
        "pointers": {
            "name": "Pointers",
            "link": ""
        },
        "custom_types": {
            "name": "Defining Custom Types",
            "link": ""
        },
        "memory_allocation": {
            "name": "Dynamic Memory Allocation",
            "link": ""
        },
        "call_stacks": {
            "name": "Call Stacks",
            "link": ""
        },
        "file_pointers": {
            "name": "File Pointers",
            "link": ""
        },
    }
}

week_5: IWeekAfter0 = {
    "name": "Data Structures",
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
            "name": "Data Structures",
            "link": ""
        },
        "structures": {
            "name": "Structures",
            "link": ""
        },
        "linked_lists": {
            "name": "Singly-Linked Lists",
            "link": ""
        },
        "doubly_linked_lists": {
            "name": "Doubly-Linked Lists",
            "link": ""
        },
        "hash_tables": {
            "name": "Hash Tables",
            "link": ""
        },
        "tries": {
            "name": "Tries",
            "link": ""
        },
        "queues": {
            "name": "Queues",
            "link": ""
        },
        "stacks": {
            "name": "Stacks",
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
            "name": "Internet Primer",
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

cybersecurity: IWeek  = {
    "name": "Cybersecurity",
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