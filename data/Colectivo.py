_colectivos = []

def agregarColectivos(colectivo):
    _colectivos.append(colectivo)

def printColectivos():
    print(_colectivos)

def mostrarColectivoPrecioyKm():
    for colectivo in _colectivos:
        print("Marca: ", colectivo.marca)
        print("Modelo colectivo: ", colectivo.modelo)
        print("Pasajeros: ", colectivo.pasajeros)
        print("Precio: ", colectivo.precio)
        print("Kilometros: ", colectivo.km)
        print("Detalles: ", colectivo.detalles)
        print("-------------------------")

def modificarKmyPrecioColectivo():
    for colectivo in _colectivos:
        colectivo.modelo = input("Ingrese el modelo del colectivo: ")
        colectivo.precio = input("Ingrese el precio: ")
        colectivo.km = input("Ingrese los kilometros: ")

