class Moto():
    def __init__(self, marca, modelo, cilindrada, kilometros,precio, detalles):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.kilometros = kilometros
        self.precio = precio
        self.detalles = detalles

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self) -> str:
        return f'Detalles {self.detalles}'