from primo import eh_primo


def testar_primo(n, esperado):
    if eh_primo(n) != esperado:
        print(f"ERRO em eh_primo({n}), esperado {esperado}")