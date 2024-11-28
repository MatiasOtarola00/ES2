import bcrypt
import mysql.connector
from models.db import conectar

# Controlador para gestionar usuarios

def agregar_usuario():
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()

    nombre = input("Ingrese nombre del usuario: ")
    passwd = input("Ingrese contraseña: ")

    # Hash de la contraseña usando bcrypt
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(passwd.encode('utf-8'), salt)

    try:
        cursor.execute("INSERT INTO usuarios (nombre, password) VALUES (%s, %s)", (nombre, hashed_password))
        conn.commit()
        print("Usuario agregado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al agregar el usuario: {err}")
    finally:
        cursor.close()
        conn.close()


def listar_usuarios():
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, nombre FROM usuarios")
        usuarios = cursor.fetchall()
        if usuarios:
            print("\n--- Lista de Usuarios ---")
            for usuario in usuarios:
                print(f"ID: {usuario[0]}, Nombre: {usuario[1]}")
        else:
            print("No hay usuarios registrados.")
    except mysql.connector.Error as err:
        print(f"Error al listar los usuarios: {err}")
    finally:
        cursor.close()
        conn.close()


def eliminar_usuario():
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()

    usuario_id = input("Ingrese el ID del usuario a eliminar: ")
    try:
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
        if cursor.rowcount > 0:
            conn.commit()
            print("Usuario eliminado exitosamente.")
        else:
            print("Usuario no encontrado.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar el usuario: {err}")
    finally:
        cursor.close()
        conn.close()


def actualizar_usuario():
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()

    usuario_id = input("Ingrese el ID del usuario a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
    nueva_passwd = input("Ingrese la nueva contraseña del usuario: ")

    # Hash de la nueva contraseña usando bcrypt
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(nueva_passwd.encode('utf-8'), salt)

    try:
        cursor.execute("UPDATE usuarios SET nombre = %s, password = %s WHERE id = %s", (nuevo_nombre, hashed_password, usuario_id))
        if cursor.rowcount > 0:
            conn.commit()
            print("Usuario actualizado exitosamente.")
        else:
            print("Usuario no encontrado.")
    except mysql.connector.Error as err:
        print(f"Error al actualizar el usuario: {err}")
    finally:
        cursor.close()
        conn.close()

