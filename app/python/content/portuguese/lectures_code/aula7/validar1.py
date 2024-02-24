# Valida o endereço de e-mail verificando a presença de . também

email = input("Qual é o seu e-mail? ").strip()

if "@" in email and "." in email:
    print("Válido")
else:
    print("Inválido")