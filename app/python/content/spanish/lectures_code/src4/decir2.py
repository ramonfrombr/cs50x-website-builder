# Demuestra un módulo propio

import sys

from dichos0 import hola

if len(sys.argv) == 2:
    hola(sys.argv[1])