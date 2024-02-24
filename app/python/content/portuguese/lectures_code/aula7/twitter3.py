# Permite http, sem protocolo e www.

import re

url = input("URL: ").strip()

nome_de_usuario = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Nome de usuário: {nome_de_usuario}")