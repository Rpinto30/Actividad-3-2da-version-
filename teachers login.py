# login teachers

def menu_login():
    print("\n Bienvenido al menú")
    print("1. Ingresar nuevo usuario")
    print("2. Modificar nombre de usuario existente")
    print("3. Modificar código de usuario existente")
    print("3. Salir del menú")

while True:
    menu_login()

    option = input("Ingresa la opción que deseas ejecutar (1-3")

    if option == "1":
        teacher = input("Ingresa el nombre del docente: ")
        code = input("Ingresa el código de identificación del docente: ")
        u.add_user(teacher, code)
        print("El usuario ha sido agregado correctamente.")

