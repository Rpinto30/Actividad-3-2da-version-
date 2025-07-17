# login teachers
from cursos import Course
# Importar los datos de las clases
from profesor import Teacher
from alumnos import Alumnos

# Función de menú
def menu_login(teachers, students, courses):
# Ciclo que permite que el menú este en repetición
    while True:
        print("\n Bienvenido al menú")
        print("1. Ingresar nuevo usuario")
        print("2. Modificar nombre de usuario existente")
        print("3. Modificar código de usuario existente")
        print("4. Mostrar todo")
        print("5. Salir del menú")
        option = input("Ingresa la opción que deseas ejecutar (1-3): ")

        # Menú secundario de opciones de registro
        if option == "1":
            print("\n Menú registro")
            print("1. Registro docente y curso")
            print("2. Registro estudiante")

            op = input("Ingresa una opción por favor: ")
            # Ingreso de nuevo usuario docente
            if op == "1":
                teacher = input("Ingresa el nombre del docente: ")
                code = input("Ingresa el código de identificación del docente: ")
                password = input("Ingresa una contraseña por favor: ")

                teachers.append(Teacher(teacher, password, code)) # Se agrega el docente a la lista

                print("\n---Creacion de cursos---")
                n = input("Ingresa nombre del curso: ")
                cred = int(input("Ingresa la cantidad de creditos que dara el curso: "))
                courses.append(Course(n, teacher[-1], cred, len(courses), []))
                print("El usuario ha sido agregado correctamente.")
            # Ingreso de nuevo usuario estudiante
            elif op == "2":
                name = input("Ingresa el nombre del estudiante: ")
                card = input("Ingresa el cárnet del estudiante: ")
                password = input("Ingresa una contraseña: ")
                students.append(Alumnos(name, card, password, [])) # Se agrega el estudiante a la lista
                print("\nEl estudiante ha sido ingresado correctamente.\n")

        # Modificación del nombre del docente
        elif option == "2":
            teacher = input("Ingresge el código del docente el cual desea modificar el nombre: ")
            for t in teachers: # Detectar que el códio es valido
                if t.code == teacher:
                    new_teacher = input("Ingresa el nuevo nombre del docente: ") # Ingreso de nuevo nombre
                    t.name = new_teacher
                    print(f"El nombre del docente ha sido modificado correctamente a {new_teacher}.")
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
            print("+"*15+"ESTUDIANTES REGISTRADOS"+"+"*15)
            print(f"{'Nombre':<30}{'Carnet':<10}{'Contraseña':<10}")
            for i in students: print(f"{i.name:<30}{i.card:<10}{i.password:<10}")
            print("-"*50)
            print("+" * 15 + "PROFESORES REGISTRADOS" + "+" * 15)
            print(f"{'Nombre':<30}{'Codigo':<10}{'Contraseña':<10}")
            for j in teachers: print(f"{j.name:<30}{j.code:<10}{j.password:<10}")
            print("-" * 50)
            print("+" * 15 + "CURSOS REGISTRADOS" + "+" * 15)
            print(f"{'Nombre':<30}{'Creditos':<10}{'ID':<10}")
            for k in courses: print(f"{k.name:<30}{k.credits:<10}{k.id:<10}")
            print("-" * 50)

        elif option == "5":
            print("Has salido del login correctamente.")
            break
        else:
            print("Opcion inválida, intentalo de nuevo.")

