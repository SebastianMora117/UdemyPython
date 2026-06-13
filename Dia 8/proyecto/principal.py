from numeros import *

gen_perfumeria = mensaje(perfumeria())
gen_farmacia = mensaje(farmacia())
gen_cosmeticos = mensaje(cosmeticos())

while True:
    inicio = input("Ingrese el lugar: 1. Perfumeria, 2. Farmacia, 3. Cosmeticos (0 para salir): ")

    if inicio == "0":
        print("Saliendo del programa...")
        break
    elif inicio == "1":
        gen_perfumeria()
    elif inicio == "2":
        gen_farmacia()
    elif inicio == "3":
        gen_cosmeticos()

    otro = input("¿Desea sacar otro turno? (s/n): ")
    if otro.lower() != "s":
        print("Saliendo del programa...")
        break