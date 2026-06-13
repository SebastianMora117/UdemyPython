
def mensaje(funcion):
    def wrapper():
        resultado = next(funcion)
        print(resultado)
    return wrapper

def perfumeria():
    turno = 0
    while True:
        turno += 1
        yield f"Turno P{turno}: Bienvenido a la perfumeria"

def farmacia():
    turno = 0
    while True:
        turno += 1
        yield f"Turno F{turno}: Bienvenido a la farmacia"

def cosmeticos():
    turno = 0
    while True:
        turno += 1
        yield f"Turno C{turno}: Bienvenido a la cosmetica"