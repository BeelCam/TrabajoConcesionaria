class Auto():
    def __init__(self, marca, modelo, km,precio, detalles):
        self.marca = marca
        self.modelo = modelo
        self.km = km
        self.precio = precio
        self.detalles = detalles

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self) -> str:
        return f'Detalles {self.detalles}'