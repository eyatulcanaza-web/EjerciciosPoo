class Dispositivo:
    def __init__(self, marca, almacenamiento, color):
        self.marca = marca
        self.almacenamiento = almacenamiento
        self.color = color
    

    def encender(self):
        return f"El dispositivo {self.marca} se ha encendido."

class Smartphone(Dispositivo):
    def tomar_foto(self):
        return f"Tomando foto con la cámara trasera del dispositivo."


# FUERA DE LA CLASE

mi_celular = Smartphone("Apple", "128GB", "Azul Marino")
print(f"Marca: {mi_celular.marca}")
print(f"Almacenamiento: {mi_celular.almacenamiento}")
print(f"Color del dispositivo: {mi_celular.color}")
print(mi_celular.encender())
print(mi_celular.tomar_foto())