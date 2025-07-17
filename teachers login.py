# login teachers

# Importar los datos de las clases
from profesor import Teacher
from alumnos import Alumnos

# Función de menú
def menu_login(teachers, students):
    print("\n Bienvenido al menú")
    print("1. Ingresar nuevo usuario")
    print("2. Modificar nombre de usuario existente")
    print("3. Modificar código de usuario existente")
    print("4. Salir del menú")

# Ciclo que permite que el menú este en repetición
    while True:

        option = input("Ingresa la opción que deseas ejecutar (1-3")

        # Menú secundario de opciones de registro
        if option == "1":
            print("\n Menú registro")
            print("1. Registro docente")
            print("2. Registro estudiante")

            op = input("Ingresa una opción por favor: ")
            # Ingreso de nuevo usuario docente
            if op == "1":
                teacher = input("Ingresa el nombre del docente: ")
                code = input("Ingresa el código de identificación del docente: ")
                password = input("Ingresa una contraseña por favor: ")
                course = input("Ingrese el curso que imparte: ")
                teachers.append(Teacher(teacher, password, course,[], code)) # Se agrega el docente a la lista
                print("El usuario ha sido agregado correctamente.")

            # Ingreso de nuevo usuario estudiante
            elif op == "2":
                name = input("Ingresa el nombre del estudiante: ")
                card = input("Ingresa el cárnet del estudiante: ")
                password = input("Ingresa una contraseña: ")
                name.append(Alumnos(name, card, password, [])) # Se agrega el estudiante a la lista
                print("El estudiante ha sido ingresado correctamente.")

        # Modificación del nombre del docente
        elif option == "2":
            teacher = input("Ingrese el código del docente el cual desea modificar: ")
            for t in teachers: # Detectar que el código es valido
                if t.code == teacher:
                    new_teacher = input("Ingresa el nuevo nombre del docente: ") # Ingreso de nuevo nombre
                    t.name = new_teacher
                    print("El nombre del docente ha sido modificado correctamente.")
                    break # Fin del ciclo
            else:
                print("No se ha encontrado el docente ingresado")

        # Modificación de código docente
        elif option == "3":
            code = input("Ingresa el código que deseas modificar: ")
            for c in teachers: # Detecta si el código es valido
                if c.code == code:
                    new_code = input("Ingresa el nuevo código del docente: ")
                    c.code = new_code # Ingreso de nuevo código
                    print("El código del docente ha sido modificado correctamente.")
                    break
            else:
                print("No se ha encontrado el código ingresado")


        elif option == "4":
            print("Has salido del login correctamente.")
            break
        else:
            print("Opcion inválida, intentalo de nuevo.")

