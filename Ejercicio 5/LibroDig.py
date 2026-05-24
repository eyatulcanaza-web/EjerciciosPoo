class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def abrir_libro(self):
        return f"Abriendo el libro"

class LibroDigital(Libro):
    def descargar(self):
        return f"Descargando del libro en formato PDF..."


# FUERA DE LA CLASE
mi_libro = LibroDigital("Cien años de soledad", "Gabriel García Márquez", 496)
print(f"Titulo del libro: {mi_libro.titulo}")
print(f"Autor: {mi_libro.autor}")
print(f"Total de páginas: {mi_libro.paginas}")

print(mi_libro.abrir_libro())
print(mi_libro.descargar())
