from views.vista_usuario import main_usuario, add_user
from views.menu_view import mostrar_menu
from controllers.autentificacion_controller import hay_usuarios, autenticar

usuario = None

if __name__ == "__main__":
    if hay_usuarios():
        print("Inicio de sesión")
        nombre = input("Ingrese nombre: ")
        passwd = input("Ingrese contraseña: ")
        usuario = autenticar(nombre, passwd)
        if usuario is not None:
            print(f"Bienvenido {usuario[1]}")
            mostrar_menu()  # Mostrar el menú completo desde el archivo de vista
        else:
            print("Usuario o contraseña incorrecta.")
    else:
        print("No hay usuarios registrados. Por favor, registre un nuevo usuario.")
        add_user()

