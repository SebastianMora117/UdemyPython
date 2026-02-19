from pathlib import *

carpeta = Path("C:/Users/User/Desktop/udemy/Dia 6/prueba1.txt")

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print("El archivo no exite")
else:
    print("Existe")