# Adiciona descrição, ajuda

import argparse

parser = argparse.ArgumentParser(description="Miar como um gato")
parser.add_argument("-n", help="número de vezes para miar")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("miau")