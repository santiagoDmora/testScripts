name = "Santiago"
last_name = "Mora"
print(name)
print(last_name)


#concatenacion 
full_name = name + ' ' + last_name
print(full_name)

#Uso de comillas
quote = "I'm Nicolas"
print(quote)

quote2 = "She said 'hello'"
print(quote2)

#format
template = "Hola mi nombre es " + name + " y mi apellido es " + last_name
print(template)

template2 = "Hola , mi nombre es {} y mi apellido es {}".format(name,last_name)
print(template2)

edad = 23

template = f"hola, mi nombre es {name} y mi apellido es {last_name} y tengo {edad} años "
print(template)