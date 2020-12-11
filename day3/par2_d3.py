
# abrir y leer archivo
f = open ('input.txt','r')
mensaje = f.read()
f.close()

map_squares_trees = mensaje.split('\n')
# print(map_squares_trees)

# cantidad de elementos (square or tree) por cada fila
lenght_of_one_line = len(map_squares_trees[0])

def number_of_trees(map_squares_trees,right,down):
    trees = 0
    linea = down
    pos_columna = right
    map_squares_trees = map_squares_trees
    down = down
    
    for i, item in enumerate(map_squares_trees,start=-1):
        
        # ignoro el primer elemento de la linea
        if(down==1): 
            if(i==-1):
                continue
        #print(i,item)
        if(down==2):
            if(i==-1 or i==0):
                continue
            if(i % 2 == 0):
                continue
        # print( "La linea ahora es: "+ str(linea))
        # print(i,item)
        pos_columna = pos_columna % lenght_of_one_line
        if(item[pos_columna]=="#"):
            #print("Hay un árbol en: "+ str(i) + "en la position: "+str(pos_columna) )
            trees = trees + 1 
        pos_columna = pos_columna + right
        linea = linea + down
        #print(linea)
    return trees


# print("Total de arboles "+ str(number_of_trees(map_squares_trees,3,1)))
'''print(number_of_trees(map_squares_trees,1,1))
print(number_of_trees(map_squares_trees,3,1))
print(number_of_trees(map_squares_trees,5,1))
print(number_of_trees(map_squares_trees,7,1))
print(number_of_trees(map_squares_trees,1,2))'''

# la solucion debe ser: 9354744432

print("Total result= "+ 
    str(number_of_trees(map_squares_trees,1,1) *
        number_of_trees(map_squares_trees,3,1) *
        number_of_trees(map_squares_trees,5,1) *
        number_of_trees(map_squares_trees,7,1) *
        number_of_trees(map_squares_trees,1,2)))