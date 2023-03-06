from productos import Productos # Importa el modulo Productos
from tiendas import Tiendas # Importa el modulo Tiendas
#TODO importar Despensa

class Main(): # Clase principal

    def __init__(self) -> None: # Constructor de la clase Main
        pass # inicializa el objeto Main

    def menu(self): # Metodo que muestra el menu del sistema
        productos = Productos() # Crea un objeto de la clase Prodcutos
        while True: # Bucle infinito para mostrar las opciones del sistema
            print("0.- Listar productos") # Opcion para listar los prodcutos
            print("1.- Insertar producto") # Opcion para insertar un nuevo producto
            print("2.- Buscar producto por SKU") # Opcion para buscar productos por SKU
            print("3.- Actualizar producto") # Opcion para actualizar un producto
            print("4.- Borrar producto") # Opcion para borrar un producto
            print("s.- Salir") # Opcion para salir del sistema
            opcion = input("Seleccione una opcion: ") # Solicita al usuario que seleccione una opcion del menu
            if opcion == "0": # Valida si la opcion elegida es el 0
                productos.listarProductos() # Llama al metodo listarProductos a traves del objeto productos
            elif opcion == "1": # Valida si la opcion elegida es el 1
                # TODO Llamar al metodo insertarProducto()
                print("Llamar metodo insertarProducto()")
            elif opcion == "2": # Valida si la opcion elegida es el 2
                # TODO Llamar al metodo buscarProducto()
                print("Llamar metodo buscarProducto()")
            elif opcion == "3": # Valida si la opcion elegida es el 3
                # TODO Llamar al metodo actualizarProducto()
                print("Llamar metodo actualizarProducto()")
            elif opcion == "4": # Valida si la opcion elegida es el 4
                # TODO Llamar al metodo borrarProducto()
                print("Llamar metodo borrarProducto()")
            elif opcion == "5": # Valida si la opcion elegida es el 5
                # TODO Programar salir del programa
                print("Salir del programa")

            # TODO rediseñar el menu para agregar los submenus necesarios


if __name__ == "__main__":
    principal = Main() # Crea un objeto de la clase Main
    principal.menu() # Llama al metodo menu a traves del objeto principal
