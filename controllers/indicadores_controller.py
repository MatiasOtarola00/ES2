import requests
import json

def obtener_indicadores():
    url = "https://mindicador.cl/api"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la respuesta tiene un estado HTTP de error
        datos = response.json()
        mostrar_indicadores(datos)
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los indicadores: {e}")

def mostrar_indicadores(datos):
    print("\n--- Indicadores Económicos ---")
    try:
        indicadores = {
            "Unidad de Fomento (UF)": datos["uf"],
            "Índice de valor Promedio (IVP)": datos["ivp"],
            "Índice de Precio al Consumidor (IPC)": datos["ipc"],
            "Unidad Tributaria Mensual (UTM)": datos["utm"],
            "Dólar Observado": datos["dolar"],
            "Euro": datos["euro"]
        }
        for nombre, valor in indicadores.items():
            print(f"{nombre}: {valor['valor']} {valor['unidad']} (Fecha: {valor['fecha']})")
    except KeyError as e:
        print(f"Error al procesar los indicadores: clave no encontrada {e}")
