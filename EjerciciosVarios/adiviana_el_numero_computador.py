import random


def adivina_el_numero_computador(x):

    print ("Bienvenido al juego compu jejej"   )

    print(f" Selecciona un numero entre 1 y {x} para que la computadora lo adivine")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior,limite_superior)
        else:
            prediccion = limite_inferior

        respuesta = input(f"Mi prediccion es {prediccion} Si es muy alta ingresa (A) . Si es muy baja ingresa (B), Si es correcto ingresa (C)").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
    print (f" Felicidades la computadora es mas inteligente que tu {prediccion} ")


adivina_el_numero_computador(100)   


