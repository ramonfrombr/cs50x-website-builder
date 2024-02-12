# Valida la dirección de correo electrónico comprobando el nombre de usuario y el dominio por separado

correo_electronico = input("¿Cuál es tu correo electrónico? ").strip()

nombre_usuario, dominio = correo_electronico.split("@")

if nombre_usuario and "." in dominio:
    print("Válido")
else:
    print("Inválido")