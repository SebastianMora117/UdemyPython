texto = "Buena mis perros"

mayusculas = texto.upper()
minusculas = texto.lower()
separado = texto.split()#dentro del parentesis se puede poner un caracter para separar, por defecto es el espacio

print(separado)

a = "Hola"
b = "Mundo"

unir = " ".join([a, b]) #une la lista con el caracter que le ponga
print(unir)

remplazar = texto.replace("Buena", "Mala") #reemplaza una cadena por otra
print(remplazar)