'''
MENU PRINCIPAL
'''

from menu_alumnos import alumnos_menu
from alumnos import Alumnos
from cursos import Course
from profesor import Teacher


students = [Alumnos("Rodrigo", "1505925","12345",
                    [Course ("Matematicas", "Osmio", "85"), Course ("Ingles", "Dodo", "93")],)]
teacher = []

print("-"*10+"Bienvenidos"+"-"*10)
while True:
    print("Opciones:" +
          "\n  1) Catedratico\n  2) Alumnos\n  3) Crear nuevo usuario\n  4) Salir")
    op = int(input("Elige una de las siguientes opciones: "))

    if op == 1:
        pass
    elif op == 2:
        log = input("Ingrese su carnet: ")
        pasw = input("Ingrese su contraseña: ")

        for i in students:
            if i.card == log and i.password == pasw:
                alumnos_menu(i)
        pass
    elif op == 3:
        pass
    else:
        break

print("Hasta pronto!")


