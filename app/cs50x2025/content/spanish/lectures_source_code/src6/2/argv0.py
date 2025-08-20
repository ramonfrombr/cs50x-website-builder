# Impresión de argumentos de línea de comandos, indexación en argv

from sys import argv

for i in range(len(argv)):
    print(argv[i])