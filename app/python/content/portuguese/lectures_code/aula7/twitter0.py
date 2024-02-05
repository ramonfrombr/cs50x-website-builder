# Extrai o nome de usuário do Twitter de uma URL usando str.replace

url = input("URL: ").strip()

nome_de_usuario = url.replace("https://twitter.com/", "")
print(f"Nome de usuário: {nome_de_usuario}")