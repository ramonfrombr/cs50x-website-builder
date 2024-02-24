# Valida o endereço de email verificando o nome de usuário e o domínio separadamente

email = input("Qual é o seu email? ").strip()

nome_de_usuario, dominio = email.split("@")

if nome_de_usuario and "." in dominio:
    print("Válido")
else:
    print("Inválido")