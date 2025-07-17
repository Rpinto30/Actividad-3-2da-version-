# Creacion menu de alumnos
from cursos import Course

def alumnos_menu(alum):
    while True:
        print("----Menu Alumnos----\n"
              "\n1. Consultar notas\n"
              "2. Asignacion de cursos\n"
              "3. Desasignacion de cursos\n"
              "4. Salir")
        option = input("\nIngresa una opcion: ")
        if option == "1":
            for i in alum.course:
                print(i.name, i.score)
        elif option == "2":
            cours = input("\nIngrese a que curso se quiere asignar: ").lower()
            cat = input("escoge al catedratico: ")
            alum.course.append(Course(cours, cat, 0))

        elif option == "3":
            pass
        elif option == "4":
            print("\nRegresando al menu principal")
            break
        else:
            print("Ingresa una opcion valida")


