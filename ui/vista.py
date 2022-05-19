from constructores.Constructores import crearUsuario
from data.Moto import printMotos
from data.Acoplado import printAcoplados
from data.Bicicleta import printBicicletas
from modelo.Camion import Camion
from data.Camioneta import printCamionetas
from data.Colectivo import printColectivos
from data.Auto import printAutos

def bienvenida():
    print("Concesionaria 'La concesionaria'")
    crearUsuario()

def msjUsuario():
    return input("Ingrese correo: ")

def msjErrorUsuario():
    print("Usuario Incorrecto")

def msjContraseña():
    return input("Ingrese contraseña: ")
 
def msjErrorContraseña():
     print("Contraseña incorrecta")

def Admin():
    print("---- Menu Administrador ----")
    print("1 Ver Camiones")
    print("2 Ver Autos")
    print("3 Ver Motos")
    print("4 Ver Camionetas")
    print("5 Ver Colectivos")
    print("6 Ver Acoplados")
    print("7 Ver Bicicletas")
    print("0 Salir")
    opcionIngresada = int(input("Ingrese una opcion: "))
    if (opcionIngresada == 1):
        print("---- Ver Camiones ----")
        #Cargar nuevos camiones
        #cargar y modificar detalles, kilometros, precios, detalles
        #Crear nuevos usuarios invitados y usuarios standard.
    if (opcionIngresada == 2):
        print("---- Ver Autos ----")
        #Cargar nuevos Autos
        #cargar y modificar detalles, kilometros, precios, detalles
        #Crear nuevos usuarios invitados y usuarios standard.
    if (opcionIngresada == 3):
        print("---- Ver Motos ----")
        #Cargar nuevos Motos
        #cargar y modificar detalles, kilometros, precios, detalles
        #Crear nuevos usuarios invitados y usuarios standard.
    if (opcionIngresada == 4):
        print("---- Ver Camionetas ----")
        #Cargar nuevos camionetas
        #cargar y modificar detalles, kilometros, precios, detalles
        #Crear nuevos usuarios invitados y usuarios standard.
    if (opcionIngresada == 5):
        print("---- Ver Colectivos ----")
        #Cargar nuevos colectivos
        #cargar y modificar detalles, kilometros, precios, detalles
        #Crear nuevos usuarios invitados y usuarios standard.
    if (opcionIngresada == 6):
        print("---- Ver Acoplados ----")
        #Cargar nuevos acoplados
        printAcoplados
        #cargar y modificar detalles, kilometros, precios, detalles
        #Crear nuevos usuarios invitados y usuarios standard.
    if (opcionIngresada == 7):
        print("---- Ver Bicicletas ----")
        #Cargar nuevos bicicletas
        #cargar y modificar detalles, kilometros, precios, detalles
        #Crear nuevos usuarios invitados y usuarios standard.

    if(opcionIngresada == 0):
        return False


def Empleado():
    print("---- Menu Empleado ----")
    print("1 Ver Camiones")
    print("2 Ver Autos")
    print("3 Ver Motos")
    print("4 Ver Camionetas")
    print("5 Ver Colectivos")
    print("6 Ver Acoplados")
    print("7 Ver Bicicletas")
    print("0 Salir")
    opcionIngresada = int(input("Ingrese una opcion: "))
    if (opcionIngresada == 1):
        print("---- Ver Camiones ----")
        #Ver precio y kilometros
        #Modificar kilometros
        #Agregar detalles
    if (opcionIngresada == 2):
        print("---- Ver Autos ----")
         #Ver precio y kilometros
        #Modificar kilometros
        #Agregar detalles
    if (opcionIngresada == 3):
        print("---- Ver Motos ----")
         #Ver precio y kilometros
        #Modificar kilometros
        #Agregar detalles
    if (opcionIngresada == 4):
        print("---- Ver Camionetas ----")
         #Ver precio y kilometros
        #Modificar kilometros
        #Agregar detalles
    if (opcionIngresada == 5):
        print("---- Ver Colectivos ----")
         #Ver precio y kilometros
        #Modificar kilometros
        #Agregar detalles
    if (opcionIngresada == 6):
        print("---- Ver Acoplados ----")
         #Ver precio y kilometros
        #Modificar kilometros
        #Agregar detalles
    if (opcionIngresada == 7):
        print("---- Ver Bicicletas ----")
         #Ver precio y kilometros
        #Modificar kilometros
        #Agregar detalles

    if(opcionIngresada == 0):
        return False


def Invitado():
    print("---- Menu Invitado ----")
    print("1 Ver Camiones")
    print("2 Ver Autos")
    print("3 Ver Motos")
    print("4 Ver Camionetas")
    print("5 Ver Colectivos")
    print("6 Ver Acoplados")
    print("7 Ver Bicicletas")
    print("0 Salir")
    opcionIngresada = int(input("Ingrese una opcion: "))
    if (opcionIngresada == 1):
        print("---- Ver Camiones ----")
        #Detalles camion
    if (opcionIngresada == 2):
        print("---- Ver Autos ----")
        #Detalles auto
    if (opcionIngresada == 3):
        print("---- Ver Motos ----")
        #Detalles moto
    if (opcionIngresada == 4):
        print("---- Ver Camionetas ----")
        #Detalles camioneta
    if (opcionIngresada == 5):
        print("---- Ver Colectivos ----")
        #Detalles colectivo
    if (opcionIngresada == 6):
        print("---- Ver Acoplados ----")
        #Detalles acoplado
    if (opcionIngresada == 7):
        print("---- Ver Bicicletas ----")
        #Detalles bicicleta

    if(opcionIngresada == 0):
        return False
