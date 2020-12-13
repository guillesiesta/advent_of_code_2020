# abrir y leer archivo
f = open ('input.txt','r')
mensaje = f.read()
f.close()

# he visto en internet que con esto divides por los espacios en blanco
# funciona
output = mensaje.split('\n\n')

# elimino el \n de todos los elementos de la lista
passports = [i.replace('\n',' ') for i in output]

# check byr (Birth Year) - four digits; at least 1920 and at most 2002.
def checkByr(byr):
    if(len(byr)==4 and 1920<=int(byr)<=2002): return True
# check iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# check eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# check hgt (Height) - a number followed by either cm or in: 
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
# check hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# check ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# check pid (Passport ID) - a nine-digit number, including leading zeroes.
# check cid (Country ID) - ignored, missing or not.

valids = 0
# la clave:valor del diccionario me puede venir bien para analizar cada campo
new_passports=[]
for i in passports:
    passport_dict={}
    pas = i.split(" ")
    # pongo cada elemento de la lista en forma de clave valor {byr:1925, iyr:2013...} 
    # para que sea más fácil acceder a ese valor en el diccionario y hacer un análisis
    for j in pas:
        a,b = j.split(":")
        passport_dict[a] = b
    # aquí debo de hacer el análisis de cada línea/pasaporte para ver que sea correcta
    # hago esta pequeña prueba para testear la funcion de antes
    if("byr" in passport_dict and checkByr(passport_dict["byr"])):
        print(passport_dict["byr"])
    #new_passports.append(dict(passport_dict))

'''for i in new_passports:
    print(i)'''