import csv  # Librería para abrir, leer y escribir archivos CSV

class ListarTienda:

    def __init__(self) -> None:
        pass

    def listarTienda(self):
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            with open("data/tiendas.csv", "r") as file: # Abre el archivo para tener acceso a los registros
                reader = csv.DictReader(file, delimiter=";") # Crer un objeto reader para leer los registros separandolos por el delimitador ,
                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    print(f"Registro: {row}") # imprime los datos del registro como un diccionario
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error listarTienda() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo
