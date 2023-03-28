from tiendas.listar_tienda import ListarTienda  # Importa el modulo Tiendas
from productos.listar_producto import ListarProducto  # Importa el modulo ListarProductos
# TODO importar modulos


class Main():  # Clase principal

    def __init__(self) -> None:  # Constructor de la clase Main
        pass  # inicializa el objeto Main

    def menu(self):  # Metodo que muestra el menu del sistema
        # Objetos de cada clase
        listarP = ListarProducto()  # Objeto de la clase ListarProducto
        listarT = ListarTienda()  # Objeto de la clase ListarTienda
        # Bucle del menu
        while True:  # Bucle infinito para mostrar las opciones del sistema
            print("0.- Listar productos")  # Opcion para listar los productos
            print("1.- Insertar producto")  # Opcion para insertar un nuevo producto
            print("2.- Buscar producto por SKU")  # Opcion para buscar productos por SKU
            print("3.- Actualizar producto")  # Opcion para actualizar un producto
            print("4.- Borrar producto")  # Opcion para borrar un producto
            print("---------------------")  # Salto de menu
            print("5.- Listar tiendas")  # Opcion para listar las tiendas
            print("6.- Insertar tienda")  # Opcion para insertar una nueva tienda
            print("7.- Buscar tienda por Nombre")  # Opcion para buscar tiendas
            print("8.- Actualizar tienda")  # Opcion para actualizar una tienda
            print("9.- Borrar tienda")  # Opcion para borrar una tienda
            print("---------------------")  # Salto de menu
            print("s.- Salir")  # Opcion para salir del sistema
            opcion = input("Seleccione una opcion: ")  # Solicita al usuario que seleccione una opcion del menu
            if opcion == "0":  # Valida si la opcion elegida es el 0
                listarP.listarProductoV1()  # Llama al metodo listarProductos a traves del objeto listarP
            elif opcion == "1":  # Valida si la opcion elegida es el 1
                # TODO Llamar al metodo insertarProducto()
                print("Llamar metodo insertarProducto()")  # Mensaje de prueba
            elif opcion == "2":  # Valida si la opcion elegida es el 2
                # TODO Llamar al metodo buscarProducto()
                print("Llamar metodo buscarProducto()")  # Mensaje de prueba
            elif opcion == "3":  # Valida si la opcion elegida es el 3
                # TODO Llamar al metodo actualizarProducto()
                print("Llamar metodo actualizarProducto()")  # Mensaje de prueba
            elif opcion == "4":  # Valida si la opcion elegida es el 4
                # TODO Llamar al metodo borrarProducto()
                print("Llamar metodo borrarProducto()")  # Mensaje de prueba
            elif opcion == "5":  # Valida si la opcion elegida es el 5
                listarT.listarTienda()
            elif opcion == "6":  # Valida si la opcion elegida es el 6
                # TODO Llamar al metodo insertarTienda()
                print("Llamar metodo insertarTienda()")  # Mensaje de prueba
            elif opcion == "7":  # Valida si la opcion elegida es el 7
                # TODO Llmar al metodo buscarTienda()
                print("Llamar metodo buscarTienda()")  # Mensaje de prueba
            elif opcion == "8":  # Valida si la opcion elegida es el 8
                # TODO Llamar al metido actualizarTienda()
                print("Llamar metodo actualizarTienda()")  # Mensaje de prueba
            elif opcion == "9":  # Valida si la opcion elegida es el 9
                # TODO Llamar al metodo borrarTienda()
                print("Llamar metodo borrarTienda()")  # Mensaje de prueba
            elif opcion == "s":  # Valida si la opcion elegida es el s
                print("Salir del sistema")  # Mensaje de prueba

            # TODO rediseñar el menu para agregar los submenus 0- Productos, 1- Tiendas, 2- Despensa


if __name__ == "__main__":  # Define el modulo principal
    principal = Main()  # Crea un objeto de la clase Main
    principal.menu()  # Llama al metodo menu a traves del objeto principal
