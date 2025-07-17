# login teachers
from profesor import Teacher
from alumnos import Alumnos
# Definicion de variables

def menu_login(teachers, students):
    print("\n Bienvenido al menú")
    print("1. Ingresar nuevo usuario")
    print("2. Modificar nombre de usuario existente")
    print("3. Modificar código de usuario existente")
    print("4. Salir del menú")


    while True:

        option = input("Ingresa la opción que deseas ejecutar (1-3")

        if option == "1":
            print("\n Menú registro")
            print("1. Registro docente")
            print("2. Registro estudiante")

            op = input("Ingresa una opción por favor: ")
            if op == "1":

                teacher = input("Ingresa el nombre del docente: ")
                code = input("Ingresa el código de identificación del docente: ")
                password = input("Ingresa una contraseña por favor: ")
                course = input("Ingrese el curso que imparte: ")
                teachers.append(Teacher(teacher, password, course,[], code))
                print("El usuario ha sido agregado correctamente.")
            elif op == "2":
                name = input("Ingresa el nombre del estudiante: ")
                card = input("Ingresa el cárnet del estudiante: ")
                password = input("Ingresa una contraseña: ")
                name.append(Alumnos(name, card, password, []))
                print("El estudiante ha sido ingresado correctamente.")

        elif option == "2":
            teacher = input("Ingrese el código del docente el cual desea modificar: ")
            for t in teachers:
                if t.code == teacher:
                    new_teacher = input("Ingresa el nuevo nombre del docente: ")
                    t.name = new_teacher
                    break
            else:
                print("No se ha encontrado el docente ingresado")

        elif option == "3":
            code = input("Ingresa el código que deseas modificar: ")
            for c in teachers:
                if c.code == code:
                    new_code = input("Ingresa el nuevo código del docente: ")
                    c.code = new_code
                    break
            else:
                print("No se ha encontrado el código ingresado")


        elif option == "4":
            print("Has salido del login correctamente.")
            break
        else:
            print("Opcion inválida, intentalo de nuevo.")

