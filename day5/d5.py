# abrir y leer archivo
f = open ('input.txt','r')
mensaje = f.read()
f.close()

# divido por linea y guardo en una lista
list_sits = mensaje.split('\n')

def extractRow(row,ini,end):
    ini = ini
    end = end
    distance = end - ini
    current = list(row)
    for i in current:
        distance = int(distance/2)
        if(i=="F"):
            end = ini + distance
        elif(i=="B"):
            ini = end - distance
    
    return ini

def extractColumn(column,ini,end):
    ini = ini
    end = end
    distance = end - ini
    current = list(column)
    for i in current:
        distance = int(distance/2)
        if(i=="L"):
            end = ini + distance
        elif(i=="R"):
            ini = end - distance
    
    return ini

higher_seat_id = 0
for i in list_sits:
    row = extractRow(i[:-3],0,127)
    column = extractColumn(i[-3:],0,7)
    seat_id = row * 8 + column
    if(higher_seat_id<=seat_id):
        higher_seat_id = seat_id

print(higher_seat_id)