# Demonstra uma constante de classe


class Gato:
    MIAUS = 3

    def miau(self):
        for _ in range(Gato.MIAUS):
            print("miau")


gato = Gato()
gato.miau()