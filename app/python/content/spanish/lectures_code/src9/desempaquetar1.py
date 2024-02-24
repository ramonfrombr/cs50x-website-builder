# Pasa los argumentos posicionales como de costumbre
# https://harrypotter.fandom.com/wiki/Wizarding_currency


def total(galeones, sickles, knuts):
    return (galeones * 17 + sickles) * 29 + knuts


print(total(100, 50, 25), "Knuts")