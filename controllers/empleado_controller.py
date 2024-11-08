import mysql.connector
from models.db import conectar

def crear_empleado(nombre, direccion, telefono, email, fecha_inicio, salario):
    conn = conectar()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO empleados (nombre, direccion, telefono, email, fecha_inicio, salario)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (nombre, direccion, telefono, email, fecha_inicio, salario))
        conn.commit()
        cursor.close()
        conn.close()
        print("Empleado creado exitosamente.")
    except:
        print("f,Error al crear empleado: {e}")
        
def obtener_empleados():
    conn = conectar()
    if conn is None:
        return []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    cursor.close()
    conn.close()
    return empleados

def actualizar_empleado(empleado_id, nuevo_nombre, nueva_direccion, nuevo_telefono, nuevo_email, nueva_fecha_inicio, nuevo_salario):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE empleados SET nombre = %s, direccion = %s, telefono = %s, email = %s, fecha_inicio = %s, salario = %s
        WHERE id = %s
    """, (nuevo_nombre, nueva_direccion, nuevo_telefono, nuevo_email, nueva_fecha_inicio, nuevo_salario, empleado_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Empleado actualizado exitosamente.")

def eliminar_empleado(empleado_id):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("DELETE FROM empleados WHERE id = %s", (empleado_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Empleado eliminado exitosamente.")
