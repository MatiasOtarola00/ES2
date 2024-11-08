class Persona:
    def __init__(self, nombre, direccion, telefono, email):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def presentarse(self):
        return f"Hola, soy {self.nombre} y mi contacto es: {self.email}."
