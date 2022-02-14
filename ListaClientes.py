import json
from Clientes import Clientes  #Clase Producto
import pymongo

conn_str = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.prtaa.mongodb.net/myFirstDatabase"
myclient = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
mydb = myclient["ejemploventas"]

class Lista_Clientes:
    
    def __init__(self):
        self.Lista_Clien = []
        self.ListaD = [] #Lista de productos (diccionarios)

    def agregar_cliente(self,cliente):
        self.Lista_Clien.append(cliente)

    def delete(self, cliente):
        del self.Lista_Clien[cliente]


    #Agrega un producto a la lista
    def Agregar(self, elemento):
        self.Lista.append(elemento)

    #Te devuelve la lista
    def GetLista(self):
        return self.Lista

    #Convierte de Json a Diccionario  y lo agrega a una lista de diccionarios (self.ListaD)
    def abrirJson(self):
        try: #Crea una lista de diccionarios a partir de el archivo Json
            f = open("clientes.json", "r") #Abrimos el archivo "productos.json" - Mediante la "r" podemos leer el archivo
            aux = f.read() #Devuelve el texto
            self.ListaD=json.loads(aux) #El método loads, convierte el Json a diccionario
            f.close() #Pa' cerrar el archivo
            self.cargarJson() #manda a llamar a un método de la misma clase
        except:
            f = open("clientes.json", "x") #crea un archivo si es que no existe
            f.close() #Pa' cerrar el archivo X2
    
    #Convierte de diccionario a objeto y lo agrega a una lista de objetos (self.Lista)
    def cargarJson(self): 
        for cliente in self.ListaD: #Recorre la lista de diccionarios
            nuevoCliente = Clientes(cliente["_id"], 
            cliente["nombre"], 
            cliente["rfc"], 
            cliente["direccion"])
            self.Lista_Clien.append(nuevoCliente) #Agrega el producto a la lista
    
    def GuardarJson(self):
        self.ListaD = [] #Vaciar lista
        for cliente in self.Lista_Clien: #Recorre la lista de productos (objeto)
            aux = cliente.__dict__ #Convierte de producto (objeto) a diccionario
            self.ListaD.append(aux) #Agrega a la lista el diccionario
        
        f = open("clientes.json", "w")#El parámetro "w" significa escribir (llenamos el archivo)
        aux = json.dumps(self.ListaD, indent=4) #El método "dumbs" convierte de diccionario a Json - El "indent" es para que se vea bonito
        f.write(aux) #Excribe el json en el archivo 
        f.close() #Pa' cerrar el archivo X3

    def guardarBasedatos(self):  
        mycol = mydb["clientes"]
        mycol.delete_many({})
        listdict = self.ListaD
        mycol.insert_many(listdict)
