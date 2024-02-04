# Demonstração de menos comparações

pontuacao = int(input("Pontuação: "))

if pontuacao >= 90:
    print("Pontuação: A")
elif pontuacao >= 80:
    print("Pontuação: B")
elif pontuacao >= 70:
    print("Pontuação: C")
elif pontuacao >= 60:
    print("Pontuação: D")
else:
    print("Pontuação: F")