from typing import TypedDict

class IMenu(TypedDict):
    title: str
    intro: str
    week: str
    week0: str
    week1: str
    week2: str
    week3: str
    week4: str
    week5: str
    week6: str
    week7: str
    week8: str
    week9: str
    seminars: str
    project: str
    honesty: str
    certificate: str
    faqs: str
    gradebook: str
    staff: str

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
    pdf_code_link: str
    zip_code_link: str
    google_slides_link: str
    pdf_slides_link: str

menu: IMenu = {
    "title": "Introduction to Programming with Python",
    "intro": "CS50x",
    "week": "Week",
    "week0": "Functions, Variables",
    "week1": "Conditionals",
    "week2": "Loops",
    "week3": "Exceptions",
    "week4": "Libraries",
    "week5": "Unit Tests",
    "week6": "File I/O",
    "week7": "Regular Expressions",
    "week8": "Object-Oriented Programming",
    "week9": "Et Cetera",
    "seminars": "",
    "project": "",
    "honesty": "",
    "certificate": "",
    "faqs": "",
    "gradebook": "",
    "staff": "",
}

week_page: IWeekPage = {
    "week": "Week",
    "lecture": "Lecture",
    "audio": "Audio",
    "notes": "Notes",
    "slides": "Slides",
    "source_code": "Source Code",
    "subtitles": "Subtitles",
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
    "name": "Functions, Variables",
    "number": 0,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
}

week_1: IWeek = {
    "name": "Conditionals",
    "number": 1,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
}

week_2: IWeek = {
    "name": "Loops",
    "number": 2,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
}

week_3: IWeek = {
    "name": "Exceptions",
    "number": 3,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
}

week_4: IWeek = {
    "name": "Libraries",
    "number": 4,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
}

week_5: IWeek = {
    "name": "Unit Tests",
    "number": 5,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
}

week_6: IWeek = {
    "name": "File I/O",
    "number": 6,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
}

week_7: IWeek = {
    "name": "Regular Expressions",
    "number": 7,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
}

week_8: IWeek = {
    "name": "Object-Oriented Programming",
    "number": 8,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
}

week_9: IWeek = {
    "name": "Et Cetera",
    "number": 9,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
}
