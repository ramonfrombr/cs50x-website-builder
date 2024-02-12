# Demuestra una constante de clase


class Gato:
    MAULLIDOS = 3

    def maullar(self):
        for _ in range(Gato.MAULLIDOS):
            print("miau")


gato = Gato()
gato.maullar()