from controllers.usuario_controller import agregar_usuario
from views.menu_view import mostrar_menu
from controllers.autentificacion_controller import hay_usuarios, autenticar
from models.db import crear_tablas

crear_tablas()

usuario = None

if __name__ == "__main__":
    while usuario is None:
        if hay_usuarios():
            print("Inicio de sesión")
            nombre = input("Ingrese nombre: ")
            passwd = input("Ingrese contraseña: ")
            usuario = autenticar(nombre, passwd)
            if usuario is not None:
                print(f"Bienvenido {usuario[1]}")
                mostrar_menu()
            else:
                print("Usuario o contraseña incorrecta. Intenta nuevamente.")
        else:
            print("No hay usuarios registrados. Por favor, registre un nuevo usuario.")
            agregar_usuario()
