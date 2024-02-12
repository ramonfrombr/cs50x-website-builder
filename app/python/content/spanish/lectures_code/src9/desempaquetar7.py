# Imprime argumentos posicionales

def f(*args, **kwargs):
    print("Posicional:", args)

f(100, 50, 25)