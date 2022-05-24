from constructores.Constructores import *
from data.Acoplado import *
from data.Bicicleta import *
from data.Moto import *
from modelo.Camion import *
from data.Camion import *
from data.Camioneta import *
from data.Colectivo import*
from data.Auto import *

def bienvenida():
    print("Concesionaria 'La concesionaria'")
    crearUsuario()
    crearCamion()
    crearAcoplado()
    crearAuto()
    crearBicicleta()
    crearCamioneta()
    crearMoto()
    
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
    print("8 Agregar nuevo usuaurio")
    print("0 Salir")
    opcionIngresada = int(input("Ingrese una opcion: "))


    if (opcionIngresada == 1):
        print("---- Camiones ---- \n")
        print("1 Insertar nuevo camion")
        print("2 Mostrar camiones")

        op = int(input("Ingrese una opcion: "))
        if (op == 1):
                insertarCamion()
        if (op == 2):
                printCamiones()
        
    if (opcionIngresada == 2):
        print("---- Autos ---- \n")
        print("1 Insertar nuevo auto")
        print("2 Mostrar autos")

        op = int(input("Ingrese una opcion: "))
        if (op == 1):
                insertarAuto()
        if (op == 2):
                printAutos()
        
    if (opcionIngresada == 3):
        print("---- Motos ---- \n")
        print("1 Insertar nueva moto")
        print("2 Mostrar motos")

        op = int(input("Ingrese una opcion: "))
        if (op == 1):
                insertarMoto()
        if (op == 2):
                printMotos()
        
    if (opcionIngresada == 4):
        print("---- Ver Camionetas ----")
        print("---- Camionetas ---- \n")
        print("1 Insertar nueva camioneta")
        print("2 Mostrar camionetas")

        op = int(input("Ingrese una opcion: "))
        if (op == 1):
                insertarCamioneta()
        if (op == 2):
                printCamionetas()
        
    if (opcionIngresada == 5):
        print("---- Colectivos ---- \n")
        print("1 Insertar nuevo colectivo")
        print("2 Mostrar colectivo")

        op = int(input("Ingrese una opcion: "))
        if (op == 1):
                insertarColectivo()
        if (op == 2):
                printColectivos()
        
    if (opcionIngresada == 6):
        print("---- Acoplados ---- \n")
        print("1 Insertar nuevo acoplado")
        print("2 Mostrar acoplados")

        op = int(input("Ingrese una opcion: "))
        if (op == 1):
                insertarAcoplado()
        if (op == 2):
                printAcoplados()
        
    if (opcionIngresada == 7):
        print("---- Bicicletas ---- \n")
        print("1 Insertar nueva bicicletas")
        print("2 Mostrar bicicletas")

        op = int(input("Ingrese una opcion: "))
        if (op == 1):
                insertarBicicleta()
        if (op == 2):
                printBicicletas()
        
    
    if (opcionIngresada == 8):
        crearUsuario()

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
        printCamiones()
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
