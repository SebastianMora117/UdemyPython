class Pajaro:
    alas = True #atributo de clase
    def __init__(self, nombre, color): #atributos de instancia
        self.nombre = nombre
        self.color = color

    def piar(self):
        print("Pío, pío")

    def volar(self, metros):
        print(f"El pajaro {self.color} vuela {metros} metros")

miPajaro = Pajaro("Loro", "Verde")

miPajaro.piar()
miPajaro.volar(10)