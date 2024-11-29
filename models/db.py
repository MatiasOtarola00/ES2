import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        # Conectar a la base de datos
        conn = mysql.connector.connect(
            host='localhost',  # Nombre del host, en este caso localhost
            database='sistema_gestion_empleados',  # Nombre de la base de datos
            user='Matias',  # Usuario para conectar a la base de datos
            password='123'  # Contraseña del usuario de la base de datos
        )
        if conn.is_connected():
            print("Conexión exitosa a la base de datos.")
        return conn
    except Error as e:
        print(f"Error al conectar a MariaDB: {e}")
        return None
        
def crear_tablas():
    conn = conectar()
    if conn is None:
        return

    cursor = conn.cursor()


    cursor.execute('''
            CREATE TABLE IF NOT EXISTS empleados (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                edad INT NOT NULL,
                departamento_id INT,
                FOREIGN KEY (departamento_id) REFERENCES departamentos(id) ON DELETE SET NULL
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS departamentos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                gerente_id INT,
                FOREIGN KEY (gerente_id) REFERENCES empleados(id) ON DELETE SET NULL
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS proyectos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                descripcion TEXT,
                fecha_inicio DATE
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                rol VARCHAR(50) NOT NULL
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS empleados_proyectos (
                empleado_id INT,
                proyecto_id INT,
                FOREIGN KEY (empleado_id) REFERENCES empleados(id) ON DELETE CASCADE,
                FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) ON DELETE CASCADE,
                PRIMARY KEY (empleado_id, proyecto_id)
            )
        ''')
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS registros_consultas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre_indicador VARCHAR(255) NOT NULL,
                fecha_valor DATE NOT NULL,
                fecha_consulta DATETIME NOT NULL,
                usuario_id INT,
                fuente VARCHAR(255) NOT NULL,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE SET NULL
            )
        ''')


    conn.commit()
    print("Tablas creadas exitosamente.")
    cursor.close()
    conn.close()
    