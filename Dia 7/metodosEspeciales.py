class Cd:

    def __init__(self, autor, titulo, cancion):
        self.autor = autor
        self.titulo = titulo
        self.cancion = cancion

    def __str__(self):
        return f"Autor: {self.autor}, Título: {self.titulo}, Canciones: {self.cancion}"

    def __len__(self):
        return self.cancion
    
    def __del__(self):
        print(f"El CD '{self.titulo}' de {self.autor} ha sido eliminado.")

miCd = Cd("Metallica", "Master of Puppets", 18)

print(len(miCd))

del miCd