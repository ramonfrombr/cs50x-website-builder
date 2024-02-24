# Demuestra módulo propio

import sys

from dichos1 import hola

if len(sys.argv) == 2:
    hola(sys.argv[1])