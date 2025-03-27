from models.Producto import Producto
from os import system
from time import sleep

class Program:
    def __init__(self):
        self.__menu_principal()
    
    def __menu_principal(self):
        system("cls")
        sleep(1)
        print("========================")
        print("    CRUD - PRODUCTOS")
        print("========================")
        print("1. LISTAR TODOS")
        print("2. BUSCAR POR ID")
        print("3. AGREGAR NUEVO")
        print("4. ACTUALIZAR PRODUCTO")
        print("5. ELIMINAR")
        print("6. SALIR")
        print("========================")
        operation = int(input("Selecciona la opción: "))
        if operation == 1:
            self.__menu_listar()
        elif operation == 2:
            self.__menu_buscar()
        elif operation == 3:
            self.__menu_crear()
        elif operation == 4:
            self.__menu_actualizar()
        elif operation == 5:
            self.__menu_eliminar()
        elif operation == 6:
            self.__salir()
            
    def __menu_listar(self):
        system("cls")
        sleep(1)
        print("========================")
        print("LISTA DE PRODUCTOS")
        print("========================")
        p = Producto()
        for i in p.read():
            print(i)
        print("========================")
        decision = input("VOLVER AL MENÚ PRINCIPAL [Z]: ").lower()
        if decision == "z":
            self.__menu_principal()
    
    def __menu_crear(self):
        system("cls")
        sleep(1)
        print("========================")
        print("CREAR NUEVO PRODUCTO")
        print("========================")
        nombre = input("Nombre: ")
        precio = float(input("Precio ($): "))
        p = Producto(nombre, precio)
        p.create()
        print("========================")
        print("PRODUCTO NUEVO AGREGADO")
        sleep(2)
        self.__menu_principal()
    
    def __menu_buscar(self):
        system("cls")
        sleep(1)
        print("========================")
        print("BUSCAR PRODUCTO")
        print("========================")
        id = int(input("Id del producto: "))
        print("========================")
        p = Producto()
        print(p.find_by_id(id))
        print("========================")
        decision = input("VOLVER AL MENÚ PRINCIPAL [Z]: ").lower()
        if decision == "z":
            self.__menu_principal()
    
    def __menu_actualizar(self):
        system("cls")
        sleep(1)
        print("========================")
        print("ACTUALIZAR PRODUCTO")
        print("========================")
        id = int(input("Id para actualizar: "))
        nombre = input("Nuevo nombre: ")
        precio = input("Nuevo precio: ")
        p = Producto(nombre, precio)
        p.update(id)
        print("========================")
        print("PRODUCTO ACTUALIZADO")
        sleep(2)
        self.__menu_principal()
    
    def __menu_eliminar(self):
        system("cls")
        sleep(1)
        print("========================")
        print("ELIMINAR PRODUCTO")
        print("========================")
        id = int(input("Id del producto: "))
        p = Producto()
        p.delete(id)
        print("========================")
        print("PRODUCTO ELIMINADO")
        sleep(2)
        self.__menu_principal()
    
    def __salir(self):
        system("cls")
        print("Saliendo.")
        sleep(0.5)
        system("cls")
        print("Saliendo..")
        sleep(0.5)
        system("cls")
        print("Saliendo...")
        sleep(0.5)
        system("cls")
        