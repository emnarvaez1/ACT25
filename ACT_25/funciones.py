#creamos la lista donde almacenaremos lo vehiculos
vehiculos=[]

# 0.- Funcion para validar la patente
def buscar(patente):
    for i in range(len(vehiculos)):
        if vehiculos[i]["patente"]==patente: 
            return i
    return -1

# 1.- Agregar
def agregar(patente,tipo,anio,precio):
    # Validar que tenga 6 caracteres sin espacios en blanco
    # Validar que la patente no se repita 
    if len(patente)!=6:
        print(f"Número de caracteres no válido")
        return
    #Válidar que no tenga espacios en blancos
    elif " " in patente:
        print("No puede tener espacion en blanco")
        return
    # Validar que la patente no se repita
    elif buscar(patente)>=0:
        print("No se puede repetir la patente")
        return
    # Válidar tipo
    elif tipo.lower() not in ("sedan","suv","camioneta"):
        print("Tipo no valido")
        return
    #Validar año
    elif anio<2025 or anio>2026:
        print("Año no valido")
        return
    elif precio<=5000000:
        print("Precio no válido")
        return
    # Si los datos son válidos creamos el diccionario con los datos
    auto={"patente":patente,"tipo":tipo,"anio":anio,"precio":precio}
    vehiculos.append(auto)
print("Vehiculo registrado")

def mostrar(patente):
    posicion=patente    
    if posicion>=0:
        print(f"Patente encontrada : {vehiculos[posicion]}")
    else:
        print("Patente no encontrada")


# Listar vehiculos con iva
def listariva():
    if len(vehiculos)>0:
        for i in range(len(vehiculos)):
            print(f"{i+1} {vehiculos[i]["patente"]:<8} {vehiculos[i]["tipo"]:<10} {vehiculos[i]["anio"]:<6} ${vehiculos[i]["precio"]:<10}")
            
    else:
        print("No hay vehiculos registrados")