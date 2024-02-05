# Compara várias strings

resposta = input("Você concorda? ").strip().lower()
if resposta.startswith("s"):
    print("Concordou")
else:
    print("Não concordou")