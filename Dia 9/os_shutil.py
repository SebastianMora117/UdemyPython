import os

# print(os.getcwd())  # Obtener el directorio actual

# archivo = open("archivo.txt", "w")
# archivo.write("Texto de prueba")

# print(os.listdir())  # Listar los archivos en el directorio actual

# archivo.close()

# os.unlink("nuevo_archivo.txt")  # Eliminar el archivo

# os.rmdir("nueva_carpeta")  # Eliminar una carpeta vacía

print(os.walk("C:\\Users\\juans\\OneDrive\\Documentos\\UdemyPython") ) # Recorrer un directorio y sus subdirectorios

for carpeta, subcarpetas, archivos in os.walk("C:\\Users\\juans\\OneDrive\\Documentos\\UdemyPython"):
    print(f"Carpeta: {carpeta}")
    print(f"Subcarpetas: {subcarpetas}")
    print(f"Archivos: {archivos}")
    print("-" * 20)

# import shutil

# shutil.move("nuevo_archivo.txt", "C:\\Users\\juans\\OneDrive\\Documentos\\UdemyPython")  # Mover el archivo a una nueva ubicación

# shutil.rmtree("carpeta_con_archivos")  # Eliminar una carpeta con archivos dentro

# import send2trash #hay que instalar la librería send2trash para usar esta función

# send2trash.send2trash("archivo_para_eliminar.txt")  # Enviar el archivo a la papelera de reciclaje en lugar de eliminarlo permanentemente
