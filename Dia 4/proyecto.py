from random import randint

nombre = input("Ingrese su nombre: ")

intentos = 0
adivinar = randint(1, 100)
print(f"Hola {nombre} tienes que adivinar un numero del 1 al 100 y solo tienes 8 intentos")

while intentos < 8:
    intentos += 1
    numero = int(input("Porfavor ingrese un numero: "))
    if numero > 100 or numero <= 0:
        print("El numero es invalido tiene que ser un numero de 1 a 100")
    elif numero < adivinar:
        print("El numero ingresado es menor a la respuesta")
    elif numero > adivinar:
        print("El numero ingresado es mayor a la respuesta")
    elif numero == adivinar:
        print(f"Felicidades {nombre} adivinaste en numero en {intentos} intentos")
        break
else:
    print("Como nos haz adivinado el numero se reiniciaran los intentos con un numero diferente")