# Compara várias strings

resposta = input("Você concorda? ").strip().lower()
if resposta == "sim" or resposta == "s":
    print("Concordou")
else:
    print("Não concordou")