import os
class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    
    def __init__(self, nombre, apellido, numeroCuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numeroCuenta = numeroCuenta
        self.balance = balance

    def mostrarInfoCliente(self):

        print(f"El cliente {self.nombre} {self.apellido} tiene un balance en su cuenta de: {self.balance}")
    
    def depositar(self):
        cantidad = 0
        try:
            cantidad = int(input(f"Sr@ Cuanto dinero desea ingresar a su cuenta: "))
        except ValueError:
            print("Porfavor ingrese un valor valido")
            cantidad = 0
        
        self.balance = self.balance + cantidad 

        return f"Su nuevo saldo es: {self.balance}"

    def retirar(self):
        cantidad = 0        
        try:
            cantidad = int(input(f"Sr@ Cuanto dinero desea retirar a su cuenta: "))
        except ValueError:
            print("Porfavor ingrese un valor valido")
            cantidad = 0
        
        
        if cantidad > self.balance:
            return "No se tiene el saldo suficiente para realizar ese retiro"
        else:
            self.balance = self.balance - cantidad 

        return f"Su nuevo saldo es: {self.balance}"

nombre = input("Porfavor ingrese su nombre: ")
apellido = input("Porfavor ingrese su apellido: ")
numCuenta = input("Porfavor ingrese su cumero de cuenta")

cliente = Cliente(nombre, apellido, numCuenta)

def menu ():
    opcion = 0

    while opcion != 3:
        os.system('cls')
        cliente.mostrarInfoCliente()
        print("Opcion 1: Depositar ")
        print("Opcion 2: Retirar ")
        print("Opcion 3: Salir ")

        try:
            opcion = int(input("Porfavor ingrese alguna de las anteriores opciones: "))
            os.system('cls')
        except ValueError:
            os.system('cls')
            opcion = 0
        
        if opcion > 0 and opcion < 3:
            match opcion:
                case 1:
                    print(cliente.depositar())
                case 2:
                    print(cliente.retirar())
        else:
            print("Ingrese una opcion valida")

menu()
