# Verificar __name__

def principal():
    hola("mundo")
    adios("mundo")

def hola(nombre):
    print(f"hola, {nombre}")

def adios(nombre):
    print(f"adiós, {nombre}")

if __name__ == "__main__":
    principal()