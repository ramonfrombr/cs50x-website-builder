# Demonstração de solicitações

import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

resposta = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(resposta.json())