
class Persona:
    def __init__(self, nombre, id_Profesora, genero):
        self.nombre = nombre
        self.id_Profesora = id_Profesora
        self.genero = genero

    def presentarse(self):
        return f"Presentacion: Hola, mi nombre es {self.nombre}."

class Profesor(Persona):
    def calificar(self):
        return f"La profesora esta calificando los examenes."


# FUERA DE LA CLASE

mi_profe = Profesor("Mary Davila", "EMP-404", "Femenino")
print(mi_profe.presentarse())
print(mi_profe.calificar())
print(f"ID de la Profesora: {mi_profe.id_Profesora}")
print(f"Género: {mi_profe.genero}")