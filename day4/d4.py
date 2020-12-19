# abrir y leer archivo
f = open ('input.txt','r')
mensaje = f.read()
f.close()

# he visto en internet que con esto divides por los espacios en blanco
# funciona
output = mensaje.split('\n\n')

# elimino el \n de todos los elementos de la lista
passports = [i.replace('\n',' ') for i in output]

valids = 0
for i in passports:
    # primera parte
    # todas las que cumplan que tienen 8 fields las cuento como válidas
    # separo el passport por espacios, y analizo si están los 8 fields
    # segunda parte
    # si cid no está no pasa nada, pero si no está ese solamente
    # es decir, si hay 7 y es cid el que falta, también es válido
    if((len(i.split(" "))==8) or ("cid" not in i and len(i.split(" "))==7)):
        valids = valids + 1
        
print(valids)