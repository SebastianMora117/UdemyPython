def numCuatro():
    lista = []

    for i in range(1, 5):
        lista.append(i * 10)
    return lista

def genCuatro():
    for i in range(1, 5):
        yield i * 10

print(numCuatro())
print(genCuatro())

g = genCuatro()

print(next(g))
print(next(g))
print(next(g))
print(next(g))