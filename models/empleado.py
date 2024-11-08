from models.persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, direccion, telefono, email, fecha_inicio, salario):
        super().__init__(nombre, direccion, telefono, email)
        self.fecha_inicio = fecha_inicio
        self.salario = salario

    def presentarse(self):
        return f"Hola, soy {self.nombre}, trabajo desde {self.fecha_inicio} y mi salario es {self.salario}."

