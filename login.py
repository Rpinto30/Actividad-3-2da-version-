
class Login:
    def __init__(self):
        self.login = {}

    def add_user(self, teacher, code):
        if teacher not in self.login:
            self.login[teacher] = code
            print(f"El docente {teacher}, con el código {code} ha sido ingresado correctamente")
        else:
            print(f"El docente {teacher} ya ha sido agregado previamente.")
