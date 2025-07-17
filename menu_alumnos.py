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
            for i in alum.course: #ciclo for para mostrar lo contenido en la lista de curso
                print(f"{i.name}, {i.score}, {i.teacher}")
        elif option == "2":
            cours = input("\nIngrese a que curso se quiere asignar: ").lower()
            cat = input("escoge al catedratico: ")
            alum.course.append(Course(cours, cat, 0)) # Guardar el input dentro de la lista curso

        elif option == "3":
            print("--Nombre--Carnet---\n")
            print(alum.name, alum.card) #imprime los datos del estudiante con el impor alumnos
        elif option == "4":
            print("\nRegresando al menu principal")
            break
        else:
            print("Ingresa una opcion valida")


