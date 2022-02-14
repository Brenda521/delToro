import json
from Articulos import Articulos  #Clase Producto


class ListaArticulo:
    def __init__(self):
        self.Lista = [] #Lista de productos (objetos)
        self.ListaD = [] #Lista de productos (diccionarios)

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
            nuevoArticulo = Articulos(articulo["id"], 
            articulo["clave"], 
            articulo["nombre"], 
            articulo["precio"])
            self.Lista.append(nuevoArticulo) 
    
    def GuardarJson(self):
        self.ListaD = [] #Vaciar lista
        for articulo in self.Lista: 
            aux = articulo.__dict__ #Convierte de producto (objeto) a diccionario
            self.ListaD.append(aux) #Agrega a la lista el diccionario
        
        f = open("articulos.json", "w")
        aux = json.dumps(self.ListaD, indent=4) #El método "dumbs" convierte de diccionario a Json - El "indent" es para que se vea bonito
        f.write(aux) 
        f.close()  
