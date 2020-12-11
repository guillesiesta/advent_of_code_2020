
# abrir y leer archivo
f = open ('input.txt','r')
mensaje = f.read()
f.close()

map_squares_trees = mensaje.split('\n')
# print(map_squares_trees)

# cantidad de elementos (square or tree) por cada fila
lenght_of_one_line = len(map_squares_trees[0])

pos_columna = 3
pos_linea = 0
iteraciones = 0
tree = 0

# con [1:] ignoro el primer elemento de la lista
for i in map_squares_trees[1:]:
    # ahora busco que todas las columnas no sean mayores de 11,
    # para ello siempre hago el modulo sobre 11 de las posiciones
    # de la columna, así si al sumar 3 casillas sale 12, se refiere a
    # que es la posición 1 de la siguiente fila
    # recordar que empiezo a contar desde 0 las filas
    pos_columna = pos_columna % (lenght_of_one_line)
    if(i[pos_columna]=="#"):
        tree = tree + 1 
    pos_columna = pos_columna + 3
    iteraciones = iteraciones + 1

print(tree)