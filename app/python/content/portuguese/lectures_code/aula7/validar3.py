# Valida o endereço de email verificando se o domínio termina com .edu

email = input("Qual é o seu email? ").strip()

nome_de_usuario, dominio = email.split("@")

if nome_de_usuario and dominio.endswith(".edu"):
    print("Válido")
else:
    print("Inválido")