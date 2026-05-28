
class Personaje:
    def __init__(self, nombre_videojuego, nombre_personajes, nivel):
        self.nombre_videojuego = nombre_videojuego
        self.nombre_personaje = nombre_personajes
        self.nivel = nivel

    def subir_nivel(self):
        self.nivel += 1
        return f"¡Usted subió al nivel {self.nivel}!"

class Guerreros(Personaje):
    def atacar(self):
        return f"Salvan al mundo del videojuego!"


# FUERA DE LA CLASE
mi_heroe = Guerreros("Super Mario Bros", "Mario, Luigi, Princesa Peach", 7)
print(mi_heroe.atacar())
print(mi_heroe.subir_nivel())
print(f"Nombre del videojuego: {mi_heroe.nombre_videojuego}")  
print(f"Nombre de los personajes: {mi_heroe.nombre_personaje}") 
print(f"Nivel alcanzado: {mi_heroe.nivel}")