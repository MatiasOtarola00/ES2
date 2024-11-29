import requests
import mysql.connector
from mysql.connector import Error
from datetime import datetime

def conectar():
    try:
        # Conectar a la base de datos
        conn = mysql.connector.connect(
            host='localhost',  # Nombre del host, en este caso localhost
            database='sistema_gestion_empleados',  # Nombre de la base de datos
            user='admin',  # Usuario para conectar a la base de datos
            password='secure_password'  # Contraseña del usuario de la base de datos
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error al conectar a MariaDB: {e}")
        return None

def mostrar_indicadores():
    url = "https://mindicador.cl/api"
    try:
        response = requests.get(url)
        response.raise_for_status()
        datos = response.json()
        procesar_indicadores(datos)
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los indicadores: {e}")

def procesar_indicadores(datos):
    print("\n--- Indicadores Económicos ---")
    indicadores = {
        "Unidad de Fomento (UF)": datos.get("uf"),
        "Índice de valor Promedio (IVP)": datos.get("ivp"),
        "Índice de Precio al Consumidor (IPC)": datos.get("ipc"),
        "Unidad Tributaria Mensual (UTM)": datos.get("utm"),
        "Dólar Observado": datos.get("dolar"),
        "Euro": datos.get("euro")
    }
    for nombre, valor in indicadores.items():
        if valor:
            fecha_valor = valor.get("fecha")
            valor_indicador = valor.get("valor")
            if fecha_valor and valor_indicador:
                print(f"{nombre}: {valor_indicador} {valor.get('unidad', '')} (Fecha: {fecha_valor})")
                registrar_consulta(nombre, fecha_valor, valor_indicador)
            else:
                print(f"{nombre}: Datos incompletos, no se puede registrar la consulta.")
        else:
            print(f"{nombre}: No disponible")

def registrar_consulta(nombre_indicador, fecha_valor, valor):
    registrar = input(f"¿Desea registrar la consulta del indicador '{nombre_indicador}' del {fecha_valor}? (s/n): ")
    if registrar.lower() == 's':
        conn = conectar()
        if conn is None:
            print("No se pudo conectar a la base de datos para registrar la consulta.")
            return

        cursor = conn.cursor()
        try:
            fecha_consulta = datetime.now()
            usuario_id = obtener_usuario_id()
            fuente = "https://mindicador.cl/api"

            cursor.execute('''
                INSERT INTO registros_consultas (nombre_indicador, fecha_valor, fecha_consulta, usuario_id, fuente)
                VALUES (%s, %s, %s, %s, %s)
            ''', (nombre_indicador, fecha_valor, fecha_consulta, usuario_id, fuente))

            conn.commit()
            print("Consulta registrada exitosamente.")
        except Error as e:
            print(f"Error al registrar la consulta: {e}")
        finally:
            cursor.close()
            conn.close()

def obtener_usuario_id():
    return 1

def main_api():
    while True:
        print("\n--- Menú de Indicadores Económicos ---")
        print("1. Consultar Indicadores Económicos")
        print("0. Volver al Menú Principal")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            mostrar_indicadores()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")
