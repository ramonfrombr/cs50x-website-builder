# UnboundLocalError

saldo = 0


def principal():
    print("Saldo:", saldo)
    depositar(100)
    retirar(50)
    print("Saldo:", saldo)


def depositar(n):
    saldo += n


def retirar(n):
    saldo -= n


if __name__ == "__main__":
    principal()