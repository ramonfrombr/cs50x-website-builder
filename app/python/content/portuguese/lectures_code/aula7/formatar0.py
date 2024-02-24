# Reformata "last, first" como "first last"

nome = input("Qual é o seu nome? ").strip()
if "," in nome:
    sobrenome, nome = nome.split(", ")
    nome_completo = f"{nome} {sobrenome}"
print(f"olá, {nome_completo}")