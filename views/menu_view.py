from controllers.empleado_controller import crear_empleado, obtener_empleados, actualizar_empleado, eliminar_empleado
from controllers.departamento_controller import crear_departamento, obtener_departamentos, actualizar_departamento, eliminar_departamento
from controllers.proyecto_controller import crear_proyecto, obtener_proyectos, actualizar_proyecto, eliminar_proyecto
from controllers.exception_controller import validar_nombre, validar_numero, validar_entero, validar_telefono
from controllers.usuario_controller import agregar_usuario, listar_usuarios, eliminar_usuario
from controllers.indicadores_controller import main_api
from models.db import crear_tablas

def mostrar_menu():
    crear_tablas()

    while True:
        try:
            print("\n--- Menú de Gestión de Empleados, Departamentos y Proyectos ---")
            print("1. Crear Empleado")
            print("2. Mostrar Empleados")
            print("3. Actualizar Empleado")
            print("4. Eliminar Empleado")
            print("5. Crear Departamento")
            print("6. Mostrar Departamentos")
            print("7. Actualizar Departamento")
            print("8. Eliminar Departamento")
            print("9. Crear Proyecto")
            print("10. Mostrar Proyectos")
            print("11. Actualizar Proyecto")
            print("12. Eliminar Proyecto")
            print("13. Getión de Usuarios")
            print("14. Mostrar indicadores")
            print("15. Salir del programa")

            opcion = input("Elige una opción: ")

            if opcion not in [str(i) for i in range(1, 16)]:
                raise ValueError("Opción inválida. Por favor, elige una opción válida entre 1 y 15.")

            # Gestión de Empleados
            if opcion == "1":
                nombre = validar_nombre("Nombre del empleado: ")
                direccion = input("Dirección del empleado: ")
                telefono = validar_telefono("Teléfono del empleado: ")
                email = input("Email del empleado: ")
                fecha_inicio = input("Fecha de inicio (AAAA-MM-DD): ")
                salario = validar_numero("Salario del empleado: ")
                crear_empleado(nombre, direccion, telefono, email, fecha_inicio, salario)
            elif opcion == "2":
                empleados = obtener_empleados()
                if empleados:
                    for empleado in empleados:
                        print(f"{empleado[0]} - {empleado[1]}, {empleado[2]}, Teléfono: {empleado[3]}, Email: {empleado[4]}, Fecha inicio: {empleado[5]}, Salario: {empleado[6]}")
                else:
                    print("No hay empleados registrados.")
            elif opcion == "3":
                empleado_id = validar_entero("ID del empleado a actualizar: ")
                nuevo_nombre = validar_nombre("Nuevo nombre del empleado: ")
                nueva_direccion = input("Nueva dirección del empleado: ")
                nuevo_telefono = validar_telefono("Nuevo teléfono del empleado: ")
                nuevo_email = input("Nuevo email del empleado: ")
                nueva_fecha_inicio = input("Nueva fecha de inicio (AAAA-MM-DD): ")
                nuevo_salario = validar_numero("Nuevo salario del empleado: ")
                actualizar_empleado(empleado_id, nuevo_nombre, nueva_direccion, nuevo_telefono, nuevo_email, nueva_fecha_inicio, nuevo_salario)
            elif opcion == "4":
                empleado_id = validar_entero("ID del empleado a eliminar: ")
                eliminar_empleado(empleado_id)

            # Gestión de Departamentos
            elif opcion == "5":
                nombre = validar_nombre("Nombre del departamento: ")
                gerente_id = input("ID del gerente (opcional, presiona Enter para omitir): ")
                gerente_id = int(gerente_id) if gerente_id else None
                crear_departamento(nombre, gerente_id)
            elif opcion == "6":
                departamentos = obtener_departamentos()
                if departamentos:
                    for departamento in departamentos:
                        gerente_nombre = departamento[2] if departamento[2] else "Sin asignar"
                        print(f"{departamento[0]} - {departamento[1]}, Gerente: {gerente_nombre}")
                else:
                    print("No hay departamentos registrados.")
            elif opcion == "7":
                departamento_id = validar_entero("ID del departamento a actualizar: ")
                nuevo_nombre = validar_nombre("Nuevo nombre del departamento: ")
                nuevo_gerente_id = input("Nuevo ID del gerente (opcional, presiona Enter para omitir): ")
                nuevo_gerente_id = int(nuevo_gerente_id) if nuevo_gerente_id else None
                actualizar_departamento(departamento_id, nuevo_nombre, nuevo_gerente_id)
            elif opcion == "8":
                departamento_id = validar_entero("ID del departamento a eliminar: ")
                eliminar_departamento(departamento_id)

            # Gestión de Proyectos
            elif opcion == "9":
                nombre = validar_nombre("Nombre del proyecto: ")
                descripcion = input("Descripción del proyecto: ")
                fecha_inicio = input("Fecha de inicio del proyecto (AAAA-MM-DD): ")
                crear_proyecto(nombre, descripcion, fecha_inicio)
            elif opcion == "10":
                proyectos = obtener_proyectos()
                if proyectos:
                    for proyecto in proyectos:
                        print(f"{proyecto[0]} - {proyecto[1]}, {proyecto[2]}, Fecha inicio: {proyecto[3]}")
                else:
                    print("No hay proyectos registrados.")
            elif opcion == "11":
                proyecto_id = validar_entero("ID del proyecto a actualizar: ")
                nuevo_nombre = validar_nombre("Nuevo nombre del proyecto: ")
                nueva_descripcion = input("Nueva descripción del proyecto: ")
                nueva_fecha_inicio = input("Nueva fecha de inicio del proyecto (AAAA-MM-DD): ")
                actualizar_proyecto(proyecto_id, nuevo_nombre, nueva_descripcion, nueva_fecha_inicio)
            elif opcion == "12":
                proyecto_id = validar_entero("ID del proyecto a eliminar: ")
                eliminar_proyecto(proyecto_id)
            #Gestión Usuarios
            elif opcion == "13":
                print("\n--- Gestión de Usuarios ---")
                print("1. Crear Usuario")
                print("2. Listar Usuarios")
                print("3. Eliminar Usuario")
                gestion_opcion = input("Elige una opción: ")
                if gestion_opcion not in [str(i) for i in range(1, 4)]:
                    raise ValueError("Opción inválida. Por favor, elige una opción válida entre 1 y 3.")
                if gestion_opcion == "1":
                    agregar_usuario()
                elif gestion_opcion == "2":
                    listar_usuarios()
                elif gestion_opcion == "3":
                    eliminar_usuario()
                else:
                    print("Opción inválida en gestión de usuarios.")
                #Api
            elif opcion == "14":
                main_api()
            elif opcion == "15":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")
        except ValueError as ve:
            print(f"Error: {ve}")
