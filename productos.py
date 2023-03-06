import csv  # Librería para abrir, leer y escribir archivos CSV


class Productos:  # Clase Productos
    def __init__(self): # Constructor de la clase Productos
        pass # Inicializa el objeto de la clase Productos

    def listarProductos(self) -> bool: # Metodo para listar los productos registrados
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            with open("productos.csv", "r") as file: # Abre el archivo para tener acceso a los registros
                reader = csv.DictReader(file, delimiter=",") # Crer un objeto reader para leer los registros separandolos por el delimitador ,
                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    print(row) # imprime los datos del registro como un diccionario
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error listarProdcutos() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo

    def insertarProducto(self, sku: str, nombre: str, unidad: str) -> bool: # Metodo para insertar un producto
        # TODO programar el método insertarProducto()
        return False # Regresa False si ocurrio un error en el metodo

    def buscarProducto(self, sku: str) -> bool: # Metodo para buscar un producto
        # TODO programar el método buscarProducto()
        return False # Regresa False si ocurrio un error en el metodo

    def borrarProducto(self, sku: str) -> bool: # Metodo para borrar un producto
        # TODO programar el método borrarProducto()
        return False # Regresa False si ocurrio un error en el metodo

    def actualizarProducto(self, sku: str, nombre: str, unidad: str) -> bool: # Metodo para actualizar un producto
        # TODO programar el método actualizarProducto()
        return False # Regresa False si ocurrio un error en el metodo

productos = Productos()
productos.listarProductos()
