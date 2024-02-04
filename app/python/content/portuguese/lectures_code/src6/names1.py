# Armazena nomes em uma lista

nomes = []

for _ in range(3):
    nomes.append(input("Qual é o seu nome? "))

for nome in sorted(nomes):
    print(f"olá, {nome}")