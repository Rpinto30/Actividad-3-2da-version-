# Creacion menu de alumnos
from cursos import Course
from alumnos import Alumnos

def alumnos_menu(alum, cour):
    while True:
        print("----Menu Alumnos----\n"
              "\n1. Consultar notas\n"
              "2. Asignacion de cursos\n"
              "3. Datos personales\n"
              "4. Salir")
        option = input("\nIngresa una opcion: ")
        if option == "1":
            print("---Cursos---nota---docente")
            for i in alum.course:
                print(f"{i.name}, {i.score}, {i.teacher}")
        elif option == "2":
            for num,i in enumerate(cour):
                print(f"  {int(num)+1})Nombre: {i.name}, docente: {i.teacher.name}, creditos: {i.credits}")

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


