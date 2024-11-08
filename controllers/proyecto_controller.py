import mysql.connector
from models.db import conectar

def crear_proyecto(nombre, descripcion, fecha_inicio):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO proyectos (nombre, descripcion, fecha_inicio)
        VALUES (%s, %s, %s)
    """, (nombre, descripcion, fecha_inicio))
    conn.commit()
    cursor.close()
    conn.close()
    print("Proyecto creado exitosamente.")

def obtener_proyectos():
    conn = conectar()
    if conn is None:
        return []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM proyectos")
    proyectos = cursor.fetchall()
    cursor.close()
    conn.close()
    return proyectos

def actualizar_proyecto(proyecto_id, nuevo_nombre, nueva_descripcion, nueva_fecha_inicio):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE proyectos SET nombre = %s, descripcion = %s, fecha_inicio = %s
        WHERE id = %s
    """, (nuevo_nombre, nueva_descripcion, nueva_fecha_inicio, proyecto_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Proyecto actualizado exitosamente.")

def eliminar_proyecto(proyecto_id):
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("DELETE FROM proyectos WHERE id = %s", (proyecto_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Proyecto eliminado exitosamente.")
