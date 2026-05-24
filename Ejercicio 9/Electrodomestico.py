
class Electrodomestico:
    def __init__(self, voltaje, marca, eficiencia):
        self.voltaje = voltaje
        self.marca = marca
        self.eficiencia = eficiencia

    def conectar(self):
        return f"El aparato {self.marca} está conectado correctamente."

class Microondas(Electrodomestico):
    def calentar_comida(self):
        return "El microondas está calentando..."

# FUERA DE LA CLASE

mi_micro = Microondas(110, "LG", "Clase A")

print(f"Marca del microondas: {mi_micro.marca}")
print(f"Voltaje requerido: {mi_micro.voltaje}V")
print(f"Eficiencia energética: {mi_micro.eficiencia}")
print(mi_micro.conectar())
print(mi_micro.calentar_comida())
