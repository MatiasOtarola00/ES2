class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self,nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad
    
    def set_edad(self,edad):
        self._edad = edad

        
    def __str__(self):
        return f"Persona: {self._nombre}, Edad: {self._edad}"
