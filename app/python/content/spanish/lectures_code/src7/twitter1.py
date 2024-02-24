# Extrae el nombre de usuario de Twitter de la URL utilizando str.removeprefix

url = input("URL: ").strip()

nombre_usuario = url.removeprefix("https://twitter.com/")
print(f"Nombre de usuario: {nombre_usuario}")