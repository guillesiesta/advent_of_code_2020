# abrir y leer archivo
f = open('input.txt','r')
mensaje = f.read()
f.close()

# meto en una lista enorme todo el input separado por final de línea
map_squares_trees = mensaje.split('\n')

# cantidad de elementos (square or tree) por cada fila
lenght_of_one_line = len(map_squares_trees[0])

def number_of_trees(map_squares_trees, right, down):
    trees = 0
    pos_columna = right
    
    for i, item in enumerate(map_squares_trees, start=0):
        # ignoro el primer elemento de la linea cuando 
        # hay que bajar de 1 en 1 línea
        if(down==1 and i==0): continue
        # ignoro los dos primeros elementos de la lista
        # cuando hay que bajar de 2 en 2
        # y luego voy de 2 en 2 bajando, es decir,
        # aquellas posiciones de la lista que son impares
        # algo % 2 != 0, tampoco las tengo en cuenta para el proceso
        if(down==2):
            if(i==0 or i==1): continue
            # me salto las líneas que no son pares, es decir, me salto las impares
            # así me garantizo el ir de 2 en 2 bajando
            if(i % 2 != 0): continue
        # aqui calculo el modulo de la posicion de la columna
        # para que no se salga del rango maximo de valores de la 
        # longitud de los caracteres de la fila o linea cuando se sume
        # el da X pasos hacia la derecha
        pos_columna = pos_columna % lenght_of_one_line
        # si encuentro un arbol en la position, aumento el contador de árboles en 1
        if(item[pos_columna]=="#"): trees = trees + 1
        # actualizo la position de la columna tantos pasos a la derecha como se indique
        pos_columna = pos_columna + right
    return trees

# calculo la solucion final
print("Total result= "+ 
    str(number_of_trees(map_squares_trees,1,1) *
        number_of_trees(map_squares_trees,3,1) *
        number_of_trees(map_squares_trees,5,1) *
        number_of_trees(map_squares_trees,7,1) *
        number_of_trees(map_squares_trees,1,2)))

#Con el input que tengo a día de hoy, la solucion debe ser: 9354744432