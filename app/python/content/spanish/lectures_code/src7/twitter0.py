# Extrae el nombre de usuario de Twitter de la URL usando str.replace

url = input("URL: ").strip()

nombre_usuario = url.replace("https://twitter.com/", "")
print(f"Nombre de usuario: {nombre_usuario}")