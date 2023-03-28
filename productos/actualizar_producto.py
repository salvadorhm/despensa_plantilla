import csv  # Librería para abrir, leer y escribir archivos CSV

class ActualizarProducto:

    def __init__(self) -> None:
        pass

    def actualizarProductoV1(self, sku: str, nombre: str, unidad: str) -> bool: # Metodo para actualizar un producto
        """
        Metodo para actualizar el nombre y la unidad del producto que coincida con el sku recibido,
        modificando los datos en el archivo productos.csv

        Args:
            sku (str): SKU del producto a actualizar
            nombre (str): Nombre y descripción del producto
            unidad (str): Unidad del producto (Pieza, Kilo, Litro, Caja)

        Returns:
            bool: Regresa True si el producto se actualizo correctamente, y False si
            ocurrio una falla al actualizar los valores
        """
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            # TODO Código para actualizar los valores en el archivo productos.csv
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error actualizarProducto() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo

    def actualizarProductoV2(self) -> bool: # Metodo para actualizar un producto
        """
        Metodo que solicita el sku, nombre y unidad de un producto, lo busca en el archivo productos.csv
        y si encuentra una coincidencia sustituye el nombre y la unidad.

        Returns:
            bool: Regresa True si el producto se actualizo correctamente, y False si
            ocurrio una falla al actualizar los valores
        """
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error actualizarProducto() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo
