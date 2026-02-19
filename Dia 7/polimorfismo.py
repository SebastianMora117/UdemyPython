class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice mu")

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice beee")

vaca1 = Vaca("Lola")
oveja1 = Oveja("Mimi")

vaca1.hablar()
oveja1.hablar()

def animal_hablar(animal):
    animal.hablar()

animal_hablar(vaca1)
animal_hablar(oveja1)
