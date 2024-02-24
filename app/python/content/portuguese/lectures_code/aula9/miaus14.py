# Adiciona padrão, tipo; remove int()

import argparse

parser = argparse.ArgumentParser(description="Miar como um gato")
parser.add_argument("-n", default=1, help="número de vezes para miar", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("miau")