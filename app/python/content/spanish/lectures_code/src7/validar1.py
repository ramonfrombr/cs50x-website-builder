# Valida la dirección de correo electrónico revisando si contiene un .

email = input("Cuál es tu correo electrónico? ").strip()

if "@" in email and "." in email:
    print("Válido")
else:
    print("Inválido")