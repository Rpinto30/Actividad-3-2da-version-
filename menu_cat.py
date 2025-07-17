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
                #MODIFICAR NOTA
        elif op == 2:
            print("Mostar alumnos")
            if cat.alums > 0:
                for i in cat.alums:
                    #for j in i.course:


                    print(f"{'Nombre':<20}{'Carnet':<30}{'Nota':<20}")
                    print(f"{i.name:<20}{i.card:<30}{i.course:<20}")
            else:
                print("No existen alumnos asignados a este profesor")
        elif op == 3:
            pass

        else:
            break