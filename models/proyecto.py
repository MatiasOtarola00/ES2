class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio):
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_inicio = fecha_inicio

    def get_nombre(self):
        return self._nombre

    def get_descripcion(self):
        return self._descripcion

    def get_fecha_inicio(self):
        return self._fecha_inicio

    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre del proyecto debe ser una cadena no vacía.")

    def set_descripcion(self, nueva_descripcion):
        if isinstance(nueva_descripcion, str):
            self._descripcion = nueva_descripcion
        else:
            raise ValueError("La descripción del proyecto debe ser una cadena.")

    def set_fecha_inicio(self, nueva_fecha_inicio):
        self._fecha_inicio = nueva_fecha_inicio

    def __str__(self):
        return f"Proyecto: {self._nombre}, Descripción: {self._descripcion}, Fecha de Inicio: {self._fecha_inicio}"

    def actualizar_informacion(self, nuevo_nombre=None, nueva_descripcion=None, nueva_fecha_inicio=None):
        if nuevo_nombre:
            self.set_nombre(nuevo_nombre)
        if nueva_descripcion:
            self.set_descripcion(nueva_descripcion)
        if nueva_fecha_inicio:
            self.set_fecha_inicio(nueva_fecha_inicio)
