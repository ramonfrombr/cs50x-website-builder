# Adiciona um loop

while True:
    try:
        x = int(input("Qual é o valor de x? "))
    except ValueError:
        print("x não é um número inteiro")
    else:
        break

print(f"x é {x}")