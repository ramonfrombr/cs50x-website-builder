# Demonstra embaralhamento

import random

cartas = ["valete", "dama", "rei"]
random.shuffle(cartas)
for carta in cartas:
    print(carta)