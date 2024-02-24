# UnboundLocalError

saldo = 0


def principal():
    print("Saldo:", saldo)
    depositar(100)
    sacar(50)
    print("Saldo:", saldo)


def depositar(n):
    saldo += n


def sacar(n):
    saldo -= n


if __name__ == "__main__":
    principal()