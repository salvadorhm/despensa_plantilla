import csv


class Productos:
    def __init__(self):
        pass

    def listarProductos(self) -> bool:
        try:
            with open("productos.csv", "r") as file:
                reader = csv.DictReader(file, delimiter=",")
                for row in reader:
                    print(row)
            return True
        except Exception as e:
            print(f"Error :{e.args}")
            return False

    def insertarProducto(self, sku: str, nombre: str, unidad: str) -> bool:
        # TODO programar el método insertarProducto()
        return False

    def buscarProducto(self, sku: str) -> None:
        # TODO programar el método buscarProducto()
        return False

    def borrarProducto(self, sku: str) -> None:
        # TODO programar el método borrarProducto()
        return False

    def actualizarProducto(self, sku: str, nombre: str, unidad: str) -> None:
        # TODO programar el método actualizarProducto()
        return False
