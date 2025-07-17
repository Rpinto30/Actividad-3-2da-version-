# Creacion menu de alumnos
from cursos import Course
from alumnos import Alumnos

def alumnos_menu(alum, courses):
    while True:
        print(f"\n----Menu Alumnos, Bienvenido {alum.name}----"
              "\n1. Consultar notas\n"
              "2. Asignacion de cursos\n"
              "3. Datos personales\n"
              "4. Salir")
        option = input("\nIngresa una opcion: ")
        if option == "1":
            if len(alum.course) > 0:
                print(f"{'Cursos asingados':<40}{'Punteo':<20}")
                for i in alum.course: print(f"{i[0].name:<40}{i[1]:<20}")
            else: print("Lo siento, no encontramos cursos asignados")
        elif option == "2":
            for num,i in enumerate(courses): print(f"  {num+1})Nombre:{i.name}  Catedratico:{i.teacher.name}  Creditos:{i.credits}")

            cours = int(input("\nIngrese a que curso se quiere asignar: "))
            if cours <=  int(num)+1: alum.course.append([courses[cours-1], 0])
            else: print("Lo siento, entrada invalida")

            print("Curso asignado!")
        elif option == "3":
            print(f"{'Nombre':<30}{'Carnet':<20}")
            print(f"{alum.name:<30}{alum.card:<20}")
            print("-"*50)
        elif option == "4":
            print("\nRegresando al menu principal")
            break
        else:
            print("Ingresa una opcion valida")


