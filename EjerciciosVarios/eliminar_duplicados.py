def eliminar_duplicados(lista:list):
    posicion = 0
    for item in lista:
        cantidad = lista.count(item)
        if cantidad > 1:
            lista.pop(posicion)
            print(f"{item} en posicion {posicion} y su cantidad es {cantidad}")
        posicion += 1


l = [1,1,2,2,3,4,4,5,1]
x = set(l)
print(x)
# eliminar_duplicados(l)
# print(l)