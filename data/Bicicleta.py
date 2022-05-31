from pyrsistent import b


_bicicletas = []

def agregarBicicletas(bicicleta):
    _bicicletas.append(bicicleta)

def printBicicletas():
    print(_bicicletas)

def mostrarBiciPrecioyRodado():
    for bicicleta in _bicicletas:
        print("Marca: ", bicicleta.marca)
        print("Precio: ", bicicleta.precio)
        print("Color: ", bicicleta.color)
        print("Rodado: ", bicicleta.rodado)
        print("Precio: ", bicicleta.precio)
        print("Detalles: ", bicicleta.detalles)
        print("-------------------------")

def modificarPrecioyColorBici():
    for bicicleta in _bicicletas:
        bicicleta.modelo = input("Ingrese el modelo del la bicicleta: ")
        bicicleta.color = input("Ingrese los color: ")
        bicicleta.precio = input("Ingrese el precio: ")