"""Cursor de  POOL"""

from loger_base import log
from conexcion2 import Connection
class CursorDePool:
    def __init__(self):
        self._cursor = None
        self._connection = None
    def __enter__(self):
        log.debug("Se a iniciado el metodo _enter_")
        self._connection = Connection.obtenerConexion()
        self._cursor = self._connection.cursor()
        return self._cursor
    def __exit__(self, exc_type, exc_value,traceback):
        log.debug("se a iniciado el metodo _exit_")
        if exc_type:
            self._connection.rollback()
            log.error(f"se a detectado un error,rollback {exc_type} {exc_value} {traceback}")
        else:
            self._connection.commit()
            log.debug("commit de la transacion ")
            
        self._cursor.close()
        Connection.liberarConexion(self._connection)
        
if __name__ == "__main__":
    with CursorDePool() as cursor:
        log.debug("dentro del bloque with")
        cursor.execute("SELECT * FROM users")
        log.debug(cursor.fetchall())
        
        
    
#successful







