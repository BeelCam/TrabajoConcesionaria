_camionetas = []

def agregarCamionetas(camioneta):
   _camionetas.append(camioneta)

def printCamionetas():
   print(_camionetas)

def mostrarCamionetaPrecioyKm():
   for camioneta in _camionetas:
      print("Marca: ", camioneta.marca)
      print("Modelo camioneta: ", camioneta.modelo)
      print("Cantidad cabinas: ", camioneta.camioneta)
      print("Precio: ", camioneta.precio)
      print("Kilometros: ", camioneta.km)
      print("Detalles: ", camioneta.detalles)
      print("-------------------------")

def modificarKmyPrecioCamioneta():
   for camioneta in _camionetas:
      camioneta.modelo = input("Ingrese el modelo de la camioneta: ")
      camioneta.precio = input("Ingrese el precio: ")
      camioneta.km = input("Ingrese los kilometros: ")

