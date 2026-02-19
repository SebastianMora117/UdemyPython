# def tresCifras(numero):
#     lista = []
#     for n in numero:
#         if n in range(100, 1000):
#             lista.append(n)
#         else:
#             pass
#     return f"Los numeros de tres digitos de tu lista son: {lista}"

# resultado = tresCifras([55, 100, 999])

# print(resultado)

lista_numeros = [1, 50, 502, 755, 34]

def cantidad_pares(lista_numeros):
    cantidad = 0
    for n in lista_numeros:
        if n % 2 == 0:
            cantidad += 1
        else:
            pass
    return cantidad

print(cantidad_pares(lista_numeros))
    