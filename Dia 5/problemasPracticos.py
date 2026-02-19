#problema 1

def devolver_distintos(num1, num2, num3):
    lista = [num1, num2, num3]
    lista.sort()
    suma = num1 + num2 + num3

    if suma > 15:
        return f"El numero mayor es {lista[-1]}"
    elif suma < 10:
        return f"El numero menor es {lista[0]}"
    else:
        return f"El numero intermedio es {lista[1]}"

print(devolver_distintos(9, 6, 0))

#problema 2
def palabra(palabra):
    lista = []

    for i in palabra:
        if i not in lista:
            lista.append(i)
    lista.sort()
    return lista

print(palabra("Sebastian"))

#Problema 3

def cero(*args):
    contador = 0
    if contador + 1 == len(args):
        return False
    elif args[contador] == 0 and args[contador + 1] == 0:
        return True
    else:
        contador =+1
    return False
print(cero(6,0,5,1,0,3,0,1))

#Problema 4

def contar_primos(numero):
    if numero < 2:
        print("No hay números primos en ese rango.")
        return 0

    primos = []

    for n in range(2, numero + 1):
        es_primo = True
        for divisor in range(2, int(n**0.5) + 1):
            if n % divisor == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(n)

    print("Números primos encontrados:", primos)
    return len(primos)

# Ejemplo de uso
cantidad = contar_primos(30)
print("Cantidad de números primos:", cantidad)   