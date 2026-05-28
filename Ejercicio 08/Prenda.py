
class Prenda:
    def __init__(self, talla, material, color):
        self.talla = talla
        self.material = material
        self.color = color

    def mostrar_etiqueta(self):
        return f"Ropa de {self.material}/Talla: {self.talla}."

class Camisa(Prenda):
    def abrochar_botones(self):
        return "Abrochando los botones de la camisa de vestir."


# FUERA DE LA CLASE

mi_camisa = Camisa("M", "Algodón", "Blanco")
print(f"Talla camisa: {mi_camisa.talla}")
print(f"Color: {mi_camisa.color}")
print(f"Material camisa: {mi_camisa.material}")
print(mi_camisa.mostrar_etiqueta())
print(mi_camisa.abrochar_botones())
