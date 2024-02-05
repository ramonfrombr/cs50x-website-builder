# Ignora consulta e fragmento

import re

url = input("URL: ").strip()

correspondencias = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)
if correspondencias:
    print("Nome de usuário:", correspondencias.group(1))