import csv  # Librería para abrir, leer y escribir archivos CSV

class BuscarProducto:

    def __init__(self) -> None:
        pass

    def buscarProductoV1(self, sku: str) -> bool: # Metodo para buscar un producto
        """
        Metodo que busca un producto en el archivo productos.csv mediante el sku del producto,
        en caso de encontrar el producto imprime el sku, nombre y unidad.
        Args:
            sku (str): SKU del producto que se desea buscar

        Returns:
            bool: Regresa True si el producto se encontro, y False si el producto no existe
        """
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            # TODO código para buscar el producto por sku
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error buscarProducto() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo

    def buscarProductoV2(self) -> bool: # Metodo para buscar un producto
        """
        Metodo que busca un producto en el archivo productos.csv, solicitando con un input el sku
        del producto a buscar, y en caso de encontrar el producto imprime sku, nombre y unidad, y
        en caso de no encontrar el producto imprime el mensaje 'Producto no encontrado'

        Returns:
            bool: Regresa True si el producto se encontro, y False si el producto no existe
        """
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            sku = input("SKU del producto a buscar: ")
            # TODO código para buscar el producto por sku
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error buscarProducto() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo
