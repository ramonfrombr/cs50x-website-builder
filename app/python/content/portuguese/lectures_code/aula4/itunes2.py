# Demonstração de iteração sobre JSON

import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

resposta = requests.get(
    "https://itunes.apple.com/search?entity=song&term=" + sys.argv[1]
)
o = resposta.json()
for resultado in o["results"]:
    print(resultado["trackName"])