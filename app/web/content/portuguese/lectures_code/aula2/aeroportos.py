aeroportos = [
    {
        "nome": "Aeroporto Internacional de Pequim Capital",
        "codigo": "PEK",
        "país": "China"
    },
    {
        "nome": "Aeroporto Internacional de Los Angeles",
        "codigo": "LAX",
        "país": "Estados Unidos"
    },
    {
        "nome": "Aeroporto de Heathrow de Londres",
        "codigo": "LHR",
        "país": "Reino Unido"
    }
]

for aeroporto in aeroportos:
    print(f"{aeroporto['nome']} ({aeroporto['codigo']}) está em {aeroporto['país']}.")
