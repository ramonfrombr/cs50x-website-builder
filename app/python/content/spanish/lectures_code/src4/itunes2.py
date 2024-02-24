# Demuestra la iteración sobre JSON

import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

respuesta = requests.get(
    "https://itunes.apple.com/search?entity=song&term=" + sys.argv[1]
)
o = respuesta.json()
for resultado in o["results"]:
    print(resultado["trackName"])