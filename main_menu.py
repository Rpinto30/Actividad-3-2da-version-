'''
MENU PRINCIPAL
'''

from menu_alumnos import alumnos_menu
from alumnos import Alumnos
from cursos import Course

students = []
teacher = []

print("-"*10+"Bienvenidos"+"-"*10)
while True:
    print("Opciones:" +
          "\n  1) Catedratico\n  2) Alumnos\n  3) Crear nuevo usuario\n  4) Salir")
    op = int(input("Elige una de las siguientes opciones: "))

    if op == 1:
        pass
    elif op == 2:
        #alumnos_menu(students, teacher)
        pass
    elif op == 3:
        pass
    else:
        break

print("Hasta pronto!")


