# Muestra el paquete instalado con pip

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hola, " + sys.argv[1])