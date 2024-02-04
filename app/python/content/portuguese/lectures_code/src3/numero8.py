# Adiciona pass


def principal():
    x = receber_inteiro()
    print(f"x é {x}")


def receber_inteiro():
    while True:
        try:
            return int(input("Qual é o valor de x? "))
        except ValueError:
            pass


principal()