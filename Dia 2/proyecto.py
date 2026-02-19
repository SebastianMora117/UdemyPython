nombre = input("Introduce tu nombre: ")
ventas = int((input("Introduce el total de ventas: ")))

comision = round((ventas * 13) / 100, 2)

print (F"Hola {nombre}, tu comisión es de {comision} pesos.")