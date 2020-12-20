# abrir y leer archivo
f = open ('input_light.txt','r')
mensaje = f.read()
f.close()

# divido por linea y guardo en una lista
list_sits = mensaje.split('\n') 