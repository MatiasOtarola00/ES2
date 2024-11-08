class Departamento:
    def __init__(self, nombre, gerente_id=None):
        self.nombre = nombre
        self.gerente_id = gerente_id

    def asignar_gerente(self, empleado_id):
        self.gerente_id = empleado_id
        
    def detalles(self):
        return f"Departamento: {self.nombre}, Gerente ID: {self.gerente_id if self.gerente_id else 'Sin asignar'}"