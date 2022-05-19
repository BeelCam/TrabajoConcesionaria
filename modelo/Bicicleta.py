class Bicicleta():
    def __init__(self, color, marca, rodado,precio, detalles):
        self.color = color
        self.marca = marca
        self.rodado = rodado
        self.precio = precio
        self.detalles = detalles

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self) -> str:
        return f'Detalles {self.detalles}'