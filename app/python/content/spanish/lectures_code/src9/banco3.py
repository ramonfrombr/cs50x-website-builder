# Usa clase

class Cuenta:
    def __init__(self):
        self._balance = 0

    @property
    def saldo(self):
        return self._balance

    def depositar(self, n):
        self._balance += n

    def retirar(self, n):
        self._balance -= n


def principal():
    cuenta = Cuenta()
    print("Saldo:", cuenta.saldo)
    cuenta.depositar(100)
    cuenta.retirar(50)
    print("Saldo:", cuenta.saldo)


if __name__ == "__main__":
    principal()