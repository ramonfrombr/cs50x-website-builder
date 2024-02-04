# Demonstração de IndexError

import sys

try:
    print("olá, meu nome é", sys.argv[1])
except IndexError:
    print("Argumentos insuficientes")