import csv  # Librería para abrir, leer y escribir archivos CSV

class InsertarProducto:

    def __init__(self) -> None:
        pass

    def insertarProductoV1(self, sku: str, nombre: str, unidad: str) -> bool: # Metodo para insertar un producto
        """
        Metodo que recibe los datos de un producto nuevo y los agrega en el archivo productos.csv
        Args:
            sku (str): SKU del producto
            nombre (str): Nombre y descripción del producto
            unidad (str): Unidad del producto (Pieza, Kilo, Litro, Caja)

        Returns:
            bool: Regresa True si el registro se agrego correctamente, y False
            si ocurrio un error al agregar el registro
        """
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            # TODO codigo para agregar un producto al archivo producos.csv
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error insertarProducto() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo


    def insertarProductoV2(self) -> bool: # Metodo para insertar un producto
        """
        Metodo para agregar un nuevo producto al archivo productos.csv solicitando por input los
        valores a almacenar

        Returns:
            bool: Regresa True si el registro se agrego correctamente, y False
            si ocurrio un error al agregar el registro
        """
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            sku = input("SKU: ")
            nombre = input("Nombre y descripción del producto: ")
            unidad = input("Tipo de unidad (Pieza, Kilo, Litro, Caja): ")
            # TODO codigo para agregar un producto al archivo producos.csv
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error insertarProducto() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo
