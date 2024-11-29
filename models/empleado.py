from models.persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, departamento_id=None):
        super().__init__(nombre, edad)
        self._departamento_id = departamento_id

    def get_departamento_id(self):
        return self._departamento_id

    def set_departamento_id(self,departamento_id):
        self._departamento_id = departamento_id

    def __str__(self):
        return f"Empleado: {self._nombre}, Edad: {self._edad}, Departamento ID: {self._departamento_id if self._departamento_id else 'No asignado'}"
