# Usa global

saldo = 0


def principal():
    print("Saldo:", saldo)
    deposito(100)
    saque(50)
    print("Saldo:", saldo)


def deposito(n):
    global saldo
    saldo += n


def saque(n):
    global saldo
    saldo -= n


if __name__ == "__main__":
    principal()