# Usa argumento de linha de comando

import sys

if len(sys.argv) == 1:
    print("miau")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("miau")
else:
    print("uso: miaus11.py [-n NÚMERO]")