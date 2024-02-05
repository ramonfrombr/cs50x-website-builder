# Demonstração das funções str

nome = input("Qual é o seu nome? ").strip().title()
primeiro, ultimo = nome.split(" ")
print(f"olá, {primeiro}")