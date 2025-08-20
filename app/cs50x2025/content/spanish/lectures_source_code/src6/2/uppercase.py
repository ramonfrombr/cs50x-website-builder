# String en mayúsculas

from cs50 import get_string

s = get_string("Antes: ")
print("Después: ", end="")
print(s.upper())