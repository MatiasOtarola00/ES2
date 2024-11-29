class Usuario:
    def __init__(self, nombre, hashed_password, perfil):
        self._nombre = nombre
        self._hashed_password = hashed_password
        self._perfil = perfil
        
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
       
    def get_hashed_password(self):
        return self._hashed_password

    def set_hashed_password(self,hashed_password):
        self._hashed_password=hashed_password

    def get_perfil(self):
        return self._perfil
    
    def set_perfil(self,perfil):
        self._perfil=perfil
        
    def __str__(self):
        return f"Usuario: {self._nombre}"
