"""usuarioDAO
CRUD
CREATE
-READ
-UPDATE
-DELETE"""
from loger_base import log
from conexcion2 import Connection
from cursorDePool import CursorDePool
from usuario import Usuario
class UserDAO:
    _SELECT = "SELECT * FROM users ORDER BY id_users"
    _UPDATE = "UPDATE users SET username=%s, password=%s WHERE id_users=%s"
    _DELETE = "DELETE FROM users WHERE id_users=%s"
    _INSERT = "INSERT INTO users(username, password) VALUES(%s, %s)"
    @classmethod
    def seleccionar(cls):
        with CursorDePool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                persona = Usuario(registro[0],registro[1],registro[2])
                usuarios.append(persona)
            return usuarios
        
    @classmethod
    def insertar(cls,usuario):
        with CursorDePool() as cursor:
            datos = (usuario.username,usuario.password)
            cursor.execute(cls._INSERT,datos)
            log.debug(f"user insert {usuario}")
            return cursor.rowcount
            
            
            
            
    @classmethod
    def actualizar(cls,usuario):
        with CursorDePool() as cursor:
            datos = (usuario.username, usuario.password,usuario.id_user)
            cursor.execute(cls._UPDATE,datos)
            log.debug(f"user update {usuario}")
            return cursor.rowcount
        
        
    
    @classmethod
    def eliminar(cls,usuario):
        with CursorDePool() as cursor:
            datos = (usuario.id_user,)
            cursor.execute(cls._DELETE,datos)
            log.debug(f"user delete: {usuario}")
            return cursor.rowcount
    
# if __name__ == "__main__":
    #puebas
    #insertar
    # persona1 =Usuario(username="Deverlan",password="thomsom")
    # persona_insertada = UserDAO.insertar(persona1)
    # log.debug(f"personas insertadas {persona_insertada}")
    
    
    # seleccionsar
    # personas=UserDAO.seleccionar()
    # for persona in personas:
    #     log.debug(persona)
    
    
    # # actualizar
    # persona=Usuario(id_user=10,username="criter",password="us@criter")
    # persona_actualizada =UserDAO.actualizar(persona)
    # log.debug(f"personas actualizadas {persona_actualizada}")
    
    
    # #eliminar
    # persona=Usuario(id_user=4)
    # persona_eliminada = UserDAO.eliminar(persona)
    # log.debug(f"persona eliminada {persona_eliminada}")
    
    
#successful