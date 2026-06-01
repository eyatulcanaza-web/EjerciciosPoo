
from abc import ABC, abstractmethod

# 1. ABSTRACCION
class Habitacion(ABC):
    def __init__(self, numero, precio_noche):
        self.numero = numero
        # 2. ENCAPSULAMIENTO
        self.__precio_noche = precio_noche

    def get_precio(self):
        return self.__precio_noche

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio_noche = nuevo_precio

    @abstractmethod
    def calcular_costo_estancia(self, noches):
        pass

# 3. HERENCIA
class HabitacionEstandar(Habitacion):
    # 4. POLIMORFISMO
    def calcular_costo_estancia(self, noches):
        precio_base = self.get_precio()
        total = precio_base * noches
        
        print("Calculando costo de Habitacion Estandar")
        print("Numero de habitacion:", self.numero)
        print("Precio por noche:", precio_base)
        print("Noches reservadas:", noches)
        print("Total a pagar:", total)
        print("-" * 30)
        return total

class HabitacionSuite(Habitacion):
    def __init__(self, numero, precio_noche, servicio_cuarto):
        super().__init__(numero, precio_noche)
        self.servicio_cuarto = servicio_cuarto

    # 4. POLIMORFISMO
    def calcular_costo_estancia(self, noches):
        precio_base = self.get_precio()
        # La suite incluye un cargo unico por servicio a la habitacion
        total = (precio_base * noches) + self.servicio_cuarto
        
        print("Calculando costo de la Suite")
        print("Numero de habitacion:", self.numero)
        print("Precio por noche:", precio_base)
        print("Cargo de servicio incluido:", self.servicio_cuarto)
        print("Noches reservadas:", noches)
        print("Total a pagar:", total)
        print("-" * 30)
        return total

# --- USO FUERA DE LA CLASE ---
if __name__ == "__main__":
    habitacion_vip = HabitacionSuite(401, 250, 100)
    habitacion_vip.calcular_costo_estancia(3)