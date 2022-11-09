def multiplicar (numero1,numero2):
    resultado = numero1 * numero2
    return resultado
# 
# 
# print(multiplicar(4,5))

# multiplicarnumeros = lambda n1 ,n2: n1*n2
# print(multiplicarnumeros(2,3))

listaa = [4,7,3,8,9,6]

def encontrar_posicion_lista (lista:list,numero):
    posicion = lista.index(numero)
    return posicion
# print (encontrar_posicion_lista(listaa,0))

encontrarnumero = lambda lista,numero: lista.index(numero)
print(encontrarnumero(listaa,6))
  


            

