
class Login:
    def __init__(self):
        self.login = {}

    def add_user(self, teacher, code):
        if teacher not in self.login:
            self.login[teacher] = code
            print(f"El docente {teacher}, con el código {code} ha sido ingresado correctamente")
        else:
            print(f"El docente {teacher} ya ha sido agregado previamente.")

    def edit_user(self, teacher, new_teacher):
        if teacher in self.login:
            code = self.login[teacher] #Ayuda a que no se genere error al ingresar los datos en el diccionario
            del self.login[teacher]
            self.login[new_teacher] = code # Se ingresan los datos en el diccionario en el orden correcto
            print(self.login)
        else:
            print("No se ha actualizado correctamente el docente en el listado")



