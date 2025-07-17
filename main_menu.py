'''
MENU PRINCIPAL
'''

from menu_alumnos import alumnos_menu
from alumnos import Alumnos
from cursos import Course
from profesor import Teacher

teacher = [
    Teacher("Osmar", "12345", "cat123"),
    Teacher("Miguel", "Hola128op", "cat259"),
    Teacher("Luis", "Adios152", "cat010")

]


courses = [
    Course('Calculo', teacher[0], 5, 0),
    Course('Programación', teacher[2], 2, 1),
    Course('Magis', teacher[1], 1, 2)
]

students = [Alumnos("Rodrigo", "1","12345",[])]


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
                alumnos_menu(i, courses)
        pass
    elif op == 3:
        pass
    else:
        break

print("Hasta pronto!")


