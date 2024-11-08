import mysql.connector
from models.db import conectar

def crear_departamento(nombre, gerente_id=None):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("INSERT INTO departamentos (nombre, gerente_id) VALUES (%s, %s)", (nombre, gerente_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Departamento creado exitosamente.")

def obtener_departamentos():
    conn = conectar()
    if conn is None:
        return []
    cursor = conn.cursor()
    cursor.execute("SELECT d.id, d.nombre, e.nombre AS gerente_nombre FROM departamentos d LEFT JOIN empleados e ON d.gerente_id = e.id")
    departamentos = cursor.fetchall()
    cursor.close()
    conn.close()
    return departamentos

def actualizar_departamento(departamento_id, nuevo_nombre, nuevo_gerente_id):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("UPDATE departamentos SET nombre = %s, gerente_id = %s WHERE id = %s", (nuevo_nombre, nuevo_gerente_id, departamento_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Departamento actualizado exitosamente.")

def eliminar_departamento(departamento_id):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("DELETE FROM departamentos WHERE id = %s", (departamento_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Departamento eliminado exitosamente.")
