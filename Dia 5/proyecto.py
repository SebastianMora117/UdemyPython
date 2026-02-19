from random import *

listaPalabras = ["HOLA", "MUNDO", "SEBASTIAN", "PERRO", "GATO", "AHORCADO"]
print("Bienvenido al juego del ahorcado\nel programa eligira una palabra al azar\nDeberas ingresar una letra para ir adivinando\n" \
"Tienes solo 6 oportunidades para equivocarte")

def escogerPalabra(palabras):
    return choice(palabras)

def pedirLetra():
    valida = False
    letra = ""
    while valida == False:
        letra = input("Porfavor ingrese una letra: ").upper()

        if len(letra) > 1 or not letra.isalpha():
            valida = False
            print("Solo puede ser una sola letra y tampoco puede ser un numero")
        else:
            valida = True
    return letra

def ahorcado(palabra):
    cantidad = len(palabra)
    guiones = ["_"] * cantidad
    intentos = 6
    print(f"La palabra es: {' '.join(guiones)}")

    while intentos > 0:
        letra = pedirLetra()
        
        if letra in palabra:
            for i, p in enumerate(palabra):
                if p == letra:
                    guiones[i] = p
            print("La palabra es:", " ".join(guiones))
            
            if "".join(guiones) == palabra:
                return "¡Felicidades, adivinaste la palabra!"
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

    print("Han terminado tus intentos.")
    print(f"La palabra era: {palabra}")

palabra = escogerPalabra(listaPalabras)
ahorcado(palabra)