def llenar_elementos(lista:list):
    posicion = 0
    for item_lista in lista:
        if item_lista is None:
            print(f"{item_lista} es none en la posicion {posicion}")
            lista[posicion] = lista[posicion-1]
        posicion += 1
            
            

lista = [1,2,3,None,7,8,None,9]
llenar_elementos(lista)
print(lista)


