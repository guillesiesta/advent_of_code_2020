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

# check byr (Birth Year) - four digits; at least 1920 and at most 2002.
def checkByr(byr):
    if(len(byr)==4 and 1920<=int(byr)<=2002): return True

# check iyr (Issue Year) - four digits; at least 2010 and at most 2020.
def checkIyr(iyr):
    if(len(iyr)==4 and 2010<=int(iyr)<=2020): return True

# check eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
def checkEyr(eyr):
    if(len(eyr)==4 and 2020<=int(eyr)<=2030): return True

# check hgt (Height) - a number followed by either cm or in: 
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
def checkHgt(hgt):
    if("cm" in hgt):
        new_hgt, cm = hgt.split("cm")
        if(150<=int(new_hgt)<=193): return True
    if("in" in hgt):
        new_hgt, inm = hgt.split("in")
        if(59<=int(new_hgt)<=76): return True

# check hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def checkHcl(hcl):
    return bool(re.search("^#[a-f0-9]{6}$", hcl))


def valid(passport):
    # Validate mandatory fields
    fields = ['byr' ,'iyr' ,'eyr' ,'hgt' ,'hcl' ,'ecl' ,'pid']
    for f in fields:
        if(f not in passport):
            return False

    # Validate numerical
    if not ( 1920 <= int(passport['byr']) <= 2002):
        return False
    if not ( 2010 <= int(passport['iyr']) <= 2020):
        return False
    if not ( 2020 <= int(passport['eyr']) <= 2030):
        return False

    # Validate Height
    if 'cm' in passport['hgt'] and not (150 <= int(passport['hgt'][:-2]) <=193):
        return False
    elif 'in' in passport['hgt'] and not (59 <= int(passport['hgt'][:-2]) <= 76):
        return False
    if 'cm' not in passport['hgt'] and 'in' not in passport['hgt']:
        return False

    # Validate strings/enums
    if  passport['ecl'] not in ['amb', 'blu', 'brn','gry','grn','hzl','oth']:
        return False
    if re.match(r'^\#[0-9a-f]{6}$', passport['hcl']) is None:
        return False
    if re.match(r'^\d{9}$', passport['pid']) is None:
        return False

    return True

# check ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def checkEcl(ecl):
    if(ecl=="amb" or ecl=="blu" or ecl=="brn" 
        or ecl=="brn" or ecl=="gry" or ecl=="grn"
        or ecl=="hzl" or ecl=="oth"):
        return True

# check pid (Passport ID) - a nine-digit number, including leading zeroes.
def checkPid(pid):
    if(len(pid)==9 and pid.isdigit()): return True

# check cid (Country ID) - ignored, missing or not.

invalids = 0
valids = 0
# la clave:valor del diccionario me puede venir bien para analizar cada campo
for i in passports:
    passport_dict={}
    pas = i.split(" ")
    # pongo cada elemento de la lista en forma de clave valor {byr:1925, iyr:2013...} 
    # para que sea más fácil acceder a ese valor en el diccionario y hacer un análisis
    for j in pas:
        a,b = j.split(":")
        passport_dict[a] = b
    
    if valid(passport_dict):
        valids += 1
    # aquí debo de hacer el análisis de cada línea/pasaporte para ver que sea correcta
    # hago esta pequeña prueba para testear la funcion de antes
    '''
    # primero busco los que son no válidos, que les falta cid y también otro campo
    if("cid" not in passport_dict and len(passport_dict)<=6):
        invalids = invalids + 1
    elif(("cid" not in passport_dict and len(passport_dict)>6) or len(passport_dict)==8):
        if("byr" in passport_dict and not checkByr(passport_dict["byr"])):
            invalids = invalids + 1
            continue
        if("iyr" in passport_dict and not checkIyr(passport_dict["iyr"])):
            invalids = invalids + 1
            continue
        if("eyr" in passport_dict and not checkEyr(passport_dict["eyr"])):
            invalids = invalids + 1
            continue
        if("hgt" in passport_dict and not checkHgt(passport_dict["hgt"])):
            invalids = invalids + 1
            continue
        if("hcl" in passport_dict and not checkHcl(passport_dict["hcl"])):
            invalids = invalids + 1
            continue
        if("ecl" in passport_dict and not checkEcl(passport_dict["ecl"])):
            invalids = invalids + 1
            continue
        if("pid" in passport_dict and not checkPid(passport_dict["pid"])):
            invalids = invalids + 1
            continue'''

print("Total de pasaportes: "+str(len(passports)))
print("Pasaportes inválidos: "+str(invalids))
print("Pasaportes válidos: "+str(len(passports) - invalids))
print("Pasaportes válidos: "+str(valids))