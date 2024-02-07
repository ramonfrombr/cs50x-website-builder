import unittest

from primo import eh_primo


class Testes(unittest.TestCase):

    def teste_1(self):
        """Verificar que 1 não é primo."""
        self.assertFalse(eh_primo(1))

    def teste_2(self):
        """Verificar que 2 é primo."""
        self.assertTrue(eh_primo(2))

    def teste_8(self):
        """Verificar que 8 não é primo."""
        self.assertFalse(eh_primo(8))

    def teste_11(self):
        """Verificar que 11 é primo."""
        self.assertTrue(eh_primo(11))

    def teste_25(self):
        """Verificar que 25 não é primo."""
        self.assertFalse(eh_primo(25))

    def teste_28(self):
        """Verificar que 28 não é primo."""
        self.assertFalse(eh_primo(28))


if __name__ == "__main__":
    unittest.main()