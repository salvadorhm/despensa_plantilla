import csv  # Librería para abrir, leer y escribir archivos CSV

class BorrarProducto:

    def __init__(self) -> None:
        pass

    def borrarProductoV1(self, sku: str) -> bool: # Metodo para borrar un producto
        """
        Metodo para borrar del archivo productos.csv el producto que coincida con el sku recibido

        Args:
            sku (str): SKU del producto a borrar

        Returns:
            bool: Regresa True si el producto se borro y False si ocurrio un error.
        """
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            # TODO código para borrar un producto del archivo productos.csv
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error borrarrProducto() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo

    def borrarProductoV2(self) -> bool: # Metodo para borrar un producto
        """
        Metodo que solicita un SKU y despues borra del archivo productos.csv
        el producto que coincida con el sku leido

        Returns:
            bool: Regresa True si el producto se borro y False si ocurrio un error.
        """
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            sku = input("SKU del producto a borrar")
            # TODO código para borrar un producto del archivo productos.csv
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error borrarrProducto() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo
