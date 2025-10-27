from datetime import datetime


class Nota:
    """
    Representa una nota con nombre , contenido y fecha de creaci ón.
    """

    def __init__(self, nombre, contenido):
        """Genera una nueva nota a partir del nombre y el cuerpo recibido."""
        
        self.nombre = nombre.strip()
        self.contenido = contenido.strip()
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def __str__(self):
        """Devuelve la representación lista para persistirla en un archivo."""
        return f"Fecha: {self.fecha}\n\n{self.contenido}"
