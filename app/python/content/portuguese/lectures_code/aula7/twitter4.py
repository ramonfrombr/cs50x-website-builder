# Usa grupo de captura

import re

url = input("URL: ").strip()

correspondencias = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if correspondencias:
    print("Nome de usuário:", correspondencias.group(1))