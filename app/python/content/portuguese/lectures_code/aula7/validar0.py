# Valida o endereço de email verificando a presença de @

email = input("Qual é o seu email? ").strip()

if "@" in email:
    print("Válido")
else:
    print("Inválido")