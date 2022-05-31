from constructores.Constructores import *
from ui.vista import *
from controlador.UsuariosControllers import *
from constructores.Constructores import *

bienvenida()
userOk = buscarUsuario(msjUsuario())
intentos = 3
try:
    if(userOk):

        usuarioconPass = validarContraseña(msjContraseña())
        while userOk:
            if(usuarioconPass[0]):
                userOk = menu(usuarioconPass[1])
    else:
        print('No se encontro el Usuario')

finally:
    print('Gracias por Visitarnos')

