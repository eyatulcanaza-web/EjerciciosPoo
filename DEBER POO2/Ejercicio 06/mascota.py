
from abc import ABC, abstractmethod

# 1. ABSTRACCION
class Mascota(ABC):
    def __init__(self, nombre, peso):
        self.nombre = nombre
        # 2. ENCAPSULAMIENTO
        self.__peso = peso

    def get_peso(self):
        return self.__peso

    def set_peso(self, nuevo_peso):
        if nuevo_peso > 0:
            self.__peso = nuevo_peso

    @abstractmethod
    def calcular_dosis_medicina(self):
        pass

# 3. HERENCIA
class Perro(Mascota):
    # 4. POLIMORFISMO
    def calcular_dosis_medicina(self):
        peso_actual = self.get_peso()
        # Los perros necesitan 0.5ml por cada kg de peso
        dosis = peso_actual * 0.5
        
        print("Dosis Veterinaria para Perro")
        print("Nombre de la mascota:", self.nombre)
        print("Peso registrado:", peso_actual, "kg")
        print("Dosis calculada:", dosis, "ml")
        print("-" * 30)
        return dosis

class Gato(Mascota):
    # 4. POLIMORFISMO
    def calcular_dosis_medicina(self):
        peso_actual = self.get_peso()
        # Los gatos al ser mas sensibles necesitan solo 0.2ml por cada kg de peso
        dosis = peso_actual * 0.2
        
        print("Dosis Veterinaria para Gato")
        print("Nombre de la mascota:", self.nombre)
        print("Peso registrado:", peso_actual, "kg")
        print("Dosis calculada:", dosis, "ml")
        print("-" * 30)
        return dosis

# --- USO FUERA DE LA CLASE ---
if __name__ == "__main__":
    paciente = Gato("Zeus", 5)
    paciente.calcular_dosis_medicina()
    paciente = Gato("Benja", 8)
    paciente.calcular_dosis_medicina()