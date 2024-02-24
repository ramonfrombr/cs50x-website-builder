# Extrai o nome de usuário do Twitter a partir de uma URL usando str.removeprefix

url = input("URL: ").strip()

nome_de_usuario = url.removeprefix("https://twitter.com/")
print(f"Nome de usuário: {nome_de_usuario}")