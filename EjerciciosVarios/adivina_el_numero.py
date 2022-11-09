import random

def adivina_el_numero (x):
    print (f" Hola bienvenido al juego ")


    numero_aleatorio = random.randint(1 , x)
    prediccion = 0

    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Ingrese un valor entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print ("Intenta de nuevo tu numero es muy pequeño")
        if prediccion > numero_aleatorio:
            print ("Intenta de nuevo tu numero es muy grande")

    print (F" Ganaste el numero es {numero_aleatorio} ")


adivina_el_numero(10)    



        


    