
from abc import ABC, abstractmethod

#ABSTRACCION
class Vehiculo(ABC):
    def __init__(self, placa):
        #ENCAPSULAMIENTO: Placa privada sin metodo set para que no se altere
        self.__placa = placa

    def get_placa(self):
        return self.__placa

    @abstractmethod
    def calcular_peaje(self):
        pass

#HERENCIA
class Auto(Vehiculo):
    #POLIMORFISMO
    def calcular_peaje(self):
        return 5.0

class Camion(Vehiculo):
    def __init__(self, placa, ejes):
        super().__init__(placa)
        self.ejes = ejes

    #POLIMORFISMO
    def calcular_peaje(self):
        return 4.0 * self.ejes


#USO FUERA DE LA CLASE
if __name__ == "__main__":
    lista_vehiculos = [Auto("ABC-123"), Camion("XYZ-789", 3)]

    for v in lista_vehiculos:
        print("Vehiculo placa:", v.get_placa(), "| Peaje:", v.calcular_peaje())