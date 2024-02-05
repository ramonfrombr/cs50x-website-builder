# Usa classe


class Conta:
    def __init__(self):
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, n):
        self._saldo += n

    def sacar(self, n):
        self._saldo -= n


def principal():
    conta = Conta()
    print("Saldo:", conta.saldo)
    conta.depositar(100)
    conta.sacar(50)
    print("Saldo:", conta.saldo)


if __name__ == "__main__":
    principal()