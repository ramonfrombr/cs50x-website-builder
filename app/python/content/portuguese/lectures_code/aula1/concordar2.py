# Transforma a string em minúsculas antes de comparar

resposta = input("Você concorda? ").strip().lower()
if resposta == "sim":
    print("Concordou")
else:
    print("Não concordou")