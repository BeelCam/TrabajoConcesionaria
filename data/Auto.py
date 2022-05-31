_autos = []

def agregarAutos(auto):
    _autos.append(auto)

def printAutos():
    print(_autos)

def mostrarAutoPrecioyKm():
    for auto in _autos:
        print("Marca: ", auto.modelo)
        print("Modelo auto: ", auto.modelo)
        print("Precio: ", auto.precio)
        print("Kilometros: ", auto.km)
        print("Detalles: ", auto.detalles)
        print("-------------------------")
        

def modificarKmAuto():
    for auto in _autos:
        auto.modelo = input("Ingrese el modelo del auto: ")
        auto.precio = input("Ingrese el precio: ")
        auto.km = input("Ingrese los kilometros: ")
