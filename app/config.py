import os
from .cs50x2024.content.english.language import menu as menu_english
from .cs50x2024.content.spanish.language import menu as menu_spanish
from .cs50x2024.content.french.language import menu as menu_french
from .cs50x2024.content.portuguese.language import menu as menu_portuguese
from .cs50x2024.content.english.language import pages_url as pages_url_english
from .cs50x2024.content.spanish.language import pages_url as pages_url_spanish
from .cs50x2024.content.french.language import pages_url as pages_url_french
from .cs50x2024.content.portuguese.language import pages_url as pages_url_portuguese


class Config(object):
    FREEZER_DESTINATION = "build_" + os.environ["COURSE_LANGUAGE"]


class EnglishConfig(Config):
    LANGUAGE = 'english',
    BACKGROUND_COLOR = '#a51c30'
    TITLE = "CS50x in English"
    INTRO = "CS50’s Introduction to Computer Science"
    DESCRIPTION = "Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, and software engineering. Languages include C, Python, and SQL plus students' choice of: HTML, CSS, and JavaScript (for web development); Java or Swift (for mobile app development); or Lua (for game development). Problem sets inspired by the arts, humanities, social sciences, and sciences. Course culminates in a final project. Designed for concentrators and non-concentrators alike, with or without prior programming experience. Two thirds of CS50 students have never taken CS before. Among the overarching goals of this course are to inspire students to explore unfamiliar waters, without fear of failure, create an intensive, shared experience, accessible to all students, and build community among students."
    MENU_CS50X_2024 = menu_english
    PAGES_URLS = pages_url_english


class SpanishConfig(Config):
    LANGUAGE = 'spanish',
    BACKGROUND_COLOR = 'red'
    TITLE = "CS50x en Español"
    INTRO = "Curso de Introducción a la Ciencia de la Computación de la Universidad de Harvard"
    DESCRIPTION = "Introducción a las empresas intelectuales de la informática y el arte de la programación. Este curso enseña a los estudiantes a pensar de manera algorítmica y resolver problemas de manera eficiente. Los temas incluyen abstracción, algoritmos, estructuras de datos, encapsulación, gestión de recursos, seguridad e ingeniería de software. Los lenguajes incluyen C, Python y SQL, además de la opción de los estudiantes de: HTML, CSS y JavaScript (para el desarrollo web); Java o Swift (para el desarrollo de aplicaciones móviles); o Lua (para el desarrollo de juegos). Los conjuntos de problemas están inspirados en las artes, las humanidades, las ciencias sociales y las ciencias. El curso culmina en un proyecto final. Diseñado para concentradores y no concentradores por igual, con o sin experiencia previa en programación. Dos tercios de los estudiantes de CS50 nunca han tomado CS antes. Entre los objetivos generales de este curso están inspirar a los estudiantes a explorar territorios desconocidos, sin miedo al fracaso, crear una experiencia intensiva y compartida, accesible a todos los estudiantes, y construir comunidad entre los estudiantes."
    MENU_CS50X_2024 = menu_spanish
    PAGES_URLS = pages_url_spanish


class FrenchConfig(Config):
    LANGUAGE = 'french',
    BACKGROUND_COLOR = 'darkblue'
    TITLE = "CS50x en Français"
    INTRO = "Cours d'Introduction à la Science Informatique de l'Université de Harvard"
    DESCRIPTION = "Introduction aux entreprises intellectuelles de l'informatique et à l'art de la programmation. Ce cours enseigne aux étudiants à penser de manière algorithmique et à résoudre des problèmes de manière efficace. Les sujets incluent l'abstraction, les algorithmes, les structures de données, l'encapsulation, la gestion des ressources, la sécurité et l'ingénierie logicielle. Les langages incluent C, Python et SQL, ainsi que le choix des étudiants de : HTML, CSS et JavaScript (pour le développement web) ; Java ou Swift (pour le développement d'applications mobiles) ; ou Lua (pour le développement de jeux). Les ensembles de problèmes sont inspirés des arts, des humanités, des sciences sociales et des sciences. Le cours se termine par un projet final. Conçu pour les étudiants concentrateurs et non concentrateurs, avec ou sans expérience préalable en programmation. Deux tiers des étudiants de CS50 n'ont jamais suivi de cours de CS auparavant. Parmi les objectifs globaux de ce cours figurent l'inspiration des étudiants à explorer des territoires inconnus, sans peur de l'échec, la création d'une expérience intensive et partagée, accessible à tous les étudiants, et la construction d'une communauté entre les étudiants."
    MENU_CS50X_2024 = menu_french
    PAGES_URLS = pages_url_french


class PortugueseConfig(Config):
    LANGUAGE = 'portuguese',
    BACKGROUND_COLOR = 'darkgreen'
    TITLE = "CS50x em Português"
    INTRO = "Curso de Introdução à Ciência da Computação da Universidade de Harvard"
    DESCRIPTION = "Introdução às faculdades intelectuais da ciência da computação e à arte da programação. Este curso ensina os alunos a pensar de forma algorítmica e a resolver problemas de maneira eficiente. Os tópicos incluem abstração, algoritmos, estruturas de dados, encapsulamento, gerenciamento de recursos, segurança e engenharia de software. Os idiomas incluem C, Python e SQL, além da escolha dos alunos de: HTML, CSS e JavaScript (para desenvolvimento web); Java ou Swift (para desenvolvimento de aplicativos móveis); ou Lua (para desenvolvimento de jogos). Os conjuntos de problemas são inspirados nas artes, humanidades, ciências sociais e ciências naturais. O curso culmina em um projeto final. Projetado para concentradores e não concentradores, com ou sem experiência prévia em programação. Dois terços dos alunos do CS50 nunca cursaram CS antes. Entre os objetivos principais deste curso estão inspirar os alunos a explorar águas desconhecidas, sem medo do fracasso, criar uma experiência intensiva e compartilhada, acessível a todos os alunos, e construir uma comunidade entre os alunos."
    MENU_CS50X_2024 = menu_portuguese
    PAGES_URLS = pages_url_portuguese
