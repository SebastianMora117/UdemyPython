from random import *

aleatorio = randint(1, 50) #randint

print(aleatorio)

aleatorio = round(uniform(1, 5), 1)#uniform

print(aleatorio)

aleatorio = random()#random

print(aleatorio)

nombres = ["Juan", "Sebastian" ,"Mora"]

print(choice(nombres))#choise

numeros = list(range(5, 50, 5))

shuffle(numeros)#shufles

print(numeros)