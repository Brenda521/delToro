import json
from Articulos import Articulos  #Clase Producto
import pymongo

conn_str = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.prtaa.mongodb.net/myFirstDatabase"
myclient = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
mydb = myclient["ejemploventas"]

class Lista_Articulos:
    def __init__ (self):
        self.Lista_Art = []
        self.ListaD = [] #Lista de productos (diccionarios)


    def agregar_articulo(self, articulo):
        self.Lista_Art.append(articulo)
    
    def delete(self, articulo):
        del self.Lista_Art[articulo]
   
    #Agrega un producto a la lista
    def Agregar(self, elemento):
        self.Lista.append(elemento)


    def GetLista(self):
        return self.Lista

    #Convierte de Json a Diccionario  y lo agrega a una lista de diccionarios (self.ListaD)
    def abrirJson(self):
        try: 
            f = open("articulos.json", "r") 
            aux = f.read() 
            self.ListaD=json.loads(aux) #El método loads, convierte el Json a diccionario
            f.close() 
            self.cargarJson() #manda a llamar a un método de la misma clase
        except:
            f = open("articulos.json", "x") 
            f.close()  
    
    #Convierte de diccionario a objeto y lo agrega a una lista de objetos (self.Lista)
    def cargarJson(self): 
        for articulo in self.ListaD: 
            nuevoArticulo = Articulos(articulo["_id"], 
            articulo["clave"], 
            articulo["nombre"], 
            articulo["precio"])
            self.Lista_Art.append(nuevoArticulo) 
    
    def GuardarJson(self):
        self.ListaD = [] #Vaciar lista
        for articulo in self.Lista_Art: 
            aux = articulo.__dict__ #Convierte de producto (objeto) a diccionario
            self.ListaD.append(aux) #Agrega a la lista el diccionario
        
        f = open("articulos.json", "w")
        aux = json.dumps(self.ListaD, indent=4) #El método "dumbs" convierte de diccionario a Json - El "indent" es para que se vea bonito
        f.write(aux) 
        f.close()  

    def guardarBasedatos(self):  
        mycol = mydb["articulos"]
        mycol.delete_many({})
        listdict = self.ListaD
        mycol.insert_many(listdict)
