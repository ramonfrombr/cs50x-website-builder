# Abre y guarda archivos binarios

import sys

from PIL import Image

imagenes = []

for arg in sys.argv[1:]:
    imagen = Image.open(arg)
    imagenes.append(imagen)

imagenes[0].save(
    "disfraces.gif", save_all=True, append_images=[imagenes[1]], duration=200, loop=0
)