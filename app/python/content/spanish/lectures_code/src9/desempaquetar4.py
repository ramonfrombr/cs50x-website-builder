# Pasa los argumentos con nombre como de costumbre

def total(galeones, sickles, knuts):
    return (galeones * 17 + sickles) * 29 + knuts

print(total(galeones=100, sickles=50, knuts=25), "Knuts")