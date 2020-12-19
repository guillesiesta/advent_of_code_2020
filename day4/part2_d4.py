import re

# abrir y leer archivo
f = open ('input.txt','r')
mensaje = f.read()
f.close()

# he visto en internet que con esto divides por los espacios en blanco
# funciona
output = mensaje.split('\n\n')

# elimino el \n de todos los elementos de la lista
passports = [i.replace('\n',' ') for i in output]


def is_valid(passport):
    # Checkeo que no falte ninguno de estos fields
    # como cid es opcional, no lo pongo
    fields = ["byr" ,"iyr" ,"eyr" ,"hgt" ,"hcl" ,"ecl" ,"pid"]
    for f in fields:
        if(f not in passport):
            return False
    
    # Hago un primer checkeo de los valores numéricos
    if(not  1920 <= int(passport["byr"]) <= 2002):
        return False
    if(not  2010 <= int(passport["iyr"]) <= 2020):
        return False
    if(not  2020 <= int(passport["eyr"]) <= 2030):
        return False

    # Valido la altura
    # con [:-2] ignoro los dos últimos caracteres
    if("cm" in passport["hgt"] and not (150 <= int(passport["hgt"][:-2]) <=193)):
        return False
    elif("in" in passport["hgt"] and not (59 <= int(passport["hgt"][:-2]) <= 76)):
        return False
    if("cm" not in passport["hgt"] and "in" not in passport["hgt"]):
        return False

    # Valido los strings
    if(passport["ecl"] not in ["amb", "blu", "brn","gry","grn","hzl","oth"]):
        return False
    if(re.match(r'^\#[0-9a-f]{6}$', passport["hcl"]) is None):
        return False
    if(re.match(r'^\d{9}$', passport["pid"]) is None):
        return False

    return True

# contador
valids = 0
# la clave:valor del diccionario me puede venir bien para analizar cada campo
for i in passports:
    current_passport_dict={}
    pas = i.split(" ")
    # pongo cada elemento de la lista en forma de clave valor {byr:1925, iyr:2013...} 
    # para que sea más fácil acceder a ese valor en el diccionario y hacer un análisis
    for j in pas:
        a,b = j.split(":")
        current_passport_dict[a] = b
    # valido que  el pasaporte actual esté correcto
    if is_valid(current_passport_dict):
        valids += 1

print("Pasaportes válidos: "+str(valids))