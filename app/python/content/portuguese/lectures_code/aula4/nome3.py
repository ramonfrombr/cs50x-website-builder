# Demonstra sys.exit

import sys

if len(sys.argv) < 2:
    sys.exit("Argumentos insuficientes")
elif len(sys.argv) > 2:
    sys.exit("Argumentos demais")

print("olá, meu nome é", sys.argv[1])