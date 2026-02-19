class Pajaro:
    alas = True 
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def piar(self):
        print("Pío, pío")

    def volar(self, metros):
        print(f"El pajaro {self.color} vuela {metros} metros")
        self.piar()
    def pintarNegro(self):
        self.color = "Negro"
        print(f"Ahora el pajaro es de color {self.color}")

    @classmethod
    def ponerHuevo(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(cls.alas)

    @staticmethod
    def mirar():
        print("El pajaro mira")


miPajaro = Pajaro("Loro", "Verde")

miPajaro.volar(10)
miPajaro.pintarNegro()
miPajaro.alas = False

print(miPajaro.alas)

miPajaro.ponerHuevo(3)