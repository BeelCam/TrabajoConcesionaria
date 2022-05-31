class Colectivo():
    def __init__(self,marca,modelo,pasajeros,precio,km,  detalles):
        self.marca = marca
        self.modelo = modelo
        self.pasajeros = pasajeros
        self.precio = precio
        self.km = km
        self.detalles = detalles

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self) -> str:
        return f'Detalles {self.detalles}'