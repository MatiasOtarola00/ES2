class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio):
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_inicio = fecha_inicio

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self,nombre):
         self._nombre = nombre

    def get_descripcion(self):
        return self._descripcion

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion
        
    def get_fecha_inicio(self):
        return self._fecha_inicio
    
    def set_fecha_inicio(self,fecha_inicio):
        self._fecha_inicio = fecha_inicio

    def __str__(self):
        return f"Proyecto: {self._nombre}, Descripción: {self._descripcion}, Fecha de Inicio: {self._fecha_inicio}"
