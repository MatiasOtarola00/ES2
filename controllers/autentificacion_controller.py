import bcrypt
import mysql.connector
from models.db import conectar

def autenticar(nombre, passwd):
    conn = conectar()
    if conn is None:
        return None
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, nombre, password FROM usuarios WHERE nombre = %s", (nombre,))
        usuario = cursor.fetchone()
        if usuario:
            stored_password = usuario[2]
            
            if bcrypt.checkpw(passwd.encode('utf-8'), stored_password.encode('utf-8')):
                return usuario 
            else:
                print("Contraseña incorrecta.")
                return None
        else:
            print("Usuario no encontrado.")
            return None
    except mysql.connector.Error as err:
        print(f"Error al autenticar el usuario: {err}")
        return None
    finally:
        cursor.close()
        conn.close()

def hay_usuarios():
    conn = conectar()
    if conn is None:
        return False
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT COUNT(*) FROM usuarios")
        count = cursor.fetchone()[0]
        return count > 0
    except mysql.connector.Error as err:
        print(f"Error al verificar la existencia de usuarios: {err}")
        return False
    finally:
        cursor.close()
        conn.close()

