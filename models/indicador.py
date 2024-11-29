class Indicador:
    def __init__(self, nombre, valor, unidad, fecha):
        self._nombre = nombre
        self._valor = valor
        self._unidad = unidad
        self._fecha = fecha

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre 
        
    def get_valor(self):
        return self._valor
    
    def set_valor(self,valor):
        self._valor = valor
        
    def get_unidad(self):
        return self._unidad

    def set_unidad(self,unidad):
        self._unidad = unidad
        
    def get_fecha(self):
        return self._fecha

    def set_fecha(self,fecha):
        self._fecha = fecha

    def __str__(self):
        return f"Indicador: {self._nombre}, Valor: {self._valor} {self._unidad}, Fecha: {self._fecha}"

