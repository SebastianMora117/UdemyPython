import os

ruta = ("c:\\Users\\User\\Desktop\\udemy\\Dia 6\\prueba1.txt")

ruta = os.path.split(ruta)

print(ruta)

from pathlib import *

carpeta = Path("C:/Users/User/Desktop/udemy/Dia 6")
archivo = carpeta / "prueba1.txt"

miArchivo = open(archivo)
print(miArchivo.read())