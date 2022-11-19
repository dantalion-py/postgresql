"""conexion"""


from loger_base import log
from psycopg2 import pool
import sys

class Connection:
    _DB_HOST="localhost"
    _DB_PORT="5432"
    _DATABASE="test_db"
    _USER="postgres"
    _PASSWORD="admin"
    _MAX_CO=5
    _MIN_CO=1
    _pool=None
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool =pool.SimpleConnectionPool(cls._MIN_CO,cls._MAX_CO,
                                                     user=cls._USER,
                                                     password=cls._PASSWORD,
                                                     host=cls._DB_HOST,
                                                     port=cls._DB_PORT,
                                                     database=cls._DATABASE)
                log.debug("successful connection ")
                return cls._pool
            except Exception as e:
                log.debug(f"se a encontrado un error:{e}")
                sys.exit()
        else:
            return cls._pool
    @classmethod
    def obtenerConexion(cls):
        conexion =cls.obtenerPool().getconn()
        log.debug(f"successful connection: {conexion}")
        return conexion
    
    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f"connection released {conexion}")
    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()
        
        
if __name__ == "__main__":
    conexion1=Connection.obtenerConexion()
    Connection.liberarConexion(conexion1)
    conexion3=Connection.obtenerConexion()
    
    
#successful