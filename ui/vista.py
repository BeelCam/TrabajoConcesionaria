from pickle import TRUE
from constructores.Constructores import *
from data.Acoplado import *
from data.Bicicleta import *
from data.Moto import *
from modelo.Camion import *
from data.Camion import *
from data.Camioneta import *
from data.Colectivo import*
from data.Auto import *

import os

def borrarPantalla():
        if os.name == "posix":
                os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system ("cls")

def bienvenida():
        print("-----Concesionaria 'La concesionaria'-----")
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
        borrarPantalla()
        print("---- Menu Administrador ----")
        print("1 Ver Camiones")
        print("2 Ver Autos")
        print("3 Ver Motos")
        print("4 Ver Camionetas")
        print("5 Ver Colectivos")
        print("6 Ver Acoplados")
        print("7 Ver Bicicletas")
        print("8 Agregar nuevo usuario")
        print("0 Salir")
        opcionIngresada = int(input("Ingrese una opcion: "))
        while opcionIngresada <=0 or opcionIngresada >3:
                try:
                        opcionIngresada = int(input("Ingrese una opcion: "))
                                
                except ValueError:
                        print("Ingrese una opcion valida")
                        opcionIngresada = int(input("Ingrese una opcion: "))
        borrarPantalla()


        if (opcionIngresada == 1):
                print("---- Camiones ---- \n")
                print("1 Insertar nuevo camion")
                print("2 Mostrar camiones")
                print("3 Volver al menu principal")

                op = int(input("Ingrese una opcion: "))
                while op <=0 or op >3:
                        try:
                                op = int(input("Ingrese una opcion: "))
                                
                        except ValueError:
                                print("Ingrese una opcion valida")
                                op = int(input("Ingrese una opcion: "))
                borrarPantalla()

                if (op == 1) :
                        print("--- Insertar nuevo camion ---\n")
                        insertarCamion()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Admin()
                elif (op == 2):
                        print("--- Lista de camiones ---\n")
                        mostrarCamionPrecioyKm()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Admin() 
                elif (op == 3):
                        return Admin()

        if (opcionIngresada == 2):
                print("---- Autos ---- \n")
                print("1 Insertar nuevo auto")
                print("2 Mostrar autos")
                print("3 Volver al menu principal")
                op = int(input("Ingrese una opcion: "))
                while op <=0 or op >3:
                        try:
                                op = int(input("Ingrese una opcion: "))
                                
                        except ValueError:
                                print("Ingrese una opcion valida")
                                op = int(input("Ingrese una opcion: "))
        
                borrarPantalla()

                if (op == 1):
                        print("--- Insertar nuevo auto ---\n")
                        insertarAuto()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Admin()
                        
                if (op == 2):
                        print("--- Lista de autos ---\n")
                        mostrarAutoPrecioyKm()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Admin() 
                if (op == 3):
                        return Admin()
                
                
        if (opcionIngresada == 3):
                print("---- Motos ---- \n")
                print("1 Insertar nueva moto")
                print("2 Mostrar motos")
                print("3 Volver al menu principal")

                op = int(input("Ingrese una opcion: "))
                while op <=0 or op >3:
                        try:
                                op = int(input("Ingrese una opcion: "))
                                
                        except ValueError:
                                print("Ingrese una opcion valida")
                                op = int(input("Ingrese una opcion: "))
                borrarPantalla()

                if (op == 1):
                        print("--- Insertar nueva moto ---\n")
                        insertarMoto()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Admin()
                        
                if (op == 2):
                        print("--- Lista de motos ---\n")
                        mostrarMotoPrecioyKm()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Admin() 
                if (op == 3):
                        return Admin()

        if (opcionIngresada == 4):
                print("---- Camionetas ---- \n")
                print("1 Insertar nueva camioneta")
                print("2 Mostrar camionetas")
                print("3 Volver al menu principal")

                op = int(input("Ingrese una opcion: "))
                while op <=0 or op >3:
                        try:
                                op = int(input("Ingrese una opcion: "))
                                        
                        except ValueError:
                                print("Ingrese una opcion valida")
                                op = int(input("Ingrese una opcion: "))
                borrarPantalla()
                if (op == 1):
                        print("--- Insertar nueva camioneta ---\n")
                        insertarCamioneta()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Admin()
                        
                if (op == 2):
                        print("--- Lista de camionetas ---\n")
                        mostrarCamionetaPrecioyKm()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Admin() 
                if (op == 3):
                        return Admin()
                
        if (opcionIngresada == 5):
                print("---- Colectivos ---- \n")
                print("1 Insertar nuevo colectivo")
                print("2 Mostrar colectivo")
                print("3 Volver al menu principal")

                op = int(input("Ingrese una opcion: "))
                while op <=0 or op >3:
                        try:
                                op = int(input("Ingrese una opcion: "))
                        except ValueError:
                                print("Ingrese una opcion valida")
                                op = int(input("Ingrese una opcion: "))
                borrarPantalla()
                if (op == 1):
                        print("--- Insertar nuevo colectivo ---\n")
                        insertarColectivo()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Admin()
                        
                if (op == 2):
                        print("--- Lista de colectivos ---\n")
                        mostrarColectivoPrecioyKm()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Admin() 
                if (op == 3):
                        return Admin()
                else:
                        print("¡Opcion invalida!")
                        return  Admin()
                
        if (opcionIngresada == 6):
                print("---- Acoplados ---- \n")
                print("1 Insertar nuevo acoplado")
                print("2 Mostrar acoplados")
                print ("3 Volver al menu principal")

                op = int(input("Ingrese una opcion: "))
                while op <=0 or op >3:
                        try:
                                op = int(input("Ingrese una opcion: "))
                        except ValueError:
                                print("Ingrese una opcion valida")
                                op = int(input("Ingrese una opcion: "))
                borrarPantalla()
                if (op == 1):
                        print("--- Insertar nuevo acoplado ---\n")
                        insertarAcoplado()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Admin()
                        
                if (op == 2):
                        print("--- Lista de acoplados ---\n")
                        mostrarAcopladoPrecioyTamaño()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Admin() 
                if (op == 3):
                        return Admin()
                
        if (opcionIngresada == 7):
                print("---- Bicicletas ---- \n")
                print("1 Insertar nueva bicicletas")
                print("2 Mostrar bicicletas")
                print("3 Volver al menu principal")

                op = int(input("Ingrese una opcion: "))
                while op <=0 or op >3:
                        try:
                                op = int(input("Ingrese una opcion: "))
                        except ValueError:
                                print("Ingrese una opcion valida")
                                op = int(input("Ingrese una opcion: "))
                borrarPantalla()
                if (op == 1):
                        print("--- Insertar nueva bicicleta ---\n")
                        insertarBicicleta()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Admin()
                        
                if (op == 2):
                        print("--- Lista de bicicletas ---\n")
                        mostrarBiciPrecioyRodado()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Admin() 
                if (op == 3):
                        return Admin()
                
        
        if (opcionIngresada == 8):
                print("--- Insertar nuevo usuario ---\n")
                agregarUsuariosNuevos()
                enter = input("Presione 'Enter' para continuar")
                borrarPantalla()
                return Admin()
                

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
                while opcionIngresada <=0 or opcionIngresada >3:
                        try:
                                opcionIngresada = int(input("Ingrese una opcion: "))
                                        
                        except ValueError:
                                print("Ingrese una opcion valida")
                                opcionIngresada = int(input("Ingrese una opcion: "))
                borrarPantalla()

                if (opcionIngresada == 1):
                        print("---- Camiones ----")
                        print("1 Mostrar camiones")
                        print("2 Modificar")
                        print("3 Volver al menu principal")

                        op = int(input("Ingrese una opcion: "))
                        while op <=0 or op >3:
                                try:
                                        op = int(input("Ingrese una opcion: "))
                                except ValueError:
                                        print("Ingrese una opcion valida")
                                        op = int(input("Ingrese una opcion: "))
                        borrarPantalla()
                        if (op == 1):
                                print("--- Lista de camiones ---\n")
                                mostrarCamionPrecioyKm()
                                enter = input("Presione 'Enter' para continuar")
                                borrarPantalla()
                                return Empleado()
                                
                        if (op == 2):
                                print("--- Modificar ---")
                                modificarKmCamion()
                                enter = input("Presione 'Enter' para continuar")
                                borrarPantalla()
                                return Empleado() 
                        if (op == 3):
                                print("")

                if (opcionIngresada == 2):
                        print("---- Ver Autos ----")
                        print("1 Mostrar autos")
                        print("2 Modificar")
                        print("3 Volver al menu principal")

                        op = int(input("Ingrese una opcion: "))
                        while op <=0 or op >3:
                                try:
                                        op = int(input("Ingrese una opcion: "))
                                except ValueError:
                                        print("Ingrese una opcion valida")
                                        op = int(input("Ingrese una opcion: "))
                        borrarPantalla()
                        if (op == 1):
                                print("--- Lista de autos ---\n")
                                mostrarAutoPrecioyKm()
                                enter = input("Presione 'Enter' para continuar")
                                borrarPantalla()
                                return Empleado()
                                
                        if (op == 2):
                                print("--- Modificar ---\n")
                                modificarKmAuto()
                                enter = input("Presione 'Enter' para continuar")
                                borrarPantalla()
                                return Empleado() 
                        if (op == 3):
                                return Empleado()

                if (opcionIngresada == 3):
                        print("---- Ver Motos ----")
                        print("1 Precio y kilometros")
                        print("2 Modificar")
                        print("3 Volver al menu principal")

                        op = int(input("Ingrese una opcion: "))
                        while op <=0 or op >3:
                                try:
                                        op = int(input("Ingrese una opcion: "))
                                except ValueError:
                                        print("Ingrese una opcion valida")
                                        op = int(input("Ingrese una opcion: "))
                        borrarPantalla()
                        if (op == 1):
                                print("--- Lista de motos ---\n")
                                mostrarMotoPrecioyKm()
                                enter = input("Presione 'Enter' para continuar")
                                borrarPantalla()
                                return Empleado()
                                
                        if (op == 2):
                                print("--- Modificar ---\n")
                                modificarKmyPrecioMoto()
                                enter = input("Presione 'Enter' para continuar")
                                borrarPantalla()
                                return Empleado() 
                        if (op == 3):
                                return Empleado()

                if (opcionIngresada == 4):
                        print("---- Ver Camionetas ----")
                        print("1 Precio y kilometros")
                        print("2 Modificar")
                        print("3 Volver al menu principal")

                        op = int(input("Ingrese una opcion: "))
                        while op <=0 or op >3:
                                try:
                                        op = int(input("Ingrese una opcion: "))
                                except ValueError:
                                        print("Ingrese una opcion valida")
                                        op = int(input("Ingrese una opcion: "))
                        borrarPantalla()
                        if (op == 1):
                                print("--- Lista de camionetas ---\n")
                                mostrarCamionetaPrecioyKm()
                                enter = input("Presione 'Enter' para continuar")
                                borrarPantalla()
                                return Empleado()
                                
                        if (op == 2):
                                print("--- Modificar ---\n")
                                modificarKmyPrecioCamioneta()
                                enter = input("Presione 'Enter' para continuar")
                                borrarPantalla()
                                return Empleado() 
                        if (op == 3):
                                return Empleado()

                if (opcionIngresada == 5):
                        print("---- Ver Colectivos ----")
                        print("1 Lista Vehiculos")
                        print("2 Modificar")
                        print("3 Volver al menu principal")

                        op = int(input("Ingrese una opcion: "))
                        while op <=0 or op >3:
                                try:
                                        op = int(input("Ingrese una opcion: "))
                                except ValueError:
                                        print("Ingrese una opcion valida")
                                        op = int(input("Ingrese una opcion: "))
                        borrarPantalla()
                        if (op == 1):
                                print("--- Lista de colectivos ---\n")
                                mostrarColectivoPrecioyKm()
                                enter = input("Presione 'Enter' para continuar")
                                borrarPantalla()
                                return Empleado()
                                
                        if (op == 2):
                                print("--- Modificar ---\n")
                                modificarKmyPrecioColectivo()
                                enter = input("Presione 'Enter' para continuar")
                                borrarPantalla()
                                return Empleado() 
                        if (op == 3):
                                return Empleado()

                if (opcionIngresada == 6):
                        print("---- Ver Acoplados ----")
                        print("1 Lista acocplados")
                        print("2 Modificar")
                        print("3 Volver al menu principal")

                        op = int(input("Ingrese una opcion: "))
                        while op <=0 or op >3:
                                try:
                                        op = int(input("Ingrese una opcion: "))
                                except ValueError:
                                        print("Ingrese una opcion valida")
                                        op = int(input("Ingrese una opcion: "))
                        borrarPantalla()
                        if (op == 1):
                                print("--- Lista de acoplados ---\n")
                                mostrarAcopladoPrecioyTamaño()
                                enter = input("Presione 'Enter' para continuar")
                                borrarPantalla()
                                return Empleado()
                                
                        if (op == 2):
                                print("--- Modificar ---\n")
                                modificarAcoplado()
                                enter = input("Presione 'Enter' para continuar")
                                borrarPantalla()
                                return Empleado() 
                        if (op == 3):
                                return Empleado()

                if (opcionIngresada == 7):
                        print("---- Ver Bicicletas ----")
                        print("1 Lista Vehiculos")
                        print("2 Modificar")
                        print("3 Volver al menu principal")

                        op = int(input("Ingrese una opcion: "))
                        while op <=0 or op >3:
                                try:
                                        op = int(input("Ingrese una opcion: "))
                                except ValueError:
                                        print("Ingrese una opcion valida")
                                        op = int(input("Ingrese una opcion: "))
                        borrarPantalla()
                        if (op == 1):
                                print("--- Lista de bicicletas ---\n")
                                mostrarBiciPrecioyRodado()
                                enter = input("Presione 'Enter' para continuar")
                                borrarPantalla()
                                return Empleado()
                                
                        if (op == 2):
                                print("--- Modificar ---\n")
                                modificarPrecioyColorBici()
                                enter = input("Presione 'Enter' para continuar")
                                borrarPantalla()
                                return Empleado() 
                        if (op == 3):
                                return Empleado()

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
                while opcionIngresada <=0 or opcionIngresada >3:
                        try:
                                opcionIngresada = int(input("Ingrese una opcion: "))
                                        
                        except ValueError:
                                print("Ingrese una opcion valida")
                                opcionIngresada = int(input("Ingrese una opcion: "))
                borrarPantalla()

                if (opcionIngresada == 1):
                        print("---- Ver Camiones ----")
                        mostrarCamionPrecioyKm()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Invitado()
                if (opcionIngresada == 2):
                        print("---- Ver Autos ----")
                        mostrarAutoPrecioyKm()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Invitado()
                if (opcionIngresada == 3):
                        print("---- Ver Motos ----")
                        mostrarMotoPrecioyKm()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Invitado()
                if (opcionIngresada == 4):
                        print("---- Ver Camionetas ----")
                        mostrarCamionetaPrecioyKm()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Invitado()
                if (opcionIngresada == 5):
                        print("---- Ver Colectivos ----")
                        mostrarColectivoPrecioyKm()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Invitado()
                if (opcionIngresada == 6):
                        print("---- Ver Acoplados ----")
                        mostrarAcopladoPrecioyTamaño()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Invitado()
                if (opcionIngresada == 7):
                        print("---- Ver Bicicletas ----")
                        mostrarBiciPrecioyRodado()
                        enter = input("Presione 'Enter' para continuar")
                        borrarPantalla()
                        return Invitado()

                if(opcionIngresada == 0):
                        return False
