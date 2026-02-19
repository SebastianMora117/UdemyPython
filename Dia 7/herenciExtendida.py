class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("Ja, ja, ja")

    def hablar(self):
        print("Hola desde la madre")
        
class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

miNieto = Nieto()
miNieto.hablar()#muestra en orden de herencia
miNieto.reir()