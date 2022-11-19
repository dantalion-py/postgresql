""""ventana de opciones"""
from loger_base import log
from conexcion2 import Connection
from usuario import Usuario
from usuarioDao import UserDAO
opcion=None
while opcion!=5:
    print("funcionalidad del lado del usuario".center(50,"="))
    print("1)Listar usuarios\n2)Agregar usuario\n3)Actualizar usuario\n4)elimimar usuario\n5)salir")
    opcion=int(input("elige una opcion:\t"))
    if opcion==1:
        usuarios = UserDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion==2:
        usr = input("introduce el usuario:\t")
        psw = input("introduce la contraseña:\t")
        valueUser = Usuario(username=usr,password=psw)
        user=UserDAO.insertar(valueUser)
        log.info(f"nuevo usuario {user}")
    elif opcion==3:
        id = input("introduce el id del usuario a actualizar: ")
        usr = input("introduce el nuevo usuario: ")
        psw = input("introduce la nueva contraseña: ")
        valueuser = Usuario(username=usr,password=psw,id_user=id)
        user = UserDAO.actualizar(valueuser)
        log.info(f"nuevo usuario {user}")
    elif opcion==4:
        id=input("introduce el id del usuario a elimimar: ")
        valueuser = Usuario(id_user=id)
        user = UserDAO.eliminar(valueuser)
        log.info(f"usuario eliminado {user}")
else:
    log.debug("Saliendo de las opciones:")