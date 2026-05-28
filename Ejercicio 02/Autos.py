
class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def mostrar_info(self):
        return f"Vehículo: {self.marca} {self.modelo}"

class CocheElectrico(Vehiculo):
    def cargar_bateria(self):
        return f"El {self.marca} se está cargando..."

# FUERA DE LA CLASE
mi_coche = CocheElectrico("Tesla", "X", 45000)

print(mi_coche.mostrar_info())
print(mi_coche.cargar_bateria())
print(f"Modelo: {mi_coche.modelo}")
print(f"Precio de venta: ${mi_coche.precio}")