import json
from Ventas import Ventas  #Clase Producto
from DetalleVenta import Detalle_de_Venta
import pymongo

conn_str = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.prtaa.mongodb.net/myFirstDatabase"
myclient = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
mydb = myclient["ejemploventas"]

class Lista_Venta:
    def __init__(self):
        self.Lista_Venta = []
        self.ListaD = [] #Lista de productos (diccionarios)


    def agregarVenta(self, venta):
        self.Lista_Venta.append(venta)

    #Agrega un producto a la lista
    def Agregar(self, elemento):
        self.Lista.append(elemento)

    def GetLista(self):
        return self.Lista

    #Convierte de Json a Diccionario  y lo agrega a una lista de diccionarios (self.ListaD)
    def abrirJson(self):
        try: 
            f = open("ventas.json", "r") 
            aux = f.read() 
            self.ListaD=json.loads(aux) #El método loads, convierte el Json a diccionario
            f.close() 
            self.cargarJson() #manda a llamar a un método de la misma clase
        except:
            f = open("ventas.json", "x") 
            f.close()  
    
    #Convierte de diccionario a objeto y lo agrega a una lista de objetos (self.Lista)
    def cargarJson(self): 
        for venta in self.ListaD:
            listanueva = [] 
            for articulo in venta["listaven"]:
                nuevoArticulo = Detalle_de_Venta(articulo["id_art"], 
                articulo["cant"], 
                articulo["total"], 
                articulo["id_venta"],
                articulo["arcant"],
                articulo["iva"],
                articulo["subtotal"])
                listanueva.append(nuevoArticulo)
            nuevaVenta = Ventas(venta["_id"], 
            venta["clien"], 
            venta["fech"], 
            venta["IVA"],
            venta["total"],
            venta["subtotal2"],
            listanueva)
            self.Lista_Venta.append(nuevaVenta) 
    
    def GuardarJson(self):
        self.ListaD = [] #Vaciar lista
        for venta in self.Lista_Venta: 
            nuevalist = []
            aux = venta.__dict__ #Convierte de producto (objeto) a diccionario 
            for j in venta.listaven:
                nuevalist.append(j.__dict__)
            aux ["listaven"] =  nuevalist
            self.ListaD.append(aux) #Agrega a la lista el diccionario
                
            
        f = open("ventas.json", "w")
        aux = json.dumps(self.ListaD, indent=4) #El método "dumbs" convierte de diccionario a Json - El "indent" es para que se vea bonito
        f.write(aux) 
        f.close()  
  

    def guardarBasedatos(self):  
        mycol = mydb["ventas"]
        mycol.delete_many({})
        listdict = self.ListaD
        mycol.insert_many(listdict)