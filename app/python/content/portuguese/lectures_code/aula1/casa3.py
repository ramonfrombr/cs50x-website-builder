# Usa |

nome = input("Qual é o seu nome? ")

match nome:
    case "Harry" | "Hermione" | "Ron":
        print("Grifinória")
    case "Draco":
        print("Sonserina")
    case _:
        print("Quem?")