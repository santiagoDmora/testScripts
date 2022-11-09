def calcularCosto(altura,ancho,profundo):
    volumen = altura * ancho * profundo
    costo = volumen * 5
    if altura > 30:
        costo = costo + 2000
    if costo > 10000:
        iva = costo * 0.19
        costo = costo + iva
        return costo

def costoTotal(npaquetes, dcto):
    costoTotal=0
    for _ in range(0, npaquetes):
        alto = float(input(""))
        ancho = float(input(""))
        profundo = float(input(""))
        costoTotal+=calcularCosto(alto, ancho, profundo)
    costoTotal-=costoTotal*(dcto/100)
    return costoTotal