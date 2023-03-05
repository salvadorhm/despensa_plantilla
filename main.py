from productos import Productos
from tiendas import Tiendas
#TODO importar Despensa

class Main():

    def __init__(self) -> None:
        pass

    def menu(self):
        productos = Productos()
        while True:
            print("0.- Listar Productos")
            print("1.- Insertar producto")
            print("2.- Buscar producto por sku")
            print("3.- Actualizar producto")
            print("4.- Borrar producto")
            print("5.- Salir")
            opcion = input("Seleccione una opcion: ")
            if opcion == "0":
                productos.listarProductos()
            elif opcion == "1":
                print("Llamar metodo insertarProducto()")
            elif opcion == "2":
                print("Llamar metodo buscarProducto()")
            elif opcion == "3":
                print("Llamar metodo actualizarProducto()")
            elif opcion == "4":
                print("Llamar metodo borrarProducto()")
            elif opcion == "5":
                print("Salir del programa")

despensa = Main()
despensa.menu()
