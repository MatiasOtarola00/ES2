class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio

    def detalle_proyecto(self):
        return f"Proyecto: {self.nombre}, Iniciado en: {self.fecha_inicio}. Descripción: {self.descripcion}"
