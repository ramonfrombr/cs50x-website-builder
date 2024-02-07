def anunciar(f):
    def envelope():
        print("Prestes a executar a função...")
        f()
        print("Função executada com sucesso.")
    return envelope

@anunciar
def ola():
    print("Olá, mundo!")

ola()
