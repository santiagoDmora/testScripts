def bubleShort(list):
    length = len(list)- 1

    #Recorre 
    for i in range (0,length):
        
        for j in range(0,length):
            if list [j] > list [j+1]:
                temp = list[j]
                list [j] = list[j+1]
                list [j+1] = temp

    return list


list = [70,90,0,80,60,85]
print("Antes de ordenar")
print (list)
print("Despues de ordenar")
print (list)
print(bubleShort(list))