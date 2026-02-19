from random import *
#lista inicial
palitos = ['-', '--', '---', '----']

#mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#pedirle intento

def intento():
    intento = ''

    while intento not in [1, 2, 3, 4]:
        intento = int(input("Elige un numero del 1 al 4: "))
    
    return intento

#comprobar intento
def comprobarIntento(lista, intento):
    if lista[intento - 1] == '-':
        print("A lavar los platos")
    else:
        print("Se salvo")
    
    print(f"Te ha tocado {lista[intento -1]}")

palitosMezclados = mezclar(palitos)
seleccion = intento()
comprobarIntento(palitosMezclados, seleccion)