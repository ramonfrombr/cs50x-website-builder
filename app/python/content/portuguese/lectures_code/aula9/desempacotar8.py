# Imprime argumentos nomeados

def f(*args, **kwargs):
    print("Nomeados:", kwargs)

f(galeoes=100, sicles=50, knuts=25)