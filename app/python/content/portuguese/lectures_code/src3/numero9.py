# Adicione prompt


def principal():
    x = receber_inteiro("Qual é o valor de x? ")
    print(f"x é {x}")


def receber_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            pass


principal()