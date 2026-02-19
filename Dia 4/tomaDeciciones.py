if 10 > 9:
    print("10 es mayor que 9") 
else:
    print("10 no es mayor que 9")

mascota = "perro"

if mascota == "gato":
    print("Tu mascota es un gato")
elif mascota == "perro":
    print("Tu mascota es un perro")
elif mascota == "pez":
    print("Tu mascota es un pez")
else:
    print("No se que mascota tienes")

edad = 18
calificacion = 9

if edad < 18:
    print("Eres menor de edad")
    if calificacion >= 7:
        print("Aprobado")
    else:
        print("Reprobado")
else:
    print("Eres mayor de edad")