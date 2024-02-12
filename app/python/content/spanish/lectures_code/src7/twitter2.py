# Utiliza re.sub

import re

url = input("URL: ").strip()

nombre_usuario = re.sub(r"^https://twitter\.com/", "", url)
print(f"Nombre de usuario: {nombre_usuario}")