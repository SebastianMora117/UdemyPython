#r lectura
#w limpia y escribe
#a escribe al final del archivo
archivo = open("Dia 6/prueba1.txt", 'a')

archivo.write("Nuevo texto")
archivo.writelines(["hola", "Mundo"]) #los escribe todos pegados 

archivo = open("Dia 6/prueba1.txt", "r")

print(archivo.read())