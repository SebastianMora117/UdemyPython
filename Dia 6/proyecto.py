from pathlib import *
import os

nombre = input("Porfavor ingrese su nombre: ")
os.system('cls')
ruta = Path(Path.home(), "Desktop", "udemy", "Recetas")
extensiones = ['.txt', '.pdf', '.docx']
cantidadRecetas = sum(1 for archivo in ruta.glob('**/*') if archivo.suffix in extensiones)

def saludo(nombre, ruta, cantidadRecetas):
    print(f"Bienvenido {nombre}\nTu directorio de recetas se encuentra en: ")
    print(f"{ruta}\nEn la cual tienes {cantidadRecetas} recetas")

def verReceta():
    contador = 0
    categoria = []
    receta = []
    numCategoria = 0
    for a in ruta.iterdir():
        categoria.append(a.name)
        contador += 1
        print(f"{contador} {a.name}")
    
    while numCategoria == 0:
        try:
            numCategoria = int(input("Elige una de las categorias de recetas: "))
        except ValueError:
            print("Porfavor ingrese un numero valido")
            numCategoria = 0

    os.system('cls')
    
    if  numCategoria not in range(1, contador + 1):
        print("Porfavor ingrese un numero valido")
        return
    else:
        rutaNueva = Path(ruta, categoria[numCategoria-1])

        if not any(rutaNueva.iterdir()):
                print("No hay recetas en esta categoria")
                return

        print(f"Has elegido la categoria: {categoria[numCategoria-1]}\nLa cual contiene las siguientes recetas: ")

        contador = 0
        for a in rutaNueva.iterdir():
                contador += 1
                receta.append(a.name)
                print(f"Receta #{contador} {a.stem}")

        numReceta = int(input("Elige una de las recetas: "))

        os.system('cls')

        rutaReceta = Path(rutaNueva, receta[numReceta-1])

        print(f"Has elegido la receta: {receta[numReceta-1]}")

        archivoReceta = open(rutaReceta, "r")

        print(archivoReceta.read())

        archivoReceta.close()

def crearReceta():
    contador = 0
    categoria = []
    numCategoria = 0
    for a in ruta.iterdir():
        categoria.append(a.name)
        contador += 1
        print(f"{contador} {a.name}")
    while numCategoria == 0:
        try:
            numCategoria = int(input("Elige una de las categorias de recetas: "))
        except ValueError:
            print("Porfavor ingrese un numero valido")
            numCategoria = 0
    os.system('cls')

    if  numCategoria not in range(1, contador + 1):
        print("Porfavor ingrese un numero valido")
        return
    else:
        rutaNueva = Path(ruta, categoria[numCategoria-1])

        nuevaReceta = input(f"Que receta quieres crear en {categoria[numCategoria-1]}: ")

        rutaReceta = Path(rutaNueva, nuevaReceta + ".txt")

        archivoReceta = open(rutaReceta, "w")

        contenidoReceta = input("Escribe el contenido de la receta: ")
        archivoReceta.write(contenidoReceta)
        archivoReceta.close()
        os.system('cls')

def crearCategoria():
    nuevaCategoria = input("Que categoria quieres crear: ")
    rutaNueva = Path(ruta, nuevaCategoria)
    os.system('cls')

    if not rutaNueva.exists():
        rutaNueva.mkdir()
        print(f"Se ha creado la categoria: {nuevaCategoria}")
        return
    else:
        print(f"La categoria {nuevaCategoria} ya existe")
        return

def eliminarReceta():
    contador = 0
    categoria = []
    receta = []
    numCategoria = 0
    for a in ruta.iterdir():
        categoria.append(a.name)
        contador += 1
        print(f"{contador} {a.name}")
    while numCategoria == 0:
        try:
            numCategoria = int(input("Elige una de las categorias de recetas: "))
        except ValueError:
            print("Porfavor ingrese un numero valido")
            numCategoria = 0
    
    os.system('cls')
    
    rutaNueva = Path(ruta, categoria[numCategoria-1])
    if  numCategoria not in range(1, contador + 1):
        print("Porfavor ingrese un numero valido")
        return
    else:
        if not any(rutaNueva.iterdir()):
                print("No hay recetas en esta categoria")
                return

        print(f"Has elegido la categoria: {categoria[numCategoria-1]}\nLa cual contiene las siguientes recetas: ")

        contador = 0
        for a in rutaNueva.iterdir():
                contador += 1
                receta.append(a.name)
                print(f"Receta #{contador} {a.stem}")

        numReceta = int(input("Elige la receta que se va a eliminar: "))

        os.system('cls')

        rutaReceta = Path(rutaNueva, receta[numReceta-1])

        print(f"Has elegido la receta: {receta[numReceta-1]}")

        if rutaReceta.exists():
            rutaReceta.unlink()
            print(f"Archivo {rutaReceta.name} eliminado exitosamente.")
        else:
            print("El archivo no existe.")
def eliminarCategoria():
    contador = 0
    categoria = []
    numCategoria = 0
    for a in ruta.iterdir():
        categoria.append(a.name)
        contador += 1
        print(f"{contador} {a.name}")
    
    while numCategoria == 0:
        try:
            numCategoria = int(input("Elige la categoria que sera eliminada: "))
        except ValueError:
            print("Porfavor ingrese un numero valido")
            numCategoria = 0

    os.system('cls')

    
    if  numCategoria not in range(1, contador + 1):
        print("Porfavor ingrese un numero valido")
        return
    else:
        rutaNueva = Path(ruta, categoria[numCategoria-1])
        if rutaNueva.exists():
            rutaNueva.rmdir()
            print(f"Categoria {categoria[numCategoria-1]} eliminada exitosamente.")
        else:
            print("La categoria no existe.")

def menu():   
    opcion = 0
    print("Bienvenido al menu de recetas")
    while opcion !=6:
        print("Opcion 1: Ver recetas")
        print("Opcion 2: Crear receta")
        print("Opcion 3: Crear categoria")
        print("Opcion 4: Eliminar receta")
        print("Opcion 5: Eliminar categoria")
        print("Salir 6")

        try:
            opcion = int(input("Porfavor ingrese alguna de las anteriores opciones: "))
            os.system('cls')
        except ValueError:
            os.system('cls')
            opcion = 0

        if opcion >= 1 and opcion <= 6:
            match opcion:
                case 1:
                    verReceta()
                case 2:
                    crearReceta()
                case 3:
                    crearCategoria()
                case 4:
                    eliminarReceta()
                case 5:
                    eliminarCategoria()
                case 6:
                    print("Gracias por usar el programa\nHasta luego!")
        else:
            print("Porfavor ingrese un numero valido")

saludo(nombre, ruta, cantidadRecetas)
menu()
