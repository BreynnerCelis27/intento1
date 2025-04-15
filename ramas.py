'''ramas.py
    Esta parte va la descri
    Autor: Breynner Celis
    Código: 1.092.531.892
    Tel: 3504639016
    Email:breynner.celisflo@unipamplona.edu.co
    fecha: 17-03-2025
    asignatura= poo
    ingenieria mecatronica 
    '''
'''importar modulos'''
import time

'''clases y funciones'''
print("hola")
def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def division(a,b):
    return a/b

def multiplicacion(a,b):
    return a*b


def multiplo():
    multiplos = int(input("¿Cuántos múltiplos desea? "))  # Convertir input a entero
    contador = 1  # Empezar desde el primer múltiplo de 2
    
    while contador <= multiplos:
        B = contador * 2  # Calcular el múltiplo de 2
        print(B)  # Mostrar el múltiplo
        contador += 1  # Incrementar el contador para el siguiente múltiplo

multiplo()  # Llamar a la función

def multiplo_2(cant):
    multiplos=[2 * i  for i in range(1,cant+1)]
    return multiplos
def ingresar():
    a = input("ingresar el primer numero")
    b = input("ingresar el segundo numero")
    return a,b

'''Variables  y constantes'''
GRAVEDAD= 9.81         #las constantes estan escritas en mayusculas #tipo float
a = 2                  #tipo int
nombre_cliente="juanito"          #tipo char

'''Algoritmo principal'''
print("bienvenido (a)")
print(f"menú:" \n 1) sumar \n 2) Restar \n 3) Dividir \n 4) Multiplicar \n 5) Multiplo")
op= input("ingresar la opcion preferida: ")
print(multiplo_2(a))

if(op =="1"):
    print("suma...")
    a,b = ingresar()
    print("el resultado de la suma es: " , suma(a,b))
elif(op =="2"):
    a,b = ingresar()
    print("el resultado de la suma es: " , resta(a,b))
elif(op =="3"):
    print("division...")
    a,b = ingresar()
    print("el resultado de la suma es: " , division(a,b))
elif (op=="4"):
    print("multiplicar")
    a,b= ingresar()
    print("el resultado de la multiplicacion es: ", multiplicacion(a,b))
else:
    print("opcion incorrecta  bb")


    
