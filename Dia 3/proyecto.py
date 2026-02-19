texto = input("Introduce un texto: ")
texto = texto.lower()

letras = []
letras.append(input("Introduce la primera letra: ").lower())
letras.append(input("Introduce la segunda letra: ").lower())
letras.append(input("Introduce la tercera letra: ").lower())

#1.Contador de letras

print("\n")
print("CONTADOR DE LETRAS")

print(f"La primera letra se repite {texto.count(letras[0])} veces")
print(f"La segunda letra se repite {texto.count(letras[1])} veces")
print(f"La tercera letra se repite {texto.count(letras[2])} veces")

#2.Contador de palabras
print("\n")
print("CONTADOR DE PALABRAS")

palabras = texto.split(" ")

print(f"El texto tiene {len(palabras)} palabras")

#3.Primera y Ultima letra
print("\n")
print("PRIMERA Y ÚLTIMA PALABRA")

print(f"La primera palabra es: {texto[0]}")
print(f"La última palabra es: {texto[-1]}")

#4.Texto invertido
print("\n")
print("TEXTO INVERTIDO")

palabras.reverse()
print("El texto invertido es:")
print(" ".join(palabras))

#5.Se encuentra la palabra python
print("\n")
print("SE ENCUENTRA LA PALABRA PYTHON")

buscarPython = "python" in texto

resultadoBusqueda = {"False": "No se encuentra la palabra 'python'", "True": "Se encuentra la palabra 'python'"}
print(resultadoBusqueda[str(buscarPython)])