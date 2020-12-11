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
    if(len(i.split(" "))==8):
        valids = valids + 1
    elif("cid" not in i and len(i.split(" "))==7):
        valids = valids + 1

print(valids)