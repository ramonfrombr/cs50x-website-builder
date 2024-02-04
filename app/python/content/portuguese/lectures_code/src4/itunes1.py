# Demonstração de json

import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

resposta = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(json.dumps(resposta.json(), indent=2))