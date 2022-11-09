def es_par(numero:int):
    if numero % 2 == 0:
        return True
    else:
        return False


lista = [2,5,6,8,9.234,3456,765,1245]
lista_pares = list(filter(es_par,lista))    
print (lista_pares)
