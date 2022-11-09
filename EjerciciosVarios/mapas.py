def incrementar (numero):
    nuevonumero = numero + 10
    return nuevonumero
print (incrementar(5))

lista = [2,2,6,7,8,9]
resultado = list(map(incrementar,lista))
print (resultado)