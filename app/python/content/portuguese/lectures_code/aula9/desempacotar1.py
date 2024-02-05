# Passa argumentos posicionais como de costume
# https://harrypotter.fandom.com/wiki/Wizarding_currency


def total(galeoes, sicles, nuts):
    return (galeoes * 17 + sicles) * 29 + nuts


print(total(100, 50, 25), "Nuts")