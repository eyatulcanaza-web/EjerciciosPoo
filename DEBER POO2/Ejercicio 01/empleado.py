
from abc import ABC, abstractmethod

#ABSTRACCION: Clase base que sirve de plantilla
class Empleado(ABC):
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        #ENCAPSULAMIENTO: Atributo privado interno
        self.__sueldo_base = 0
        self.set_sueldo(sueldo_base)

    # Métodos para acceder desde fuera de la clase
    def get_sueldo(self):
        return self.__sueldo_base

    def set_sueldo(self, valor):
        if valor >= 0:
            self.__sueldo_base = valor
        else:
            print("Error: El sueldo no puede ser negativo")

    @abstractmethod
    def calcular_salario(self):
        pass

#HERENCIA: Subclase que hereda de Empleado
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, sueldo_base, bono):
        super().__init__(nombre, sueldo_base)
        self.bono = bono

    #POLIMORFISMO: Implementacion especifica de este empleado
    def calcular_salario(self):
        return self.get_sueldo() + self.bono

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, tarifa_hora, horas_trabajadas):
        super().__init__(nombre, 0)
        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = horas_trabajadas

    #POLIMORFISMO: Calculo distinto para el mismo metodo
    def calcular_salario(self):
        return self.tarifa_hora * self.horas_trabajadas


#FUERA DE LA CLASE
if __name__ == "__main__":
    emp1 = EmpleadoTiempoCompleto("Carlos", 2000, 500)
    emp2 = EmpleadoPorHoras("Ana", 20, 40)
    print("Salario Carlos:", emp1.calcular_salario())
    print("Salario Ana:", emp2.calcular_salario())
    emp1.set_sueldo(2200) 
    emp2.set_sueldo(200)
    print("Nuevo salario base de Carlos:", emp1.get_sueldo())
    print("Nuevo salario base de Ana:", emp2.get_sueldo())