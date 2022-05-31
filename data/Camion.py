_camiones = []

def agregarCamiones(camion):
    _camiones.append(camion)

def printCamiones():
    print(_camiones)

def mostrarCamionPrecioyKm():
    for camion in _camiones:
        print("Marca camion: ", camion.marca)
        print("Modelo: ", camion.modelo)
        print("Precio: ", camion.precio)
        print("Kilometros: ", camion.km)
        print("Detalles: ", camion.detalles)
        print("-------------------------")

def modificarKmCamion():
    for camion in _camiones:
        camion.modelo = input("Ingrese el modelo del camion: ")
        camion.km = input("Ingrese los kilometros: ")
        camion.precio = input("Ingrese el precio: ")
        camion.detalles = input("Ingrese los detalles: ")
