class Articulos:

    def __init__ (self, _id, clave, nombre, precio):
        self._id=int(_id)
        self.clave=str(clave)
        self.nombre=str(nombre)
        self.precio=float(precio)