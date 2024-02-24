# Añade descripción, ayuda

import argparse

parser = argparse.ArgumentParser(description="Maullar como un gato")
parser.add_argument("-n", help="número de veces para maullar")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("miau")