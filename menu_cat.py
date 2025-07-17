from alumnos import Alumnos


def menu_cat(cat, courses):
    while True:
        print(f"\n----Menu Catedraticos, Bienvenido {cat.name}----" +
              "\n  1) Agregar nota\n  2) Mostrar alumnos\n  3) Salir")
        op = int(input("Elige una de las siguientes opciones: "))

        if op == 1: #actualizar notas
            while True:
                est = input("Porfavor, ingresa el carnet del estudiante: ")
                estu, c  = None, None
                for cou in courses:
                    if cou.teacher.code == cat.code:
                        if len(cou.alums) > 0:
                            for est_list in cou.alums:
                                c = cou
                                estu = est_list
                                if est_list.card == est:
                                    break
                            else:
                                print(f"Lo siento, no tiene registado el estudiante con carnet: {estu}")
                                break
                            break
                        else: print("Lo siento, no tiene estudiantes asignados")

                if len(c.alums) > 0:
                    no = int(input(f"Ingresa nueva nota para el curso de {c.name} para el estudiante {estu.name}: "))
                    nota = None
                    for i in estu.course:
                        if i[0].id == c.id:
                            i[1] = no
                            nota = i
                            break
                    print(f"La nueva nota de {estu.name} en el curso de {c.name} es {nota[1]}")
                    break
        elif op == 2:
            for cou in courses:
                if cou.teacher.code == cat.code:
                    if len(cou.alums) > 0:
                        for i in cou.alums:
                            print(f"{'Nombre':<20}{'Carnet':<30}")
                            print(f"{i.name:<20}{i.card:<30}")
                    else:
                        print("No existen alumnos asignados a este profesor")
                        break
        else:
            break