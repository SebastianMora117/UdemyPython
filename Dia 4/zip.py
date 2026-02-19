nombre = ["Sebastian", "Juan", "Mora"]
edad = [21, 20, 19]

combinados = list(zip(nombre, edad))

print(combinados)

for nombre, edad in combinados:
    print(f"{nombre} tiene {edad} años")