# Usando o match com case

nome = input("Qual é o seu nome? ")

match nome:
    case "Harry":
        print("Grifinória")
    case "Hermione":
        print("Grifinória")
    case "Ron":
        print("Grifinória")
    case "Draco":
        print("Sonserina")
    case _:
        print("Quem?")