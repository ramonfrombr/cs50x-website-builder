# Utiliza re.sub

import re

url = input("URL: ").strip()

nome_de_usuario = re.sub(r"^https://twitter\.com/", "", url)
print(f"Nome de usuário: {nome_de_usuario}")