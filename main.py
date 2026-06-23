from os import system
from funciones import *
while True:
    try:
        system("pause")
        system("cls")
        print(f""" 
        ========== CONTROL DE INVENTARIO AUTOMOTRIZ ==========
        1. Ingresar Nuevo Vehículo
        2. Verificar Existencia de Patente
        3. Actualizar Datos de un Vehículo (Precio y Año)
        4. Aplicar Descuento Masivo por Año
        5. Exportar Inventario Filtrado por Tipo
        6. Listar Catálogo Completo con IVA Incluido
        7. Finalizar Programa
        ======================================================
        """)
        opcion=int(input(f"Seleccione: "))
        match opcion:
            case 1:
                patente=input(f"Ingrese patente: ").upper().strip()
                tipo=input(f"Ingrese tipo: ")
                anio=input(f"Ingrese año (2015-2026): ")
                precio=input(f"Ingrese precio: ")
                agregar(patente,tipo,anio,precio)
            case 2:
                patente=input(f"Ingrese patente: ").upper().strip()
                mostrar(patente)
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case _:
                print("No valido")

        pass
    except Exception as e:
        print(f"Error. {e}")
