# Demuestra un módulo propio

import sys

from dichos2 import adios

if len(sys.argv) == 2:
    adios(sys.argv[1])