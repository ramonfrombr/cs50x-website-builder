# Utiliza el emparejamiento con casos

nombre = input("¿Cuál es tu nombre? ")

match nombre:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("¿Quién?")