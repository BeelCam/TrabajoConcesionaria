class Acoplado():
    def __init__(self,color,tamaño, peso,precio, detalles):
        self.color = color
        self.tamaño = tamaño
        self.peso = peso
        self.precio = precio
        self.detalles = detalles

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self) -> str:
        return f'Detalles {self.detalles}'