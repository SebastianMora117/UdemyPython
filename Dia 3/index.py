miTexto = "Algo"

resultado = miTexto[3]
resultado2 = miTexto[-3]
print(resultado)
print(resultado2)

resultado3 = miTexto.index("g")

print(resultado3)

resultado4 = miTexto.index("g", 0, 4)#busca del 0 al 4
print(resultado4)

resultado5 = miTexto.rindex("o")#busca desde el final
print(resultado5)
############################################################
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"

resultado6 = frase[::-1]##invierte la cadena

print(resultado6)