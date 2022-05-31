_acoplados = []

def agregarAcoplados(acoplado):
    _acoplados.append(acoplado)

def printAcoplados():
    print(_acoplados)

def mostrarAcopladoPrecioyTamaño():
    for acoplado in _acoplados:
        print("Color acoplado: ", acoplado.color)
        print("Precio: ", acoplado.precio)
        print("Tamaño: ", acoplado.tamaño)
        print("-------------------------")

def modificarAcoplado():
    for acoplado in _acoplados:
        acoplado.color = input("Ingrese el color del acoplado: ")
        acoplado.precio = input("Ingrese el precio: ")
        acoplado.detalle = input("Ingrese los detalles: ")


