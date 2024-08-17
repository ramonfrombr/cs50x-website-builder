# Salir con valor explícito, importando argv y exit

de sys import argv, exit

si len(argv) != 2:
    imprimir("argumento de línea de comandos faltante")
    salir(1)
imprimir(f"hola, {argv[1]}")
salir(0)