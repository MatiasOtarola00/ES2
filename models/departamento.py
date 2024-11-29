class Departamento:
    def __init__(self, nombre, gerente_id=None):
        self._nombre = nombre
        self._gerente_id = gerente_id

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self,nombre):
        self._nombre = nombre
        
    def get_gerente_id(self):
        return self._gerente_id

    def set_gerente_id(self,gerente_id):
        self._gerente_id = gerente_id

    def __str__(self):
        return f"Departamento: {self._nombre}, Gerente ID: {self._gerente_id if self._gerente_id else 'No asignado'}"