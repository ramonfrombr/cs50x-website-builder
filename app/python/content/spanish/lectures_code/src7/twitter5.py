# Ignora la consulta y el fragmento

import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)
if matches:
    print("Nombre de usuario:", matches.group(1))