def infinitos(i):
    while True:
        i += 1
        yield i

generador = infinitos(1)

while True:
    print(next(generador))