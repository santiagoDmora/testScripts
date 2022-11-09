alto=float(input())
ancho=float(input())
profundo=float(input())
incremento=0

volumen=alto*ancho*profundo
v_previo=volumen*5

if alto>30:
    incremento=2000

costo=v_previo+incremento

if costo>10000:
    costo=costo*1.19
print(volumen)
print(costo)