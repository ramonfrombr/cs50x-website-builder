# Índices en la lista

# Función para calcular el total en knuts
def total(galeones, sickles, knuts):
    return (galeones * 17 + sickles) * 29 + knuts

# Lista de monedas
monedas = [100, 50, 25]

# Imprime el total de knuts
print(total(monedas[0], monedas[1], monedas[2]), "Knuts")