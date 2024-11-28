class Departamento:
    def __init__(self, nombre, gerente_id=None):
        self._nombre = nombre
        self._gerente_id = gerente_id

    def get_nombre(self):
        return self._nombre

    def get_gerente_id(self):
        return self._gerente_id

    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre del departamento debe ser una cadena no vacía.")

    def set_gerente_id(self, nuevo_gerente_id):
        if isinstance(nuevo_gerente_id, int) or nuevo_gerente_id is None:
            self._gerente_id = nuevo_gerente_id
        else:
            raise ValueError("El ID del gerente debe ser un entero o None.")

    def __str__(self):
        return f"Departamento: {self._nombre}, Gerente ID: {self._gerente_id if self._gerente_id else 'No asignado'}"

    def actualizar_informacion(self, nuevo_nombre=None, nuevo_gerente_id=None):
        if nuevo_nombre:
            self.set_nombre(nuevo_nombre)
        if nuevo_gerente_id is not None:
            self.set_gerente_id(nuevo_gerente_id)
