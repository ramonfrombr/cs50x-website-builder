# Valida una dirección de correo electrónico verificando si el dominio termina en .edu

email = input("¿Cuál es tu correo electrónico? ").strip()

nombreusuario, dominio = email.split("@")

if nombreusuario and dominio.endswith(".edu"):
    print("Válido")
else:
    print("Inválido")