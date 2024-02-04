# Introduz o continue, break

while True:
    n = int(input("Qual o valor de n? "))
    if n <= 0:
        continue
    else:
        break

for _ in range(n):
    print("miau")