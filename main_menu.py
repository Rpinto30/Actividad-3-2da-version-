'''
MENU PRINCIPAL
'''

from menu_alumnos import alumnos_menu
from menu_cat import menu_cat
from teachers_login import menu_login

from alumnos import Alumnos
from cursos import Course
from profesor import Teacher

teacher = [
    Teacher("Osmar", "12345", "cat123"),
    Teacher("Miguel", "Hola128op", "cat259"),
    Teacher("Jorge Tello", "Adios152", "cat010")

]

courses = [
    Course('Calculo', teacher[0], 5, 0, []),
    Course('Programación', teacher[2], 2, 1, []),
    Course('Magis', teacher[1], 1, 2, [])
]

students = [
    Alumnos("Rodrigo Herman", "1505925","12345678",[]),
    Alumnos("Aileen", "1541925","12345678",[]),
    Alumnos("Rodrigo Pinto", "0","12345",[])
]

courses[0].alums.append(students[0])
students[0].course.append([courses[0], 0])

print("-"*10+"Bienvenidos"+"-"*10)
while True:
    print("Opciones:" +
          "\n  1) Catedratico\n  2) Alumnos\n  3) Administrador\n  4) Salir")
    op = int(input("Elige una de las siguientes opciones: "))

    if op == 1: #CATEDRATICOS
        log = input("Ingrese su codigo: ")
        pasw = input("Ingrese su contraseña: ")

        for i in teacher:
            if i.code == log and i.password == pasw:
                menu_cat(i, courses)
    elif op == 2: #ALUMNOS
        log = input("Ingrese su carnet: ")
        pasw = input("Ingrese su contraseña: ")

        for i in students:
            if i.card == log and i.password == pasw:
                alumnos_menu(i, courses)
    elif op == 3:
        print("----Menú de administrador----")
        print("  1) Soy administrativo\n  2) No soy administrativo")
        op_adm = int(input("Usted es un administrativo?: "))
        if op_adm == 1:
            menu_login(teacher, students, courses)
    else:
        break

print("Hasta pronto!")


