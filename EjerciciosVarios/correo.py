def get_final()->list:
    return ['com','es','co','edu']
def get_dominios()->list:
    return['gmail','outlook','hotmail','yahoo']
def is_an_email(correo:str)->bool:
    dominos = get_dominios()
    final = get_final()
    test_1 = correo.find("@")
    test_2 = correo.find(".")
    if correo.find("@")==-1 or correo.find(".")==-1:
        return False
    else:
        explode_1 = correo.split("@")
        longitud = len(explode_1[0])

        if longitud >= 3:
            segunda_parte = explode_1[1]
            explode_2 = segunda_parte.split(".")
            print (explode_2)
            if explode_2[0] in dominos:
                if explode_2[1] in final:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False



is_valide = is_an_email("David@outlook.com")
if is_valide == True:
    print("Correo valido")
else:
    print("Correo Invalido")



