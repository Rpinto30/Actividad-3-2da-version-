from alumnos import Alumnos


def menu_cat(cat):
    while True:
        print("Opciones:" +
              "\n  1) Agregar nota\n  2) Mostrar alumnos\n  3) Mostrar promedios\n  4) Salir")
        op = int(input("Elige una de las siguientes opciones: "))

        if op == 1:
            while True:
                print("Agregar nota")
                est = input("Porfavor, ingresa el carnet del estudiante: ")
                estu = None
                for est_list in cat.alums:
                    estu = est_list
                    if est_list.card == est:
                        break
                else:
                    print(f"Lo siento, no tiene registado el estudiante con carnet: {estu.card}")
                    break

                no = int(input("Ingrese la nota modificada del estudiante: "))

        elif op == 2:
            pass
        elif op == 3:
            pass
        else:
            break