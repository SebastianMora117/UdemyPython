def sumar(*args):
    total = 0
    for r in args:
        total += r
    return total

print(sumar(4+4+4))