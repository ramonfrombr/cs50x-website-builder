# Remove o ponto de interrupção


def principal():
    x = receber_inteiro()
    print(f"x é {x}")


def receber_inteiro():
    while True:
        try:
            x = int(input("Qual é o valor de x? "))
        except ValueError:
            print("x não é um número inteiro")
        else:
            return x


principal()