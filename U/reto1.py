activo = True
def calculadora ():
  subT = float(0)  
  v_unit=float(input("Ingrese el valor unitario: "))  
  d_iva=input("El producto cuenta con iva? ") 
  cant=float(input("Ingrese la cantidad de productos a cobrar: "))
  if d_iva == 'S' or d_iva == 's':        
        iva=v_unit*0.19
        v_unit=v_unit+iva
        subT=v_unit*cant
        print("IVA inclido")
        print("SUBTOTAL: ",subT)
  elif d_iva == 'N' or d_iva == 'n':
        subT=v_unit*cant
        print("PRODUCTO SIN IVA")
        print("SUBTOTAL: ",subT)
total = 0
while activo == True:
  subT=calculadora()
  total = total + subT
  dec=input("¿Faltan productos por cobrar? S/N ")   
  if dec == 'S':
    activo = True
  elif dec == 'N':
    activo = False
    print("TOTAL A COBRAR: ",total)
    break