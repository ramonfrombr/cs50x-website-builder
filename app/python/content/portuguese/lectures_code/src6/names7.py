# Acrescenta nomes a uma lista para ordenar

nomes = []

with open("nomes.txt") as arquivo:
    for linha in arquivo:
        nomes.append(linha.rstrip())

for nome in sorted(nomes):
    print(f"olá, {nome}")