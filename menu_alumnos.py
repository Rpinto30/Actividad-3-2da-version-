# Creacion menu de alumnos
from cursos import Course
from alumnos import Alumnos

def alumnos_menu(alum):
    while True:
        print("----Menu Alumnos----\n"
              "\n1. Consultar notas\n"
              "2. Asignacion de cursos\n"
              "3. Datos personales\n"
              "4. Salir")
        option = input("\nIngresa una opcion: ")
        if option == "1":
            print("---Cursos---nota---docente")
            if len(alum.cursos) > 0:
                for i in alum.course: #ciclo for para mostrar lo contenido en la lista de curso
                    print(f"{i.name}, {i.score}, {i.teacher}")
            else:
                print("No hay cursos asignadoos")

        elif option == "2":
            cours = input("\nIngrese a que curso se quiere asignar: ").lower()
            cat = input("escoge al catedratico: ")
            alum.course.append(Course(cours, cat, 0))

            cours = int(input("\nIngrese a que curso se quiere asignar: "))
            if cours <=  int(num)+1: alum.course.append([cour[num-1], 0])
            else: print("Lo siento, entrada invalida")

            print("Curso asignado!")
        elif option == "3":
            print("---Nombre---Carnet---")
            print(alum.name, alum.card)
            print("--Cursos asignados--Notas")
            for i in alum.course: print(f"  {i[0].name}  {i[1]} ")
        elif option == "4":
            print("\nRegresando al menu principal")
            break
        else:
            print("Ingresa una opcion valida")
