from models.persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, departamento_id=None):
        super().__init__(nombre, edad)
        self._departamento_id = departamento_id

    def get_departamento_id(self):
        return self._departamento_id

    def set_departamento_id(self, nuevo_departamento_id):
        if isinstance(nuevo_departamento_id, int) or nuevo_departamento_id is None:
            self._departamento_id = nuevo_departamento_id
        else:
            raise ValueError("El ID del departamento debe ser un entero o None.")

    def __str__(self):
        return f"Empleado: {self._nombre}, Edad: {self._edad}, Departamento ID: {self._departamento_id if self._departamento_id else 'No asignado'}"

    def actualizar_informacion(self, nuevo_nombre=None, nueva_edad=None, nuevo_departamento_id=None):
        if nuevo_nombre:
            self.set_nombre(nuevo_nombre)
        if nueva_edad is not None:
            self.set_edad(nueva_edad)
        if nuevo_departamento_id is not None:
            self.set_departamento_id(nuevo_departamento_id)
