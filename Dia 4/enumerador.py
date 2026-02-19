lista = ["a", "b", "c"]

for indice, i in enumerate(lista):
    print(indice, i)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indices, i in enumerate(lista_nombres):
    if i[0] == "M":
        print(indices, i)