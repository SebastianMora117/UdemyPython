import zipfile

#comprimir archivos

# mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "w")

# mi_zip.write("textoA.txt")
# mi_zip.write("textoB.txt")
# mi_zip.close()

#descomprimir archivos

# zip_abierto = zipfile.ZipFile("archivo_comprimido.zip", "r")
# zip_abierto.extractall("archivos_descomprimidos")
# zip_abierto.close()

import shutil

carpeta_origen = "archivos_descomprimidos"#ruta de la carpeta que quieres comprimir
carpeta_destino = "archivos_comprimidos.zip"#ruta del archivo comprimido

shutil.make_archive(carpeta_destino, 'zip', carpeta_origen)