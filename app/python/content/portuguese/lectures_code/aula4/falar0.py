# Demonstração de pacote instalado pelo pip

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("olá, " + sys.argv[1])