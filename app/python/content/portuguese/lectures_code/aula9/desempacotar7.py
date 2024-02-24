# Imprime argumentos posicionais

def f(*args, **kwargs):
    print("Posicional:", args)

f(100, 50, 25)