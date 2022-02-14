#importar
import ClaseJSONClientes  #Clase lista (Productos)
from Clientes import Clientes  #Clase Producto

#-----------| INICIO |-----------#

#instancia de la lista
cliente = ClaseJSONClientes.ListaCliente()

#Convierte el archivo .json a una lista de articulo
cliente.abrirJson() #Json -> Diccionario -> Objeto

#-----------| PROCESO |-----------#

#instancia del producto
cli = Clientes(1, "Brenda", "qwerty", "Sol de Ote")

cliente.Agregar(cli) #Agrega un producto a la lista

#Te devuelve la lista
verCliente = cliente.GetLista()

#Imprime los nombres de todos los productos en la lista
for x in verCliente:
    print("Nombre: " + x.nombre)
    print("rfc: " + str(x.rfc))
    print("----------------------")

#x.nombre #Objetos
#x["nombre"] #Diccionarios

#-----------| FINAL |-----------#

#Inserta datos en el archivo json
cliente.GuardarJson() #Objeto -> diccionario -> Json