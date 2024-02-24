# Utiliza |

nombre = input("¿Cuál es tu nombre? ")

match nombre:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("¿Quién?")