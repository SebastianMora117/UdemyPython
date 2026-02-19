# def cambiarLetras(tipo):

#     def mayusculas(texto):
#         print(texto.upper())


#     def minuscula(texto):
#         print(texto.lower())

#     if tipo == "may":
#         return mayusculas
#     elif tipo == "min":
#         return minuscula

# operacion = cambiarLetras("min")

# operacion("palabra")


def decorarSaludo(funcion):

    def otraFuncion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return otraFuncion

def mayusculas(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())


mayusculasDecorada = decorarSaludo(mayusculas)

mayusculasDecorada("mundo")