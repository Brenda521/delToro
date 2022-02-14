import Articulos 
import ListaArticulos 
import Ventas 
import ListaVentas 
import Clientes
import ListaClientes 
import DetalleVenta 
import ClaseJSONArticulos
import ClaseJSONClientes
import pymongo

#IMPORTAR MONGODB

from datetime import datetime

listArt = ListaArticulos.Lista_Articulos()
listCli = ListaClientes.Lista_Clientes()
listVen = ListaVentas.Lista_Venta()

#METODOS JSON ARTICULOS
listArt.abrirJson()

#METODOS JSON CLIENTES
listCli.abrirJson()

#METODOS JSON VENTAS
listVen.abrirJson()

#FECHA
fecha = str(datetime.today().strftime('%Y-%m-%d %H:%M'))

#BASE DE DATOS MONGODB
conn_str = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.prtaa.mongodb.net/myFirstDatabase"
myclient = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
mydb = myclient["ejemploventas"]

#ARTICULOS

def agregarArticulo():
    salir_articulos = input()
    while salir_articulos !="n":
        id= int(len(listArt.Lista_Art)) + 1
        clave = input("Clave: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        print("-------------------------------------------------------------------------------------------")
        articuloAgregado=Articulos.Articulos(id, clave, nombre, precio)
        listArt.agregar_articulo(articuloAgregado)
        print("¿Desea agregar otro articulo?")
        salir_articulos = input()
        listArt.GuardarJson()
        listArt.guardarBasedatos()
        print("")
        print("----------------------------------------------------------------------------------------------")
        

def verArticulos():
    print("ID" + '\t\t\t' + "Clave" + '\t\t\t' + "Nombre" + '\t\t\t' + "Precio")
    print("************************************************************************************")   
    for x in range(len(listArt.Lista_Art)):
        id = str(listArt.Lista_Art[x]._id)
        clave = (listArt.Lista_Art[x].clave)
        nombre = (listArt.Lista_Art[x].nombre)
        precio = str(listArt.Lista_Art[x].precio)
        print(id + '\t\t\t' + clave + '\t\t\t' + nombre + '\t\t\t' + "$" + precio)
        print("---------------------------------------------------------------------------------------")

def borrarArticulo():
    print("Se eliminara de manera permanente el articulo")
    verArticulos()
    entrada = input("ID del articulo: ")
    listArt.delete(int(entrada) - 1)
    print("Articulo eliminado")

#CLIENTES
    
def agregarCliente():
    salir_clientes = input()
    while salir_clientes !='n':
        id= int(len(listCli.Lista_Clien)) + 1 
        nombre = input("Nombre: ")
        rfc = input("RFC: ")
        direccion = input("Dirección: ")
        print("-------------------------------------------------------------------------------------------")
        clienteAgregado=Clientes.Clientes(id,nombre,rfc,direccion)
        listCli.agregar_cliente(clienteAgregado)
        print("¿Desea agregar otro cliente?")
        salir_clientes = input()
        listCli.GuardarJson()
        listCli.guardarBasedatos()
        print("")
        print("----------------------------------------------------------------------------------------------")


def verClientes():
    print("ID" + '\t\t\t' + "Nombre" + '\t\t\t' + "RFC" + '\t\t\t' + "Direccion")
    print("********************************************************************************************")   
    for x in range(len(listCli.Lista_Clien)):
        id = str(listCli.Lista_Clien[x]._id)
        nombre = (listCli.Lista_Clien[x].nombre)
        rfc = (listCli.Lista_Clien[x].rfc)
        direccion = str(listCli.Lista_Clien[x].direccion)
        print(id + '\t\t\t' + nombre + '\t\t\t' + rfc + '\t\t\t' + direccion)
        print("-------------------------------------------------------------------------------------------------------")

def borrarClientes():
    print("Se eliminara de manera permanente al cliente")
    verClientes()
    entrada = input("ID del cliente: ")
    listCli.delete(int(entrada) - 1)
    print("Cliente eliminado")

#VENTAS

def agregarVenta():
    id_venta= int(len(listVen.Lista_Venta)) + 1
    subtotalv = 0.0
    subtotal = 0.0
    detalles=[]
    verClientes()
    idCli=int(input("Inserte la ID del cliente: ")) 
    print("-----Agregar Articulos-----")      
    seguir = 's'
    while seguir == 's':
        verArticulos() 
        id_art=int(input("Inserte la ID del articulo: "))
        for k in range(len(listArt.Lista_Art)):
            if id_art == listArt.Lista_Art[k]._id:
                cant = int(input("Ingrese la cantidad: "))
                arcant=float(listArt.Lista_Art[k].precio)
                subtotal=float(cant * arcant)
                iva=float(subtotal * 0.16) 
                total=float(iva + subtotal)
                agArt = DetalleVenta.Detalle_de_Venta( id_art, cant, total, id_venta,arcant,iva, subtotal)
                detalles.append(agArt)
        subtotalv += subtotal
        seguir=input("¿Desea agregar otro articulo?")
    fecha = str(datetime.today().strftime('%Y-%m-%d %H:%M'))
    IVA = float(subtotalv * 0.16)
    totalv = float(subtotalv * 1.16)
    subtotal2 = float(subtotalv)
    print("Id de Cliente: " + str(idCli)) 
    print("Fecha :" + str(fecha))
    print("Subtotal: $" + str(subtotal2))
    print("IVA: $" + str(IVA))
    print("Total: $" + str(totalv))
    ventaAg = Ventas.Ventas(id_venta, idCli, fecha, subtotal2, IVA, totalv, detalles)
    listVen.agregarVenta(ventaAg)
 
    
    
def verVentas(): 
    for i in range(len(listVen.Lista_Venta)) :
        id =str(listVen.Lista_Venta[i]._id)
        print("---------------------------------------------------------------------------")  
        print("Venta " + id)
        clien = str(listVen.Lista_Venta[i].clien) 
        fech = str(listVen.Lista_Venta[i].fech)
        print("-----Articulos-----")
        for x in listVen.Lista_Venta[i].listaven:
            cant = str (x.cant)
            subtotalf =str(x.subtotal)
            ivaf = str(x.iva)
            totalf = str(x.total)
            print("Cantidad de Articulos: " + cant)
            print("Subtotal: $" + subtotalf)
            print("IVA : $" + ivaf)
            print("Total : $" + totalf)
        print("---------------------------------------------------------------------------------------------------")  
        subtotal  = str(listVen.Lista_Venta[i].subtotal2)     
        IVA = str(listVen.Lista_Venta[i].IVA)
        total= str(listVen.Lista_Venta[i].total) 
        print("ID del Cliente: " + clien)
        print("Fecha: " + fech)
        print("Subtotal: $" + subtotal)
        print("IVA: $" + IVA)
        print("Total: $" + total)
        print("-------------------------------------------------------------------")

        
        
#MENU
def menu():
    print("-----ARTICULOS-----")
    print("1) Agregar Articulo")
    print("2) Ver Articulos")
    print("3) Eliminar Articulo")
    print("")
    print("-----CLIENTES-----")
    print("")
    print("4) Agregar Clientes")
    print("5) Ver Clientes")
    print("6) Eliminar Cliente")
    print("")
    print("-----VENTAS-----")
    print("")
    print("7) Agregar una Venta")
    print("8) Ver Ventas")
   
while True:
    menu()

    opc = input("Elija donde quiere ingresar: ")
    print("--------------------------------------------------------------------------------------------")
    if opc == '1':
        agregarArticulo()
        print("")
    elif opc == '2':
        verArticulos()
        print("")
    elif opc == '3':
        borrarArticulo()
        print("")
    elif opc == '4':
        agregarCliente() 
        print("")
    elif opc == '5':
        verClientes() 
        print("")
    elif opc == '6':
        borrarClientes() 
        print("")
    elif opc == '7':
        agregarVenta()
        print("")
    elif opc == '8':
        verVentas()
        print("")
    else :
        opc != 'e'
        print("")
        break

listVen.GuardarJson() 
#listVen.guardarBasedatos() 