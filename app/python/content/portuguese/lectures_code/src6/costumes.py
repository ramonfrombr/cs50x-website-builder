# Abre e salva arquivos binários

import sys

from PIL import Image

imagens = []

for arg in sys.argv[1:]:
    imagem = Image.open(arg)
    imagens.append(imagem)

imagens[0].save(
    "figurinos.gif", save_all=True, append_images=[imagens[1]], duration=200, loop=0
)