from data.Usuarios import *
from data.Moto import agregarMotos
from data.Acoplado import agregarAcoplados
from data.Bicicleta import agregarBicicletas
from data.Camion import *
from data.Camioneta import agregarCamionetas
from data.Colectivo import agregarColectivos
from data.Auto import agregarAutos


from modelo.Usuario import UsuarioInvitado, UsuarioEmpleado, UsuarioAdmin
from modelo.Acoplado import Acoplado
from modelo.Moto import Moto
from modelo.Bicicleta import Bicicleta
from modelo.Auto import Auto
from modelo.Camion import Camion
from modelo.Colectivo import Colectivo
from modelo.Camioneta import Camioneta


def crearUsuario():
    usuario_admin = UsuarioAdmin('Belen', 'Camargo','belen@gmail.com', 'contraseña1' ,1)
    agregarUsuario(usuario_admin)

    usuario_empleado = UsuarioEmpleado('Juan', 'Perez','juan@gmail.com', 'contraseña2' ,2)
    agregarUsuario(usuario_empleado)

    usuario_invitado = UsuarioInvitado('Pedro', 'Garcia','pedro@gmail.com', 'contraseña3' ,3)
    agregarUsuario(usuario_invitado)

def agregarUsuariosNuevos():
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        correo = input("Ingrese el correo: ")
        contraseña = input("Ingrese la contraseña: ")
        nivelUsuario = input("Ingrese el nivel de usuario [1: admin] [2: empleado] [3: invitado]: ")
        if (nivelUsuario == 1):
            usuario_ingresado = UsuarioAdmin(nombre, apellido,correo,contraseña)
        if (nivelUsuario == 2):
            usuario_ingresado = UsuarioEmpleado(nombre, apellido,correo,contraseña)
        if (nivelUsuario == 3):
            usuario_ingresado = UsuarioInvitado(nombre, apellido,correo,contraseña)
        


def crearAuto():
    auto = Auto('VW', 'Gol trend', 65000, 800000, 'opticas opacas')
    agregarAutos(auto)

def insertarAuto():
    marca = input("Ingrese la marca: ")
    modelo = input("Ingrese el modelo: ")
    km = input ("Ingrese los kilometros: ")
    precio = input("Ingrese el precio: ")
    detalles = input("Ingrese los detalles: ")
    auto_ingresado = Auto(marca, modelo, km,precio, detalles)
    agregarAutos(auto_ingresado)

def crearMoto():
    moto = Moto('Honda', '2013', '150cc', 23000, 160.000 ,'Ruedas gastadas')
    agregarMotos(moto)

def insertarMoto():
    marca = input("Ingrese la marca: ")
    modelo = input("Ingrese el modelo: ")
    cilindrada = input ("Ingrese las cilindradas: ")
    kilometros = input ("Ingrese los kilometros: ")
    precio = input("Ingrese el precio: ")
    detalles = input("Ingrese los detalles: ")
    moto_ingresada = Moto(marca, modelo,cilindrada, kilometros,precio, detalles)
    agregarMotos(moto_ingresada)

def crearAcoplado():
    acoplado = Acoplado('Rojo', 'Grande', '18 toneladas',300.000, 'Pintura gastadas')
    agregarAcoplados(acoplado)

def insertarAcoplado():
    color = input("Ingrese el color: ")
    tamaño = input("Ingrese el tamaño: ")
    peso = input ("Ingrese el peso que soporta: ")
    precio = input("Ingrese el precio: ")
    detalles = input("Ingrese los detalles: ")
    acoplado_ingresado = Acoplado(color, tamaño, peso,precio, detalles)
    agregarAcoplados(acoplado_ingresado)

def crearBicicleta():
    bicicleta = Bicicleta('Verde', 'Venzo', '29',40.000, 'Excelente estado')
    agregarBicicletas(bicicleta)

def insertarBicicleta():
    color = input("Ingrese el color: ")
    marca = input("Ingrese la marca: ")
    rodado = input ("Ingrese el rodado: ")
    precio = input("Ingrese el precio: ")
    detalles = input("Ingrese los detalles: ")
    bicicleta_ingresada = Bicicleta(color, marca, rodado,precio, detalles)
    agregarBicicletas(bicicleta_ingresada)

def crearCamion():
    camion = Camion('Mercedes Benz', '2020',120000,11000000, 'Excelente estado')
    agregarCamiones(camion)

def insertarCamion():
    marca = input("Ingrese la marca: ")
    modelo = input ("Ingrese el modelo: ")
    km = input("Ingrese los kilometros: ")
    precio = input("Ingrese el precio: ")
    detalles = input("Ingrese los detalles: ")
    camion_ingresado = Camion( marca, modelo, km,precio, detalles)
    agregarCamiones(camion_ingresado)

def crearCamioneta():
    camioneta = Camioneta('Ford', '2021',2 ,120000,5000000, 'Excelente estado')
    agregarCamionetas(camioneta)

def insertarCamioneta():
    marca = input("Ingrese la marca: ")
    modelo = input ("Ingrese el modelo: ")
    cabina = input("Ingrese el total de cabinas: ")
    km = input("Ingrese los kilometros: ")
    precio = input("Ingrese el precio: ")
    detalles = input("Ingrese los detalles: ")
    camioneta_ingresada = Camioneta( marca, modelo,cabina, km,precio, detalles)
    agregarCamionetas(camioneta_ingresada)

def crearColectivo():
    colectivo = Colectivo('Mercedes Benz', '2019',30,200000, 5000000, 'Excelente estado')
    agregarColectivos(colectivo)

def insertarColectivo():
    marca = input("Ingrese la marca: ")
    modelo = input ("Ingrese el modelo: ")
    pasajeros = input("Ingrese el total de pasajeros: ")
    precio = input("Ingrese el precio: ")
    km = input("Ingrese los kilometros: ")
    detalles = input("Ingrese los detalles: ")
    colectivo_ingresado = Colectivo(marca, modelo, pasajeros,precio,km, detalles)
    agregarColectivos(colectivo_ingresado)


