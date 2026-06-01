from abc import ABC, abstractmethod

# 1. ABSTRACCION
class Paquete(ABC):
    def __init__(self, codigo, peso_kg):
        self.codigo = codigo
        # 2. ENCAPSULAMIENTO
        self.__peso_kg = peso_kg

    def get_peso(self):
        return self.__peso_kg

    def set_peso(self, nuevo_peso):
        if nuevo_peso > 0:
            self.__peso_kg = nuevo_peso

    @abstractmethod
    def calcular_costo_envio(self):
        pass

# 3. HERENCIA
class EnvioEstandar(Paquete):
    # 4. POLIMORFISMO
    def calcular_costo_envio(self):
        peso_actual = self.get_peso()
        # Tarifa fija de 3.5 por kilo
        total = peso_actual * 3.5
        
        print("Calculando Costo de Envio Estandar")
        print("Codigo de paquete:", self.codigo)
        print("Peso registrado:", peso_actual, "kg")
        print("Costo total de envio:", total)
        print("-" * 30)
        return total

class EnvioExpress(Paquete):
    def __init__(self, codigo, peso_kg, cargo_urgente):
        super().__init__(codigo, peso_kg)
        self.cargo_urgente = cargo_urgente

    # 4. POLIMORFISMO
    def calcular_costo_envio(self):
        peso_actual = self.get_peso()
        # Tarifa express de 5.0 por kilo mas un cargo fijo por urgencia
        total = (peso_actual * 5.0) + self.cargo_urgente
        
        print("Calculando Costo de Envio Express")
        print("Codigo de paquete:", self.codigo)
        print("Peso registrado:", peso_actual, "kg")
        print("Cargo por urgencia aplicado:", self.cargo_urgente)
        print("Costo total de envio:", total)
        print("-" * 30)
        return total

# --- USO FUERA DE LA CLASE ---
if __name__ == "__main__":
    entrega = EnvioExpress("EXP-9921", 10, 15)
    # Ejecutamos el metodo desde fuera de la clase
    entrega.calcular_costo_envio()