def busqueda_binaria(list,numero_busqueda):
    list.sort()
    derecha = len(list)-1
    izquierda = 0
    while izquierda <= derecha:
        medio = izquierda+(derecha-izquierda)//2
        print (f"{izquierda},{derecha},{medio}")
        if numero_busqueda == list[medio]:
            return True
        if numero_busqueda > list[medio]:
            izquierda = medio + 1
        if numero_busqueda < list[medio]:
            derecha = medio -1
        
        
    return False


lst = [4,10,12,8,6,9]
encontrado = busqueda_binaria(lst,6)
print(encontrado)