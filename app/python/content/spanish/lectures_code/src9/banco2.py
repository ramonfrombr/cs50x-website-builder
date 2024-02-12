# Utiliza global

balance = 0


def principal():
    print("Balance:", balance)
    depositar(100)
    retirar(50)
    print("Balance:", balance)


def depositar(n):
    global balance
    balance += n


def retirar(n):
    global balance
    balance -= n


if __name__ == "__main__":
    principal()