# Permite http, sin protocolo y www.

import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Nombre de usuario: {username}")