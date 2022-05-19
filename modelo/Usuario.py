class Usuario():

    def __init__(self, nombre, apellido, correo,contraseña, nivelUsuario):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña
        self.nivelUsuario = nivelUsuario
    
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        return print("Nombre: ", (self.nombre), "Apellido: " , (self.apellido), "Correo: ", (self.correo), "Contraseña: ", (self.contraseña), "Nivel del usuario: ", (self.nivelUsuario))