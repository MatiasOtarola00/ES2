def validar_nombre(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isalpha(): 
            return valor
        else:
            print("Entrada inválida. Por favor, ingrese solo letras.")

def validar_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def validar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def validar_telefono(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit(): 
            return valor
        else:
            print("Entrada inválida. Por favor, ingrese solo números.")