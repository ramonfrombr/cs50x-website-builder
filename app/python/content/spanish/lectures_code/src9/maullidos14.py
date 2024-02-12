# Agrega valor por defecto, tipo; remueve int()

import argparse

parser = argparse.ArgumentParser(description="Maullar como un gato")
parser.add_argument("-n", default=1, help="número de veces que maullar", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("miau")