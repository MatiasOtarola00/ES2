# models/db.py
import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        # Intentamos conectar a la base de datos
        conn = mysql.connector.connect(
            host='localhost',  # Nombre del host (localhost para XAMPP)
            database='sistema_gestion_empleados',  # Nombre de la base de datos
            user='root',  # Usuario de MySQL
            password=''  # Contraseña del usuario de MySQL
        )

        return conn
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def crear_tablas():
    conn = conectar()
    if conn is None:
        print("Error de conexión. No se pueden crear las tablas.")
        return

    cursor = conn.cursor()

    # Crear tabla de Empleados
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empleados (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            direccion VARCHAR(255),
            telefono VARCHAR(20),
            email VARCHAR(255),
            fecha_inicio DATE,
            salario DECIMAL(10, 2)
        )
    ''')

    # Crear tabla de Departamentos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS departamentos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            gerente_id INT,
            FOREIGN KEY (gerente_id) REFERENCES empleados(id) ON DELETE SET NULL
        )
    ''')

    # Crear tabla de Proyectos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS proyectos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            descripcion TEXT,
            fecha_inicio DATE
        )
    ''')

    # Crear tabla de Asignaciones de Empleados a Proyectos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS asignacion_empleados_proyectos (
            empleado_id INT,
            proyecto_id INT,
            PRIMARY KEY (empleado_id, proyecto_id),
            FOREIGN KEY (empleado_id) REFERENCES empleados(id) ON DELETE CASCADE,
            FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    cursor.close()
    conn.close()
    print("Tablas creadas exitosamente o ya existen en la base de datos.")

# Llamar a la función para probar la conexión y creación de tablas
if __name__ == "__main__":
    crear_tablas()
