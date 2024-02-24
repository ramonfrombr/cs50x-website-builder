# Imprime los argumentos con nombre


def f(*args, **kwargs):
    print("Con nombre:", kwargs)


f(galeones=100, sickles=50, knuts=25)