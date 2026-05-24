
class Instrumento:
    def __init__(self, tipo, marca, material_fabricacion):
        self.tipo = tipo
        self.marca = marca
        self.material_fabricacion = material_fabricacion

    def afinar(self):
        return f"Afinando el instrumento de tipo {self.tipo}."

class Guitarra(Instrumento):
    def tocar_acorde(self):
        return f"Tocando un acorde en la guitarra {self.marca}."


# FUERA DE LA CLASE

mi_guitarra = Guitarra("Cuerdas", "Fender", "Madera de Caoba")
print(f"tipo del instrumento: {mi_guitarra.tipo}")
print(f"Marca seleccionada: {mi_guitarra.marca}")
print(f"Material: {mi_guitarra.material_fabricacion}")
print(mi_guitarra.afinar())
print(mi_guitarra.tocar_acorde())
