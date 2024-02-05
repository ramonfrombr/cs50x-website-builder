# Demonstração de desigualdades and operadores lógicos

pontuacao = int(input("Pontuação: "))

if 90 <= pontuacao and pontuacao <= 100:
    print("Pontuação: A")
elif 80 <= pontuacao and pontuacao < 90:
    print("Pontuação: B")
elif 70 <= pontuacao and pontuacao < 80:
    print("Pontuação: C")
elif 60 <= pontuacao and pontuacao < 70:
    print("Pontuação: D")
else:
    print("Pontuação: F")