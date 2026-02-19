class Animal:
    
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("El animal ha nacido")
    
    def hablar(self):
        print("El animal hace un sonido")

class Pajaro(Animal):

    def __init__(self, edad, color, alturaVuelo):
        super().__init__(edad, color)
        self.alturaVuelo = alturaVuelo
        


    def hablar(self):
        print("El pájaro dice pio")
    
    def volar(self, metros):
        print(f"El pájaro vuela {metros} metros")

piolin = Pajaro(2, "Rojo", 30)
animal = Animal(5, "Marrón")
piolin.hablar()

animal.hablar()
