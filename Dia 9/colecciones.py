from collections import *

numeros = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10 , 1, 2]

# defaultdict: devuelve un valor por defecto si la clave no existe
numeros = defaultdict(lambda: "NADA", Counter(numeros))

prioridad = Counter(numeros)
print(prioridad)

#counter: cuenta la cantidad de veces que aparece cada elemento en una secuencia
frase = "Hola mundo, hola a todos"
contador_frase = Counter(frase.split())
print(contador_frase)

#namedtuple: crea una clase con campos nombrados
persona = namedtuple("Persona", ["nombre", "edad", "ciudad"])
persona1 = persona("Juan", 30, "Madrid")
print(persona1)