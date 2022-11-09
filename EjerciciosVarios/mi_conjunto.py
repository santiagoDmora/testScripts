def f1(mi_conjunto):
    mi_conjunto.append(8)
    print(mi_conjunto)
    for a in mi_conjunto:
        mi_conjunto.append(a)
    print(mi_conjunto)

mi_conjunto = [4,10]
resultado = f1(mi_conjunto)
print (resultado)