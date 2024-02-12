# Utiliza grupo de captura

import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print("Nombre de usuario:", matches.group(1))