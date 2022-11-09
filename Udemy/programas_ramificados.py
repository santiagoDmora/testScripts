nombre_1 = input('Cual es tu nombre: ')
edad_1 = input('Cual es tu Edad: ')
nombre_2 = input('Cual es tu nombre: ')
edad_2 = input('Cual es tu Edad: ')

if edad_1 > edad_2 :
    print (f' {nombre_1} es mayor con {edad_1} años de edad ')
elif edad_1 < edad_2 :  
    print (f' {nombre_2} es mayor con {edad_2} años de edad ')
elif edad_1 == edad_2 :
    print (f' {nombre_1} y {nombre_2} tienen la misma edad {edad_1} , {edad_2} ')

