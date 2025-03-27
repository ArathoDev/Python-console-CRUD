import mysql.connector

class Conexion:
    def __init__(self):
        self.__host = "localhost"
        self.__user = "root"
        self.__password = ""
        self.__database = "bd_python_prueba"
        self.connection = None
        self.cursor = None
        self.__abrir()
    
    def __abrir(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.__host,
                user = self.__user,
                password = self.__password,
                database = self.__database       
            )
            self.cursor = self.connection.cursor()
            #print("Conexion abierta")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")
        
    def cerrar(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
            #print("Conexion cerrada")
        except Exception as ex:
            print(f"Error al cerrar conexion: {ex}")
    
    def select_all(self, query: str, params: tuple = None):
        try:
            self.cursor.execute(query, params)
            response = self.cursor.fetchall()
            self.cerrar()
            return response
        except Exception as ex:
            print(f"Error en el proceso de consulta: {ex}")
            
    def insert(self, query: str, params: tuple):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            #print("Insercion exitosa")
            self.cerrar()
        except Exception as ex:
            print(f"Error de insercion: {ex}")

    def find(self, query: str, params: tuple):
        try:
            self.cursor.execute(query, params)
            response = self.cursor.fetchone()
            self.cerrar()
            return response
        except Exception as ex:
            print(f"Error de busqueda: {ex}")
            
    def update(self, query: str, params: tuple):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            self.cerrar()
            #print("Actualizacion exitosa")
        except Exception as ex:
            print(f"Error de actualizacion: {ex}")
    
    def delete(self, query: str, params: tuple):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            self.cerrar()
            #print("Eliminacion exitosa")
        except Exception as ex:
            print(f"Error de eliminacion: {ex}")
    
        