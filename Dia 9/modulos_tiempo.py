import time

def prueba_for(numero):
    lista = []
    for i in range(numero):
        lista.append(i)
    return lista

def prueba_while(numero):
    lista = []
    i = 0
    while i < numero:
        lista.append(i)
        i += 1
    return lista

inicio = time.time() #obtener el tiempo actual en segundos

prueba_for(10000000)

final = time.time() #obtener el tiempo actual en segundos

# print(final - inicio) #calcular el tiempo que tardó la función en ejecutarse

inicio = time.time()

prueba_while(10000000)

final = time.time()

# print(final - inicio)


import timeit


declaracion = """
prueba_for(10)
"""

misetup = """
def prueba_for(numero):
    lista = []
    for i in range(numero):
        lista.append(i)
    return lista
"""
duracion_for =timeit.timeit(declaracion, setup=misetup, number=1000000)

print(duracion_for)

declaracion = """
prueba_while(10)
"""
misetup = """
def prueba_while(numero):
    lista = []
    i = 0
    while i < numero:
        lista.append(i)
        i += 1
    return lista
"""
duracion_while =timeit.timeit(declaracion, setup=misetup, number=1000000)

print(duracion_while)