# Adiciona verificação de erro

import sys

if len(sys.argv) < 2:
    print("Argumentos insuficientes")
elif len(sys.argv) > 2:
    print("Argumentos demais")
else:
    print("Olá, meu nome é", sys.argv[1])