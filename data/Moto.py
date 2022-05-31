_motos = []

def agregarMotos(moto):
    _motos.append(moto)

def printMotos():
    print(_motos)

def mostrarMotoPrecioyKm():
    for moto in _motos:
        print("Marca: ", moto.marca)
        print("Modelo moto: ", moto.modelo)
        print("Cilindrada: ", moto.cilindrada)
        print("Precio: ", moto.precio)
        print("Kilometros: ", moto.km)
        print("Detalles: ", moto.detalles)
        print("-------------------------")

def modificarKmyPrecioMoto():
    for moto in _motos:
        moto.modelo = input("Ingrese el modelo de la moto: ")
        moto.precio = input("Ingrese el precio: ")
        moto.km = input("Ingrese los kilometros: ")