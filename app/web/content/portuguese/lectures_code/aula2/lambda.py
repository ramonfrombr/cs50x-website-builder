filmes = [
    {"título": "Green Book", "ano": 2018},
    {"título": "A Forma da Água", "ano": 2017},
    {"título": "Moonlight", "ano": 2016},
    {"título": "Spotlight", "ano": 2015},
    {"título": "Birdman", "ano": 2014},
    {"título": "12 Anos de Escravidão", "ano": 2013}
]

filmes.sort(key=lambda filme: filme["ano"])

for filme in filmes:
    print("{título} foi lançado em {ano}".format(**filme))