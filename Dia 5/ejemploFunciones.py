preciosCafe = [("Capuchino", 1.5), ("Expreso", 2), ("Moka", 1.9)]

def cafeCaro(preciosCafe):
    precioMayor = 0
    cafeMasCaro = 0
    for c,p in preciosCafe:

        if p > precioMayor:
            precioMayor = p
            cafeMasCaro = c
        else:
            pass
    return(cafeMasCaro, precioMayor)

print(cafeCaro(preciosCafe))