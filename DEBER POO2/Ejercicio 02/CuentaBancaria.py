from abc import ABC, abstractmethod

#ABSTRACCION
class CuentaBancaria(ABC):
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        #ENCAPSULAMIENTO
        self.__saldo = saldo_inicial

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, cantidad):
        self.__saldo = cantidad

    @abstractmethod
    def retirar(self, cantidad):
        pass

#HERENCIA
class CuentaAhorros(CuentaBancaria):
    #POLIMORFISMO
    def retirar(self, cantidad):
        saldo_anterior = self.get_saldo()
        
        if cantidad <= saldo_anterior:
            nuevo_saldo = saldo_anterior - cantidad
            self.set_saldo(nuevo_saldo)
            print("Retiro exitoso en ahorros")
            print("Saldo anterior:", saldo_anterior)
            print("Monto retirado:", cantidad)
            print("Saldo restante:", nuevo_saldo)
            print("-" * 30)
        else:
            print("Error: Fondos insuficientes")
            print("Saldo disponible:", saldo_anterior)
            print("Monto que intento retirar:", cantidad)
            print("-" * 30)

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, sobregiro):
        super().__init__(titular, saldo_inicial)
        self.sobregiro = sobregiro

    #POLIMORFISMO
    def retirar(self, cantidad):
        saldo_anterior = self.get_saldo()
        limite_total = saldo_anterior + self.sobregiro
        
        if cantidad <= limite_total:
            nuevo_saldo = saldo_anterior - cantidad
            self.set_saldo(nuevo_saldo)
            print("Retiro exitoso con sobregiro")
            print("Saldo anterior:", saldo_anterior)
            print("Monto retirado:", cantidad)
            print("Saldo restante:", nuevo_saldo)
            print("-" * 30)
        else:
            print("Error: Limite de sobregiro superado")
            print("Saldo disponible:", saldo_anterior)
            print("Limite de sobregiro:", self.sobregiro)
            print("Monto que intento retirar:", cantidad)
            print("-" * 30)


# --- USO FUERA DE LA CLASE ---
if __name__ == "__main__":
    cuenta = CuentaCorriente("Sofia", 3000, 200)
    # Ejecutamos el retiro
    cuenta.retirar(250)