import MySQLdb 
from MySQLdb import Error
class DataConection:
    
    def __init__(self,usuario='',contrasena='',baseDatos='',query=''):
        self.usuario = usuario
        self.contrasena = contrasena
        self.baseDatos = baseDatos
        self.query = query

    def ejecuteQuery(self):
        stat = {}
        try:
            dbconnect = MySQLdb.connect('phpmyadmin.test', self.usuario, self.contrasena, self.baseDatos )
            cursor = dbconnect.cursor()
            cursor.execute(self.query)
            stat["status"] = 'true'
            stat["msg"] = "Usuario registrado de manera correcta"
        except Error as ex:
            stat["status"] = 'false'
            stat["msg"] = "Ocurrio un error al registar el usuario"+str(ex)
        dbconnect.close()
        return stat

    def testConnection(self):
        stat = {}
        try:
            dbconnect = MySQLdb.connect('phpmyadmin.test', self.usuario, self.contrasena, self.baseDatos )
            cursor = dbconnect.cursor()
            stat["status"] = True
            stat["msg"] = "Conexión establecida"
        except Error as ex:
            stat["status"] = False
            stat["msg"] = ex

        return stat