
import ClaseJSONArticulos  #Clase lista (Productos)
from Articulos import Articulos  #Clase Producto

articulo = ClaseJSONArticulos.ListaArticulo()

articulo.abrirJson() #Json -> Diccionario -> Objeto

arti = Articulos(2, "234", "Soda", 10 )

articulo.Agregar(arti) 

#Imprime los nombres de todos los productos en la lista
for x in verArticulos:
    print("Nombre: " + x.nombre)
    print("Precio: $" + str(x.precio))
    print("----------------------")

#x.nombre #Objetos
#x["nombre"] #Diccionarios

articulo.GuardarJson() #Objeto -> diccionario -> Json