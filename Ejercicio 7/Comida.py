
class Comida:
    def __init__(self, nombre_plato, precio, calorias):
        self.nombre_plato = nombre_plato
        self.precio = precio
        self.calorias = calorias

    def servir(self):
        return f"Sirven el plato en la mesa indicada"

class Pizza(Comida):
    def cortar_porciones(self):
        return f"Cortan la pizza de {self.nombre_plato} en 8 porciones."

# FUERA DE LA CLASE
mi_cena = Pizza("Pepperoni", 12.99, 800)
print(mi_cena.cortar_porciones())
print(mi_cena.servir())
print(f"Precio Pizza: ${mi_cena.precio}")
print(f"Calorías estimadas: {mi_cena.calorias} kcal")