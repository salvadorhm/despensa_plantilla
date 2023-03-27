import csv  # Librería para abrir, leer y escribir archivos CSV

class InsertarTienda:

    def __init__(self) -> None:
        pass

    def insertarTienda(self) -> bool: # Metodo para insertar un producto
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error insertarTienda() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo
