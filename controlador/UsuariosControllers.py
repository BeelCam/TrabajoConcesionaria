from asyncio.windows_events import NULL
from modelo.Usuario import Usuario
from data.Usuarios import _usuariosRegistrados
from data.Usuarios import agregarUsuario, printUsuarios
from ui.vista import *


user = Usuario('','','','','')

def buscarUsuario(correo):
    for usuario in _usuariosRegistrados:
        if usuario.correo == correo:
            user.nombre = usuario.nombre
            user.apellido = usuario.apellido
            user.correo = usuario.correo
            user.contraseña = usuario.contraseña
            user.nivelUsuario = usuario.nivelUsuario
            return True

def validarContraseña(contraseña):

    if user.contraseña == str(contraseña):
        print("Bienvenido")
        return [True, user.nivelUsuario]

def menu(args):
    if(args == 1):
        return menuAdmin()
    elif args == 2:
        return menuEmpleado()
    else:
        return menuInvitado()

def menuAdmin():
    Admin()

def menuEmpleado():
    Empleado()
    
def menuInvitado():
   Invitado()