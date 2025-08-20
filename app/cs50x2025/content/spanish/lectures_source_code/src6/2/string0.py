# Imprime el caracter del string caracter por caracter, indexando en el string

from cs50 import get_string

s = get_string("Entrada: ")
print("Salida: ", end="")
for i in range(len(s)):
    print(s[i], end="")
print()