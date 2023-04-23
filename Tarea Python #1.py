#!/usr/bin/env python
# coding: utf-8


#Ejercicio 1

Nombres=input(("Ingrese sus nombres: "))
Apellidos=input(("Ingrese sus apellidos: "))
edad=input(("Ingrese su edad: "))
talla=input(("Ingrese su altura: "))

print("Sus nombres son: ", Nombres)
print("Sus apellidos son: ", Apellidos)
print("Su talla es: ", edad)
print("Su edad es: ", talla, " metros")


#Ejercicio 2

Radio=float(input("Ingrese el radio del circulo: "))
print("El area del circulo es: ", 3.14*pow(Radio,2))

T_Triangulo=input("Ingrese el tipo de triangulo a calcular: ")
if(T_Triangulo=="Equilatero"):
    lado=float(input("Ingrese el valor del lado: "))
    print("El area del triangulo equilatero es: ", (1.73*lado*lado)/4)
if(T_Triangulo=="Isosceles"):
    base=float(input("Ingrese el valor de la base: "))
    altura=float(input("Ingrese el valor de la altura: "))
    print("El area del triangulo equilatero es: ", (base*altura)/2)
if(T_Triangulo=="Escaleno"):
    lado1=float(input("Ingrese el valor del lado 1: "))
    lado2=float(input("Ingrese el valor del lado 2: "))
    lado3=float(input("Ingrese el valor del lado 3: "))
    p=(lado1+lado2+lado3)/2
    print("El area del triangulo escaleno es: ", math.sqrt(p*(p-lado1)*(p-lado2)*(p-lado3)))

LadoC=float(input("Ingrese el lado del cuadrado: "))
print("El area del cuadrado es: ", pow(LadoC,2))


#Ejercicio 3

V1=float(input("Ingrese el primer numero: "))
V2=float(input("Ingrese el segundo numero: "))
V3=float(input("Ingrese el tercer numero: "))

print("La suma de los tres numeros es: ", V1+V2+V3)
print("La sustraccion de los tres numeros es: ", V1-V2-V3)
print("El producto de los tres numeros es: ", V1*V2*V3)
print("La division de los tres numeros es: ", (V1/V2)/V3)
print("El division exacta de los tres numeros es: ", (V1//V2)//V3)



#Ejercicio 4

y=(input("Ingrese el dato: "))
type(y)


#Ejercicio 5

import sys
variable =sys.argv[0]
print("La ruta actual es: ",variable)


#Ejercicio 6

suma=0
a=1
valor=float(input("Ingrese el limite de valores a sumar: "))
while(a<=valor):
    suma=suma + a
    a=a+1
print("La suma total es: ", suma)    


#Ejercicio 7

num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
           
if(num1==num2):
           print("Los numeros son iguales")
if(num1!=num2):
           print("Los numeros no son iguales")
           if(num1<num2):
                print("El primer numero es menor que el segundo numero")
           else:
               print("El primer numero es mayor que el segundo numero")


#Ejercicio 8

contra1="ICKKCK69"
contra=input("Ingrese su clave: ")
if(contra==contra1):
    print("Las claves coinciden")
if(contra!=contra1):
    print("La claves no coinciden")
    
#Alternativa    
#contra1
#contra=input("Ingrese su clave: ")
#contra1=contra
#contra=input("Vuelva a ingresar su clave: ")
#if(contra==contra1):
    #print("Las claves coinciden")
#if(contra!=contra1):
    #print("La claves no coinciden")


#Alternativa 8    
contra1
contra=input("Ingrese su clave: ")
contra1=contra
contra=input("Vuelva a ingresar su clave: ")
if(contra==contra1):
    print("Las claves coinciden")
if(contra!=contra1):
    print("La claves no coinciden")



#Ejercicio 9

print("1. Agrega lista de python \n2. Agregar a lista de SQL \n3. Agregar a lista de Power BI")



#Ejercicio 10

DNIs=['58693012','89603867','79397671','19287590']
Name=['Jose Manuel','Manuel Rosas','Rosa Merino','Benito Camilo']
Edad=['18','19','20','21']
Distrito=['JM','SJL','SMP','LV']
Curso=['datux','curso:sql']
Datos=[Name,Edad,Distrito,Curso]
cdni=input("Ingrese su DNI: ")
if(cdni==DNIs[0]):
    print("El nombre del DNI ingresado es: ",Datos[0][0],"\nLa edad del ciudadano es: ",Datos[1][0], "\nEl distrito donde reside es: ",Datos[2][0])
    Vcur=input("Ingrese su curso: ")
    if(Vcur==Curso[0]):
        print("Usted esta matriculado en el curso de Python Datux")
    else:
        print("Usted no esta matriculado en el curso de Python Datux. Retirese")
elif(cdni==DNIs[1]):
    print("El nombre del DNI ingresado es: ",Datos[0][1],"\nLa edad del ciudadano es: ",Datos[1][1], "\nEl distrito donde reside es: ",Datos[2][1])
    Vcur=input("Ingrese su curso: ")
    if(Vcur==Curso[0]):
        print("Usted esta matriculado en el curso de Python Datux")
    else:
        print("Usted no esta matriculado en el curso de Python Datux. Retirese")
elif(cdni==DNIs[2]):
    print("El nombre del DNI ingresado es: ",Datos[0][2],"\nLa edad del ciudadano es: ",Datos[1][2], "\nEl distrito donde reside es: ",Datos[2][2])
    Vcur=input("Ingrese su curso: ")
    if(Vcur==Curso[0]):
        print("Usted esta matriculado en el curso de Python Datux")
    else:
        print("Usted no esta matriculado en el curso de Python Datux. Retirese")
elif(cdni==DNIs[3]):
    print("El nombre del DNI ingresado es: ",Datos[0][3],"\nLa edad del ciudadano es: ",Datos[1][3], "\nEl distrito donde reside es: ",Datos[2][3])
    Vcur=input("Ingrese su curso: ")
    if(Vcur==Curso[0]):
        print("Usted esta matriculado en el curso de Python Datux")
    else:
        print("Usted no esta matriculado en el curso de Python Datux. Retirese")
else:
    print("Ingrese un DNI registrado en el curso de Python Datux. Muchas Gracias")

