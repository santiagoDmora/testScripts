import random


def jugar():

    usuario = input("Escoge una opcion 'pi' = piedra , 'pa' = papel , 'ti' = tijera.\n").lower()
    computadora = random.choice(['pi','pa','ti'])
    print (f" La computador escogio {computadora} ")

    if usuario == computadora:
        return 'Empate'
    
    if gano_jugador(usuario,computadora):
        return 'ganaste'

    return 'Perdiste renuncia a tu vida'


def gano_jugador(jugador,oponente):

    if ((jugador == 'pi' and oponente == 'ti' )
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False

print(jugar())


