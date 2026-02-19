import os

def limpiar_consola():
    os.system('cls')

# Ejemplo de uso
print("Este texto se verá primero")
input("Presiona Enter para limpiar la consola...")
limpiar_consola()
print("La consola fue limpiada")
