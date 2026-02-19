def multiplicar(num1, num2):
    return num1 * num2

resultado = multiplicar(2, 3)
print(resultado)

def invertir_palabra(palabra):
    palabra = palabra.upper()
    return palabra[::-1]
palabra = (invertir_palabra("hola"))

print(palabra)