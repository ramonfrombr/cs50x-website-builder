# Valida la dirección de correo electrónico comprobando la presencia de @

email = input("¿Cuál es tu correo electrónico? ").strip()

if "@" in email:
    print("Válido")
else:
    print("Inválido")