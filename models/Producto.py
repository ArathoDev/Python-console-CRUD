from models.Conexion import Conexion

class Producto:
    def __init__(self, nombre: str = "", precio: float = 0.0):
        self.__nombre = nombre
        self.__precio = precio
    
    def read(self):
        query = "SELECT * FROM productos"   
        cnx = Conexion()
        data = cnx.select_all(query)
        return data
    
    def create(self): #CORREGIR: EN LUGAR DE PARAMS PASARLE EL OBJETO PRODUCTO
        query = "INSERT INTO productos (nombre, precio) VALUES (%s, %s)"
        cnx = Conexion()
        params = tuple([self.__nombre, self.__precio])
        cnx.insert(query, params)
    
    def find_by_id(self, id: int):
        query = "SELECT * FROM productos WHERE id = %s"
        cnx = Conexion()
        data = cnx.find(query, (id, ))
        return data
    
    def update(self, id: int): #CORREGIR: EN LUGAR DE PARAMS PASARLE EL OBJETO PRODUCTO
        query = "UPDATE productos SET nombre = %s, precio = %s WHERE id = %s"
        cnx = Conexion()
        params = tuple([self.__nombre, self.__precio, id])
        cnx.update(query, params)
    
    def delete(self, id: int):
        query = "DELETE FROM productos WHERE id = %s"
        cnx = Conexion()
        cnx.delete(query, (id, ))
       