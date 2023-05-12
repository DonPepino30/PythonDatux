#!/usr/bin/env python
# coding: utf-8


#EJERCICIO 1

while True:
    print("Seleccione una opción:")
    print("1.Dibujar un cuadrado en consola con *")
    print("2.Identificar números múltiplos de 2 en una lista")
    print("3.Imprimir solo los mayores de edad en una lista de personas")
    print("4.Terminar bucle")

    op=int(input("Ingrese el número de la opción que desea ejecutar: "))

    if op==1:
        lado=int(input("Ingrese el tamaño del lado del cuadrado: "))
        for i in range(lado):
            print("*" * lado)

    elif op==2:
        numeros=[5, 2, 8, 13, 17, 25, 39, 42, 16, 24, 50, 51]
        for N in numeros:
            if N%2==0:
                print(N)
    elif op==3:
        personas = [("Alexo", 35), ("Manuel", 14), ("Rosa", 16), ("Roberto", 13),("Geraldine", 27),("Luzmila", 70)]
        for Nom, Eda in personas:
            if Eda>=18:
                print(Nom)
    elif op==4:
        print("Muchas gracias por usar el programa")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


#Ejercicio 2

Biblioteca = {
    "Dramatico": ["Hamlet - William Shakespeare", "La Celestina - Fernando de Rojas", "Romeo y Julieta - William Shakespeare"],
    "Lirico": ["Edipo Rey - Sofocles", "Prometeo Encadenado - Esquilo", "Los Heraldos Negros - Cesar Vallejo"]
}

def Obt_Cat():
    print("Categorías de libros(por genero):")
    for Cats in Biblioteca.keys():
        print("- " + Cats)

def Obt_Lib():
    print("Los libros disponibles son:")
    for Catg, libros in Biblioteca.items():
        print( Catg + ":")
        for libro in libros:
            print("- " + libro)

def Prestar_Lib():
    libro=input("Ingrese el nombre del libro que desea prestar: ")
    for Catg, libros in Biblioteca.items():
        if libro in libros:
            libros.remove(libro)
            libros.append(libro + " (Prestado)")
            print("El libro: " + libro + " ha sido prestado.")
            return #Cierra la funcion, por eso si no está el libro te devuelve el siguiente print
    print("El libro no se encuentra disponible en la biblioteca.")

Users = ["PepitoGuirnaldo13", "ValentinaKar13", "ZacariasFlores15"] 
def Obt_users():
    print("Usuarios de la biblioteca:")
    for User in Users:
        print("- " + User)
        
while True:
    print("Seleccione una opción:")
    print("1.Obtener la lista de categorías de libros")
    print("2.Obtener nombres de los libros y autores")
    print("3.Poder cambiar el estado de un libro a prestado")
    print("4.Lista de usuarios de la biblioteca")
    print("5.Salir")

    opc=int(input("Ingrese el número de la opción que desea ejecutar: "))

    if opc==1:
        Obt_Cat()
    elif opc==2:
        Obt_Lib()
    elif opc==3:
        Prestar_Lib()
    elif opc==4:
        Obt_users()
    elif opc==5:
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


#Ejercicio 3

def Obt_May():
    N1=int(input("Ingrese el primer numero a evaluar: "))
    N2=int(input("Ingrese el segundo numero a evaluar: "))
    if N1 > N2:
        print("El numero mayor es: ", N1)
    else:
        print("El numero mayor es: ",  N2)

Obt_May()




#Ejercicio 4 //Necesité un poco de ayuda 

import sys

def Imp_Argumentos(*args):
    for arg in args:
        print(arg)

if __name__ == '__main__':
    argumentos = sys.argv[1:]
    Imp_Argumentos(*argumentos)



#Ejercicio 5 //Necesité otra ayudita : c

import os

def List_Elemtns(path):
    for elemt in os.listdir(path):
        Ruta_Compl = os.path.join(path, elemt)
        if os.path.isdir(Ruta_Compl):
            print(f"{Ruta_Compl} es una carpeta:")
            List_Elemtns(Ruta_Compl)
        else:
            print(Ruta_Compl)

List_Elemtns('C:\Program Files (x86)')


#Ejercicio 6 

def main():
    Evento = Obt_Evento()
    Asistentes = Obt_Asistentes()
    Check_Asistentes(Asistentes, Evento)
    print("El evento ha sido registrado exitosamente.")

def Obt_Evento():
    Evento = input("Ingrese el nombre del evento: ")
    return Evento

def Obt_Asistentes():
    Asistentes = []
    while True:
        Nombre = input("Ingrese el nombre del asistente ('.' para cerrar la lista): ")
        if Nombre == '.':
            break
        Asistentes.append(Nombre)
    return Asistentes

def Check_Asistentes(Asistentes, Evento):
    if len(Asistentes) > 20:
        print("No se pueden registrar más de 20 asistentes.")
    elif len(Asistentes) == 0:
        print("Debe haber al menos un asistente registrado.")
    else:
        print(f"Se han registrado {len(Asistentes)} asistentes para el evento {Evento}.")

main()



#Ejercicio 7


def Cont_Palabra(Text1, Palabra1):
    Cantidad = Text1.count(Palabra1)
    return Cantidad

Text1 = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y  archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galeria de textos y los mezcló de tal manera que logré hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas, las cuales contenían pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum"
Palabra1 = "Lorem Ipsum"
Result1 = Cont_Palabra(Text1, Palabra1)

def Busq_Pal(Text2, Palabra2):
    Lugar = Text2.find(Palabra2)
    return Lugar

Text2 = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y  archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galeria de textos y los mezcló de tal manera que logré hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas, las cuales contenían pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum"
Palabra2 = "galeria"
Result2 = Busq_Pal(Text2, Palabra2)

def Repl_Pal(Text3, Palabra3, Palabra4):
    Reemplazo= Text3.replace(Palabra3, Palabra4)
    return Reemplazo

Text3 = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y  archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galeria de textos y los mezcló de tal manera que logré hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas, las cuales contenían pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum"
Palabra3 = "texto"
Palabra4 = "escrito"
Result3 = Repl_Pal(Text3, Palabra3, Palabra4)
print(Result1)
print(Result2)
print(Result3)


#Ejercicio 8

def Hallar_Primos(Max, Step):
    Primos = []
    
    def es_primo(Num):
        if Num < 2:
            return False
        for i in range(2, int(Num**0.5)+1):
            if Num % i == 0:
                return False
        return True
    
    for i in range(2, Max, Step):
        if es_primo(i):
            Primos.append(i)
    
    return Primos

Result5 = Hallar_Primos(10**5, 1)
print(Result5)


#Ejercicio 9

colegio={
    "name":"colegio1",
    "grades":[1,2,3,4,5],
    "profesores":{
        "profesor1":{
            "listGrades":[1,2,3]
        },
        "profesor2":{
          "listGrades":[4,5]
        }
    },
    "cursos":["python","sql","power bi"],
    "students":[
        {
            "fullname":"alumno1",
            "grade":1,
            "cursos":["python","sql"],
            "notas":{
                "python":[],
                "sql":[]
            }
        },
        {"fullname":"alumno2",
            "grade":2,
            "cursos":["python","power bi"],
            "notas":{
                "python":[],
                "power bi":[]
            }
        }
    ]
}
templateStudents={
    "fullname":"",
    "grade":"",
    "cursos":[],
    "notas":{}
}

msg="""
    1.) agregar alumno nuevo
    2.) agregar profesor 
    3.) agregar nota
    4.) Mostrar sistema
    5.) Salir
"""
def verificarGrado(colegio,grado):
    if grado in colegio["grades"]:
        return True 
    else:
        return False

def agregarAlumno():
    fullname=input('ingrese su nombre completo')
    while True:
        grade=int(input('ingrese el grado'))
        if verificarGrado(colegio,grade) :
            break
    cantidadCursos=int(input("que cantidad de cursos desea agregar"))
    cursosNew=[]
    print(f"""la lista de cursos son {colegio['cursos']}""")
    for i in range(cantidadCursos):
        curso=input(f'ingrese el curso numero {i}')
        cursosNew.append(curso)
    templateStudents["fullname"]=fullname
    templateStudents["grade"]=grade
    templateStudents["cursos"]=cursosNew
    colegio['students'].append(templateStudents)


def agregarProfesor():
    name=input("nombre de profesor")
    cantidad=int(input("ingrese la cantidad de grados "))
    listGradesNew=[]
    for i in range(cantidad):
        while True:
         grade=int(input(f'ingrese el grado numero{i}'))
         #reutilizacion
         if verificarGrado(colegio,grade) :
                listGradesNew.append(grade)
                break
    colegio["profesores"][name]={"listGrades":listGradesNew}
        
def agregarNota():
    Notas=[]
    while(True):
        Nota = float(input("Ingrese la nota del alumno: "))
        if(Nota >= 0 and Nota <=20):
            Notas.append(Nota)
            return False
            break
            
        else:
            print("Ingrese un valor dentro del rango")
    
def mostrarSistema():
    print(colegio)

while True:
    print("Bienvenido al sistema escolar")
    print(msg)
    opcion=int(input("elija opcion por realizar"))
    match opcion:
        case 1:
            agregarAlumno()
        case 2:
            agregarProfesor()
        case 3:
            agregarNota()
        case 4:
            mostrarSistema()
            break
        case 5:
            print("Saliendo...")
            break
        case _:
            print("Elija acction correcta")
