
class Contenido:
    def __init__(self, titulo, duracion_minutos, genero):
        self.titulo = titulo
        self.duracion_minutos = duracion_minutos
        self.genero = genero

    def reproducir(self):
        return f"Netflix esta reproduciendo: {self.titulo}..."

class Pelicula(Contenido):
    def mostrar_creditos(self):
        return f"Gracias por ver esta producción que fue un éxito total en cines."


# FUERA DE LA CLASE 
# 3 atributos
mi_peli = Pelicula("Avengers", 180, "Acción")

#acciones 
print(mi_peli.reproducir())
print(mi_peli.mostrar_creditos())
print(f"La película dura {mi_peli.duracion_minutos} minutos.")
print(f"Su género es {mi_peli.genero}.")