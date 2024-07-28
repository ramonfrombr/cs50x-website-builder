from typing import TypedDict


class MenuType(TypedDict):
    title: str
    intro: str
    youtube_link: str
    week: str
    honesty: str
    certificate: str
    faqs: str
    gradebook: str
    staff: str


class MenuCS50xType(MenuType):
    final_project: str
    office_hours: str
    seminars: str
    sections: str
    syllabus: str
    manual: str
    style: str
    python_documentation: str
