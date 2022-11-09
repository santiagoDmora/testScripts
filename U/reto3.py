numeroPaquetes=int(input())
costoTotal = 0
i = 0

for x in range(1,numeroPaquetes+1):

    alto=float(input())
    ancho=float(input())
    profundo=float(input())


    volumen = alto * ancho * profundo
    costoantes = volumen * 5

    if alto>30:
        i = 2000
    costo = costoantes + i

    if costo>10000:
        costo = costo * 1.19        
    print(volumen)
    print(costo)

    costoTotal = costoTotal + costo
print(costoTotal)
    

