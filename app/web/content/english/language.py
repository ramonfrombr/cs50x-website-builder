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
    "title": "Web Programming with Python and JavaScript",
    "intro": "",
    "week": "Week",
    "week0": "HTML, CSS",
    "week1": "Git",
    "week2": "Python",
    "week3": "Django",
    "week4": "SQL, Models, and Migrations",
    "week5": "JavaScript",
    "week6": "User Interfaces",
    "week7": "Testing, CI/CD",
    "week8": "Scalability and Security",
    "week9": "",
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
    "name": "HTML, CSS",
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
    "name": "Git",
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
    "name": "Python",
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
    "name": "Django",
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
    "name": "SQL, Models, and Migrations",
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
    "name": "JavaScript",
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
    "name": "User Interfaces",
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
    "name": "Testing, CI/CD",
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
    "name": "Scalability and Security",
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
    "name": "",
    "number": 9,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
}

week_10: IWeek = {
    "name": "",
    "number": 10,
    "study_guide": "",
    "lecture_url": "",
    "lecture_embed_url": "",
    "pdf_code_link": "",
    "zip_code_link": "",
    "google_slides_link": "",
    "pdf_slides_link": "",
}
