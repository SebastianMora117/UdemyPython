def suma():
    num1 = int(input("Ingrese en primer numero: "))
    num2 = int(input("Ingrese en segundo numero: "))
    print(num1 + num2)

try:
    suma()
except ValueError:
    print("Solo se aceptan numeros")
except TypeError:
    print("No se pueden sumar tipos distintos")
else:
    print("Todo bien")
finally:
    print("Eso fue todo")