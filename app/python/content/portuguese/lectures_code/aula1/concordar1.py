# Remove espaços em branco antes de comparar

resposta = input("Você concorda? ").strip()
if resposta == "sim":
    print("Concordou")
else:
    print("Não concordou")